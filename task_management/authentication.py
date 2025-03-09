from hashlib import sha256

def save_credentials(username, password):
    with open('user_credentials.txt', 'a') as file:
        hashed_password = sha256(password.encode()).hexdigest()
        file.write(f"{username}:{hashed_password}\n")
    print("Registration successful!")

def load_credentials():
    user_credentials = {}
    try:
        with open('user_credentials.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                username, hashed_password = line.strip().split(':')
                user_credentials[username] = hashed_password
    except FileNotFoundError:
        pass  # If the file doesn't exist initially, handle the exception
    return user_credentials

user_credentials = load_credentials()  # Load user credentials when the system starts

def save_user_credentials():
    with open('user_credentials.txt', 'w') as file:
        for username, hashed_password in user_credentials.items():
            file.write(f"{username}:{hashed_password}\n")

def user_registration():
    print("Register a new account")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_credentials[username] = sha256(password.encode()).hexdigest()
    save_credentials(username, password)
    save_user_credentials()  # Save updated credentials to the file
    print("Registration successful!")

def user_login():
    print("Login")
    username = input("Enter username: ")
    password = input("Enter password: ")
    stored_password = user_credentials.get(username)
    if stored_password and stored_password == sha256(password.encode()).hexdigest():
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
