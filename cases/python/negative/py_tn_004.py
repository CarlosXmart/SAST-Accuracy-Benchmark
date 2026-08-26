import json
def load(payload: str):
    # XG-BENCH:PY-TN-004 START
    return json.loads(payload)
    # XG-BENCH:PY-TN-004 END
