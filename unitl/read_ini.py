#coding=utf-8
import configparser

class Readini():
    def __init__(self,file_name=None,note=None):
        if file_name==None:
            self.file_name='D:\po_owens_write\config\LocalElement.ini'
        else:
            self.file_name=file_name
        if note==None:
            self.note='RegisterElement'
        else:
            self.note=note
        self.data=self.load_ini()

    def load_ini(self):
        cf=configparser.ConfigParser()
        cf.read(self.file_name,encoding='utf-8')
        return cf


    def get_value(self,key):
        value=self.data.get(self.note,key)
        return value
    def write_canshu(self,canshu_name,aaa):
        config=configparser.ConfigParser()
        config['DEFAULT'][canshu_name] = aaa
        with open('D:\po_owens_write\config\example.ini','w') as coo:
            config.write(coo)

if __name__ == '__main__':
    ope=Readini('D:\po_owens_write\config\example.ini','DEFAULT')
    print(ope.get_value('caseno'))
    # ope=Readini('D:\po_owens_write\config\example.ini','DEFAULT')
    # ope.write_canshu('nann','nihao')