import MySQLdb
from SQL.DatabaseInit import DataBaseInit

class MyMySQL():
    def __init__(self, host, port, dbName, username, password, charset):
        # 进行数据库初始化
        dbInit = DataBaseInit(host, port, dbName, username, password, charset)
        dbInit.crate()
        dbInit.insertDatas()

        self.conn = MySQLdb.connect(
            host = host,
            port = port,
            db = dbName,
            user = username,
            passwd = password,
            charset = charset
        )
        self.cur = self.conn.cursor()

    def getDataFromDataBases(self):
        self.cur.execute("select bookname, author from testdata;")
        dataTuple = self.cur.fetchall()
        return dataTuple

    def closeDatabase(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    db = MyMySQL(
        host="localhost",
        port=3306,
        dbName="gloryroad",
        username="root",
        password="123456",
        charset="utf8"
    )

    print(db.getDataFromDataBases())
    db.closeDatabase()
