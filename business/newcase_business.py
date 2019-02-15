from Handle.newcase_handle import Newcase_handle
from Handle.add_received_handle import received_handle
import time
class Newcase_business():
    def __init__(self,driver):
        self.newcase_h=Newcase_handle(driver)
        self.add_rexeived=received_handle(driver)


    def Newcase_base(self,patientname):
        self.newcase_h.send_doctor_username('15890158362')
        self.newcase_h.send_doctor_password('kle123456')
        self.newcase_h.click_doctor_button()
        time.sleep(2)
        self.newcase_h.click_newcase_button()
        time.sleep(2)
        self.newcase_h.send_Patient_name(patientname)
        self.newcase_h.click_Patient_sex()
        self.newcase_h.send_Patient_bath('2006-10-25')
        self.newcase_h.send_Patient_phone('15890158362')
        self.newcase_h.click_Dj_next()
        time.sleep(2)
        self.newcase_h.click_Formal_load()
        time.sleep(2)
        self.newcase_h.click_SG_model()
        self.newcase_h.send_Kd_number('78879789789')
        self.newcase_h.click_picture_a1()
        self.newcase_h.upload_picture_add('D:\\Ggshang1.exe')
        self.newcase_h.click_picture_a2()
        self.newcase_h.upload_picture_add('D:\\Ggshang2.exe')
        self.newcase_h.click_picture_a3()
        self.newcase_h.upload_picture_add('D:\\Ggshang3.exe')
        self.newcase_h.click_picture_a4()
        self.newcase_h.upload_picture_add('D:\\Ggshang4.exe')
        self.newcase_h.click_picture_a5()
        self.newcase_h.upload_picture_add('D:\\Ggshang5.exe')
        self.newcase_h.click_picture_a6()
        self.newcase_h.upload_picture_add('D:\\Ggshang6.exe')
        self.newcase_h.click_picture_a7()
        self.newcase_h.upload_picture_add('D:\\Ggshang7.exe')
        self.newcase_h.click_picture_a8()
        self.newcase_h.upload_picture_add('D:\\Ggshang8.exe')
        self.newcase_h.click_picture_a9()
        self.newcase_h.upload_picture_add('D:\\Ggshang9.exe')
        self.newcase_h.click_picture_a10()
        self.newcase_h.upload_picture_add('D:\\Ggshang10.exe')
        self.newcase_h.click_picture_a11()
        self.newcase_h.upload_picture_add('D:\\Ggshang11.exe')
        time.sleep(3)
        self.newcase_h.upload_picture_next()
        time.sleep(1)
        self.newcase_h.send_mian_Opinion_text('牙齿排齐')
        self.newcase_h.send_GminS_Text('无过敏史')
        self.newcase_h.send_History_treatment_text('无治疗史')
        self.newcase_h.send_Treatment_plan_test('拔除36、拔除12')
        self.newcase_h.click_lin_cuang_yijian_next()
        time.sleep(2)
        self.newcase_h.click_Case_submit()
        time.sleep(2)
    def newcase_success(self,patientname):
        self.Newcase_base(patientname)
        if self.newcase_h.get_emelent_data('T_button')!=None:
            return True
        else:
            return False
    def add_new_received(self):
        self.add_rexeived.click_add_received()


