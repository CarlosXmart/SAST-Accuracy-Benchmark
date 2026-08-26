import secrets
def reset_code() -> str:
    # XG-BENCH:PY-TN-007 START
    return secrets.token_urlsafe(24)
    # XG-BENCH:PY-TN-007 END
