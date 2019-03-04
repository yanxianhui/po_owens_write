from Handle.add_received_handle import received_handle
from Handle.erp_login_handle import erp_login_handle
from business.new_doctor_case_business import new_bussiness
from Handle.erp_demand_guanli_handle import demand_guanli_handle
from Handle.erp_search_handle import erp_search_handle
from Handle.erp_liucheng_handle import erp_liucheng_handle
from Handle.erp_orderguanli_handle import erp_orderguanli_handle
from Handle.erp_product_schedu_handle import erp_product_schedu_handle
from Handle.erp_model_print_handle import erp_model_print_handle
from Handle.erp_product_model_handle import erp_product_model_handle
from Handle.erp_product_baozhuang_handle import erp_product_baozhuang_handle
from Handle.erp_fahuo_confirm_handle import erp_fahuo_confirm_handle
from Handle.erp_production_quality_handle import erp_production_quality_handle
from Handle.erp_fahuo_list_handle import erp_fahuo_list_handle
from Handle.erp_tishi_handle import erp_tishi_handle
from Handle.erp_moxing_sm_handle import erp_moxing_sm_handle
from Handle.erp_sheji_genjin_handle import erp_sheji_genjin_handle
from Handle.erp_Dataquality_handle import erp_Dataquality_handle
from Handle.erp_shuzi_model_handle import erp_shuzi_modle_handle
from Handle.erp_moni_design_handel import erp_moni_design_handle
from Handle.erp_design_quality_handle import erp_design_quality_handle
from Handle.erp_chufang_guanli_handle import erp_chufangguanli_handle
from base.basemethod import base_method
from unitl.request import erp_requests
import time
from unitl.read_ini import Readini
class erp_login_business():
        def __init__(self,driver):
            self.case_num=Readini('D:\po_owens_write\config\example.ini','DEFAULT').get_value('caseno')
            #self.case_num='201901170018'
            self.liuzhuanghao='60'
            self.r=erp_requests()
            self.base=base_method(driver)
            self.h_r=received_handle(driver)
            self.h_l=erp_login_handle(driver)
            self.h_new=new_bussiness(driver)
            self.h_xuqiu=demand_guanli_handle(driver)
            self.h_search=erp_search_handle(driver)
            self.h_DH=erp_liucheng_handle(driver)
            self.h_sm=erp_moxing_sm_handle(driver)
            self.h_data_zj=erp_Dataquality_handle(driver)
            self.h_orderGL=erp_orderguanli_handle(driver)
            self.h_diaodu=erp_product_schedu_handle(driver)
            self.h_Print=erp_model_print_handle(driver)
            self.h_chengxing=erp_product_model_handle(driver)
            self.h_baozhuang=erp_product_baozhuang_handle(driver)
            self.h_fahuoqeuren=erp_fahuo_confirm_handle(driver)
            self.h_zijian=erp_production_quality_handle(driver)
            self.h_fahuolist=erp_fahuo_list_handle(driver)
            self.h_tishi=erp_tishi_handle(driver)
            self.h_genjin=erp_sheji_genjin_handle(driver)
            self.h_jianmo=erp_shuzi_modle_handle(driver)
            self.h_paiya=erp_moni_design_handle(driver)
            self.h_shejizhijian=erp_design_quality_handle(driver)
            self.h_chakangenduo=erp_chufangguanli_handle(driver)
        #登录erp
        def erp_login(self,account,password):
            self.h_l.send_erp_login_account(account)
            self.h_l.send_erp_login_password(password)
            self.h_l.click_erp_login_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '登录成功!':
                return True
            else:
                return False
        #点击流程，点击收货列表
        def new_add_received(self):
            time.sleep(2)
            self.h_l.click_liucheng()
            time.sleep(1)
            self.h_l.click_shouhuoliebiao()
            time.sleep(2)
            self.h_r.click_add_received()
            time.sleep(1)
            self.h_r.click_received_up()
            self.h_r.click_received_lower()
            self.h_r.send_Courier_number('15890158362')
            self.h_r.click_from_address()
            time.sleep(1)
            self.h_r.select_Province_text()
            time.sleep(1)
            self.h_r.uploads_img_one('E:\\tupian\\add1.jpg')
            time.sleep(1)
            self.h_r.uploads_img_two('E:\\tupian\\add2.jpg')
            time.sleep(2)
            self.h_r.click_Confirm_received_button()
            time.sleep(1)
            self.num = self.h_r.get_received_num()

        #按获取编号搜索-可用多页面
        def sourch(self):
            self.h_r.send_received_search_text(self.num)
            self.h_r.click_serch_received_button()
        #需求判断
        def xuqiu_panduan(self):
            self.h_xuqiu.get_tishi_xinxi_text()
        #需求管理界面模型匹配病例
        def Matched_case(self):
            time.sleep(3)
            self.h_l.click_xuqiuguanli()
            time.sleep(2)
            self.h_search.send_search_word(self.num)
            time.sleep(2)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_xuqiu.click_pipei_button()
            time.sleep(1)
            self.h_xuqiu.send_xuqiu_pipei_case(self.case_num)
            self.h_xuqiu.click_xuqiu_pipei_danan()
            time.sleep(2)
            self.h_xuqiu.click_xuqiu_queren_pipei_button()
            time.sleep(1)
            # if self.h_tishi.get_tishi_xinxi_text('error_tishi')=='该档案匹配的正常生产订单已经发货,不能再匹配!':
            #     time.sleep(1)
            #     print(self.h_xuqiu.get_tishi_xinxi_text(),'匹配失败')
            #     time.sleep(1)
            #     self.h_xuqiu.click_xuqiu_pipei_guanbi_button()
            #     return True
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '操作成功!':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False


        #收货匹配
        def new_erp_new_add_received(self):
            #self.erp_login("15890158362","123456")
            self.new_add_received()
            self.Matched_case()
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '操作成功!' :
                return True
            elif self.h_tishi.get_tishi_xinxi_text('error_tishi') == '该档案匹配的正常生产订单已经发货,不能再匹配!':
                self.h_xuqiu.click_xuqiu_pipei_guanbi_button()
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                self.h_xuqiu.click_xuqiu_pipei_guanbi_button()
                return False
        #模型扫描
        def new_erp_sm_stl(self):
            time.sleep(2)
            self.h_DH.click_moxingsaomiao_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_sm.click_sm_shangc_button()
            time.sleep(1)
            self.h_sm.upload_sm_up_stl('D:\\shangctp\\u.stl')
            time.sleep(1)
            self.h_sm.upload_sm_lower_stl('D:\\shangctp\\l.stl')
            time.sleep(2)
            self.h_sm.click_sm_queren_button()
            time.sleep(2)
            nun=self.h_tishi.get_tishi_xinxi_text('RO')
            #caseno=self.h_tishi.get_tishi_xinxi_text('caseno')
            dae="E:/clearbos/TestServer/PatientFiles/201901240002/Data2/m201901240002.cbm"
            print(dae)
            print(nun)
            data={
                "DemandBillNo": "%s"%nun,
                "UploadFilePath": dae
            }
            print(data)
            print(self.r.moxing_sm_pass(data))
            time.sleep(1)
            self.h_sm.click_sm_wnagcheng_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi')=='操作成功!':
                return True
            else:
                return False

        #资料质检
        def new_erp_data_zhijian(self):
            time.sleep(2)
            self.h_DH.click_ziliaozhijian_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_data_zj.click_data_zhijian_button()
            time.sleep(1)
            self.h_data_zj.upload_data_zj_one_img('E:\\tupian\\add1.jpg')
            time.sleep(1)
            self.h_data_zj.upload_data_zj_two_img('E:\\tupian\\add2.jpg')
            time.sleep(2)
            self.h_data_zj.upload_data_zj_img_wc()
            time.sleep(2)
            if self.h_tishi.get_tishi_xinxi_text('hege')=='合格':
                return True
            else:
                return False
        #下设计订单
        def Design_order(self):
            time.sleep(2)
            self.h_DH.click_dingdanguanli_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_orderGL.click_ordergl_sheji_button()
            time.sleep(1)
            self.h_orderGL.click_ordergl_chaungjian_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi')=='操作成功!':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False
        #设计跟进添加处方
        def Add_prescription(self):
            time.sleep(2)
            self.h_DH.click_shejigenjin_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_genjin.click_shejin_genjin_fenpei_button()
            time.sleep(1)
            self.h_genjin.click_sheji_genjin_fenpei_queren_button()
            time.sleep(1)
            #nun = self.h_tishi.get_tishi_xinxi_text('caseno')
            data={
                "CaseNo":"%s"%self.case_num
            }
            print(self.r.get_chufang_jianyi(data))
            treat=self.r.get_chufang_jianyi(data)
            time.sleep(1)
            do=self.h_tishi.get_tishi_xinxi_text('DO_num')
            datat={
                "CaseNo":"%s"%self.case_num,
                "TreatmentAdviseId":"%s"%treat,
                "DesignBillNo":"%s"%do,
                "PrescriptionTitle":"002",
                "PrescriptionContent":"排齐"
            }
            print(self.r.tianjia_chufang(datat))
            #新增
            time.sleep(1)
            self.h_genjin.click_sheji_genjin_chufang_button()
            time.sleep(1)
            #处方管理界面
            self.base.get_dangqian_chaungk_handle()
            print('处方管理',self.base.get_dangqian_chaungk_handle())
            time.sleep(1)
            url_chufangguanli=self.base.get_url()
            print(self.base.get_url())
            time.sleep(1)
            self.h_chakangenduo.clcik_sheji_genjin_chakangenduo_button()
            time.sleep(1)
            #临床诊断界面
            self.base.get_dangqian_chaungk_handle()
            print('临床诊断界面',self.base.get_dangqian_chaungk_handle())
            time.sleep(1)
            url_chakangenduo=self.base.get_url()
            time.sleep(1)
            #返回处方管理界面
            self.base.get_changkou_canshu_handle(2)
            print('处方管理',self.base.get_changkou_canshu_handle(2))
            time.sleep(1)
            #点击临床说明
            self.h_chakangenduo.click_chufangguanli_lcshuoming_button()
            time.sleep(1)
            #当前界面窗口
            self.base.get_dangqian_chaungk_handle()
            #获取临床url
            url_lc_shuoming=self.base.get_url()
            time.sleep(1)
            self.base.get_changkou_canshu_handle(0)
            time.sleep(1)
            if 'http://www.clearbos.cn:81/new/#/prescriptionManagement?' in url_chufangguanli and  'http://106.14.117.240:8080/Clearsite/' in \
                    url_chakangenduo and  'http://www.clearbos.cn:81/new//clinicalApp.html?' in url_lc_shuoming:
                return True
            else:
                return False
            # if  self.r.tianjia_chufang(datat)==200 or '200':
            #     return True
            # else:
            #     return False

         #数字建模
        def Digital_modeling(self):
            time.sleep(2)
            self.h_DH.click_shuozijianmo_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_jianmo.click_sz_zhipaidingdan_button()
            time.sleep(1)
            self.h_jianmo.click_sz_zhipai_queren_button()
            time.sleep(1)
            do = self.h_tishi.get_tishi_xinxi_text('DO_num')
            data = {
                 "DesignBillNo": "%s"%do,
                 "UploadFilePath": "E:/clearbos/TestServer/PatientFiles/201901240002/Data2/m201901240002.cbm"
            }
            print(self.r.upload_cbm(data))
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(1)
            self.h_jianmo.clcik_sz_shehetongguo_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '操作成功!':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False
        #模拟排牙
        def moni_design(self):
            time.sleep(2)
            self.h_DH.click_monipaiya_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_paiya.click_moni_zhipaidingdan_button()
            time.sleep(1)
            self.h_paiya.click_moni_zhipai_queren_button()
            data={
                "CaseNo": "%s"%self.case_num,
            }
            print(self.r.get_chufang_id(data))
            value=self.r.get_chufang_id(data)
            time.sleep(1)
            do = self.h_tishi.get_tishi_xinxi_text('DO_num')
            data = {
                "DesignBillNo": "%s" %do,
                "PrescriptionId": "%s"%value,
               "UploadFilePath": "E:/clearbos/TestServer/PatientFiles/201901240002/Data2/s201901240002DE0001.cbs"
            }
            print(self.r.upload_cbs(data))
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(1)
            self.h_paiya.clcik_moni_shehetongguo_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '操作成功!':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False

        #设计质检
        def design_quality(self):
            time.sleep(2)
            self.h_DH.click_shejizhijian_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_shejizhijian.click_sj_zj_zhipaidingdan_button()
            time.sleep(1)
            self.h_shejizhijian.click_sj_zj_zhipai_queren_button()
            time.sleep(1)
            self.h_shejizhijian.clcik_sj_zj_shehetongguo_button()
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '操作成功!':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False
        #下生产订单
        def Place_production_orders(self):
            time.sleep(1)
            self.h_DH.click_dingdanguanli_button()
            time.sleep(2)
            data = {
                "CaseNo": "%s" % self.case_num,
            }
            value = self.r.get_chufang_id(data)
            dataa={
                "CaseNo": "%s"%self.case_num,
                "PrescriptionId":"%s"%value,
            }
            time.sleep(1)
            self.r.doctor_confirm(dataa)
            time.sleep(1)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_orderGL.click_shengchang_button()
            time.sleep(2)
            self.h_orderGL.click_dingdanbianhao_button()
            time.sleep(2)
            self.h_orderGL.click_select_dingdanbianhao()
            self.h_orderGL.send_up_start('1')
            self.h_orderGL.send_up_end('8')
            self.h_orderGL.send_lower_start('1')
            self.h_orderGL.send_lower_end('8')
            time.sleep(2)
            self.h_orderGL.click_queren_xiadan_button()
            time.sleep(1)
            self.h_orderGL.click_queren_xiadan_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi')=='操作成功!':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False
        #生产调度
        def product_schedu(self):
            time.sleep(1)
            self.h_DH.click_sehngchandiaodu_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(1)
            self.h_diaodu.click_xuanze_kuan()
            time.sleep(1)
            self.h_diaodu.click_paican_yulan()
            time.sleep(2)
            self.h_diaodu.send_liuzhuanghao(self.liuzhuanghao)
            time.sleep(1)
            self.h_diaodu.click_queren_paichang()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '排产成功':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False
        #模型打印
        def model_print(self):
            time.sleep(1)
            self.h_DH.click_moxingdayin_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(1)
            self.h_Print.click_shengchan_wangcheng()
            time.sleep(2)
            self.h_Print.click_click_dayinji()
            time.sleep(1)
            self.h_Print.click_select_dayinji()
            time.sleep(1)
            self.h_Print.click_zuizhong_wancheng()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '操作成功':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False
        #产品成型
        def Product_moldle(self):
            time.sleep(1)
            self.h_DH.click_chanpinchengxing_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(1)
            self.h_chengxing.click_chengxing_wancheng_button()
            time.sleep(1)
            self.h_chengxing.click_queding_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '操作成功':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False
        #生产质检
        def production_quality(self):
            time.sleep(2)
            self.h_DH.click_erp_zhijian_button()
            time.sleep(2)
            self.h_DH.click_shengchangzhijian_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(1)
            self.h_zijian.click_baozhuang_button()
            time.sleep(2)
            self.h_zijian.click_zhijian_ok_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '操作成功!':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False
        #成品包装
        def product_baozhuang(self):
            time.sleep(1)
            self.h_DH.click_chengpinbaozhuang_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(1)
            self.h_baozhuang.click_baozhuang_wangc_button()
            time.sleep(1)
            self.h_baozhuang.click_queren_ruku_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '操作成功':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False
        #发货确认
        def fahuo_confirma(self):
            time.sleep(1)
            self.h_DH.click_fahuoqueren_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_fahuoqeuren.click_fahuo_button()
            time.sleep(1)
            self.h_fahuoqeuren.click_select_keyifahuo_button()
            time.sleep(1)
            self.h_fahuoqeuren.click_fahuo_quren_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '确认成功':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False
        #发货列表
        def fahuo_list(self):
            time.sleep(1)
            self.h_DH.click_fahuoliebiao_button()
            time.sleep(2)
            self.h_search.send_search_word(self.case_num)
            time.sleep(1)
            self.h_search.click_search_button()
            time.sleep(2)
            self.h_fahuolist.click_youji_button()
            time.sleep(1)
            self.h_fahuolist.send_kaudidanhao_text('15890158362')
            time.sleep(1)
            self.h_fahuolist.click_kaudi_queren_button()
            time.sleep(1)
            self.h_fahuolist.click_queren_button()
            time.sleep(2)
            self.h_fahuolist.click_qurenfahuo_button()
            time.sleep(1)
            if self.h_tishi.get_tishi_xinxi_text('success_tishi') == '发货成功':
                return True
            else:
                print(self.h_tishi.get_tishi_xinxi_text('error_tishi'))
                return False


