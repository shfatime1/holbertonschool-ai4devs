# Bug 3: Runtime Exception

def get_user_info(users, user_id):
    user = users[user_id]

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

get_user_info(users, 5)
