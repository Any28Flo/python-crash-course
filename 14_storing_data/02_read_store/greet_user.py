from json_functions import read_json_data, parse_json_data


def get_stored_user(path):
    """Get stored user data if available"""
    if path.exists():
        content = path.read_text()
        user = read_json_data(content)
        return user
    else:
        return None


def get_data(msg):
    """Get the data for the user input"""
    return input(msg)


def get_new_username():
    """Creates a new user obj"""
    user = {}

    name = get_data("What is your name? ")
    username = get_data("What is your username? ")
    email = get_data("What is your email? ")

    user['name'] = name
    user['username'] = username
    user['email'] = email
    return user


def great_user(path):
    """Great the user by name."""

    user = get_stored_user(path)

    if user:
        print(f"Welcome back {user['name']}")
    else:
        new_user = get_new_username()
        # convert the data to json:

        content = parse_json_data(new_user)

        path.write_text(content)

        print(f"We'll remeber you when you come back, {new_user['name']}")
