import pickle
def load(payload: bytes):
    # XG-BENCH:PY-TP-004 START
    return pickle.loads(payload)
    # XG-BENCH:PY-TP-004 END
