'''DOCSTRING'''
import sqlite3


def connect_to_sqlite(db_name='rpg_db.sqlite3'):
    # Connect to the db
    return sqlite3.connect(db_name)


def execute_query(conn, query):
    return execute_ddl(conn, query).fetchall()


def execute_ddl(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor


create_table = """
CREATE TABLE IF NOT EXISTS demo (
    s VARCHAR(1),
    x INT,
    y INT
)
"""

insert_statement = """
INSERT INTO demo (s, x, y)
VALUES
("g", 3, 9),
("v", 5, 7),
("f", 8, 7)
"""

row_count_query = """
SELECT COUNT(*)
FROM demo
"""

unique_y_query = """
SELECT COUNT (DISTINCT y)
FROM demo
"""

xy_query = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5 AND y >= 5
"""

row_count = [(3,)]

xy_at_least_5 = [(2,)]

unique_y = [(2,)]

if __name__ == '__main__':
    conn = connect_to_sqlite('demo_data.sqlite')
    print(execute_query(conn, xy_query))
    # execute_ddl(conn, create_table)
    # execute_ddl(conn, insert_statement)
    # conn.commit()
