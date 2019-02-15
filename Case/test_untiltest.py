from unitl.HTMLTestRunner import HTMLTestRunner
from Case.mew_case import Login_test
from Case.erp_process import Erp_login
import unittest
if __name__=="__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(Login_test))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(Erp_login))
    file_path='D:\po_owens_write\\report\\first_case.html'
    with open(file_path, 'wb+') as f:
        runner = HTMLTestRunner(f, verbosity=2, title="This is report",
                                description="本次测试报告")
        runner.run(testsuite)