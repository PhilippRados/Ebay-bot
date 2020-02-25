import sqlite3
import os
import sys

dat = "test.db"

# if os.path.exists(dat):
#     print(f"{dat} existiert bereits")
#     sys.exit(0)

connection = sqlite3.Connection(dat)

cursor = connection.cursor()


def creating_table():
    sql = "create table Personen("\
        "name text, "\
        "vorname text, "\
        "personalnr integer primary key,"\
        "gehalt real, "\
        "gb text)"
    cursor.execute(sql)


def adding(name, vorname, personalnr, gehalt, gb):
    sql = f"insert into Personen values('{name}',"\
        f"'{vorname}',{personalnr},{gehalt},'{gb}')"

    cursor.execute(sql)
    connection.commit()


#adding('Kreuz', 'Joachim', 8325, 1294, '1.11.1752')
adding('Kreuz', 'Maria', 2325, 3819, '12.05.1952')
connection.close()
