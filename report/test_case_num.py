from selenium import webdriver
import time

class case_num():
    driver=webdriver.Chrome('C:\\Users\yanxianhuiclearbos\PycharmProjects\drivers\chromedriver.exe')
    driver.get('http://www.clearbos.cn:81/new/#/')
    driver.maximize_window()

    time.sleep(2)
    driver.find_element_by_xpath('//input[@placeholder="请输入账号"]').send_keys('15890158362')
    driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('123456')

    driver.find_element_by_xpath('//div[@class="operation"]/following-sibling::button').click()
    time.sleep(3)

    driver.find_element_by_css_selector('li.el-menu-item:nth-child(12)').click()
    time.sleep(2)
    cont = 1
    while (cont < 6):
        xpath = '//tbody/tr/td[2]/div/div'
        dingdan = driver.find_elements_by_xpath(xpath)
        for hao in dingdan:
            print(hao.text)

        driver.find_element_by_xpath('//button[@class="btn-next"]').click()
        time.sleep(2)
        cont = cont + 1
    xpath = '//tbody/tr/td[2]/div/div'
    dingdan = driver.find_elements_by_xpath(xpath)
    for hao in dingdan:
        print(hao.text)
    driver.quit()
    print("查询完成")

