from base.findelment import Findelement


class erp_search_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取搜索输入框
    def get_sousuoshuru_text(self):
        return self.f.get_element('received_search_text')

    #获取搜索查询按钮元素
    def get_sousuochaxun_button(self):
        return self.f.get_element('received_button')