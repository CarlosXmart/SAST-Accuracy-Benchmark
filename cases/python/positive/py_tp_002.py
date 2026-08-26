import os
def run(user: str) -> int:
    # XG-BENCH:PY-TP-002 START
    return os.system("echo " + user)
    # XG-BENCH:PY-TP-002 END
