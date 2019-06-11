import csv
import time
import datetime
import os

# Fieldnames for csv file
fieldnames = ['task','time','ampm']

# Uses datetime to get the current time
nowTime = datetime.datetime.now()

realAmPm = nowTime.strftime("%p")
realMin = nowTime.strftime("%M")
realHour = nowTime.strftime("%I")
realFull = realHour + realMin

# Notify function
def notify(header,desc="Teller Alert"):
    text = "notify-send " + "'" + header + "'" + " " + "'" + desc + "'"
    os.system(text)

# Creates a csv file if none are found
def createCsv():
    exists = os.path.isfile('list.csv')
    if exists:
        return

    with open("list.csv",'w') as f:
        f.write("task,time,ampm")

# Checks time verses user's time
def checkTasks():
    nowTime = datetime.datetime.now()

    realAmPm = nowTime.strftime("%p")
    realMin = nowTime.strftime("%M")
    realHour = nowTime.strftime("%I")
    realFull = realHour + realMin
    if realHour == '12':
        realHour = '0'


    with open('list.csv','r') as listfile:
        reader = csv.DictReader(listfile)

        for row in reader:

            # w in the front
            # means want
            wtask = row['task']
            wtime = row['time']
            wampm = row['ampm']
            
            if realFull == wtime and realAmPm.lower() == wampm.lower():
                print("Yep ", wtask, " is due")
                notify(wtask,wtime)


# It asks user what tasks, time, and am or pm, and it gets number
# of tasks from menu() function.
def createTasks(numberOfTasks):
    global fieldnames

    for x in range(0,numberOfTasks):
        w = input("What is your task?: ")
        print("The time should be like this. ex: 1200 or 531")
        h = input("What hour?: ")
        m = input("What min?: ")
        ap = input("Am or Pm?: ")

        with open('list.csv','a') as listfile:
            writer = csv.DictWriter(listfile, fieldnames=fieldnames)
            if h == "12":
                h = "00"

            if len(h) == 1:
                h = '0' + h

            hmin = str(h) + str(m)
            
            writer.writerow({'task': w, 'time': hmin, 'ampm': ap})
            
            
# Reads all of the tasks
def readTasks():
    with open('list.csv','r') as listfile:
        reader = csv.DictReader(listfile)

        for row in reader:
            print(row['task'], row['time'],row['ampm'])   


# Is the starting point and asks user for what
# they want to do.    
def menu():
    print('What would you like to do?')
    print('1) Create Tasks')
    print('2) Background mode, check time verses your time and alerts you.')
    print("3) Delete all tasks. ")
    task = input("")
    
    if task == '1':
        createAmount = input("How many would you like to create?: ")
        #try:
        createTasks(int(createAmount))
        #except:
            #print("\n")
            #print('There was an error. Retuning back to menu...')
            #menu()

    if task == '2':
        print("Use control + c to exit. ")
        try:
            while True:
                checkTasks()
                time.sleep(5)
        except KeyboardInterrupt:
            menu()

    if task == "3":
        print("are you sure? y/n ")
        yes = input("")

        if yes == "y":
            with open("list.csv",'w') as f:
                f.write("task,time,ampm")


# The begining of the program
if __name__ == '__main__':
    
    createCsv()
    readTasks()
    menu()
    