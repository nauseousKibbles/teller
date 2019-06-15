import os
# Sends a notification to the notification thing on your distro.


def notify(mess, extra="Teller Notification"):

    cleanMess = str(mess).replace("'", "").replace(
        "(", "").replace(")", "").replace(",", "")

    message = "notify-send " + "'" + \
        str(cleanMess) + "' " + "'" + str(extra) + "'"
    # message.replace("'", "")
    # print(message)
    print(cleanMess)
    os.system(message.replace(",", "").replace("(", "").replace(")", ""))
