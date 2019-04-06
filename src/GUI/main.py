import googleDriveAPI
import users
import menuTypes
import encryption
import eel

eel.init('web')

loop = False


def main():
    print("starting")
    global loop
   
    u = users

    try:
        while True:
            if(u.status == 1):
                eel.loginSuccess()
                if(u.privilege == True):
                    eel.privMenu()
                    while True:
                        if not loop:
                            eel.sleep(1)
                        else:
                            loop = False
                            break
                else:
                    eel.standardMenu()
                    while True:
                        if not loop:
                            eel.sleep(1)
                        else:
                            loop = False
                            break
            elif(u.status == -1):
                eel.loginTry()
                  

            eel.sleep(1)      
    except Exception:
        pass


@eel.expose
def loopBreak():
    global loop 
    loop = True

@eel.expose
def printToConsole(string):
    print(string)

eel.start('index.html', block=False)
if __name__ == '__main__':
    main()