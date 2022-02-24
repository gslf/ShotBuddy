import time
import unittest

from tests.sessionManagementTests import TestSessionManagement
from tests.userManagementTests import TestUserManagement

def mainMenu():
    while True:
        print("")
        print("#######################")
        print("#      ShotBuddy      #")
        print("#    Testing Tools    #")
        print("#######################")
        print("")

        print("Menu:")
        print("1. Run all tests")
        print("2. Run sessions management tests")
        print("3. Run user management tests")
        print("q. Quit")
        print("")

        query = input("Choose & Enter query number available in the menu: ")

        if query == "1":
             unittest.main(TestUserManagement(), exit = False) 
             unittest.main(TestSessionManagement(), exit = False)

        elif query == "2":
             unittest.main(TestSessionManagement(), exit = False)

        elif query == "3":
             unittest.main(TestUserManagement(), exit = False) 

        elif query == "q":
                break
        else:
            print("Command not recognized, try again!")
            time.sleep(3)


if __name__ == "__main__":
    mainMenu()