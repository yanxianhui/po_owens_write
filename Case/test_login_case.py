from selenium import webdriver
from business.login_business import login_Business
import unittest
import time,os

class Login_test(unittest.TestCase):
    # def setUp(self):
    #     driver=webdriver.Chrome()
    #     self.case = login_Business(driver)
    #     driver.get('http://www.clearbos.cn/test/#/')
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.clearbos.cn/test/#/')
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.refresh()
        self.login = login_Business(self.driver)

    def tearDown(self):
        time.sleep(2)
        # if sys.exc_info()[0]:
        # for method_name, error in self._outcome.errors:
        #     if error:
        #         case_name = self._testMethodName
        #         file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
        #         self.driver.save_screenshot(file_path)
                # print("这个是case的后置调键1")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        time.sleep(1)
        cls.driver.quit()
    def test_login_ausername_error(self):
        value=self.login.login_password_error('15890158360','123456')
        print(value)
        self.assertTrue(value)

    def test_login_busername_error(self):
        value = self.login.login_password_error('15890158362', '12345')
        print(value)
        self.assertTrue(value)

    def test_login_cusername_error(self):
        value = self.login.login_password_error('1589015836', '12345')
        print(value)
        self.assertTrue(value)

    def test_login_dusername_error(self):
        value = self.login.login_password_error('', '')
        print(value)
        self.assertTrue(value)
    def test_login_eusername_error(self):
        value = self.login.login_password_error('15890158362', '')
        print(value)
        self.assertTrue(value)
    def test_login_fusername_error(self):
        value = self.login.login_password_error('', '123456')
        print(value)
        self.assertTrue(value)
    def test_login_success(self):
        value=self.login.login_sucess('15890158362','123456')
        print(value)
        self.assertTrue(value)





if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login_test('test_login_success'))
