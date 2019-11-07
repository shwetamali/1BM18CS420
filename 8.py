import sqlite3
conn=sqlite3.connect("stud1.db")
def create():
    print("Opened database successfully")
    print("Table creation:")
    conn.execute('''CREATE TABLE std(ID INT PRIMARY KEY NOT NULL,
                 NAME TEXT NOT NULL,
                 SEM INT NOT NULL,
                 DEPT CHAR(25));''')
    print("Table created successfully")
def insert():
    print("Inserting student information:")
    conn.execute("INSERT INTO std(ID,NAME,SEM,DEPT)VALUES(1,'riya',5,'CSE')")
    conn.execute("INSERT INTO std(ID,NAME,SEM,DEPT)VALUES(2,'ira',6,'ECE')")
    conn.execute("INSERT INTO std(ID,NAME,SEM,DEPT)VALUES(3,'siya',5,'EEE')")
    conn.execute("INSERT INTO std(ID,NAME,SEM,DEPT)VALUES(4,'ana',4,'MECH')")
    conn.commit()
    print("Values inserted successfully","\t")
def display():
    print("Displays student information:")
    cursor=conn.execute("SELECT * from std")
    print("Table contents are:")
    for row in cursor:
        print("ID=",row[0])
        print("NAME=",row[1])
        print("SEM=",row[2])
        print("DEPT=",row[3])
        print("---------------------------------------")
    conn.commit()
def query():
    print("Retrives data of specific student")
    cursor=conn.execute("SELECT * from std where ID=5")
    print("Query result:")
    res=cursor.fetchall()
    print(res)
def update():
    print("Updating student information:")
    conn.execute("UPDATE std SET SEM=3 where ID=3")
    conn.commit()
    print("Upadted table contents are:")
    cursor=conn.execute("SELECT * from std")
    res=cursor.fetchall()
    print(res)
    print("Updated successfully")
def delete():
    print("Deleting particular student data:")
    conn.execute("DELETE from std where ID=4")
    conn.commit()
    cursor=conn.execute("SELECT * from std")
    print("The table contents after deletion are:")
    res=cursor.fetchall()
    print(res)
    print("Deleted successfully")
create()
insert()
display()
query()
update()
delete()
    
                 
********************OUTPUT************************
Opened database successfully
Table creation:
Table created successfully
Inserting student information:
Values inserted successfully 	
Displays student information:
Table contents are:
ID= 1
NAME= riya
SEM= 5
DEPT= CSE
---------------------------------------
ID= 2
NAME= ira
SEM= 6
DEPT= ECE
---------------------------------------
ID= 3
NAME= siya
SEM= 5
DEPT= EEE
---------------------------------------
ID= 4
NAME= ana
SEM= 4
DEPT= MECH
---------------------------------------
Retrives data of specific student
Query result:
[]
Updating student information:
Upadted table contents are:
[(1, 'riya', 5, 'CSE'), (2, 'ira', 6, 'ECE'), (3, 'siya', 3, 'EEE'), (4, 'ana', 4, 'MECH')]
Updated successfully
Deleting particular student data:
The table contents after deletion are:
[(1, 'riya', 5, 'CSE'), (2, 'ira', 6, 'ECE'), (3, 'siya', 3, 'EEE')]
Deleted successfully
