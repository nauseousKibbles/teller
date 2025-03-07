import dbclasses as db
from notifyclass import notify
import datetime
import os
import time
import sys


def reloadScreen():
    os.system("clear")


nowTime = datetime.datetime.now()

realAmPm = nowTime.strftime("%p").lower()
realMin = nowTime.strftime("%M")
realHour = nowTime.strftime("%I")
if realHour == "12":
    realHour = "00"

realFull = realHour + realMin

# Init
db.init("list.db")

# print(realFull)

# END VARS-------------------------------------------

# db.readTable().readAll()
# db.editTable().add("drifnk", "0530", "pm")
# db.editTable().deleteTask('drink')
# db.readTable().readTimeNow("0530")
##########################################
# print("All")
# db.readTable().readAll()
# print("----------")


# print(db.readTable().readAmpmAcording(str(realAmPm)))

# nowTask = db.readTable().readTaskAcording(str(realFull))
# if nowTask:
#     notify(nowTask)

def delTask():
    db.readTable().readAll()
    deledTask = input("What task do you want to delete? ")
    db.editTable().deleteTask(deledTask)
    reloadScreen()
    db.readTable().readAll()
    menu()


def createStuff():
    print("To leave just click enter.")
    print("How many tasks would you like to create? ")
    amn = input("")
    if amn == "":
        menu()
    reloadScreen()
    for x in range(0, int(amn)):
        wantTasks = input("What is the task? ")
        reloadScreen()
        wantHour = input("What is the hour? ex. 11, 12, 5. ")
        while wantHour.isdigit() == False:
            print('Try again, but without letters...')
            wantHour = input("What is the hour? ")

        while len(wantHour) > 2:
            wantHour = input("Whoops... What is the hour? ex. 12 or 5")

        reloadScreen()

        wantMin = input("What is the minute? ex. 00, 03, 55. ")
        while wantMin.isdigit() == False:
            print('Try again, but without letters...')
            wantMin = input("What is the minute? ")

        reloadScreen()

        if wantHour == "12":
            wantHour = "00"

        if str(len(wantHour)) == "1":
            wantHour = "0" + wantHour

        wantAmpm = input("Am or Pm? ")
        reloadScreen()

        wantTime = wantHour + wantMin

        db.editTable().add(wantTasks, wantTime, wantAmpm)

    db.readTable().readAll()
    menu()


def warningMode():
    nowTime = datetime.datetime.now()

    realAmPm = nowTime.strftime("%p").lower()
    realMin = nowTime.strftime("%M")
    realHour = nowTime.strftime("%I")
    if realHour == "12":
        realHour = "00"

    realFull = realHour + realMin
    # print(db.readTable().readAmpmAcording(realAmPm.lower()), realAmPm)

    if db.readTable().readAmpmAcording(realAmPm.lower()) and db.readTable().readTaskAcording(realFull):
        # print(db.readTable().readAmpmAcording(realAmPm.lower()))
        notify(db.readTable().readTaskAcording(realFull))
        print(db.readTable().readTaskAcording(realFull))
        time.sleep(30)

    # elif db.readTable().readAmpmAcording(realAmPm.lower()):
    #     print("Yee")


def menu():
    print("What would you like to do? ")
    print("1) Create Tasks. ")
    print("2) Delete A task.")
    print("3) Delete all tasks. ")
    print("4) Warning Mode. ")
    print("5) Help. ")
    print("6) Exit. ")
    menuo = input("")
    reloadScreen()

    if menuo.isdigit() == False:
        print("Please put in a number. ")
        menu()

    if menuo == "1":
        createStuff()

    if menuo == "2":
        delTask()

    if menuo == "3":
        omeun = input("Are you sure? y/n ")
        reloadScreen()
        if omeun == "y":
            db.editTable().deleteAll()

            db.readTable().readAll()
            menu()
        menu()

    if menuo == "4":
        db.readTable().readAll()
        try:
            while True:

                warningMode()
                time.sleep(5)

        except KeyboardInterrupt:
            menu()

    if menuo == "5":
        reloadScreen()
        print(
            "If you need help, please go to the github page. https://github.com/nauseousKibbles/teller")

        print("\n")
        menu()

    if menuo == "6":
        sys.exit()

    if menuo == "":
        reloadScreen()
        print("Woah, plase put something here...")
        menu()

    if int(menuo) > 6 and int(menuo) < 100000:
        reloadScreen()
        print("Too high.")
        menu()

    if int(menuo) > 100000:
        reloadScreen()
        print("WAY Too high.")
        time.sleep(0.5)
        print("What are you thinking?")
        time.sleep(0.5)
        print("\n")
        menu()


reloadScreen()
db.readTable().readAll()
menu()
db.closedb()
