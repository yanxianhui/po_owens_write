from Page.erp_moni_design_page import erp_moni_design_page

class erp_moni_design_handle():
    def __init__(self,driver):
        self.p=erp_moni_design_page(driver)

    #点击模拟排牙指派订单按钮
    def click_moni_zhipaidingdan_button(self):
        self.p.get_moni_zhipaidingdan_button().click()

    #点击指派确认
    def click_moni_zhipai_queren_button(self):
        self.p.get_moni_zhipai_quren_button().click()

    #点击模拟排牙审核通过
    def clcik_moni_shehetongguo_button(self):
        self.p.get_moni_shehetongguo_button().click()