import pickle
import sys
import getpass

def save_list(obj, name ):
    with open('Users/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_list(name):
    try:
        with open('Users/' + name + '.pkl', 'rb') as f:
          return pickle.load(f)
    except FileNotFoundError:
          return {}


users = load_list("list")
privelege = False

if not users:
    accounts = 0
else:
    accounts = 1

def newUser():   
    while True:
        createLogin = input("Create login name: ")
        if createLogin in users:
            print("\nLogin name already exist! Try again\n")
        else:
            createPassword = getpass.getpass("Create password: ")
            users[createLogin] = createPassword
            save_list(users, "list")
            print("\nUser created\n")
            break
 
def login():
    global privelege
    count = 0
    while True:
   
        login = input("Enter login name: ")
        password = getpass.getpass("Enter password: ")
 
        if login in users and users[login] == password and login == "admin":
            privelege = True
            print("\nLogin successful!\n")
            break
        elif login in users and users[login] == password:
            print("\nLogin successful!\n")
            break
        elif count == 3:
            print("\nToo many wrong tries. Goodbye!")
            sys.exit()
        else:
            count = count+1
            print("\nUser doesn't exist or wrong password! Try again.\n")

def deleteUser(userName):
    if username == "admin":
        print("Cannot delete the admin account.\n")
    elif userName in users:
        del users[userName]
        print("User deleted.\n")
    else:
        print("User name does not exist in network.\n")