def auth():
    
    name = input("Enter username: ")
    password = input("Enter password: ")

    if name == "admin" and password == "1234":
        print("Authentication successful!")
    else:
        print("Invalid username or password!")