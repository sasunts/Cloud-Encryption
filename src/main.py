import googleDriveAPI
import users
import menuTypes


def main():
    u = users
    m = menuTypes
    
    u.login()

    #TODO
    if u.privelege:
        m.privelegeMenu()
    else:
        print("Non priveleged menu")





if __name__ == "__main__":
    main()