from Page.erp_production_quality_page import erp_production_quality_page

class erp_production_quality_handle():
    def __init__(self,driver):
        self.p=erp_production_quality_page(driver)

    #点击生产质检页面包装按钮
    def click_baozhuang_button(self):
        self.p.get_baozhuang_button().click()
    #点击质检通过按钮
    def click_zhijian_ok_button(self):
        self.p.get_zhijian_ok_button().click()