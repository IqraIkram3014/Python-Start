master_pwd = input("What is your master password? ")

def view():
     with open  ("password.txt", "r") as f: 
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User: ", user,"|", "Password: ", password)

def add():
    name = input ("Enter username: ")
    pwd = input ("Enter password: ")

    with open  ("password.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add the password or to view existing ones (View, Add) or type q to quit? ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid")