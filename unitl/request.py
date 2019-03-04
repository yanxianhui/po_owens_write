import requests
from unitl.read_ini import Readini
from jsonpath_rw import parse
import json
from base.configure import Configure
class erp_requests():
    def __init__(self):
        self.rr=Readini('D:\po_owens_write\config\example.ini','res')
        self.config=Configure()
        self.headers=Configure().headers
        #self.headers = {
        #"Authorization":"Bearer Oz_by0UQWiSE4LHaBeihZZMMyE7qX3vPdtk_3zBrNIVdrbdb5Um6Jxmpt1FCP4gOOSyJCwY9iFPltNA6CI_FHjuGvz48wnkvZq5a_0NfrfaTZytkhUg4RSdKE11uQxUBo8MjwExcMukLti91eXrL2Ynau1qADIbKWyw_wR5Bs-E7zKNKwUn3052p4OFdNsXi0XNXozOqQNKfmVSD44nje3Zgbx8ldnOyft8rqi-6P4RBE89ysTfDkDxCuqSdw742WJx70GficjgISt64kyB2xby4Q7bDHrDFB-4OfvL0ewkSTmBVfjG5PsFPK7hLtWfA"}
    def send_post(self,url,data,header):
        res=requests.post(url=url,data=data,headers=header)
        data='Data[0].TreatmentAdviseId'
        value=res.json()
        json_exe = parse(data)
        maile = json_exe.find(value)
        return [math.value for math in maile][0]
        #return res.json()

    #模型扫描上传
    def moxing_sm_pass(self,data):
        url=self.config.api_test+'/api/flow/dm/upload'
        #url = 'http://www.clearbos.cn:8087/api/flow/dm/upload'
        # data = {
        #     # "DemandBillNo": "RO20190116002601",
        #     "DesignBillNo": "DO20190116002601",
        #     "UploadFilePath": "E:/clearbos/TestServer/FormalPatientFiles/201901160026/Data1/m201901160026.cbm"
        # }
        res=requests.post(url,data,headers=self.headers)
        return res.json()
    #获取处方建议
    def get_chufang_jianyi(self,data):
        url=self.config.api_test+'/api/flow/df/getuntreatedadviselist'
        #url = 'http://www.clearbos.cn:8087/api/flow/df/getuntreatedadviselist'
        # data = {
        #     "CaseNo": "201901240008"
        # }
        res = requests.post(url, data, headers=self.headers)
        tata = 'Data[0].TreatmentAdviseId'
        value = res.json()
        json_exe = parse(tata)
        maile = json_exe.find(value)
        return [math.value for math in maile][0]

    #添加处方
    def tianjia_chufang(self,data):
        urlt=self.config.api_test+'/api/flow/df/addprescription'
        #urlt = 'http://www.clearbos.cn:8087/api/flow/df/addprescription'
        # datat={
        #     "CaseNo":"201901240008",
        #     "TreatmentAdviseId":"18016",
        #     "DesignBillNo":"DO20190124000801",
        #     "PrescriptionTitle":"002",
        #     "PrescriptionContent":"排齐"
        #
        # }
        res = requests.post(urlt, data, headers=self.headers)
        tata = 'Code'
        value = res.json()
        json_exe = parse(tata)
        maile = json_exe.find(value)
        return [math.value for math in maile][0]

    #上传模型
    def upload_cbm(self,data):
        url=self.config.api_test+'/api/flow/dm/upload'
        #url='http://www.clearbos.cn:8087/api/flow/dm/upload'
        #  data = {
        #      "DemandBillNo": "RO20190124000701",
        #      #"DesignBillNo":"DO20190117001801",
        #      "UploadFilePath": "E:/clearbos/TestServer/PatientFiles/201901240002/Data2/m201901240002.cbm"
        # }
        res = requests.post(url,data,headers=self.headers)
        return res.json()
    #获取处方id
    def get_chufang_id(self,data):
        url=self.config.api_test+'/api/flow/df/getprescriptionadviselist'
        #url='http://www.clearbos.cn:8087/api/flow/df/getprescriptionadviselist'
        # data={
        #     "CaseNo": "201901240013",
        # }
        res = requests.post(url,data,headers=self.headers)
        tata = 'Data[0].PrescriptionId'
        value = res.json()
        json_exe = parse(tata)
        maile = json_exe.find(value)
        return [math.value for math in maile][0]

    #上传cbs
    def upload_cbs(self,data):
        url=self.config.api_test+'/api/flow/df/upload'
       # url = 'http://www.clearbos.cn:8087/api/flow/df/upload'
        # datal = {
        #     "DemandBillNo": "DO20190103002101",
        #     "PrescriptionId": "10890",
        #     "UploadFilePath": "E:/clearbos/TestServer/PatientFiles/201901240002/Data2/s201901240002DE0001.cbs"
        # }
        res = requests.post(url,data,headers=self.headers)
        return res.json()
    #医生确认方案
    def doctor_confirm(self,data):
        url=self.config.api_test+'/Api/Flow/CaseClinicalOperation/ConfirmCurrentCaseScheme'
        #url='http://www.clearbos.cn:8087/Api/Flow/CaseClinicalOperation/ConfirmCurrentCaseScheme'
        # data={
        #     "CaseNo":"201901240013",
        #     "PrescriptionId":"12005",
        # }
        res = requests.post(url,data,headers=self.headers)
        return res.json()



