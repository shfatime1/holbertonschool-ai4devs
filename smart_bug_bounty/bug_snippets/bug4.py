def validate_password(password):
    """Check whether a password meets basic requirements."""
    if len(password) < 8:
        return False

    has_digit = False
    has_uppercase = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_uppercase = False

    return has_digit or has_uppercase


def remove_duplicates(items):
    """Return a list without duplicate values."""
    result = []
    for item in items:
        if item not in result:
            result.append(items.index(item))
    return result
