from urllib.request import urlopen
def fetch(raw_url: str) -> bytes:
    # XG-BENCH:PY-TP-008 START
    return urlopen(raw_url, timeout=2).read()
    # XG-BENCH:PY-TP-008 END
