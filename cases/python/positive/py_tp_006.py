import hashlib
def digest(password: bytes) -> str:
    # XG-BENCH:PY-TP-006 START
    return hashlib.md5(password).hexdigest()
    # XG-BENCH:PY-TP-006 END
