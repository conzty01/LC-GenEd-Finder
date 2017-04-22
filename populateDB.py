import psycopg2
import json

def importFile(f):
    jsonFile = open(f,"r").read()
    return json.loads(jsonFile)

def formatTables(cur):
    cur.execute("DELETE FROM lccourse_requirement;")
    cur.execute("DELETE FROM lccourse;")

def popCourse(cur,courseDict):
    if courseDict["description"] != None:
        d = courseDict["description"].replace("'","''")
        executeStr = "INSERT INTO lccourse (num, title, department, description) VALUES ('{}', '{}', '{}', '{}');"\
                .format(courseDict["number"], courseDict["title"].replace("'","''"), courseDict["subject"], d)

        # if the description is None, then do not include the description so the value is set to null
    else:
        executeStr = "INSERT INTO lccourse (num, title, department) VALUES ('{}', '{}', '{}');"\
                .format(courseDict["number"], courseDict["title"].replace("'","''"), courseDict["subject"])

    cur.execute(executeStr)

def popCourseReq(cur,courseDict):
    executeStr = ""
    if len(courseDict["fulfills"]) > 0:
        for i in range(len(courseDict["fulfills"])):
            cur.execute("""

                SELECT course.id, req.id
                FROM (SELECT id FROM lccourse WHERE num = '{}') AS course,
                     (SELECT id FROM lcrequirement WHERE name = '{}') AS req

            """.format(courseDict["number"],courseDict["fulfills"][i]))

            temp = cur.fetchall()

            cur.execute("INSERT INTO lccourse_requirement (course, requirement) VALUES ('{}','{}')\n"\
                            .format(temp[0][0],temp[0][1]))

def popDB(conn,obj):
    cur = conn.cursor()
    formatTables(cur)

    for item in obj:
        popCourse(cur, item)
        popCourseReq(cur, item)

def main():
    conn = psycopg2.connect(dbname="conzty01",user="conzty01",host="knuth.luther.edu")

    jsonObj = importFile("gened.json")

    popDB(conn,jsonObj)
    conn.commit()

main()
