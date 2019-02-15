from Page.erp_product_schedu_page import erp_product_schedu_page

class erp_product_schedu_handle():
    def __init__(self,driver):
        self.p=erp_product_schedu_page(driver)

    #点击选择病例框
    def click_xuanze_kuan(self):
        self.p.get_xuanze_kuan().click()
    #点击排产预览
    def click_paican_yulan(self):
        self.p.get_paican_yulan().click()
    #输入流转号
    def send_liuzhuanghao(self,aaa):
        self.p.get_liuzhuanghao().send_keys(aaa)
    #点击确认排产
    def click_queren_paichang(self):
        self.p.get_queren_paichang().click()


