import sqlite3


def init(dbName):
    global conn, c
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    try:
        c.execute("CREATE TABLE list (task text, time text, ampm text)")
        conn.commit()

    except:
        pass


def closedb():
    global conn, c
    conn.close()


class editTable:
    global conn, c

    def add(self, task, time, ampm):
        global conn, c
        c.execute("INSERT INTO list VALUES (?,?,?)", (task, time, ampm))
        conn.commit()

    def deleteTask(self, task):
        global conn, c
        c.execute("DELETE FROM list WHERE task = ?", [task])
        conn.commit()

    def deleteAll(self):
        global conn, c
        c.execute("DELETE FROM list")
        conn.commit()


class readTable:
    global conn, c

    def readAll(self):
        global conn, c
        c.execute("SELECT * FROM list")
        print(c.fetchall())

    def readTimeNow(self, nTime):
        global conn, c
        c.execute("SELECT * FROM list WHERE time=?", [nTime])
        print(c.fetchall())
    # Acording to the TIME row/collum

    def readTaskAcording(self, nTime):
        global conn, c
        c.execute("SELECT task FROM list WHERE time=?", [nTime])
        # print(c.fetchone())
        return c.fetchall()
    # Acording to the AMPM row/collum

    def readAmpmAcording(self, nTime):
        global conn, c
        c.execute("SELECT task FROM list WHERE ampm=?", [nTime])
        # print(c.fetchone())
        return c.fetchall()
