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
        cf.read(self.file_name)
        return cf


    def get_value(self,key):
        value=self.data.get(self.note,key)
        return value


if __name__ == '__main__':
    ope=Readini('D:\po_owens_write\config\\Newcase.ini','newcase')
    print(ope.get_value('Doctoruser'))