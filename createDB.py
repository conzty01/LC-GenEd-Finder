import psycopg2

def createCourse(cursor):
    cursor.execute("DROP TABLE IF EXISTS lccourse CASCADE;")
    cursor.execute("""

    CREATE TABLE lccourse (
        id              serial,
        num             varchar(50),
        description     text,
        title           varchar(100),
        department      varchar(100),
        PRIMARY KEY (id)
    );

    """)
def createRequirement(cursor):
    cursor.execute("DROP TABLE IF EXISTS lcrequirement CASCADE;")
    cursor.execute("""

    CREATE TABLE lcrequirement (
        id              serial,
        name            varchar(100),
        description     text,
        PRIMARY KEY (id)
    );

    """)
    genEds = ["Quantitative","Natural World—Lab","Wellness","Religion","Human Behavior","Human Behavior—Social Science Methods",
                "Intercultural","Human Expression","Historical","Natural World—Nonlab","Biblical Studies",
                "Human Expression—Primary Texts","Skills","Paideia111/112","Language","Wellness","Paideia 450","Senior Project",
                "Ethical"]

    for i in genEds:
        cursor.execute("INSERT INTO lcrequirement (name) VALUES ('{}')".format(i))
def createCourseReq(cursor):
    cursor.execute("DROP TABLE IF EXISTS lccourse_requirement")
    cursor.execute("""

    CREATE TABLE lccourse_requirement (
        course          int,
        requirement     int,
        PRIMARY KEY (course, requirement),
        FOREIGN KEY (course) REFERENCES lcCourse(id),
        FOREIGN KEY (requirement) REFERENCES lcRequirement(id)
    );

    """)
def main():
    conn = psycopg2.connect(dbname="conzty01",user="conzty01",host="knuth.luther.edu")
    cur = conn.cursor()

    createCourse(cur)
    createRequirement(cur)
    createCourseReq(cur)


    conn.commit()

main()
