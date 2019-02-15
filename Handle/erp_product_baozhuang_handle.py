from Page.erp_product_baozhuang_page import erp_product_baozhuang_page

class erp_product_baozhuang_handle():
    def __init__(self,driver):
        self.p=erp_product_baozhuang_page(driver)
    #点击完成按钮
    def click_baozhuang_wangc_button(self):
        self.p.get_baozhuang_wangc_button().click()
    #点击确认入库按钮
    def click_queren_ruku_button(self):
        self.p.get_queren_ruku_button().click()