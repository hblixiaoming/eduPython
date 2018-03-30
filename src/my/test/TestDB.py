import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='mysite')

cursor = conn.cursor()

cursor.execute('select * from invited_relation where user_gid=%s', ['108e85ed-dac1-4e51-9e7b-cc1dda9f8ed0'])

values = cursor.fetchall()

print(values)

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

# print cursor.rowcount

conn.commit()

cursor.close()


