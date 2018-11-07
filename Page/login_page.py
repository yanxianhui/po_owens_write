from base.findelment import Findelement

class login_Page():
    def __init__(self,driver):
        self.find_element=Findelement(driver)

    #获取登录用户名框
    def get_login_username(self):
        return self.find_element.get_element('username')

    #获取登录密码框
    def get_login_password(self):
        return self.find_element.get_element('passwod')
    #获取登录点击登录按钮
    def get_login_button(self):
        return self.find_element.get_element('buttom')

    #获取登录失败元素
    def get_login_error(self):
        return self.find_element.get_element('login_error')
    #获取登录成功元素
    # def get_login_success(self):
    #     return self.find_element.get_element('login_success')