# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_str(val):
    if isinstance(val, bool):
        return "Yes" if val else "No"

print(bool_str(False))
