from Page.demand_guanli_page import demand_guanli_page

class demand_guanli_handle():
    def __init__(self,driver):
        self.p=demand_guanli_page(driver)


    #点击需求管理界面匹配按钮
    def click_pipei_button(self):
        self.p.get_pipei_button().click()
    #输入病例号
    def send_xuqiu_pipei_case(self,aaa):
        self.p.get_xuqiu_pipei_case().send_keys(aaa)
    #点击档案选择
    def click_xuqiu_pipei_danan(self):
        self.p.get_xuqiu_pipei_danan().click()
    #点击确认匹配
    def click_xuqiu_queren_pipei_button(self):
        self.p.get_xuqiu_queren_pipei_button().click()
    #点击关闭
    def click_xuqiu_pipei_guanbi_button(self):
        self.p.get_guanbi_button().click()
    #获取弹出提示
    def get_tishi_xinxi_text(self):
        return self.p.get_tishi().text