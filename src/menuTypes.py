import users
import sys
import encryption
import googleDriveAPI

u= users
e= encryption
g= googleDriveAPI

def privelegeMenu():
    try:
        while True:
            #Menu system used to navigate the management console
            user_In = input("|U - Upload file | D - Download file | S - User settings | E - Exit|\n").lower()
            if(user_In == "s"):
                while True:
                    user_In = input("|A - Add User | D - Delete User | N - Generate New Key | E - Exit to menu|\n").lower()
                    if (user_In == "a"):
                        u.newUser()
                        break
                    elif(user_In == "d"):
                        u.deleteUser()
                        break
                    elif(user_In == "N"):
                        e.keyGen()
                        break
                    elif(user_In == "e"):
                        break
                    else:
                        print("Wrong input try again\n")

            elif(user_In == "u"):
                while True:
                    print("\nEnsure that files you wish to upload are in the 'Files' folder.\nEnter m to return to main menu.")
                    user_In = input("Enter file name: ")
                    if(user_In == "m"):
                        break
                    else:
                        #encrypt here then upload
                        g.uploadFile(fileName)

            elif(user_In == "e"):
                print("Exiting.")
                sys.exit()

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
                        #decrypt file here
                    elif(user_In == "e"):
                        break
                    else:
                        print("Wrong input try again\n")

            else:
                 print("Wrong input try again\n")
               
               

    except Exception:
        pass