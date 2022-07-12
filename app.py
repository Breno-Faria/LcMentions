from flask import Flask, render_template, request
import os
from db import conn

import psycopg2

app = Flask(__name__, static_folder="static")

def connect_to_db():
    connection = psycopg2.connect(
        host=os.environ['host'],
        database=os.environ['database'],
        port=os.environ['port'],
        user=os.environ['user'],
        password=os.environ['password'],
    )
    return connection

@app.route("/")
def home():
	connection = connect_to_db()
	cursor = connection.cursor()
	cursor.execute(
		"select title, count from problems ORDER BY count desc LIMIT 50"
	)
	problems = cursor.fetchall()
	cursor.close()
	connection.close()
	return render_template("index.html", problems=problems)