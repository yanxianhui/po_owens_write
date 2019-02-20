import pymssql

class linkDB():
    def linkdb(self,sql):
        # 数据库远程连接
        conn = pymssql.connect(host="106.14.117.240", user="Gtooth", password="E@ClearBos!@#$2017?", database="DentalDB_20190130", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        # 查询语句
        #sql = "select*from Area where AreaCode=110000"
        try:
            cursor.execute(sql)  # 游标
            result = cursor.fetchall()  # 查询
            print(result)
        except:
            print("连接数据库报错了！")
        # 关闭数据库连接
        conn.close()


if __name__ == '__main__':
    ope=linkDB()
    #ope.linkdb('select*from Area where AreaCode=110000')
    ope.linkdb('select*from  CaseDemandOrder where CaseNo=201812290028')




