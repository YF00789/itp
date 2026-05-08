import re
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[SYSTEM LOG] Executing {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper
def validate_expression(expression: str) -> tuple:
    pattern = r"^\s*([-+]?\d*\.?\d+)\s*([\+\-\*/\^])\s*([-+]?\d*\.?\d+)\s*$"
    match = re.match(pattern, expression)
    if not match:
        raise ValueError("Invalid format. Use 'Number Operator Number'.")
    return float(match.group(1)), match.group(2), float(match.group(3))
def filter_and_format_history(history: list, target_op: str) -> list:
    filtered = filter(lambda x: x['op'] == target_op, history)
    formatted = map(lambda x: f"Result: {x['result']}", filtered)
    return list(formatted)