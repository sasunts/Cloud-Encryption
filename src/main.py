import googleDriveAPI
import users
import menuTypes
import encryption


def main():
    e = encryption
    key = e.keyRead()
    try:
        while True:
            u = users
            m = menuTypes
            if(u.accounts == 0):
                print("\nYou must create an admin account. Please set username as 'admin'\n")
                u.newUser()
            else:
                u.login()

                if u.privelege:
                    m.privelegeMenu()
                else:
                    m.standardMenu()

    except Exception:
        pass


if __name__ == "__main__":
   main()