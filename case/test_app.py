#coding=utf-8
from appium import webdriver
from tokit_app.base.read_element import *
import time
class TokitApp():

    def __init__(self):
      device_info = {
        "platformName": "Android",
        "platformVersion": "7.1.2",
        "udid": "127.0.0.1:62025",
        "appPackage": "com.tokit.app",
        "appActivity": "com.tokit.app.ui.MainActivity",
        "deviceName": "VOG-AL10"
      }
      self.devices = webdriver.Remote("http://127.0.0.1:4723/wd/hub",device_info)
    #获取页面元素
    def page_element(self,values):
      pe = ReadElement(self.devices)
      pt = pe.find_element(values)
      return pt
    #页面输入元素
    def send_element(self,values,data):
      self.page_element(values).send_key(data)

    def run_main(self):
      time.sleep(5)
      self.page_element("guide_element").click()
      time.sleep(3)
      self.page_element("guide_element1").click()
      time.sleep(1)
      self.page_element("shipu_element").click()
      time.sleep(30)
      self.devices.quit()

if __name__ == "__main__":
  ta = TokitApp()
  cs = ta.run_main()
  if cs:
    print("食谱积分获取成功")
  else:
    print("你失败了")