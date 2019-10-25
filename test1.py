
import sqlite3
from sqlite3 import Error 
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()


 
def sql_connection(): 
    try: 
        con = sqlite3.connect('mydatabase.db') 
        return con 
    except Error: 
        print(Error) 
def sql_table(con): 
    cursorObj = con.cursor()
    cursorObj.execute('drop table if exists employees')
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)") 
    con.commit()    
    
 
def sql_insert(con, entities): 
    cursorObj = con.cursor()    
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()
def sql_insertall(con):
    entities = (1, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
    entities1 = (2, 'And', 800, 'IT', 'Tech', '2018-02-06')
    entities2 = (3, 'rew', 800, 'IT', 'Tech', '2018-02-06')
    entities3 = (4, 'ndr', 800, 'IT', 'Tech', '2018-02-06')
    sql_insert(con, entities)
    sql_insert(con, entities1)
    sql_insert(con, entities2)
    sql_insert(con, entities3)

def sql_update(con): 
    cursorObj = con.cursor() 
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2') 
    con.commit() 

def sql_fetch(con): 
    cursorObj = con.cursor() 
    cursorObj.execute('SELECT * FROM employees') 
    rows = cursorObj.fetchall() 
    for row in rows: 
        print(row)
def sql_specific(con): 
    cursorObj = con.cursor()
    n=str(input("Enter the employee ID to be fetched"))
    cursorObj.execute('SELECT * FROM employees Where ID='+n) 
    rows = cursorObj.fetchall() 
    for row in rows: 
        print(row)
def sql_delete(con): 
    cursorObj = con.cursor()
    n=str(input("Enter the employee ID to be deleted"))
    cursorObj.execute('Delete from employees where  id ='+n) 
    con.commit() 
        
con = sql_connection()
sql_table(con)
sql_fetch(con)
sql_insertall(con)
sql_fetch(con)
sql_update(con)
sql_fetch(con)
sql_specific(con) 
sql_delete(con)
sql_fetch(con)
