import psycopg2

# Open a connection to a Postgresql database
conn = psycopg2.connect(
        database="testdb",
        user="urian",
        host="127.0.0.1",
        port="5432"
    )
print "Opened database successfully\n"

cur = conn.cursor()

"""
# Create a table
cur.execute('''create table psycop
    (id int primary key not null,
    name text not null,
    age int not null,
    address char(50),
    salary real);
''')
conn.commit()
print "Table created successfully"
"""

"""
# Insert rows
cur.execute("insert into psycop (id,name,age,address,salary) \
    values (1, 'Paul', 32, 'California', 20000.00), \
    (2, 'Allen', 25, 'Texas', 15000.00), \
    (3, 'Teddy', 23, 'Norway', 20000.00), \
    (4, 'Mark', 25, 'Rich-Mond', 65000.00)")
conn.commit()
print "Records created successfully"
"""

"""
# Update
cur.execute("update psycop set salary = 25000.00 where id = 1")
conn.commit
print "Total number of rows updated : {}\n".format(cur.rowcount)
"""

"""
# Delete
cur.execute("delete from psycop where id = 4")
conn.commit
print "Total number of rows deleted : {}\n".format(cur.rowcount)
"""

cur.execute("select id, name, address, salary from psycop")
rows = cur.fetchall()
for row in rows:
    print("ID = {}".format(row[0]))
    print("NAME = {}".format(row[1]))
    print("ADDRESS = {}".format(row[2]))
    print("SALARY = {}\n".format(row[3]))
print "Operation done successfully"

conn.close()
