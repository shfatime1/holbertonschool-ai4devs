def get_last_items(items, n):
    """Return the last n items from a list."""
    if n <= 0:
        return []
    return items[-n:]


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


def find_user(users, user_id):
    """Find a user by ID."""
    for user in users:
        if user["id"] == user_id:
            return user
    return None
