import googleDriveAPI
import users

def main():

    u = users
    u.login()

    #TODO
    if u.privelege:
        print("MENU")
    else:
        print("Non priveleged menu")
    print(u.privelege)





if __name__ == "__main__":
    main()