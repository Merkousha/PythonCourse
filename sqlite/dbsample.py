import sqlite3 
import random

first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Jack']
last_names = ['Smith', 'Johnson', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Jackson']

random_name = random.choice(first_names) + ' ' + random.choice(last_names)


#Bulk insert
for i in range(3,110):
    random_name = random.choice(first_names) + ' ' + random.choice(last_names)
    with sqlite3.connect('db_sample.db') as conn:  #conn mains Connection to database
        cur = conn.cursor()
        cur.execute("INSERT INTO student (id,grade,name) VALUES (?, ?, ?)",
                        (i,random.randint(8,20),random_name))
        conn.commit()


#CRUD Samples :

#CREATE
with sqlite3.connect('db_sample.db') as conn:  #conn mains Connection to database
        cur = conn.cursor()
        cur.execute("INSERT INTO student (id,grade,name) VALUES (?, ?, ?)",
                        (2,15,"sadaf"))
        conn.commit()


#Read
with sqlite3.connect('db_sample.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT
	*, 
	student.*
FROM
	student
WHERE
	student.grade < 10""")
        studentslist = cur.fetchall()
        print(studentslist)


#Update
conn = sqlite3.connect('db_sample.db')
c = conn.cursor()
c.execute("UPDATE student SET grade = ? WHERE id = ?", (17,2))
conn.commit()
conn.close()
      
      
#Delete
conn = sqlite3.connect('db_sample.db')
c = conn.cursor()
c.execute("DELETE FROM student WHERE id = 10")
conn.commit()
conn.close()
            