if __name__=="__main__":
    ope = erp_requests()
    # data = {
    #         "DemandBillNo": "RO20190116002601",
    #         #"DesignBillNo": "DO20190116002601",
    #          "UploadFilePath": "E:/clearbos/TestServer/FormalPatientFiles/201901160026/Data1/m201901160026.cbm"
    #     }
    # print(ope.moxing_sm_pass(data))

   #  url='http://www.clearbos.cn:8087/api/flow/dm/upload'
   #  data = {
   #      "DemandBillNo": "RO20190124000701",
   #      #"DesignBillNo":"DO20190117001801",
   #      "UploadFilePath": "E:/clearbos/TestServer/PatientFiles/201901240002/Data2/m201901240002.cbm"
   # }
    #headers={
      #  "Authorization":"Bearer Oz_by0UQWiSE4LHaBeihZZMMyE7qX3vPdtk_3zBrNIVdrbdb5Um6Jxmpt1FCP4gOOSyJCwY9iFPltNA6CI_FHjuGvz48wnkvZq5a_0NfrfaTZytkhUg4RSdKE11uQxUBo8MjwExcMukLti91eXrL2Ynau1qADIbKWyw_wR5Bs-E7zKNKwUn3052p4OFdNsXi0XNXozOqQNKfmVSD44nje3Zgbx8ldnOyft8rqi-6P4RBE89ysTfDkDxCuqSdw742WJx70GficjgISt64kyB2xby4Q7bDHrDFB-4OfvL0ewkSTmBVfjG5PsFPK7hLtWfA"}
    #模型扫描上传cbm
   # print(ope.send_post(url,data,headers))

    #数字建模上传cbm
   # print(ope.send_post(url,data,headers))

    #模拟排牙上传cbs
    # urll = 'http://www.clearbos.cn:8087/api/flow/df/upload'
    # datal = {
    #     "DemandBillNo": "DO20190103002101",
    #     "PrescriptionId": "10890",
    #     "UploadFilePath": "E:/clearbos/TestServer/PatientFiles/201901240002/Data2/s201901240002DE0001.cbs"
    # }
    # print(ope.send_post(urll,datal,headers))


    #添加处方
    # urlt='http://www.clearbos.cn:8087/api/flow/df/addprescription'
    # datat={
    #     "CaseNo":"201901240008",
    #     "TreatmentAdviseId":"18016",
    #     "DesignBillNo":"DO20190124000801",
    #     "PrescriptionTitle":"002",
    #     "PrescriptionContent":"排齐"
    #
    # }
    # print(ope.send_post(urlt, datat, headers))
    #获取未出处方建议列表
    # url='http://www.clearbos.cn:8087/api/flow/df/getuntreatedadviselist'
    # data={
    #     "CaseNo":"201901240008"
    # }
    #
    # print(ope.send_post(url, data, headers))
    #print(ope.doctor_confirm())