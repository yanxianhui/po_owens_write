from base.findelment import Findelement

class erp_chufangguanli_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    # 获取处方管理界面查看更多button
    def get_chakangenduo_button(self):
        return self.f.get_element('cankangenduo')

    #获取处方管理-临床操作说明按钮
    def get_chakan_linchaung_button(self):
        return self.f.get_element('lc_shuoming')