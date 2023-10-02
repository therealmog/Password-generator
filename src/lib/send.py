# from New_passwordGenerator.src import main
import datetime


def showPassword(password):
    print("Your password is " + password)

    date = str(datetime.datetime.now())
    date = date + " "
    lenToCut = len(date) - 8
    date = str(date[0:lenToCut])
    date = date.replace(":", "-")
    firstPart = date[0:10]
    lastPart = date[11:]
    date = firstPart+" at "+lastPart

    toWrite = "Your password is " + password + f"\nGenerated on {date}"
    fileName = f"New_passwordGenerator//src//Saved//Password {date}.txt"

    with open(fileName, "a") as f:
        f.write(toWrite)

    print("This has been written to a file with the the current date and time.")
