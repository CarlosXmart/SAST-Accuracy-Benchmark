from urllib.parse import urlparse
from urllib.request import urlopen
def fetch(raw_url: str) -> bytes:
    # XG-BENCH:PY-TN-008 START
    u = urlparse(raw_url)
    if u.scheme != "https" or u.hostname != "api.example.test":
        raise ValueError("blocked destination")
    return urlopen(raw_url, timeout=2).read()
    # XG-BENCH:PY-TN-008 END
