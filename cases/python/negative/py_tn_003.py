from pathlib import Path
def read(name: str) -> str:
    # XG-BENCH:PY-TN-003 START
    base = Path("/srv/data").resolve()
    target = (base / name).resolve()
    if base not in target.parents and target != base:
        raise ValueError("outside base")
    return target.read_text(encoding="utf-8")
    # XG-BENCH:PY-TN-003 END
