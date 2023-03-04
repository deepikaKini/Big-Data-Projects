import pandas as p
import numpy as np
import psycopg2
import time


def genre(conn, cursor):
    # sql statement to create genre table
    print("genre run")
    sql = '''
        CREATE TABLE IF NOT EXISTS GENRE(
        ID INTEGER  PRIMARY KEY,
        GENRE VARCHAR(20)
        )'''

    cursor.execute(sql)
    conn.commit()
    cursor.execute("""SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'public'""")
    for table in cursor.fetchall():
        print(table)
    #transfer the file from a csv to database. This file was created in project1
    sql = "COPY genre(genre,id) FROM STDIN DELIMITER ',' CSV HEADER"
    cursor.copy_expert(sql, open("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/unique_genre.csv", "r"))
    conn.commit()
    #genre title mapping table
    sql = '''
            CREATE TABLE IF NOT EXISTS TITLE_GENRE(
            TITLE VARCHAR(20),
            GENRE INTEGER,
             FOREIGN KEY(TITLE) REFERENCES TITLE(id),
            FOREIGN KEY(GENRE) REFERENCES genre(id),
            primary key(title, genre)
            )'''

    cursor.execute(sql)
    conn.commit()
    sql = "COPY title_genre(title, genre) FROM STDIN DELIMITER ',' CSV HEADER"
    cursor.copy_expert(sql, open("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/genre_title_mapping.csv", "r"))
    conn.commit()

def title(conn, cursor):
    sql = '''
         CREATE TABLE IF NOT EXISTS TITLE(
         id VARCHAR(20) PRIMARY KEY,
         type VARCHAR(20),
         title varchar(500),
         originalTitle varchar(500),
         startYear  integer,
         endYear  integer,
         runtime integer,
         avgRating  FLOAT,
         numVotes INTEGER
         )'''

    cursor.execute(sql)
    conn.commit()
    sql = "COPY title FROM STDIN DELIMITER ',' CSV HEADER"
    cursor.copy_expert(sql, open("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/title1_project2.csv", "r"))
    conn.commit()

def member(conn, cursor):
    sql = '''
             CREATE TABLE IF NOT EXISTS MEMBER(
             id VARCHAR(20) PRIMARY KEY,
             NAME VARCHAR(100),
             birthYear  integer,
             deathYear  integer
             )'''

    cursor.execute(sql)
    conn.commit()
    sql = "COPY member FROM STDIN DELIMITER ',' CSV HEADER"
    cursor.copy_expert(sql,
                       open("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/member_project2.csv", "r"))
    conn.commit()
def director(conn, cursor):
    sql = '''
                 CREATE TABLE IF NOT EXISTS DIRECTOR(
                 director VARCHAR(20),
                 title VARCHAR(20),
                FOREIGN KEY(DIRECTOR) REFERENCES MEMBER(ID),
                FOREIGN KEY(TITLE) REFERENCES TITLE(id),
                primary key(director, title)
                 )'''

    cursor.execute(sql)
    conn.commit()
    sql = "COPY DIRECTOR(title, director) FROM STDIN DELIMITER ',' CSV HEADER"
    cursor.copy_expert(sql,
                       open("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/director_mapping_project2.CSV", "r"))
    conn.commit()
def writer(conn, cursor):
    sql = '''
                 CREATE TABLE IF NOT EXISTS WRITER(
                 WRITER VARCHAR(20),
                 title VARCHAR(20),
                FOREIGN KEY(WRITER) REFERENCES MEMBER(ID),
                FOREIGN KEY(TITLE) REFERENCES TITLE(id),
                primary key(WRITER, title)
                 )'''

    cursor.execute(sql)
    conn.commit()
    sql = "COPY writer(title, writer) FROM STDIN DELIMITER ',' CSV HEADER"
    cursor.copy_expert(sql,
                       open("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/writer_mapping_project2.CSV", "r"))
    conn.commit()

def actor_producer(conn, cursor):
    # sql = '''
    #              CREATE TABLE IF NOT EXISTS ACTOR(
    #              ACTOR VARCHAR(20),
    #              title VARCHAR(20),
    #             FOREIGN KEY(ACTOR) REFERENCES MEMBER(ID),
    #             FOREIGN KEY(TITLE) REFERENCES TITLE(id),
    #             primary key(ACTOR, title)
    #              )'''

    # cursor.execute(sql)
    # conn.commit()
    # sql = "COPY ACTOR(title, actor) FROM STDIN DELIMITER ',' CSV HEADER"
    # cursor.copy_expert(sql,
    #                    open("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/actor_mapping_project2.CSV",
    #                         "r"))
    # conn.commit()
    sql = '''
                    CREATE TABLE IF NOT EXISTS PRODUCER(
                    PRODUCER VARCHAR(20),
                    title VARCHAR(20),
                   FOREIGN KEY(PRODUCER) REFERENCES MEMBER(ID),
                   FOREIGN KEY(TITLE) REFERENCES TITLE(id),
                   primary key(producer, title)
                    )'''

    cursor.execute(sql)
    conn.commit()
    sql = "COPY producer(title, producer) FROM STDIN DELIMITER ',' CSV HEADER"
    cursor.copy_expert(sql,
                       open(
                           "/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/producer_mapping_project2.CSV",
                           "r"))
    conn.commit()

def actor_tables(conn, cursor):
    sql = '''
                 CREATE TABLE IF NOT EXISTS CHARACTER(
                 id integer,
                 character varchar(50),
                primary key(id)
                 )'''

    cursor.execute(sql)
    conn.commit()
    sql = "COPY character(character, id) FROM STDIN DELIMITER ',' CSV HEADER"
    cursor.copy_expert(sql,
                       open("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/character1.csv", "r"))
    conn.commit()

    sql = '''
                     CREATE TABLE IF NOT EXISTS     ACTOR_TITLE_CHARACTER(
                     ACTOR VARCHAR(20),
                     TITLE VARCHAR(20),
                     CHARACTER integer,
                    primary key(character, ACTOR, TITLE),
                     FOREIGN KEY(CHARACTER) REFERENCES CHARACTER(id),
                     FOREIGN KEY(TITLE, ACTOR) REFERENCES title_ACTOR(TITLE, ACTOR)
                     )'''
    #\copy ACTOR_TITLE_CHARACTER(title, actor, character) FROM '/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/actor_title_character2.csv'(format csv, delimiter ',', header true);
    cursor.execute(sql)
    conn.commit()
    sql = "COPY ACTOR_TITLE_CHARACTER(title, actor,character) FROM STDIN DELIMITER ',' CSV HEADER"
    cursor.copy_expert(sql,
                       open("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/actor_title_character2.csv", "r"))
    conn.commit()




def main():
    # creating a connection with the database already created for this project
    conn = psycopg2.connect(
        database='HW2_IMDB', user='postgres', password='127845', host='127.0.0.1',  # or localhost
        port='5432'
    )

    cursor = conn.cursor()
    cursor.execute("select version()")
    # genre(conn, cursor)
    # title(conn, cursor)
    # member(conn, cursor)
    # director(conn, cursor)
    # writer(conn, cursor)
    # actor_tables(conn, cursor)
    # actor_producer(conn, cursor)
    queries(conn, cursor)

    # sql = "set constraints all deferred;"
    # cursor.execute(sql)
    # conn.commit()


if __name__ == '__main__':
    main()