import random
def reset_code() -> str:
    # XG-BENCH:PY-TP-007 START
    return str(random.randint(100000, 999999))
    # XG-BENCH:PY-TP-007 END
