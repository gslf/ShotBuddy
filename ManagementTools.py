import time

from webapp.DBManager import DBManager
from webapp.UsersManager import UsersManager
from webapp.User import User
from webapp.SessionsManager import SessionsManager
from webapp.Session import Session

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
        elif query == "2":
            sessionManagement()
        elif query == "q":
                break
        else:
            print("Command not recognized, try again !")
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

def sessionManagement():
    print("")
    print(" >>>>>  SESSION MANAGEMENT <<<<< ")
    print("")

    print("1. Add New Session")
    print("2. Edit Session")
    print("3. Remove Session")
    print("4. Show all Sessions")
    print("q. Quit")
    print("")

    query = input("Choose & Enter query number available in the menu: ")

    if query == "1":
        # Create a new session
        id_user = input("ID User: ")
        percentage_target = input("Percentage target: ") 
        shots = input("Shots [x,y,z]: ") 
        duration = input("Duration: ")

        sm = SessionsManager(id_user)
        result = sm.new(id_user, percentage_target, shots, duration)
        print("Creation result: {}".format(result))

        input("Press any key to continue")

    elif query == "2":
        # Update values of a session
        id_session = input("ID Session: ")
        id_user = input("ID User: ")
        percentage_target = input("Percentage target: ") 
        shots = input("Shots [x,y,z]: ") 
        duration = input("Duration: ")
        
        sm = SessionsManager(id_user)
        loading_result = sm.load(id_session)
        print("Loading result: {}".format(loading_result))
        
        sm.session.id_user = id_user
        sm.session.percentage_target = percentage_target
        sm.session.shots = shots
        sm.session.duration = duration

        saving_result = sm.save()
        print("Saving result: {}".format(saving_result))

        input("Press any key to continue")

    elif query == "3":
        # Remove a session
        id_session = input("ID Session: ")
        id_user = input("ID User: ")
        sm = SessionsManager(id_user)
        sm.session = Session(0,0,0,0,id=id_session)
        result = sm.remove()
        print("Remove result: {}".format(result))

        input("Press any key to continue")

    elif query == "4":
        # Show all sessions
        id_user = input("ID User: ")

        sm = SessionsManager(id_user)
        session_ids = sm.list()

        for session_id in session_ids:
            session = sm.load(session_id)
            print("Session #{} - user {} - percentage target: {} - shots: {} - duration: {}".format(session.id, session.id_user, session.percentage_target, session.shots, session.duration))
        
        input("Press any key to continue")

    elif query == "q":
            return
    else:
        print("Command not recognized, try again!")
        time.sleep(3)
        return



if __name__ == "__main__":
    mainMenu()