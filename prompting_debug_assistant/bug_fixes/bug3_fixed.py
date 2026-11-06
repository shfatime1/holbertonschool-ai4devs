def get_user_info(users, user_id):
    user = users.get(user_id)

    if user is None:
        print("User not found")
        return None

    name = user["name"]
    email = user["email"]

    print("User:", name)
    print("Email:", email)

    return {
        "name": name,
        "email": email
    }


users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

assert get_user_info(users, 1)["name"] == "Alice"
assert get_user_info(users, 2)["name"] == "Bob"
assert get_user_info(users, 5) is None
