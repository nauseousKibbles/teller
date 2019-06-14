import dbclasses as db
from notifyclass import notify
import datetime
import os
import time


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


def createStuff():
    print("To leave just exit.")
    print("How many tasks would you like to create? ")
    amn = input("")
    reloadScreen()
    for x in range(0, int(amn)):
        wantTasks = input("What is the task? ")
        reloadScreen()
        wantHour = input("What is the hour? ")
        reloadScreen()
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
        time.sleep(30)

    # elif db.readTable().readAmpmAcording(realAmPm.lower()):
    #     print("Yee")


def menu():
    print("What would you like to do? ")
    print("1) Create Tasks. ")
    print("2) Delete all tasks. ")
    print("3) Warning Mode. ")
    print("4) Help. ")
    print("5) Exit. ")
    menuo = input("")
    reloadScreen()

    if menuo == "1":
        createStuff()
    if menuo == "2":
        omeun = input("Are you sure? y/n ")
        reloadScreen()
        if omeun == "y":
            db.editTable().deleteAll()
            print("del")
            menu()
        menu()

    if menuo == "3":
        try:
            while True:
                warningMode()

        except KeyboardInterrupt:
            menu()


reloadScreen()
db.readTable().readAll()
menu()
db.closedb()
