from Page.new_doctor_page import new_page
import os,sys
from selenium.webdriver.support.ui import Select

class new_handle():
    def __init__(self,driver):
        self.h=new_page(driver)


    def send_accunt(self,accunt):
        self.h.get_account().send_keys(accunt)
    def send_password(self,password):
        self.h.get_password().send_keys(password)
    def click_login_button(self):
        self.h.get_new_login_button().click()

    def click_new_case(self):
        self.h.get_new_case_button().click()

    def send_patientName(self,patientName):
        self.h.get_name_send().send_keys(patientName)

    def click_sex(self):
        self.h.get_sex_click().click()

    def click_birthdayYear(self):
        Select(self.h.get_year_click()).select_by_visible_text('1990年')

    def click_birthdayMonth(self):
        Select(self.h.get_mouth_click()).select_by_visible_text('02月')

    def click_birthdayDate(self):
        Select(self.h.get_day_click()).select_by_visible_text('02日')

    def send_phone_num(self,phone):
        self.h.get_phoneNum_click().send_keys(phone)

    def click_hospital(self):
        Select(self.h.get_hospotl_click()).select_by_visible_text('雅熙诊所')

    def click_t_button(self):
        self.h.get_t_next_click().click()

    def upodle_img1(self,aaa):
        self.h.click_img1().send_keys(aaa)

    def upodle_img2(self,aaa):
        self.h.click_img2().send_keys(aaa)

    def upodle_img3(self,aaa):
        self.h.click_img3().send_keys(aaa)

    def upodle_img4(self,aaa):
        self.h.click_img4().send_keys(aaa)

    def upodle_img5(self,aaa):
        self.h.click_img5().send_keys(aaa)

    def upodle_img6(self,aaa):
        self.h.click_img6().send_keys(aaa)

    def upodle_img7(self,aaa):
        self.h.click_img7().send_keys(aaa)

    def upodle_img8(self,aaa):
        self.h.click_img8().send_keys(aaa)

    def upodle_img9(self,aaa):
        self.h.click_img9().send_keys(aaa)

    def upodle_img10(self,aaa):
        self.h.click_img10().send_keys(aaa)

    def upodle_img11(self,aaa):
        self.h.click_img11().send_keys(aaa)

    def upload_picture_add(self, value):
        os.system(value)
    #点击上传图片下一步
    def click_s(self):
        self.h.clicl_s_button().click()
    #点击临床信息
    def click_lingc_text(self):
        self.h.click_lchuang_text_button().click()
        #test=self.h.click_lchuang_text_button()
        #print('结果',test,"元素")
    #点击患者类型
    def click_huanze_tape_button(self):
        self.h.click_huanze_tape().click()
    #点击产品类型
    def click_canpin_tape_button(self):
        self.h.click_chanpin_tape().click()
    #点击临床诊断下一步
    def click_l(self):
        self.h.click_l_button().click()
    #点击暂不邮寄
    def click_m(self):
        self.h.click_m_button().click()
    #点击已邮寄模型
    def click_shuzi_moxing_button(self):
        self.h.click_shuzi_button().click()
    #选择数字模型
    def click_select_sz_button(self):
        self.h.click_s_m_button().click()
    #上传上颌
    def upload_u_stl(self,aaa):
        self.h.click_u_stl_button().send_keys(aaa)

    # 上传下颌
    def upload_l_stl(self,aaa):
        self.h.click_l_stl_button().send_keys(aaa)

    def click_case_tijiao(self):
        self.h.click_t_bu_button().click()

    #点击病例详情
    def click_patient_details(self):
        self.h.get_patient_details().click()
    #获取新建后的病例号
    def get_add_patient_number(self):
        return self.h.get_patient_number().text
    # 获取新建后的病例姓名(详情)
    def get_patient_details_name(self):
        return self.h.get_patient_details_name().text

    #获取新建后的病例姓名
    def get_add_patient_name(self):
        return self.h.get_patinet_name().text