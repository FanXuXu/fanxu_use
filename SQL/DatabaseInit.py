from SQL import *
import MySQLdb

from SQL.Sql import create_database, create_table


class DataBaseInit():
    def __init__(self, host, port, dbName, username, password, charset):
        self.host = host
        self.port = port
        self.dbName = dbName
        self.user = username
        self.password = password
        self.charset = charset

    def crate(self):
        try:
            # 链接数据库
            conn = MySQLdb.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                passwd = self.password,
                charset = self.charset
            )

            # 获取数据游标
            cur = conn.cursor()
            # 创建数据库
            cur.execute(create_database)
            # 选择上步创建好的数据库gloryroad
            conn.select_db("gloryroad")
            # 创建测试表
            cur.execute(create_table)

        except MySQLdb.Error as e:
            raise e
        else:
            # 关闭游标
            cur.close()
            # 提交操作
            conn.commit()
            # 关闭链接
            conn.close()
            print("数据库和表 创建成功")

    def insertDatas(self):
        try:
            # 链接数据库
            conn = MySQLdb.connect(
                host=self.host,
                port=self.port,
                db=self.dbName,
                user=self.user,
                passwd=self.password,
                charset=self.charset
            )

            # 获取数据游标
            cur = conn.cursor()
            # 向测试表中插入测试数据
            sql = "insert into testdata(bookname, author) values(%s, %s);"
            res = cur.executemany(sql, [('Selenium WebDriver 实战宝典', '吴晓华'),
                                        ('HTTP权威指南', '古尔利'),
                                        ('探索式软件测试', '惠特克'),
                                        ('暗时间', '刘未鹏')])
        except MySQLdb.Error as e:
            raise e
        else:
            conn.commit()
            print("初始化数据插入成功")
            cur.execute("select * from testdata;")
            for i in cur.fetchall():
                print(i[1], i[2])
            cur.close()
            conn.close()


if __name__ == '__main__':
    db = DataBaseInit(
        host = "localhost",
        port = 3306,
        dbName = "gloryroad",
        username = "root",
        password = "123456",
        charset = "utf8"
    )

    db.crate()

    db.insertDatas()

    print("数据库初始化结束")