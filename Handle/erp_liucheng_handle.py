from Page.erp_liucheng_page import erp_liucheng_page

class erp_liucheng_handle():
    def __init__(self,driver):
        self.p=erp_liucheng_page(driver)

    #点击流程按钮
    def click_liucheng_button(self):
        self.p.get_liucheng_button().click()

    # 点击收货列表
    def click_souhuo_list_button(self):
        self.p.get_souhuo_list_button().click()

    # 点击需求管理
    def click_xuqiuguanli_button(self):
        self.p.get_xuqiuguanli_button().click()

    # 点击模型扫描
    def click_moxingsaomiao_button(self):
        self.p.get_moxingsaomiao_button().click()

    # 点击资料质检
    def click_ziliaozhijian_button(self):
        self.p.get_ziliaozhijian_button().click()

    # 点击订单管理
    def click_dingdanguanli_button(self):
        self.p.get_dingdanguanli_button().click()

    # 点击设计跟进
    def click_shejigenjin_button(self):
        self.p.get_shejigenjin_button().click()

    # 点击数字建模
    def click_shuozijianmo_button(self):
        self.p.get_shuozijianmo_button().click()

    # 点击模拟排牙
    def click_monipaiya_button(self):
        self.p.get_monipaiya_button().click()

    # 点击设计质检
    def click_shejizhijian_button(self):
        self.p.get_shejizhijian_button().click()

    # 点击生产调度
    def click_sehngchandiaodu_button(self):
        self.p.get_shengchandiaodu_button().click()

    # 点击模型打印
    def click_moxingdayin_button(self):
        self.p.get_moxingdayin_button().click()

    # 点击产品成型
    def click_chanpinchengxing_button(self):
        self.p.get_chanpinchengxing_button().click()

    # 点击成品包装
    def click_chengpinbaozhuang_button(self):
        self.p.get_chengpinbaozhuang_button().click()

    # 点击发货确认
    def click_fahuoqueren_button(self):
        self.p.get_fahuoqueren_button().click()

    # 点击发货列表
    def click_fahuoliebiao_button(self):
        self.p.get_fahuoliebiao_button().click()
    # 点击病例查询

    # 点击医生列表

    # 点击生产设备

    #点击质量按钮元素
    def click_erp_zhijian_button(self):
        self.p.get_erp_zhiliang_button().click()
    #点击生成质检按钮
    def click_shengchangzhijian_button(self):
        self.p.get_shengchangzhijian_button().click()
