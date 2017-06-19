from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import psycopg2
import json
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

conn = psycopg2.connect(dbname="gened", user="conzty01")
#conn = psycopg2.connect(os.environ["DATABASE_URL"])
@app.route("/")
def splash():
    return render_template("splash.html")

@app.route("/index")
def index():
    cur = conn.cursor()

    cur.execute("SELECT name FROM requirement WHERE name != 'None';")

    return render_template("index.html",requirement=cur.fetchall())

@app.route("/searchMult/", methods=["POST"])
def searchMult():
    cur = conn.cursor()
    queryList = []
    searchStr = ""
    genEdStr = ""

    for i in request.form:
        print(i)
        if i != "search":
            queryList.append(i)
            genEdStr += "'{}' = ANY(req) AND \n".format(i)
        else:
            searchTerms = str(request.form[i]).split(",")

    if len(searchTerms) > 0 and searchTerms[0] != "":

        for i in range(len(searchTerms)):
            searchStr += "course.num LIKE "+"'%"+searchTerms[i]+"%'"+"OR \n"
            searchStr += "course.title LIKE "+"'%"+searchTerms[i]+"%'"+"OR \n"
            searchStr += "course.department LIKE "+"'%"+searchTerms[i]+"%'"+"OR \n"
            searchStr += "course.description LIKE "+"'%"+searchTerms[i]+"%'"+"OR \n"

        searchStr = searchStr[:-4]

    if searchStr == "":
        genEdStr = genEdStr[:-5]
    else:
        if len(queryList) > 0:
            genEdStr = genEdStr[:len(genEdStr)-5] + " OR \n"

    queryList += searchTerms

    cur.execute("""
        SELECT course.num, course.department, c.title, req
        FROM (SELECT course.title, ARRAY_AGG(DISTINCT requirement.name) AS req
              FROM course JOIN course_requirement ON(course.id = course_requirement.course)
                          JOIN requirement ON(course_requirement.requirement = requirement.id)
              GROUP BY course.title) As c
              JOIN course ON(c.title = course.title)
        WHERE {} {}
        ORDER BY ARRAY_LENGTH(req,1) DESC, c.title ASC;
    """.format(genEdStr, searchStr))

    return render_template("result.html",results=cur.fetchall(),ql=queryList)

if __name__ == "__main__":
    app.run(debug=True)
