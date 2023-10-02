import string
from random import choice
from lib import send
#from New_passwordGenerator.main import showPassword
valid = string.ascii_letters + string.digits + "!£$?*"


"""def sendPassword(password):
    showPassword(password)"""


def createPassword(length):
    password = ""
    print("Creating password...")
    for i in range(length):
        password += choice(valid)
    send.showPassword(password)


def main(length):
    password = createPassword(length)
    send.showPassword(password)
