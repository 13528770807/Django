import pymysql
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'mysql',
    'db': 'db_django_py2',
    'charset': 'utf8',
}


def sql_check(n,m):
    cur = conn.cursor()
    sql = 'SELECT * FROM students LIMIT %s,%s' %((n-1)*m,m)
    sql2 = 'SELECT * FROM students'
    rv = cur.execute(sql)
    res = cur.fetchall()
    for entry in res:
        print(entry)
    cur.close()


conn = pymysql.connect(**db_config)
try:
    while True :
        n = input('请输入查询的页数：')
        if n == 'q':
            break
        if n.isdigit():
            sql_check(int(n),3)
        else:
            print("输入的不是数字！！！！")
except Exception as e :
    print('执行过程中发生了异常',e)
    conn.rollback()
finally:
    conn.commit()
    conn.close()
