from selenium import webdriver
from business.new_doctor_case_business import new_bussiness
import unittest
import time,os,sys
from base.configure import Configure
from base.basemethod import base_method
class Login_test(unittest.TestCase):
    # def setUp(self):
    #     driver=webdriver.Chrome()
    #     self.case = login_Business(driver)
    #     driver.get('http://www.clearbos.cn/test/#/')
    # @classmethod
    # def setUpClass(cls):
    #     #cls.driver = webdriver.Chrome('C:\\Users\yanxianhuiclearbos\PycharmProjects\drivers\chromedriver.exe')
    #     option = webdriver.ChromeOptions()
    #     option.add_argument("headless")
    #     cls.driver=webdriver.Chrome(chrome_options=option)
    #     cls.driver.get('http://106.14.117.240:8080/Clearsite2/index/main.do')
    #     cls.driver.maximize_window()

    def setUp(self):
        #self.driver.refresh()-------
        # option = webdriver.ChromeOptions()
        # option.add_argument("headless")
        # self.driver = webdriver.Chrome(chrome_options=option)
        #self.driver = webdriver.Chrome()
        ope=base_method(self)
        self.driver=ope.select_Different_Browser(Configure.Browser)
        self.driver.implicitly_wait(10)
        self.driver.get(Configure.doctor_url)
        #self.driver.get('http://106.14.117.240:8080/Clearsite/index/main.do')
        self.driver.maximize_window()
        self.login =new_bussiness(self.driver)


    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        self.driver.quit()

        # if sys.exc_info()[0]:
        #     for method_name, error in self._outcome.errors:
        #         if error:
        #             case_name = self._testMethodName
        #             file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
        #             self.driver.save_screenshot(file_path)
                    # print("这个是case的后置调键1")

    # @classmethod
    # def tearDownClass(cls):
    #     time.sleep(2)
    #     cls.driver.close()
    #     time.sleep(1)
    #     cls.driver.quit()
    # def test_new_erp_case_y(self):
    #     yes_m=self.login.new_case_Ymx()
    #     self.assertTrue(yes_m)

    def test_new_erp_case_n(self):
        no_m=self.login.new_case_Nmx()
        print(self.login.patient_number)
        self.assertTrue(no_m)


if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login_test('test_new_erp_case_y'))
    suite.addTest(Login_test('test_new_erp_case_n'))
