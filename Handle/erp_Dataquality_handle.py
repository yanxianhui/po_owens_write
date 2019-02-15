from Page.erp_Dataquality_page import erp_Dataquality_page

class erp_Dataquality_handle():
    def __init__(self,driver):
        self.p=erp_Dataquality_page(driver)

    #点击资料质检界面质检按钮
    def click_data_zhijian_button(self):
        self.p.get_quality_button().click()

    #上传质检第一张照片
    def upload_data_zj_one_img(self,aaa):
        self.p.get_upload_one_img().send_keys(aaa)

    # 上传质检第er张照片
    def upload_data_zj_two_img(self, aaa):
        self.p.get_upload_two_img().send_keys(aaa)

    #点击上传完成按钮
    def upload_data_zj_img_wc(self):
        self.p.get_upload_wangcheng_buttom().click()