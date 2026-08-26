import ssl
from urllib.request import urlopen
def fetch(url: str) -> bytes:
    # XG-BENCH:PY-TP-009 START
    ctx = ssl._create_unverified_context()
    return urlopen(url, context=ctx, timeout=2).read()
    # XG-BENCH:PY-TP-009 END
