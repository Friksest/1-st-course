def signIn(username, password):
    # Define a list of dictionaries that contains the correct username and password for 3 users
    users = [
        {'username': 'user1', 'password': 'pass1'},
        {'username': 'user2', 'password': 'pass2'},
        {'username': 'user3', 'password': 'pass3'}
    ]
    
    # Loop through the list of users to find a match for the given username and password
    for user in users:
        if user['username'] == username and user['password'] == password:
            # If a match is found, return the dictionary that represents that user
            return user
    
    # If no match is found, return None
    return None



result = signIn('user1', 'pass5')
if result:
    print(f"User {result['username']} signed in successfully.")
else:
    print("Invalid username or password.")