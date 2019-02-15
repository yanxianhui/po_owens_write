from base.findelment import Findelement

class erp_tishi_page():
    def __init__(self,driver):
        self.f=Findelement(driver)


    #获取错误提示信息
    def get_tishi_error(self):
        return self.f.get_element('tishi_error')
    # 获取正确提示信息
    def get_tishi_success(self):
        return self.f.get_element('tishi_success')

    #获取资料质检界面档案质检是否合格元素
    def get_zhiliaozhijian_hege(self):
        return self.f.get_element('zl_zj_hege')

    #获取模型扫描界面需求订单编号
    def get_moxing_sm_RO(self):
        return self.f.get_element('moxing_sm_RO')
    # 获取模型扫描界面需求病例编号

    def get_moxing_sm_caseno(self):
        return self.f.get_element('moxing_caseno')
    #获取设计跟进界面订单编号
    def get_shejigenjin_dingdannum(self):
        return self.f.get_element('dingdan_num')