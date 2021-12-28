import time

from tests.sessionManagementTests import sessionManagementTests
from tests.userManagementTests import userManagementTests

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
            sessionManagementTests()
            userManagementTests()

        elif query == "2":
            sessionManagementTests()

        elif query == "3":
            userManagementTests()

        elif query == "q":
                break
        else:
            print("Command not recognized, try again!")
            time.sleep(3)


if __name__ == "__main__":
    mainMenu()