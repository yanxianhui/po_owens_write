from Page.login_page import login_Page

class login_Handle():
    def __init__(self,driver):
        self.page=login_Page(driver)


    #输入用户名
    def login_send_uesrname(self,username):
        self.page.get_login_username().clear()
        self.page.get_login_username().send_keys(username)
    #输入密码
    def login_send_password(self,password):
        self.page.get_login_password().clear()
        self.page.get_login_password().send_keys(password)
    #点击登录
    def login_click_button(self):
        self.page.get_login_button().click()


    #获取文本信息
    def get_login_test(self,info):
        try:
            if info=='success':
                res=self.page.get_login_button().text
            elif info=='error':
                res=self.page.get_login_error().text
            else:
                res=None
            return res
        except:
            print('未找到元素')

