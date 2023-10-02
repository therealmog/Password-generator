# Amogh NG
# new password generator

import random
import datetime
from lib import generate


def askForLength():
    length = 0

    while not (length > 5 and length < 50):
        try:
            length = int(input("What length do you want your password to be "))
        except ValueError:
            print("This value is not an integer.")

        if length < 5:
            print("The length has to be more than 5.")
        elif length > 50:
            print("The length has to be shorter than 50.")

    print("Ok.")
    generate.createPassword(length)


def main():
    askForLength()


main()
