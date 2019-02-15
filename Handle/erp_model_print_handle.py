from Page.erp_model_print_page import erp_model_print_page

class erp_model_print_handle():
    def __init__(self,driver):
        self.p=erp_model_print_page(driver)

    #点击完成按钮
    def click_shengchan_wangcheng(self):
        self.p.get_shengchan_wangcheng().click()
    #点击打印机选择
    def click_click_dayinji(self):
        self.p.get_click_dayinji().click()
    #选择打印机
    def click_select_dayinji(self):
        self.p.get_select_dayinji().click()
    #点击打印完成
    def click_zuizhong_wancheng(self):
        self.p.get_click_wancheng().click()
