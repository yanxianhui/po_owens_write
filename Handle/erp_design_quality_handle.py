from Page.erp_design_quality_page import erp_design_quality_page

class erp_design_quality_handle():
    def __init__(self,driver):
        self.p=erp_design_quality_page(driver)

    #点击设计质检指派订单按钮
    def click_sj_zj_zhipaidingdan_button(self):
        self.p.get_d_zj_zhipaidingdan_button().click()

    #点击指派确认
    def click_sj_zj_zhipai_queren_button(self):
        self.p.get_d_zj_zhipai_quren_button().click()

    #点击审核通过
    def clcik_sj_zj_shehetongguo_button(self):
        self.p.get_d_zj_shehetongguo_button().click()