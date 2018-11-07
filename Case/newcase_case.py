from selenium import webdriver
from business.newcase_business import Newcase_business
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
        #cls.driver.get('http://doctor.clearbos.cn/index.html#/')
       #cls.driver.maximize_window()

    def setUp(self):
        #self.driver=webdriver.Chrome()
        self.driver.get('http://doctor.clearbos.cn/index.html#/')
        self.driver.maximize_window()
        #self.driver.refresh()
        self.login = Newcase_business(self.driver)


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
    def test_new_case(self):
        value=self.login.newcase_success('ts011')
        self.assertTrue(value)
    def test_new_case_one(self):
        value=self.login.newcase_success('ts0012')
        self.assertTrue(value)





if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login_test('test_new_case'))
    suite.addTest(Login_test('test_new_case_one'))
