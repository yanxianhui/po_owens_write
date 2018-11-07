from Page.newcase_page import NewcasePage
import sys,os
class Newcase_handle():
    def __init__(self,driver):
        self.page=NewcasePage(driver)

    #输入医生账号
    def send_doctor_username(self,username):
        self.page.get_doctor_login_username().clear()
        self.page.get_doctor_login_username().send_keys(username)
    #输入医生密码
    def send_doctor_password(self,password):
        self.page.get_doctor_login_password().clear()
        self.page.get_doctor_login_password().send_keys(password)
    #点击登录按钮
    def click_doctor_button(self):
        self.page.get_doctor_login_button().click()
    #点击新建病例按钮
    def click_newcase_button(self):
        self.page.get_doctor_newcase_button().click()
    #输入患者姓名
    def send_Patient_name(self,name):
        self.page.get_Patient_name().send_keys(name)
    #选择性别
    def click_Patient_sex(self):
        self.page.get_Patient_sex().click()
    #输入生日
    def send_Patient_bath(self,bath):
        self.page.get_Patient_bath().send_keys(bath)
    #输入患者手机号
    def send_Patient_phone(self,phone):
        self.page.get_Patient_phone().send_keys(phone)
    #点击登记信息下一步
    def click_Dj_next(self):
        self.page.get_Dj_next().click()
    #选择正式通道
    def click_Formal_load(self):
        self.page.get_Formal_load().click()
    #点击石膏模型
    def click_SG_model(self):
        self.page.get_SG_model().click()
    #输入快递单号
    def send_Kd_number(self,number):
        self.page.get_Kd_number().send_keys(number)
    #点击上传图片
    def click_picture_a1(self):
        self.page.get_IMG1().click()
    def click_picture_a2(self):
        self.page.get_IMG2().click()
    def click_picture_a3(self):
        self.page.get_IMG3().click()
    def click_picture_a4(self):
        self.page.get_IMG4().click()
    def click_picture_a5(self):
        self.page.get_IMG5().click()
    def click_picture_a6(self):
        self.page.get_IMG6().click()
    def click_picture_a7(self):
        self.page.get_IMG7().click()
    def click_picture_a8(self):
        self.page.get_IMG8().click()
    def click_picture_a9(self):
        self.page.get_IMG9().click()
    def click_picture_a10(self):
        self.page.get_IMG10().click()
    def click_picture_a11(self):
        self.page.get_IMG11().click()
    #上传图片
    def upload_picture_add(self,value):
        os.system(value)
    #上传步骤界面点击下一步
    def upload_picture_next(self):
        self.page.get_upload_picture_next().click()
    #输入主诉
    def send_mian_Opinion_text(self,value):
        self.page.get_mian_Opinion_text().send_keys(value)
    #输入过敏史
    def send_GminS_Text(self,value):
        self.page.get_GminS_Text().send_keys(value)
    # 输入治疗史
    def send_History_treatment_text(self,value):
        self.page.get_History_treatment_text().send_keys(value)
    #输入治疗方案
    def send_Treatment_plan_test(self,value):
        self.page.get_Treatment_plan_test().send_keys(value)
    #点击临床处方意见下一步
    def click_lin_cuang_yijian_next(self):
        self.page.get_lin_cuang_yijian_next().click()
    #点击提交病例
    def click_Case_submit(self):
        self.page.get_Case_submit().click()
    #获取元素
    def get_emelent_data(self,info):
        try:
            if info=='T_button':
                res=self.page.get_doctor_newcase_button()
            else:
                res=None
            return res
        except:
            return print("h_未找到元素")


