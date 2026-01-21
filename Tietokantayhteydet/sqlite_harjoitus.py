import sqlite3


sql_create_projects_table = """ 
CREATE TABLE IF NOT EXISTS projects (
    id integer PRIMARY KEY NOT NULL,
    name text NOT NULL,
    begin_date text,
    end_date text
); """

sql_create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY NOT NULL,
    name text NOT NULL,
    priority integer,
    status_id integer NOT NULL,
    project_id integer NOT NULL,
    begin_date text NOT NULL,
    end_date text NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
);"""

def create_table(conn, query: str) -> None:
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()

def add_project(conn, name: str, begin_date: str, end_date: str) -> int:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (name, begin_date, end_date) VALUES (?, ?, ?)", (name, begin_date, end_date))
    conn.commit()
    cursor.close()
    return cursor.lastrowid


conn = sqlite3.connect(':memory:', autocommit=False)
conn.execute('PRAGMA foreign_keys=1')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# cursor.execute(sql_create_projects_table)
# cursor.execute(sql_create_tasks_table)
create_table(conn, sql_create_projects_table)
create_table(conn, sql_create_tasks_table)

# cursor.execute("INSERT INTO projects (name, begin_date, end_date) VALUES ('project1', '2025-12-15', '2025-12-15')")

# project1 = cursor.lastrowid
project1 = add_project(conn, 'project1', '2025-12-15', '2025-12-15')

cursor.execute("INSERT INTO tasks (name, priority, status_id, project_id, begin_date, end_date) VALUES ('task1', 5, 1, ?, '2025-12-15', '2025-12-15')", (project1,))

cursor.execute("INSERT INTO tasks (name, priority, status_id, project_id, begin_date, end_date) VALUES ('task2', 3, 1, ?, '2025-12-15', '2025-12-15')", (project1,))

task2 = cursor.lastrowid

cursor.execute("UPDATE tasks SET priority = 8 WHERE id=?", (task2,))

cursor.execute("SELECT * FROM tasks")
for row in cursor.fetchall():
    print(dict(row))

conn.commit()
cursor.close()
conn.close()

