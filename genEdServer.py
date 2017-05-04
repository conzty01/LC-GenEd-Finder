from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import psycopg2
import json
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
conn = psycopg2.connect(os.environ["DATABASE_URL"])
@app.route("/")
def index():
    cur = conn.cursor()

    cur.execute("SELECT name FROM requirement;")

    return render_template("index.html",requirement=cur.fetchall())

@app.route("/<genEd>")
def searchGenEd(genEd):
    cur = conn.cursor()

    cur.execute("""
        SELECT num, title, department, name
        FROM course JOIN course_requirement ON(course.id = course_requirement.course)
             JOIN requirement ON(course_requirement.requirement = requirement.id)
        WHERE name = '{}'
    """.format(genEd))

    return render_template("result.html",results=cur.fetchall())

@app.route("/searchMult/", methods=["POST"])
def searchMultiple():
    cur = conn.cursor()
    queryStr = ""
    queryList = []

    for item in request.form:
        queryList.append(item)
        queryStr += "'{}' = ANY(req) AND ".format(item)

    queryStr = queryStr[:len(queryStr)-5]

    cur.execute("""
        SELECT course.num, course.department, c.title, req
        FROM (SELECT course.title, ARRAY_AGG(requirement.name) AS req
              FROM course JOIN course_requirement ON(course.id = course_requirement.course)
			              JOIN requirement ON(course_requirement.requirement = requirement.id)
              GROUP BY course.title) As c
              JOIN course ON(c.title = course.title)
        WHERE {}
        ORDER BY c.title ASC;

    """.format(queryStr))

    return render_template("result.html",results=cur.fetchall(),ql=queryList)

if __name__ == "__main__":
    app.run(debug=True)
