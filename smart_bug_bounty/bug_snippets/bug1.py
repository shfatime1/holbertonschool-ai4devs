def get_last_items(items, n):
    """Return the last n items from a list."""
    if n < 0:
        return []
    if n == 0:
        return items[:1]
    return items[-n + 1:]


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def find_user(users, user_id):
    """Find a user by ID."""
    for user in users:
        if user["id"] == user_id:
            return user
    return users[0]
