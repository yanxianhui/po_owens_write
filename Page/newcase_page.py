from base.findelment import Findelement

class NewcasePage():
    def __init__(self,driver):
        self.find_element=Findelement(driver)

    #z找到医生账号输入框
    def get_doctor_login_username(self):
        return self.find_element.get_element('Doctoruser')
    #z找到医生密码输入框
    def get_doctor_login_password(self):
        return self.find_element.get_element('Doctorpassword')
    #z找到医生登录提交按钮输入框
    def get_doctor_login_button(self):
        return self.find_element.get_element('Doctorbutton')
    #找到新建病例按钮
    def get_doctor_newcase_button(self):
        return self.find_element.get_element('Doctorxinzeng')
    #找到患者姓名输入框
    def get_Patient_name(self):
        return self.find_element.get_element('Patientname')
    #找到患者性别选择
    def get_Patient_sex(self):
        return self.find_element.get_element('Patientsex')
    #找到患者生日
    def get_Patient_bath(self):
        return self.find_element.get_element('Patientbrth')
    #找到患者手机输入栏位
    def get_Patient_phone(self):
        return self.find_element.get_element('Patientphone')
    #找到登记资料下一步按钮
    def get_Dj_next(self):
        return self.find_element.get_element('Patientnext')
    #找到正式通道元素
    def get_Formal_load(self):
        return self.find_element.get_element('PatientZTD')
    #找到石膏模型按钮
    def get_SG_model(self):
        return self.find_element.get_element('PatientSgMx')
    #找到快递单号输入框
    def get_Kd_number(self):
        return self.find_element.get_element('KDnumber')
    #找到上传图片位置
    def get_IMG1(self):
        return self.find_element.get_element('IMG1')
    def get_IMG2(self):
        return self.find_element.get_element('IMG2')
    def get_IMG3(self):
        return self.find_element.get_element('IMG3')
    def get_IMG4(self):
        return self.find_element.get_element('IMG4')
    def get_IMG5(self):
        return self.find_element.get_element('IMG5')
    def get_IMG6(self):
        return self.find_element.get_element('IMG6')
    def get_IMG7(self):
        return self.find_element.get_element('IMG7')
    def get_IMG8(self):
        return self.find_element.get_element('IMG8')
    def get_IMG9(self):
        return self.find_element.get_element('IMG9')
    def get_IMG10(self):
        return self.find_element.get_element('IMG10')
    def get_IMG11(self):
        return self.find_element.get_element('IMG11')
    #找到上传下一步按钮
    def get_upload_picture_next(self):
        return self.find_element.get_element('Pationxiabu')
    #找到主诉输入框
    def get_mian_Opinion_text(self):
        return self.find_element.get_element('Pationtext')
    #找到过敏史输入框
    def get_GminS_Text(self):
        return self.find_element.get_element('Pationtext1')
    #找到治疗史输入框
    def get_History_treatment_text(self):
        return self.find_element.get_element('Pationtext2')
    #找到治疗方案
    def get_Treatment_plan_test(self):
        return self.find_element.get_element('Pationtext3')
    #找到临床处方意见界面下一步按钮
    def get_lin_cuang_yijian_next(self):
        return self.find_element.get_element('Pationnext3')
    #找到提交病例按钮
    def get_Case_submit(self):
        return self.find_element.get_element('Bltijiao')


