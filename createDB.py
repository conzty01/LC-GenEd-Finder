import psycopg2
import json
import os

def createCourse(cursor):
    cursor.execute("DROP TABLE IF EXISTS course CASCADE;")
    cursor.execute("""

    CREATE TABLE course (
        id              serial,
        num             varchar(50),
        description     text,
        title           varchar(100),
        department      varchar(100),
        PRIMARY KEY (id)
    );

    """)
def createRequirement(cursor,fName):
    cursor.execute("DROP TABLE IF EXISTS requirement CASCADE;")
    cursor.execute("""

    CREATE TABLE requirement (
        id              serial,
        name            varchar(100),
        description     text,
        PRIMARY KEY (id)
    );

    """)

    genEds = getGenEdSet(fName)
    #print(genEds)

    for i in genEds:
        cursor.execute("INSERT INTO requirement (name) VALUES ('{}')".format(i))

    # Adds a 'None' requirement that will connect to courses that satisfy none
    cursor.execute("INSERT INTO requirement (name) VALUES ('None')")
def createCourseReq(cursor):
    cursor.execute("DROP TABLE IF EXISTS course_requirement")
    cursor.execute("""

    CREATE TABLE course_requirement (
        course          int,
        requirement     int,
        PRIMARY KEY (course, requirement),
        FOREIGN KEY (course) REFERENCES course(id),
        FOREIGN KEY (requirement) REFERENCES requirement(id)
    );

    """)
def getGenEdSet(fName):
    genEds = set()
    f = open(fName,"r").read()

    jsonFile = json.loads(f)

    for course in jsonFile:
        for ge in course["fulfills"]:
            genEds.add(ge)

    return genEds

def run(f):
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    #conn = psycopg2.connect(dbname="gened", user="conzty01")
    cur = conn.cursor()

    print("creating 'course' table")
    createCourse(cur)
    print("creating 'requirement' table")
    createRequirement(cur,f)
    print("creating 'courseReq' table")
    createCourseReq(cur)
    print("commiting tables")
    conn.commit()
    print("finished creation")

if __name__ == "__main__":
    run("lcCourses.json")
