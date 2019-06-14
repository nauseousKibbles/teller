import os
# Sends a notification to the notification thing on your distro.


def notify(mess, extra="Teller Notification"):
    message = "notify-send " + "'" + str(mess) + "' " + "'" + str(extra) + "'"
    message.replace("'", "")
    # print(message)

    os.system(message.replace(",", "").replace("(", "").replace(")", ""))
