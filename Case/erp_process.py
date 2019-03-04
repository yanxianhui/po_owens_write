from selenium import webdriver
from business.erp_process_business import erp_login_business
import unittest
import time,os
from base.configure import Configure
class Erp_login(unittest.TestCase):
    # def setUp(self):
    #     driver=webdriver.Chrome()
    #     self.case = login_Business(driver)
    #     driver.get('http://www.clearbos.cn/test/#/')
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:\\Users\yanxianhuiclearbos\PycharmProjects\drivers\chromedriver.exe')
        # option = webdriver.ChromeOptions()
        # option.add_argument("headless")
        # cls.driver=webdriver.Chrome(chrome_options=option)
        cls.driver.get(Configure.erp_url)
        #cls.driver.get('http://www.clearbos.cn:81/new/#/')
        cls.driver.maximize_window()

    def setUp(self):
        #self.driver.refresh()
        # option = webdriver.ChromeOptions()
        # option.add_argument("headless")
        # self.driver = webdriver.Chrome(chrome_options=option)
        # self.driver = webdriver.Chrome('C:\\Users\yanxianhuiclearbos\PycharmProjects\drivers\chromedriver.exe')
        # self.driver.get('http://www.clearbos.cn:81/new/#/')
        # self.driver.maximize_window()
        self.erp =erp_login_business(self.driver)
    def tearDown(self):
        time.sleep(1)
        # if sys.exc_info()[0]:
        # for method_name, error in self._outcome.errors:
        #     if error:
        #         case_name = self._testMethodName
        #         file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
        #         self.driver.save_screenshot(file_path)
                # print("这个是case的后置调键1")
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        time.sleep(1)
        cls.driver.quit()

     #登录erp
    def test_new_erp_case_a(self):
        denglu=self.erp.erp_login('15890158362','123456')
        self.assertTrue(denglu)
    #收货匹配
    def test_new_erp_case_b(self):
        shouhuopipei=self.erp.new_erp_new_add_received()
        self.assertTrue(shouhuopipei,'收货匹配错误')

    #模型扫描
    def test_new_erp_case_c(self):
        saomiao=self.erp.new_erp_sm_stl()
        self.assertTrue(saomiao)

    #资料质检
    def test_new_erp_case_d(self):
        zhijian_data=self.erp.new_erp_data_zhijian()
        self.assertTrue(zhijian_data)
    #下设计订单
    def test_new_erp_case_e(self):
        design_order=self.erp.Design_order()
        self.assertTrue(design_order)
    #添加处方
    def test_new_erp_case_f(self):
        tianjia_cf=self.erp.Add_prescription()
        self.assertTrue(tianjia_cf)
    #数字建模
    def test_new_erp_case_g(self):
        szjm=self.erp.Digital_modeling()
        self.assertTrue(szjm)
    #模拟排牙
    def test_new_erp_case_h(self):
        paya = self.erp.moni_design()
        self.assertTrue(paya)
    #设计质检
    def test_new_erp_case_i(self):
        sj_zhijian = self.erp.design_quality()
        self.assertTrue(sj_zhijian)
    #下生产单
    def test_new_erp_case_j(self):
        xiadan=self.erp.Place_production_orders()
        self.assertTrue(xiadan,'下单错误')
    #调度
    def test_new_erp_case_k(self):
        diaodu=self.erp.product_schedu()
        self.assertTrue(diaodu,'调度排产错误')
    #模型打印
    def test_new_erp_case_l(self):
        dayin=self.erp.model_print()
        self.assertTrue(dayin,'模型打印错误')
    #产品成型
    def test_new_erp_case_m(self):
        chengxing=self.erp.Product_moldle()
        self.assertTrue(chengxing,'产品成型错误')
    #生产质检
    def test_new_erp_case_n(self):
        zhijian=self.erp.production_quality()
        self.assertTrue(zhijian,'生产质检错误')
    #成品包装
    def test_new_erp_case_o(self):
        baozhuang=self.erp.product_baozhuang()
        self.assertTrue(baozhuang,'成品包装错误')
    # 发货确认
    def test_new_erp_case_p(self):
        fahuoqueren=self.erp.fahuo_confirma()
        self.assertTrue(fahuoqueren,'发货确认错误')
    # 发货列表
    def test_new_erp_case_q(self):
        fahuolist=self.erp.fahuo_list()
        self.assertTrue(fahuolist,'发货错误')




if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(Erp_login('test_new_erp_case_a'))
    suite.addTest(Erp_login('test_new_erp_case_b'))
    suite.addTest(Erp_login('test_new_erp_case_c'))
    suite.addTest(Erp_login('test_new_erp_case_d'))
    suite.addTest(Erp_login('test_new_erp_case_e'))
    suite.addTest(Erp_login('test_new_erp_case_f'))
    suite.addTest(Erp_login('test_pipei_moxing_g'))
    suite.addTest(Erp_login('test_new_erp_case_h'))
    suite.addTest(Erp_login('test_new_erp_case_i'))
    suite.addTest(Erp_login('test_pipei_moxing_g'))
    suite.addTest(Erp_login('test_new_erp_case_k'))
    suite.addTest(Erp_login('test_new_erp_case_l'))
    suite.addTest(Erp_login('test_new_erp_case_m'))
    suite.addTest(Erp_login('test_new_erp_case_n'))
    suite.addTest(Erp_login('test_new_erp_case_o'))
    suite.addTest(Erp_login('test_new_erp_case_p'))
    suite.addTest(Erp_login('test_new_erp_case_q'))




