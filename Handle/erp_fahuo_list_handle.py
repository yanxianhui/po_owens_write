from Page.erp_fahuo_list_page import erp_fahuo_list_page

class erp_fahuo_list_handle():
    def __init__(self,driver):
        self.p=erp_fahuo_list_page(driver)
    #点击邮寄按钮
    def click_youji_button(self):
        self.p.get_youji_button().click()
    #输入快递单号
    def send_kaudidanhao_text(self,aaa):
        self.p.get_kaudidanhao_text().send_keys(aaa)
    #点击快递单号填写确认按钮
    def click_kaudi_queren_button(self):
        self.p.get_kaudi_queren_button().click()
    #点击发货列表确认按钮
    def click_queren_button(self):
        self.p.get_queren_button().click()
    #点击确认发货
    def click_qurenfahuo_button(self):
        self.p.get_qurenfahuo_button().click()