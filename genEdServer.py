from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import psycopg2
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
conn = psycopg2.connect(dbname="conzty01",user="conzty01")

@app.route("/")
def index():
    cur = conn.cursor()

    cur.execute("SELECT name FROM requirement;")

    return render_template("index.html", requirement=cur.fetchall())

app.run(debug=True)
