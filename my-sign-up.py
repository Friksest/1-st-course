from os import system

system("clear")
def signUp(username, email, password):
    def ifLatinAndDigits(username):
        latin_lower_alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        latin_upper_alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        # latin_alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for char in username:
            if char in latin_lower_alphabet or char in latin_upper_alphabet or char in digits:
                return True
            else:
                return False
         
    if not isinstance(username, str) or not isinstance(email, str) or not isinstance(password, str):
        raise TypeError("All inputs must be strings")
    if not (5 <= len(username) <= 12) or not ifLatinAndDigits(username):
        raise ValueError("Username must be 5-12 characters and contain only letters and digits")
    if "@" not in email or "." not in email:
        raise ValueError("Email must be valid")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")

    user_info = {'username': username, 'email': email, 'password': password}
    return user_info



username = input("Add the username: ")
email = input("Add the email: ")
password = input("Add the password: ")

# signUp(username, email, password)

print(signUp(username, email, password))
