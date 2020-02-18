import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/personen/api/v1.0/info', methods=['GET'])
def get_name():
    try:
        connection = sqlite3.connect("test.db")
        cursor = connection.cursor()
    except:
        print("Couldnt access test.db")

    sql = "select * from Personen"
    cursor.execute(sql)
    Daten = [{"ID": daten[2], "name": daten[0], "vorname":daten[1], }
             for daten in cursor]
    connection.close()

    return jsonify({"informationen": Daten})


# @approute("/personen/api", methods=["POST"])
# def add_new():


app.run()
