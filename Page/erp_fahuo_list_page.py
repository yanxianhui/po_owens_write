from base.findelment import Findelement

class erp_fahuo_list_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取邮寄按钮元素
    def get_youji_button(self):
        return self.f.get_element('youji')
    #获取快递单号输入框
    def get_kaudidanhao_text(self):
        return self.f.get_element('kaudidanhao')
    #获取快递单号填写完成确认按钮
    def get_kaudi_queren_button(self):
        return self.f.get_element('kaudi_queren')
    #获取确认按钮元素
    def get_queren_button(self):
        return self.f.get_element('queren')
    #获取确认发货按钮元素
    def get_qurenfahuo_button(self):
        return self.f.get_element('qurenfahuo')