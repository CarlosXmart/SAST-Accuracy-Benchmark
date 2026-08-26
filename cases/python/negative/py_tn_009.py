import ssl
def context():
    # XG-BENCH:PY-TN-009 START
    return ssl.create_default_context()
    # XG-BENCH:PY-TN-009 END
