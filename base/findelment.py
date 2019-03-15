from unitl.read_ini import Readini
from log.user_log import UserLog
from selenium.webdriver.common.by import By #调试等待时间用
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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
                local = (By.ID, value)
                WebDriverWait(self.driver, 10,poll_frequency=0.5,ignored_exceptions=None).until(EC.presence_of_element_located(local))
                return self.driver.find_element_by_id(value)
            elif by=='xpath' or by=='Xpath' or by=='XPATH':
                local=(By.XPATH,value)
                WebDriverWait(self.driver,10,poll_frequency=0.5,ignored_exceptions=None).until(EC.presence_of_element_located(local))
                return self.driver.find_element_by_xpath(value)
            elif by=='className' or by=='ClassName':
                local = (By.CLASS_NAME, value)
                WebDriverWait(self.driver, 10,poll_frequency=0.5,ignored_exceptions=None).until(EC.presence_of_element_located(local))
                return self.driver.find_element_by_class_name(value)
            elif by=='selector' or by=='Selector':
                local = (By.CSS_SELECTOR, value)
                WebDriverWait(self.driver, 10,poll_frequency=0.5,ignored_exceptions=None).until(EC.presence_of_element_located(local))
                return self.driver.find_element_by_css_selector(value)
            else:
                return self.driver.find_element_by_class_name(value)
        except:
            self.logger.info("未找到元素定位值:" + key)
            return print('未找到元素,findelement',key)
    #获取写入的病例号
    def get_casenum(self):
        return self.resdini.get_value('caseno')





if __name__=='__main__':
    ope=Findelement('driver')
    #ope.get_element('queren_xiadan')
    print(ope.get_casenum())


