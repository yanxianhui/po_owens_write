from Page.erp_moxing_sm_page import erp_moxing_sm_page

class erp_moxing_sm_handle():
    def __init__(self,driver):
        self.p=erp_moxing_sm_page(driver)

    #点击模型扫描界面上传按钮
    def click_sm_shangc_button(self):
        self.p.get_shangchaung_button().click()

    #上传上颌stl
    def upload_sm_up_stl(self,aaa):
        self.p.get_shangc_up_stl().send_keys(aaa)
    #上传下颌stl
    def upload_sm_lower_stl(self,aaa):
        self.p.get_shangc_lower_stl().send_keys(aaa)
    #上传完成点击确认按钮
    def click_sm_queren_button(self):
        self.p.get_shangc_stl_queren().click()
    #模型扫描界面点击完成按钮
    def click_sm_wnagcheng_button(self):
        self.p.get_moxing_sm_wangcheng_button().click()