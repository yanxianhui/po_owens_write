from Page.erp_search_page import erp_search_page

class erp_search_handle():
    def __init__(self,driver):
        self.p=erp_search_page(driver)


    #输入搜索关键字
    def send_search_word(self,aaa):
        self.p.get_sousuoshuru_text().send_keys(aaa)

    #点击查询按钮

    def click_search_button(self):
        self.p.get_sousuochaxun_button().click()
