def check_key(message, password_key):

    new_key = ""
    i = 0

    for _ in message:
        new_key += password_key[i]
        i = (i + 1) % len(password_key)

    return new_key.upper()