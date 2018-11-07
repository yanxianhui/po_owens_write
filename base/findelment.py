from unitl.read_ini import Readini

class Findelement():
    def __init__(self,driver):
        self.driver=driver
        self.loadini=Readini('D:\po_owens_write\config\\Newcase.ini')
    def get_element(self,key):
        data=self.loadini.get_value(key)
        by=data.split('>')[0]
        value=data.split('>')[1]
        try:
            if by=='id':
                return self.driver.find_element_by_id(value)
            elif by=='xpath' or by=='Xpath' or by=='XPATH':
                return self.driver.find_element_by_xpath(value)
            elif by=='className' or by=='ClassName':
                return self.driver.find_element_by_class_name(value)
            elif by=='selector' or by=='Selector':
                return self.driver.find_element_by_css_selector(value)
            else:
                return self.driver.find_element_by_class_name(value)
        except:
            return print('未找到元素,findelement')




if __name__=='__main__':
    ope=Findelement('driver')
    ope.get_element('username')


