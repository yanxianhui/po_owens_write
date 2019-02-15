from base.findelment import Findelement

class demand_guanli_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取匹配按钮
    def get_pipei_button(self):
        return self.f.get_element('xuqiu_pipei')

    #获取输入病例号文本
    def get_xuqiu_pipei_case(self):
        return self.f.get_element('xuqiu_pipei_case')
    #获取关联档案
    def get_xuqiu_pipei_danan(self):
        return self.f.get_element('xuqiu_piepi_danan')
    #获取确认匹配按钮
    def get_xuqiu_queren_pipei_button(self):
        return self.f.get_element('xuqiu_pipei_button')
    #关闭匹配界面
    def get_guanbi_button(self):
        return self.f.get_element('xuqiu_pipei_guanbi')

    #判断提示
    def get_tishi(self):
        return self.f.get_element('tishi')
