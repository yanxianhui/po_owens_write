from base.findelment import Findelement

class erp_liucheng_page():
    def __init__(self,driver):
        self.f=Findelement(driver)


    #获取流程按钮
    def get_liucheng_button(self):
        return self.f.get_element('erp_dao_hang')


    #获取收货列表
    def get_souhuo_list_button(self):
        return self.f.get_element('erp_received')

    #获取需求管理
    def get_xuqiuguanli_button(self):
        return self.f.get_element('demand_management')

    #获取模型扫描
    def get_moxingsaomiao_button(self):
        return self.f.get_element('moxingsaomiao')
    #获取资料质检
    def get_ziliaozhijian_button(self):
        return self.f.get_element('ziliaoguanli')
    #获取订单管理
    def get_dingdanguanli_button(self):
        return self.f.get_element('dingdanguanli')
    #获取设计跟进
    def get_shejigenjin_button(self):
        return self.f.get_element('shejigenjin')
    #获取数字建模
    def get_shuozijianmo_button(self):
        return self.f.get_element('shuozijianmo')

    #获取模拟排牙
    def get_monipaiya_button(self):
        return self.f.get_element('monipaiya')
    #获取设计质检
    def get_shejizhijian_button(self):
        return self.f.get_element('shejizhijian')
    #获取生产调度
    def get_shengchandiaodu_button(self):
        return self.f.get_element('shengchangdiaodu')
    #获取模型打印
    def get_moxingdayin_button(self):
        return self.f.get_element('moxingdayin')
    #获取产品成型
    def get_chanpinchengxing_button(self):
        return self.f.get_element('changpinchengxing')
    #获取成品包装
    def get_chengpinbaozhuang_button(self):
        return self.f.get_element('chengpinbaozhuang')
    #获取发货确认
    def get_fahuoqueren_button(self):
        return self.f.get_element('fahuoqueren')
    #获取发货列表
    def get_fahuoliebiao_button(self):
        return self.f.get_element('fahuoliebiao')
    #获取病例查询

    #获取医生列表

    #获取生产设备

    #获取质检按钮元素
    def get_erp_zhiliang_button(self):
        return self.f.get_element('erp_zhijian')
    #获取生产质检按钮
    def get_shengchangzhijian_button(self):
        return self.f.get_element('shengchangzhijian')
