import users
import sys
import encryption
import googleDriveAPI

u= users
e= encryption
g= googleDriveAPI

#Function to generate menu for privileged (admin) user
def privilegeMenu():
    try:
        while True:
            #Menu system used to navigate the management console
            user_In = input("|U - Upload file | D - Download file | S - User settings | L - Log out | E - Exit|\n").lower()
            if(user_In == "s"):
                while True:
                    #Cases for creating or deleting users and creating a new key
                    user_In = input("|A - Add User | D - Delete User | N - Generate New Key | E - Exit to menu|\n").lower()
                    if (user_In == "a"):
                        u.newUser()
                        
                    elif(user_In == "d"):
                        u.deleteUser()
                        
                    elif(user_In == "N"):
                        e.keyGen()
                        break
                    elif(user_In == "e"):
                        break
                    else:
                        print("Wrong input try again\n")

            elif(user_In == "u"):
                while True:
                    #Upload file screen
                    print("\nEnsure that files you wish to upload are in the 'Files' folder.\nEnter m to return to main menu.\n")
                    user_In = input("Enter file name: ")
                    if(user_In == "m"):
                        break
                    else:
                       e.encrypt(user_In, e.keyRead())
                       g.uploadFile(user_In)

            elif(user_In == "e"):
                print("Exiting.")
                sys.exit()

            elif(user_In == "l"):
                #Logging out of admin account and setting admin bool to false
                u.privilege = False
                print("Logging out.")
                break

            elif(user_In == "d"):
                #Download file screen
                while True:
                    user_In = input("\n|S - Search for file | D - Download File | E - Exit to menu|\n").lower()
                    if(user_In == "s"):
                        #Incase you forgot the file name you can double check here
                        user_In = input("Enter file name: ")
                        g.searchFile(user_In)
                    elif(user_In == "d"):
                        #download file via file name
                        user_In = input("Enter file name: ")
                        fileID= g.fileID(user_In)
                        g.downloadFile(fileID, user_In)
                        e.decrypt(user_In, e.keyRead())
                    elif(user_In == "e"):
                        break
                    else:
                        print("Wrong input try again\n")
            else:
                 print("Wrong input try again\n")
               
               

    except Exception:
        pass

#Function which generates menu for standard non-privileged users
def standardMenu():
    try:
        while True:
            #Same as above minus the settings option
            user_In = input("|U - Upload file | D - Download file | L - Log Out | E - Exit|\n").lower()
            if(user_In == "u"):
                while True:
                    print("\nEnsure that files you wish to upload are in the 'Files' folder.\nEnter m to return to main menu.\n")
                    user_In = input("Enter file name: ")
                    if(user_In == "m"):
                        break
                    else:
                       e.encrypt(user_In, e.keyRead())
                       g.uploadFile(user_In)

            elif(user_In == "e"):
                print("Exiting.")
                sys.exit()

            elif(user_In == "l"):
                print("Logging out.")
                break

            elif(user_In == "d"):
                while True:
                    user_In = input("\n|S - Search for file | D - Download File | E - Exit to menu|\n").lower()
                    if(user_In == "s"):
                        user_In = input("Enter file name: ")
                        g.searchFile(user_In)
                    elif(user_In == "d"):
                        user_In = input("Enter file name: ")
                        fileID= g.fileID(user_In)
                        g.downloadFile(fileID, user_In)
                        e.decrypt(user_In, e.keyRead())
                    elif(user_In == "e"):
                        break
                    else:
                        print("Wrong input try again\n")
            else:
                 print("Wrong input try again\n")
               
               

    except Exception:
        pass