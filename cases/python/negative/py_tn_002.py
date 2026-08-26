import subprocess
def run(user: str):
    # XG-BENCH:PY-TN-002 START
    return subprocess.run(["printf", "%s", user], shell=False, check=False)
    # XG-BENCH:PY-TN-002 END
