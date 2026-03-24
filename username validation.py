p = 0

username = input("Enter your username: ")
if len(username) > 13 :
    print("Username too long")
    p = 1
if username.find(" ") > -1 :
    print("Username cannot have spaces")
    p = 1
if username.isdigit():
    print("Username cannot have digits")
    p = 1
if p == 0:
    print("Username Vaild")
