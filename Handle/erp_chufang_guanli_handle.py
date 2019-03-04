from Page.erp_chufang_guanli_page import erp_chufangguanli_page

class erp_chufangguanli_handle():
    def __init__(self,driver):
        self.p=erp_chufangguanli_page(driver)

    # 设计跟进-处方管理点击查看更多
    def clcik_sheji_genjin_chakangenduo_button(self):
        self.p.get_chakangenduo_button().click()

    #设计跟进-处方管理-临床说明
    def click_chufangguanli_lcshuoming_button(self):
        self.p.get_chakan_linchaung_button().click()