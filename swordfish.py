password_file = open("SecretPasswordFile.txt")
password = password_file.read()

print("Enter your password:")
user_input = input()

if user_input == password:  # (!) if input() == password:
    print("Access granted!")

    if password == "123456":
        print("- You should set a new password!!!")
elif user_input == "admin":
    print("Welcome to the jungle.. :)")
else:
    print("Access denied!")
