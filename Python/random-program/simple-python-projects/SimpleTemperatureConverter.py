# 00041879 reference call for royal cable
# INFO! This simple program is design to convert temperature to desired output from the user - Engr.R
import time
import datetime
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(f"{Fore.RED}[INSTRUCTION] {Fore.WHITE}Please select from 1-3 options.")


def MainProgram():
    try:
        colorama.init(autoreset=True)
        while True:
            UserInput = int(input(
                f"\n{Fore.GREEN}[1] {Fore.WHITE}Celsius --> Fahrenheit \n{Fore.GREEN}[2] {Fore.WHITE}Fahrenheit --> Celsius \n{Fore.GREEN}[3] {Fore.WHITE}Quit \nPlease SELECT conversion type: "))
            if UserInput == 1:
                print(f"You have selected {Fore.CYAN}Celsius to Fahrenheit")
                celsius = float(input("Enter Temperature: "))
                print(f"{Fore.RED}Converted to:")
                print(Fahrenheit(celsius))
                Continuation()
            elif UserInput == 2:
                print(f"You have selected {Fore.CYAN}Fahrenheit to Celsius")
                fahrenheit = float(input("Enter Temperature: "))
                print(f"{Fore.RED}Converted to:")
                print(Celsius(fahrenheit))
                Continuation()
            elif UserInput == 3:
                print(f"{Fore.RED}Program Shutting Down!")
                exit()
            else:
                print(
                    f"{Fore.BLUE}[Warning] {Fore.YELLOW}Invalid input. Please try again.")
                MainProgram()
    except ValueError as error:
        print(f"{Fore.RED}[Error 404] {Fore.YELLOW+str(error)}")
        MainProgram()


def Fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    kelvin = (fahrenheit-32)*(5/9)+273.15
    rankine = fahrenheit + 459.67
    return f"{Fore.WHITE}Fahrenheit --> {Fore.RED+str(fahrenheit)} \n{Fore.WHITE}Kelvin --> {Fore.RED+str(kelvin)} \n{Fore.WHITE}Rankine --> {Fore.RED+str(rankine)}"


def Celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    kelvin = celsius + 273.15
    rankine = (celsius+273.15)*(9/5)
    return f"{Fore.WHITE}Fahrenheit --> {Fore.RED+str(celsius)} \n{Fore.WHITE}Kelvin --> {Fore.RED+str(kelvin)} \n{Fore.WHITE}Rankine --> {Fore.RED+str(rankine)}"


def Continuation():
    QuestionToUser = input("Would you like to continue [y/n]?: ")
    if QuestionToUser.lower() == "y":
        MainProgram()
    elif QuestionToUser.lower() == "n":
        print(
            f"{Fore.LIGHTYELLOW_EX}Thank you for using my simple converter :) - Engr.R")
        exit()
    else:
        print(
            f"{Fore.BLUE}[Warning] {Fore.YELLOW}Invalid input, please try again.")
        Continuation()


MainProgram()
