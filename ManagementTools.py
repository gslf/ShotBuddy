import time

from webapp.DBManager import DBManager
from webapp.UsersManager import UsersManager
from webapp.User import User

def mainMenu():
    while True:
        print("")
        print("###########################")
        print("#         ShotBuddy       #")
        print("#     Management Tools    #")
        print("###########################")
        print("")

        print("Menu:")
        print("1. User Management")
        print("2. Session Management")
        print("q. Quit")
        print("")
        
        query = input("Choose & Enter query number available in the menu: ")

        if query == "1":
            userManagement()
        elif query == "q":
                break
        else:
            print("Command not recognized, try again!")
            time.sleep(3)

def userManagement():
    print("")
    print(" >>>>>  USER MANAGEMENT <<<<< ")
    print("")

    print("1. Add New User")
    print("2. Change User Password")
    print("3. Remove User")
    print("4. Show all users")
    print("q. Quit")
    print("")
    
    query = input("Choose & Enter query number available in the menu: ")

    if query == "1":
        username = input("Username: ")
        pwd = input("Password: ")

        user = User(username)
        um = UsersManager(user)
        um.add(pwd)

        input("Press any key to continue")

    elif query == "2":
        username = input("Username: ")
        pwd = input("Password: ")

        user = User(username)
        um = UsersManager(user)
        um.newPassword(pwd)

        input("Press any key to continue")

    elif query == "3":
        username = input("Username: ")

        user = User(username)
        um = UsersManager(user)
        um.remove()

        input("Press any key to continue")

    elif query == "4":
        um = UsersManager()
        userList = um.getAll()
        
        for user in userList:
            print ("User #{}: {}".format(user.id, user.username))

        input("Press any key to continue")
        
    elif query == "q":
            return
    else:
        print("Command not recognized, try again!")
        time.sleep(3)



if __name__ == "__main__":
    mainMenu()