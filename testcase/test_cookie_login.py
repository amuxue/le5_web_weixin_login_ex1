import json

import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestWeixinLogin():
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome()

    # def teardown_method(self):
        # self.driver.quit()
    def test_cookie(self):
        # 读取cookie到cookiejson文件中
        cookies=self.driver.get_cookies()
        with open("cookies.json","w") as f:
            json.dump(cookies,f)
        # 写入cookie
        # self.driver.get("https://work.weixin.qq.com")
        # with open("cookies.json","r") as f:
        #     cookies=json.load(f)
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # sleep(3)
        # self.driver.find_element(By.ID,"menu_contacts").click()

    # def test_weixin_login(self):
    #     self.driver.get("https://work.weixin.qq.com")
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

