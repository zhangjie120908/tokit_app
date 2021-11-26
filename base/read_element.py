#coding=utf-8
import configparser
from appium import webdriver

class ReadElement():

    def __init__(self,driver):
        self.cf = self.read_ini()
        self.driver = driver

    #读取ini文件
    def read_ini(self):
        cf = configparser.ConfigParser()
        cf.read(r"../config/test.ini", encoding="utf-8")
        return cf
    #获取节点
    def get_element(self,inivalues):
        convalues = self.cf.get("registerElement",inivalues)
        return convalues

    #获取节点内的元素
    def find_element(self,inivalues):
        data = self.get_element(inivalues)
        key = data.split(">")[0]
        value = data.split(">")[1]
        if key == "id":
            return self.driver.find_element_by_id(value)
        elif key == "class":
            return self.driver.find_element_by_class_name(value)
        elif key == "xpath":
            return self.driver.find_element_by_xpath(value)
        else:
            return self.driver.tap(value)


# if __name__ == "__main__":
#     re = ReadElement("driver")
#     print(re.get_element("guide_element"))