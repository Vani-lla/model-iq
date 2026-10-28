import json
import sys
import time
from pathlib import Path
from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from ollama import ResponseError

from tasks import check, load_tasks
from tools import SOLUTION, TOOLS

MODEL = "qwen2.5-coder:7b"
RESULTS = Path(__file__).parent / "results" / "baseline.jsonl"
SOLUTIONS = Path(__file__).parent / "solutions"
SYSTEM = (
    "You are a Python programmer. Complete the given function. "
    "Call the write_code tool with the full function source, including imports. Do not include the docstring."
)

llm = ChatOllama(model=MODEL, temperature=0).bind_tools(TOOLS)


class State(TypedDict):
    messages: Annotated[list, add_messages]


def as_tool_call(message):
    if message.tool_calls or not message.content.startswith("{"):
        return message
    try:
        call = json.loads(message.content)
    except json.JSONDecodeError:
        return message
    return AIMessage("", tool_calls=[{"name": call["name"], "args": call["arguments"], "id": "call_0"}], usage_metadata=message.usage_metadata)


def agent(state):
    return {"messages": [as_tool_call(llm.invoke(state["messages"]))]}


builder = StateGraph(State)
builder.add_node("agent", agent)
builder.add_node("tools", ToolNode(TOOLS))
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", END)
graph = builder.compile()


def solve(task):
    messages = [SystemMessage(SYSTEM), HumanMessage(task["prompt"])]
    SOLUTION.unlink(missing_ok=True)
    start = time.time()
    state = graph.invoke({"messages": messages})
    seconds = time.time() - start
    ai = [m for m in state["messages"] if isinstance(m, AIMessage)]
    return {
        "code": SOLUTION.read_text() if SOLUTION.exists() else "",
        "seconds": seconds,
        "tool_calls": sum(len(m.tool_calls) for m in ai),
        "output_tokens": sum(m.usage_metadata["output_tokens"] for m in ai),
        "error": "no_tool_call",
    }


def main():
    tasks = load_tasks()
    if len(sys.argv) > 1:
        tasks = tasks[: int(sys.argv[1])]
    RESULTS.parent.mkdir(exist_ok=True)
    SOLUTIONS.mkdir(exist_ok=True)
    RESULTS.write_text("")
    for task in tasks:
        try:
            run = solve(task)
        except ResponseError:
            run = {"code": "", "seconds": 0, "tool_calls": 0, "output_tokens": 0, "error": "model_error"}
        (SOLUTIONS / f"{task['task_id'].replace('/', '_')}.py").write_text(run["code"])
        passed, error = check(task, run["code"]) if run["code"] else (False, run["error"])
        row = {
            "task_id": task["task_id"],
            "passed": passed,
            "error": error,
            "seconds": run["seconds"],
            "tool_calls": run["tool_calls"],
            "output_tokens": run["output_tokens"],
            "prompt_len": len(task["prompt"]),
            "code_len": len(run["code"]),
        }
        with RESULTS.open("a") as f:
            f.write(json.dumps(row) + "\n")
        print(row["task_id"], row["passed"], row["error"], f"{row['seconds']:.1f}s")


if __name__ == "__main__":
    main()
