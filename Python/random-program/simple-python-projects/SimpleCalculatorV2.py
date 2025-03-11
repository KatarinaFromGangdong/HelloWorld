# simple calculator v2 program by Engr.R
import time
print("\nWelcome user! Please enter a valid input to continue :). Thanks - Engr.R")
try:
    # get user input
    def MainMenu():
        x = int(input("\nNum1: "))
        y = int(input("Num2: "))
        while True:
            SelectedOperation = input(
                "\nSelect an operation to proceed: \n[1] Addition \n[2] Subtraction \n[3] Multiplication \n[4] Division \n[5] Cancel \nEnter: ")
            if SelectedOperation == "1":
                print("\nResult >>> ", Addition(x, y))
                CommandReturnToMainMenu()
            elif SelectedOperation == "2":
                print("\nResult >>> ", Subtraction(x, y))
                CommandReturnToMainMenu()
            elif SelectedOperation == "3":
                print("\nResult >>> ", Multiplication(x, y))
                CommandReturnToMainMenu()
            elif SelectedOperation == "4":
                print("\nResult >>> ", Division(x, y))
                CommandReturnToMainMenu()
            elif SelectedOperation == "5":
                print("Exiting...")
                MainMenu()

    def Addition(x, y):
        return x+y

    def Subtraction(x, y):
        return x-y

    def Multiplication(x, y):
        return x*y

    def Division(x, y):
        if y == 0:
            return "Error: Division by zero is not allowed"
        else:
            return x/y

    def CommandReturnToMainMenu():
        confirmation = input("Would you like to continue [y/n]?: ")
        if confirmation.lower() == "y":
            MainMenu()
        elif confirmation.lower() == "n":
            print("Thank you for using the calculator!")
            time.sleep(2)
            exit()
        else:
            print("Invalid input. Please try again.")
            CommandReturnToMainMenu()
    MainMenu()
except ValueError as error:
    print("Error 404: ", error)
    print("Error 404 {}".format(error))
    MainMenu()
#  this is the final program for simple calculator!
#  it is a simple program that can perform basic addition, subtraction, multiplication, and division operations
