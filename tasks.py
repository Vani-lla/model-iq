import gzip
import json
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

URL = "https://github.com/openai/human-eval/raw/master/data/HumanEval.jsonl.gz"
DATA = Path(__file__).parent / "data" / "HumanEval.jsonl.gz"


def load_tasks():
    if not DATA.exists():
        DATA.parent.mkdir(exist_ok=True)
        urllib.request.urlretrieve(URL, DATA)
    with gzip.open(DATA, "rt") as f:
        return [json.loads(line) for line in f]


def check(task, code, timeout=10):
    program = f"{code}\n\n{task['test']}\n\ncheck({task['entry_point']})\n"
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(program)
    try:
        result = subprocess.run([sys.executable, f.name], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    if result.returncode == 0:
        return True, "ok"
    last = result.stderr.strip().splitlines()[-1]
    return False, last.split(":")[0]
