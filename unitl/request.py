import requests
from unitl.read_ini import Readini
from jsonpath_rw import parse
import json
class erp_requests():
    def __init__(self):
        self.rr=Readini('D:\po_owens_write\config\example.ini','res')
        self.headers = {
        "Authorization":"Bearer QO8ZTQawAdOO5gv8tAoI3hLMNqNzkDg1RB0Hn5m8vQJqJSHDq71bw1u8EyKq5CuBGyQgzYrRClIPvC8fSfp_n7oMnt72jEcDuXnFD_7O2222wqzfBq1gaBxUZTxeBqwurbtPMqDETCGom7SnTOp9GdtTBGot7tBMLI_aYSaES_HqzphCinZmmTbt-vhPJe8v02Xd2aksBeC6M-Mun51C9D8tprnYyU2BU-PYEyJK23U_6XGYdygoBUo05RbT7P99pPki1UeK80N2GFsz3T_yCp6T0exv7jgHtYvFtaQwx7oid-nl-GFUC9BKjYstCjzK"}
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
        url = 'http://www.clearbos.cn:8087/api/flow/dm/upload'
        # data = {
        #     # "DemandBillNo": "RO20190116002601",
        #     "DesignBillNo": "DO20190116002601",
        #     "UploadFilePath": "E:/clearbos/TestServer/FormalPatientFiles/201901160026/Data1/m201901160026.cbm"
        # }
        res=requests.post(url,data,headers=self.headers)
        return res.json()
    #获取处方建议
    def get_chufang_jianyi(self,data):
        url = 'http://www.clearbos.cn:8087/api/flow/df/getuntreatedadviselist'
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
        urlt = 'http://www.clearbos.cn:8087/api/flow/df/addprescription'
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
        url='http://www.clearbos.cn:8087/api/flow/dm/upload'
        #  data = {
        #      "DemandBillNo": "RO20190124000701",
        #      #"DesignBillNo":"DO20190117001801",
        #      "UploadFilePath": "E:/clearbos/TestServer/PatientFiles/201901240002/Data2/m201901240002.cbm"
        # }
        res = requests.post(url,data,headers=self.headers)
        return res.json()
    #获取处方id
    def get_chufang_id(self,data):
        url='http://www.clearbos.cn:8087/api/flow/df/getprescriptionadviselist'
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
        url = 'http://www.clearbos.cn:8087/api/flow/df/upload'
        # datal = {
        #     "DemandBillNo": "DO20190103002101",
        #     "PrescriptionId": "10890",
        #     "UploadFilePath": "E:/clearbos/TestServer/PatientFiles/201901240002/Data2/s201901240002DE0001.cbs"
        # }
        res = requests.post(url,data,headers=self.headers)
        return res.json()
    #医生确认方案
    def doctor_confirm(self,data):
        url='http://www.clearbos.cn:8087/Api/Flow/CaseClinicalOperation/ConfirmCurrentCaseScheme'
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
    headers={
        "Authorization":"Bearer -Wu9QTdulQ5IArfjxk_AMx_OTmoBrB9DhBx8tZXOqE6bsGTHf6u7MF03SCUrakNtvP-X6NR8SrCM1DQJcwMJ-gDr9j_xD3HOKd-RrHpme4U3Xfccm7MNyC4CUf3yZV0HmH5LseBVudvPXY5im4k5WLLV9NT-WALMLfkVmMvrnIhX6PJUgBV4wkaE6o8dxP_62Dl5n2BaohOx25bBl2_nXD7L5vde9JWv2eMiVWNXEqVYV1m53cGZAijpyJWJU40fSVtuDmp5y8RbYJQEhRCx5i0wFvuRCnIUjUdlu6sBSuf1YeLFm2w8nBimmr61rKba"}
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