from unitl.read_ini import Readini
from log.user_log import UserLog
class Findelement():
    def __init__(self,driver):
        self.driver=driver
        get_user_log = UserLog()
        self.logger = get_user_log.get_log()
        self.resdini=Readini('D:\po_owens_write\config\example.ini','DEFAULT')
        self.loadini=Readini()
    def get_element(self,key):
        data=self.loadini.get_value(key)
        by=data.split('>')[0]
        if by=='selector':
            value=data.split('>>')[1]
        else:
            value = data.split('>')[1]
        self.logger.info("定位方式:" + by + "--->定位值:" + value)
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
            self.logger.info("未找到元素定位值:" + key)
            return print('未找到元素,findelement',key)

    def get_casenum(self):
        return self.resdini.get_value('caseno')




if __name__=='__main__':
    ope=Findelement('driver')
    #ope.get_element('queren_xiadan')
    print(ope.get_casenum())


