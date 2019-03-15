import pymssql

class linkDB():
    def linkdb(self,sql):
        # 数据库远程连接
        conn = pymssql.connect(host='106.14.117.240', user="Gtooth", password="E@ClearBos!@#$2017?", database="DentalDB_20190130", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        # 查询语句
        #sql = "select*from Area where AreaCode=110000"
        try:
            cursor.execute(sql)  # 游标
            #以字典格式返回
            coloumns = [row[0] for row in cursor.description]
            result = [[str(item) for item in row] for row in cursor.fetchall()]
            return [dict(zip(coloumns, row)) for row in result]
            #以数组格式返回
            # result = cursor.fetchall()  # 查询
            # print(result)
            # return result
        except:
            print("连接数据库报错了！")
        # 关闭数据库连接
        conn.close()



if __name__ == '__main__':
    ope=linkDB()
    #ope.linkdb('select*from Area where AreaCode=110000')
    #--查询需求模型
    ape=ope.linkdb('select*from CaseDemandOrder where CaseNo=201903050003')
    print(ape[0]['ModelBillNo'])
    if 'GS201903050003' == ape[0]['ModelBillNo']:
        print('success')
    else:
        print('false')
    #print(ape[5])
    #--查询主病例流程
    # ope.linkdb('select*from CaseMainInfo where CaseNo=201903050003')
    #
    # #--查询收货模型
    # ope.linkdb('select *from CaseModelReceive where ModelBillNo=GS201903050003')




