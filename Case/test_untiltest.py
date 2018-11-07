from unitl.HTMLTestRunner import HTMLTestRunner
from Case.test_login_case import Login_test
import unittest
if __name__=="__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(Login_test))
    file_path='D:\po_owens_write\\report\\first_case.html'
    with open(file_path, 'wb+') as f:
        runner = HTMLTestRunner(f, verbosity=2, title="This is first123 report",
                                description="这个是我们第一次测试报告")
        runner.run(testsuite)