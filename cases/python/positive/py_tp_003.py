def read(name: str) -> str:
    # XG-BENCH:PY-TP-003 START
    with open("/srv/data/" + name, "r", encoding="utf-8") as fh:
        return fh.read()
    # XG-BENCH:PY-TP-003 END
