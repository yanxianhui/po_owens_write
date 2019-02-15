from base.findelment import Findelement

class erp_moxing_sm_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取点击上传stl按钮
    def get_shangchaung_button(self):
        return self.f.get_element('shangchaung')

    #获取上传上颌stl文件元素
    def get_shangc_up_stl(self):
        return self.f.get_element('shang_stl')

    #获取上传下颌stl文件元素
    def get_shangc_lower_stl(self):
        return self.f.get_element('xia_stl')

    #获取上传确认按钮元素
    def get_shangc_stl_queren(self):
        return self.f.get_element('queren_button')

    #获取模型是扫描页面完成按钮
    def get_moxing_sm_wangcheng_button(self):
        return self.f.get_element('moxing_sm_wanc')


