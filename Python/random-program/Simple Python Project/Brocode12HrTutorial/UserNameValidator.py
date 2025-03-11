# simple username validator

username = input("Enter valid username: ")
if len(username) > 12:
    print("username must 12 characters only.")
elif not username.find(" ") == -1:
    print("username must NOT contains space/s.")
elif not username.isalpha():
    print("username must NOT contains digits.")