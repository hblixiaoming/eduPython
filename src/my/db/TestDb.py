import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="test", charset="utf8")

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = "select * from test where id=%s and name=%s"

r = cursor.execute(sql, ["11", "2"])

print(r)

# 接收返回的说有数据
result = cursor.fetchall()
print(result)

for x in result:
    for k, v in x.items():
        print(k + ':' + str(v))
        pass
    pass
cursor.close()
conn.close()
