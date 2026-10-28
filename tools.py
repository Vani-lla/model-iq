from pathlib import Path

from langchain_core.tools import tool

SOLUTION = Path(__file__).parent / "workspace" / "solution.py"


@tool
def write_code(code: str) -> str:
    """Save the complete Python solution (imports and full function definition)."""
    SOLUTION.parent.mkdir(exist_ok=True)
    SOLUTION.write_text(code)
    return "saved"


TOOLS = [write_code]
