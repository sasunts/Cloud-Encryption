import googleDriveAPI
import users
import menuTypes


def main():
    try:
        u = users
        m = menuTypes
    
        u.login()

        #TODO
        if u.privelege:
            m.privelegeMenu()
        else:
            print("Non priveleged menu")
    except Exception:
        pass


if __name__ == "__main__":
    main()