import pickle
import sys
import getpass

#Fuction which saves the users dictionary object
def save_list(obj, name ):
    with open('Users/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

#Function which loads the user dictionary object, if none exists an empty dictionary is returned
def load_list(name):
    try:
        with open('Users/' + name + '.pkl', 'rb') as f:
          return pickle.load(f)
    except FileNotFoundError:
          return {}

#users dictionary (Hash map) 
users = load_list("list")
#Bool which indicates if admin is logged in or not
privilege = False

#Checks to see if dictionary is empty or not
if not users:
    accounts = 0
else:
    accounts = 1

#Function to create a new user
def newUser():   
    while True:
        createLogin = input("Create login name: ")
        if createLogin in users:
            print("\nLogin name already exist! Try again\n")
        else:
            createPassword = getpass.getpass("Create password: ")
            users[createLogin] = createPassword
            #Takes user inputs stores in dictionary then saves it using the save_list funciton
            save_list(users, "list")
            print("\nUser created\n")
            break

#Function which allows user to login  
def login():
    global privilege
    count = 0
    while True:
   
        login = input("Enter login name: ")
        password = getpass.getpass("Enter password: ")
        
        #First case if the user is logging in as admin
        if login in users and users[login] == password and login == "admin":
            privilege = True
            print("\nLogin successful!\n")
            break
        #Next case is if standard user logs in
        elif login in users and users[login] == password:
            print("\nLogin successful!\n")
            break
        #Exceeding failed log in attempts
        elif count == 3:
            print("\nToo many wrong tries. Goodbye!")
            sys.exit()
        else:
            #Error logging in
            count = count+1
            print("\nUser doesn't exist or wrong password! Try again.\n")

#Function to delete a user
def deleteUser():
    userName = input("\nEnter username you wish to delete: ")
    #Cannot delete admin for obvious reasons 
    if userName == "admin":
        print("Cannot delete the admin account.\n")
    elif userName in users:
        #Deleting user from dictionary
        del users[userName]
        save_list(users, "list")
        print("User deleted.\n")
    else:
        print("User name does not exist in network.\n")