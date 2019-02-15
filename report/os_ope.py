import os
import time
exeFile = "E:\\4.0.0.0\\bin\ClearShape.exe" #程序地址
url="WebClearShape://ID=201901150003&name=Data1&operationstyle=5&phase=Data1&StlUrl=E:/clearbos/TestServer/FormalPatientFiles/201901150003/Data1/u.stl;E:/clearbos/TestServer/FormalPatientFiles/201901150003/Data1/l.stl&modelfile=E:/clearbos/TestServer/FormalPatientFiles/201901150003/Data1/m201901150003.cbm&schemefile=&DemandBillNo=RO20190115000301&DesginBillNo=DO20190115000301&BillNo=DE0001&PrescriptionId=10973&Token=5bQ24_JeMsNmJVKZaZ8AAN6Nf_uwvaufLvFu8OpqiKULBsGTSDLxiMJmtdJxtv91R4LeXA8bSAqkGhsHMy5lWmaG5ls0-2FZN1h-j0nCngOfp-aeq4kunh6Sr2RND5xTsc8ARcFUZ2iC4VHA_2281TQD92q5QKZiFu14w9UeJ_tiPngzwICh7NQdBCm8XSFjaI0s01ydQlm3rSNCbpGbP-2XKXl66uM0e0VqudjL7Lk90_JelynAhxyO2InR0Y4oQvlrUzy4Gh7wL1zdUt8Kmvynh4QhMnbkZ7NOmSym3u1rZ9koxIh9JQ1_pbVLJ3Pf&a=123"
class osopen():

    def open(self):
        command = exeFile + " \"" + url + "\""
        print(command)
        os.system(command)
        os.system("E:\\tupian\\aa1.exe")
        time.sleep(1)
        print("确认开始")

if __name__=="__main__":
    ope=osopen()
    ope.open()