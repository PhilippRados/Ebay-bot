import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()


def ausgabe():
    sql = "select * from Personen"
    cursor.execute(sql)
    print(type(cursor))
    for daten in cursor:
        print(daten[0], daten[1], daten[2], daten[3], daten[4])


def delete(sql):
    cursor.execute(sql)
    connection.commit()


def update():
    sql = "update Personen set vorname='Juergen' where personalnr=2529"
    cursor.execute(sql)
    connection.commit()


ausgabe()

connection.close()
