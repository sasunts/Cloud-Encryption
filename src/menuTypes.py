import users
import sys

u= users


def privelegeMenu():
    try:
        while True:
            #Menu system used to navigate the management console
            user_In = input("|U - Upload file | D - Download file | S - User settings | E - Exit|\n").lower()
            if(user_In == "s"):

                user_In = input("|A - Add User | D - Delete User | E - Exit|\n").lower()
                if (user_In == "a"):
                    u.newUser()
                else:
                    u.deleteUser()

            elif(user_In == "u"):
                t=1

            elif(user_In == "e"):
                print("Exiting.")
                sys.exit()

            elif(user_In == "d"):
                print("download...")
                sys.exit()

            else:
                 print("Wrong input try again\n")
               
               

    except Exception:
        pass