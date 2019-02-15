from Page.erp_login_page import erp_login_page

class erp_login_handle():
    def __init__(self,driver):
        self.p=erp_login_page(driver)

    #输入用户名
    def send_erp_login_account(self,account):
        self.p.get_erp_accout().send_keys(account)
    #输入密码
    def send_erp_login_password(self,password):
        self.p.get_erp_password().send_keys(password)
    #点击登录
    def click_erp_login_button(self):
        self.p.get_erp_login_button().click()
    #点击流程
    def click_liucheng(self):
        self.p.get_erp_liucheng().click()
    #点击收货列表
    def click_shouhuoliebiao(self):
        self.p.get_erp_shohuoliebiao().click()
    #点击模型管理列表
    def click_xuqiuguanli(self):
        self.p.get_erp_xuqiuguanli().click()
