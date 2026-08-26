import hashlib
def digest(data: bytes) -> str:
    # XG-BENCH:PY-TN-006 START
    return hashlib.sha256(data).hexdigest()
    # XG-BENCH:PY-TN-006 END
