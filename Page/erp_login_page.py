from base.findelment import Findelement

class erp_login_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取用户账号元素
    def get_erp_accout(self):
        return self.f.get_element('erp_accout')
    #获取输入密码元素
    def get_erp_password(self):
        return self.f.get_element('erp_password')
    #获取点击登录元素
    def get_erp_login_button(self):
        return self.f.get_element('erp_login_button')
    #获取流程
    def get_erp_liucheng(self):
        return self.f.get_element('erp_dao_hang')
    def get_erp_shohuoliebiao(self):
        return self.f.get_element('erp_received')

    def get_erp_xuqiuguanli(self):
        return self.f.get_element('demand_management')
