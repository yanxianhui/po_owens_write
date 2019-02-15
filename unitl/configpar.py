import configparser
file='D:\po_owens_write\config\example.ini'


class ConfigPar():
    def write_canshu(self,canshu_name,aaa):
        config=configparser.ConfigParser()
        config['DEFAULT'][canshu_name] = aaa
        with open('D:\po_owens_write\config\example.ini','w') as coo:
            config.write(coo)



if __name__=="__main__":
    ope=ConfigPar()
    ope.write_canshu('CaseNo','2018101000020')

    ope.write_canshu('ccas','20115')