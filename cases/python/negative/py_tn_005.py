import ast
def calculate(expr: str):
    # XG-BENCH:PY-TN-005 START
    return ast.literal_eval(expr)
    # XG-BENCH:PY-TN-005 END
