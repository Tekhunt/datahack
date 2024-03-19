def validate_name(name):
    if not name:
        return False
    if not isinstance(name, str):
        return False
    if len(name) < 1 or len(name) > 100:
        return False
    return True

print(validate_name('Hello world!'))