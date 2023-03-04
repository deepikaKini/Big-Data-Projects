import psycopg2
import time
def queries(conn, cursor):
    start = time.perf_counter()
    #didn't put in first query to avoid runnin infinitely
    sql = """
    --q2
    select m.name, t.title, t.startYear from title_actor a 
    inner join member m on a.actor = m.id
    inner join title t on a.title = t.id
    where m.deathYear = 0 and t.startYear != 2014 and endYear != 2014
    and lower(m.name) like 'phi%';
    --q3
    select m.name, count(t.id) from member m
    join title_producer p on m.id = p.producer
    join title t on t.id = p.title
    join title_genre tg on tg.title = t.id
    join genre g on tg.genre = g.id
    where m.name like '%gill%' and t.startYear = 2017 and lower(g.genre) like '%talk-show%'
    group by m.name
    order by count(t.id) desc;
    --q4
    select m.name, count(t.title)
    from title_producer p 
    join member m on p.producer = m.id
    join title t on t.id = p.title
    where t.runtime > 120 and m.deathYear != 0
    group by m.name
    order by count(t.title) desc;
    --q5
    select m.name, atc.character, c.character from member m
    join atc atc on atc.actor = m.id
    join character c on c.id = atc.character
    where lower(c.character) like '%jesus christ%' and m.deathYear != 0

    

"""

    cursor.execute(sql)
    conn.commit()
    end = time.perf_counter()
    print("Time taken to run queries:", (end - start))
    #not printing output to avoid increasing time
    # for table in cursor.fetchall():
    #     print(table)

def main():
    # creating a connection with the database already created for this project
    conn = psycopg2.connect(
        database='HW2_IMDB', user='postgres', password='127845', host='127.0.0.1',  # or localhost
        port='5432'
    )

    cursor = conn.cursor()
    cursor.execute("select version()")

    queries(conn, cursor)

    # sql = "set constraints all deferred;"
    # cursor.execute(sql)
    # conn.commit()
    conn.close()

if __name__ == '__main__':
    main()