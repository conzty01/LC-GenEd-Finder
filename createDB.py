import psycopg2
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
def createRequirement(cursor):
    cursor.execute("DROP TABLE IF EXISTS requirement CASCADE;")
    cursor.execute("""

    CREATE TABLE requirement (
        id              serial,
        name            varchar(100),
        description     text,
        PRIMARY KEY (id)
    );

    """)
    genEds = ["Quantitative","Natural World—Lab","Wellness","Religion","Human Behavior","Human Behavior—Social Science Methods",
                "Intercultural","Human Expression","Historical","Natural World—Nonlab","Biblical Studies",
                "Human Expression—Primary Texts","Skills","Wellness"]

    for i in genEds:
        cursor.execute("INSERT INTO requirement (name) VALUES ('{}')".format(i))
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
def main():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    cur = conn.cursor()

    createCourse(cur)
    createRequirement(cur)
    createCourseReq(cur)

    conn.commit()

main()
