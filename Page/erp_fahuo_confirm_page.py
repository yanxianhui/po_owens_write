from base.findelment import Findelement

class erp_fahuo_confirm_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取发货确认页面发货按钮
    def get_fahuo_button(self):
        return self.f.get_element('fahuo')
    #获取可以发货按钮
    def get_select_keyifahuo_button(self):
        return self.f.get_element('select_keyifahuo')

    #获取确认按钮
    def get_fahuo_quren_button(self):
        return self.f.get_element('fahuo_quren')