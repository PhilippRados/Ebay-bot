import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False


@app.route('/personen/api/v1.0/info', methods=['GET'])
def get_all():
    try:
        connection = sqlite3.connect("test.db")
        cursor = connection.cursor()
    except:
        print("Couldnt access test.db")

    sql = "select * from Personen"
    cursor.execute(sql)
    Daten = [{"ID": f"{daten[2]}", "name": daten[0], "vorname":daten[1], "Geld":{"gehalt": f"{daten[3]}$", "Geburtstag": daten[4]}}
             for daten in cursor]
    connection.close()

    return jsonify({"informationen": Daten})


@app.route("/personen/api/v1.0/info/<int:personalnr>", methods=['GET'])
def get_by_id(personalnr):
    try:
        connection = sqlite3.connect("test.db")
        cursor = connection.cursor()
    except:
        print("Couldnt access test.db")

    sql = f"select * from Personen where personalnr = '{personalnr}'"
    cursor.execute(sql)
    Daten = [
        {"Name": daten[0], "Vorname":daten[1]}for daten in cursor
    ]

    return jsonify(Daten)


app.run()
