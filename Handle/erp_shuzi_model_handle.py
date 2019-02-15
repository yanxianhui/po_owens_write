from Page.erp_shuzi_modle_page import erp_shuzi_modle_page

class erp_shuzi_modle_handle():
    def __init__(self,driver):
        self.p=erp_shuzi_modle_page(driver)

    #点击数字建模指派订单按钮
    def click_sz_zhipaidingdan_button(self):
        self.p.get_sz_zhipaidingdan_button().click()

    #点击指派确认
    def click_sz_zhipai_queren_button(self):
        self.p.get_sz_zhipai_quren_button().click()

    #点击审核通过
    def clcik_sz_shehetongguo_button(self):
        self.p.get_sz_shehetongguo_button().click()