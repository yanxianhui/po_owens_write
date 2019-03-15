from selenium import webdriver

class base_method():
    def __init__(self,driver):
        self.driver=driver

    # 获取当前页面的url
    def get_url(self):
        return self.driver.current_url

    # 获取所有的窗户句柄
    def get_dangqian_chaungk_handle(self):
        handles = self.driver.window_handles  # 获取当前打开的所有窗口的句柄
        for handle in handles:
            if handle != self.driver.current_window_handle:
                print('switch to second window', handle)
                # brower.close() # 关闭第一个窗口
                self.driver.switch_to.window(handle)

    # 根据参数切换窗口
    def get_changkou_canshu_handle(self, aaa):
        handles = self.driver.window_handles  # 获取当前打开的所有窗口的句柄
        print(handles)
        self.driver.switch_to.window(handles[aaa])  # 切换到第二个窗口的句柄
        print(self.driver.current_window_handle)

    #选择不同的浏览器
    def select_Different_Browser(self,info):
        if info=='Chrome':
            return webdriver.Chrome()
        elif info=='Firefox':
            return webdriver.Firefox()
        elif info=='Ie':
            return webdriver.Ie()
        else:
            return webdriver.Edge()

