from Page.erp_product_model_page import erp_product_model_page

class erp_product_model_handle():
    def __init__(self,driver):
        self.p=erp_product_model_page(driver)
    #点击产品成型页面完成按钮
    def click_chengxing_wancheng_button(self):
        self.p.get_chengxing_wancheng().click()
    #点击确认按钮
    def click_queding_button(self):
        self.p.get_queding().click()

