from base.findelment import Findelement

class erp_Dataquality_page():
    def __init__(self,driver):
        self.f=Findelement(driver)
    #获取质检按钮元素
    def get_quality_button(self):
        return self.f.get_element('zhijian_button')
    #获取上传第一张元素
    def get_upload_one_img(self):
        return self.f.get_element('upload_one_img')
    #获取上传第二张元素
    def get_upload_two_img(self):
        return self.f.get_element('upload_two_img')
    #获取质检完成按钮元素
    def get_upload_wangcheng_buttom(self):
        return self.f.get_element('click_zj_wanc')