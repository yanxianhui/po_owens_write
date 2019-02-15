from Page.erp_fahuo_confirm_page import erp_fahuo_confirm_page

class erp_fahuo_confirm_handle():
    def __init__(self,driver):
        self.p=erp_fahuo_confirm_page(driver)
    #点击发货界面发货按钮
    def click_fahuo_button(self):
        self.p.get_fahuo_button().click()
    #选择可以发货按钮
    def click_select_keyifahuo_button(self):
        self.p.get_select_keyifahuo_button().click()

    #选择确认
    def click_fahuo_quren_button(self):
        self.p.get_fahuo_quren_button().click()