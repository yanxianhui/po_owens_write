from base.findelment import Findelement

class new_page():
    def __init__(self,driver):
        self.p=Findelement(driver)

    def get_account(self):
        return self.p.get_element('doctor_account')

    def get_password(self):
        return self.p.get_element('doctor_password')

    def get_new_login_button(self):
        return self.p.get_element('doctor_button')

    def get_new_case_button(self):
        return self.p.get_element('new_case')

    def get_name_send(self):
        return self.p.get_element('patientName')

    def get_sex_click(self):
        return self.p.get_element('patientSex')

    def get_year_click(self):
        return self.p.get_element('birthdayYear')

    def get_mouth_click(self):
        return self.p.get_element('birthdayMonth')

    def get_day_click(self):
        return self.p.get_element('birthdayDate')

    def get_phoneNum_click(self):
        return self.p.get_element('patientTel')

    def get_hospotl_click(self):
        return self.p.get_element('hospital')
    #点击填写基本信息界面的下一步
    def get_t_next_click(self):
        return self.p.get_element('t_button')

    def click_img1(self):
        return self.p.get_element('45Profile1')

    def click_img2(self):
        return self.p.get_element('FrontalRepose1')

    def click_img3(self):
        return self.p.get_element('FrontalSmile1')

    def click_img4(self):
        return self.p.get_element('Profile1')

    def click_img5(self):
        return self.p.get_element('Upper1')

    def click_img6(self):
        return self.p.get_element('Left1')

    def click_img7(self):
        return self.p.get_element('Lower1')

    def click_img8(self):
        return self.p.get_element('Anterior1')

    def click_img9(self):
        return self.p.get_element('Right1')

    def click_img10(self):
        return self.p.get_element('Cephalometric1')

    def click_img11(self):
        return self.p.get_element('Panoramic1')
    #点击上传照片界面的下一步
    def clicl_s_button(self):
        return self.p.get_element('s_button')
    #勾选临床诊断情况
    def click_lchuang_text_button(self):
        return self.p.get_element('lc_tape')
    #勾选治疗选择-患者类型
    def click_huanze_tape(self):
        return self.p.get_element('ziliao_tape')
    #勾选治疗选择-产品类型
    def click_chanpin_tape(self):
        return self.p.get_element('canpin_tape')
    #点击临床诊断下一步
    def click_l_button(self):
        return self.p.get_element('l_button')
    #选择已邮寄模型
    def click_shuzi_button(self):
        return self.p.get_element('shuzi_m_buttom')
    #数字模型
    def click_s_m_button(self):
        return self.p.get_element('s_m_button')
    #上传上颌
    def click_u_stl_button(self):
        return self.p.get_element('u_stl')
    #上传下颌
    def click_l_stl_button(self):
        return self.p.get_element('l_stl')


    def click_m_button(self):
        return self.p.get_element('m_button')

    def click_t_bu_button(self):
        return self.p.get_element('t_bu_button')
    #获取病例详情按钮元素
    def get_patient_details(self):
        return self.p.get_element('patient_details')
    #获取病例元素
    def get_patient_number(self):
        return self.p.get_element('patient_number')
    #获取病例详情中的病例姓名
    def get_patient_details_name(self):
        return self.p.get_element('patient_details_name')
    #获取病例姓名
    def get_patinet_name(self):
        return self.p.get_element('patient_name')
