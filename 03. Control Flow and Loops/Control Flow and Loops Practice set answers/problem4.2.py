password = "Y2k123"
entered_pass = input("Enter Password: ")

while (entered_pass != password):
    entered_pass = input("Wrong Password! Try again and enter Password: ")

print("Success! You are logged in")
