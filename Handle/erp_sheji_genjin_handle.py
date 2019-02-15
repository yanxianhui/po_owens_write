from Page.erp_sheji_genjin_page import erp_sheji_genjin_page


class erp_sheji_genjin_handle():
    def __init__(self,driver):
        self.p=erp_sheji_genjin_page(driver)

    #设计跟进界面点击分配
    def click_shejin_genjin_fenpei_button(self):
        self.p.get_shejigenjin_fenpei_button().click()
    #设计跟进界面点击分配确认
    def click_sheji_genjin_fenpei_queren_button(self):
        self.p.get_shejigenjin_fenpei_queren_button().click()