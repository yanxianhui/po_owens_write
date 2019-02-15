from base.findelment import Findelement
import os,sys
class received_page():
    def __init__(self,driver):
        self.F=Findelement(driver)


    #点击新增收货
    def button_add_received(self):
        return self.F.get_element('add_received_button')
    #选择硅胶上颌
    def button_received_up(self):
        return self.F.get_element('received_up')
    #选择硅胶下颌
    def button_received_lower(self):
        return self.F.get_element('received_lower')
    #快递单号元素
    def text_Courier_number(self):
        return self.F.get_element('Courier_number')
    #物流来源
    def seclect_from_address(self):
        return self.F.get_element('from_address')
    #选择物流来源中的省份
    def select_Province(self):
        return self.F.get_element('select_Province')
    #上传第一张照片元素
    def upload_img_one(self):
        return self.F.get_element('upload_img_one')
    #上传第二张照片元素
    def upload_img_two(self):
        return self.F.get_element('upload_img_two')
    #获取确认收货按钮元素
    def Confirm_receipt_button(self):
        return self.F.get_element('Confirm_receipt_button')
    #获取搜索框元素
    def text_received_search(self):
        return self.F.get_element('received_search_text')
    #获取搜索按钮元素
    def serch_received_button(self):
        return self.F.get_element('received_button')

    #获取第一行货物编号
    def received_num(self):
        return self.F.get_element('received_num')