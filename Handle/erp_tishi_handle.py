from Page.erp_tishi_page import erp_tishi_page

class erp_tishi_handle():
    def __init__(self,driver):
        self.p=erp_tishi_page(driver)
    #获取弹出提示内容
    def get_tishi_xinxi_text(self,info):
        try:
            if info=='error_tishi':
               text= self.p.get_tishi_error().text
            elif info=='success_tishi':
                text=self.p.get_tishi_success().text
            elif info=='hege':
                text=self.p.get_zhiliaozhijian_hege().text
            elif info=='RO':
                text=self.p.get_moxing_sm_RO().text
            elif info == 'caseno':
                text = self.p.get_moxing_sm_caseno().text
            elif info == 'DO_num':
                text = self.p.get_shejigenjin_dingdannum().text
            else:
                text='不用获取'
        except:
            text=None
        return text