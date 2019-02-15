from Page.add_received_page import received_page
import os,sys

class received_handle():
    def __init__(self,driver):
        self.p=received_page(driver)
    #点击新增收货
    def click_add_received(self):
        self.p.button_add_received().click()
    #选择石膏上颌
    def click_received_up(self):
        self.p.button_received_up().click()
    #选择石膏下颌
    def click_received_lower(self):
        self.p.button_received_lower().click()
    #输入快递单号
    def send_Courier_number(self,aaa):
        self.p.text_Courier_number().send_keys(aaa)
    #点击物流来源
    def click_from_address(self):
        self.p.seclect_from_address().click()
    #选择省份
    def select_Province_text(self):
        self.p.select_Province().click()
    #上传第一张收货图片
    def uploads_img_one(self,aaa):
        self.p.upload_img_one().send_keys(aaa)
    # 上传第二张收货图片
    def uploads_img_two(self,aaa):
        self.p.upload_img_two().send_keys(aaa)
    #点击确认收货
    def click_Confirm_received_button(self):
        self.p.Confirm_receipt_button().click()
    #获取新增的货物编号
    def get_received_num(self):
        return self.p.received_num().text
    #输入获取编号
    def send_received_search_text(self,aaa):
        self.p.text_received_search().send_keys(aaa)
    #点击搜索
    def click_serch_received_button(self):
        self.p.serch_received_button().click()