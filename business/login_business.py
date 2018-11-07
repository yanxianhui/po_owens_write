from Handle.login_handle import login_Handle
import time
class login_Business():
    def __init__(self,driver):
        self.handle=login_Handle(driver)

    def login_base(self, username, password):
        self.handle.login_send_uesrname(username)
        self.handle.login_send_password(password)
        self.handle.login_click_button()
        time.sleep(2)

    def login_password_none(self,uesrname,password):
        self.login_base(uesrname,password)
        if self.handle.get_login_test('success')!=None:
            return True
        else:
            return False

    def login_username_error(self, uesrname, password):
        self.login_base(uesrname, password)
        if self.handle.get_login_test('success') != None:
            return True
        else:
            return False

    def login_password_error(self, uesrname, password):
        time.sleep(1)
        self.login_base(uesrname, password)
        if self.handle.get_login_test('success') != None:
            return True
        else:
            return False
    def login_double_none(self,uesrname,password):
        self.login_base(uesrname,password)

        if self.handle.get_login_test('success')!=None:
            return True
        else:
            return False
    def login_sucess(self,uesrname,password):
        self.login_base(uesrname,password)
        print(self.handle.get_login_test('error'))
        if self.handle.get_login_test('error')=='登录成功':
            return True
        else:
            return False
