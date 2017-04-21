import psycopg2

conn = psycopg2.connect(dbname="conzty01",user="conzty01",host="knuth.luther.edu")

cur = conn.cursor()

cur.execute("""

CREATE TABLE lcCourse (
    id              serial,
    num             varchar(50),
    description     text,
    title           varchar(100),
    PRIMARY KEY (id)
);

""")

cur.execute("""

CREATE TABLE lcRequirement (
    id              serial,
    name            varchar(100),
    description     text,
    PRIMARY KEY (id)
);

""")

cur.execute("""

CREATE TABLE lcCourse_requirement (
    course          int,
    requirement     int,
    PRIMARY KEY (course, requirement),
    FOREIGN KEY (course) REFERENCES lcCourse(id),
    FOREIGN KEY (requirement) REFERENCES lcRequirement(id)
);

""")

conn.commit()
