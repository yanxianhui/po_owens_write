from unitl.HTMLTestRunner import HTMLTestRunner
from unitl.send_email import Email
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
    e = Email(title='ERP测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='825651673@qq.com',
              server='smtp.126.com',
              sender='luckyanhui@126.com',
              password='yan986165220',
              path=file_path)
    e.send()