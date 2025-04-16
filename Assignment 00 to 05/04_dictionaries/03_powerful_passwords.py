import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
    "user@gmail.com": hash_password("password123"),
    "admin@gmail.com": hash_password("adminpass"),
}

def login(mail, password):
    if email in stored_logins:
        return stored_logins[mail] == hash_password(password)
    return False

if __name__ == "__main__":
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password):
        print("Login successful!")
    else:
        print("Invalid email or password.")