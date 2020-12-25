#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
from selenium.webdriver.common.by import By
cc = webdriver.Chrome()
cc.get("https://mail.qq.com/")
print(WebDriverWait(cc,10).until(EC.title_is("登录QQ邮箱")))
cc.switch_to.frame(1)
sleep(1)

#知识点：class_name定位出现多个值处理方法
#1.先去console输入代码：document.getElementsByClassName("")，然后找到对应的下标
# cc.find_elements_by_class_name("inputstyle")[0].send_keys("你邮箱")
# cc.find_elements_by_class_name("inputstyle")[1].send_keys("你密码")
# cc.find_element_by_class_name("login_button").click()

#知识点：判断元素是否可见
# kj = (By.CLASS_NAME,"inputstyle")
# print(WebDriverWait(cc,1).until(EC.visibility_of_element_located(kj)))
# visibility = cc.find_element_by_class_name("inputstyle")
# print(WebDriverWait(cc,1).until(EC.visibility_of(visibility)))

#知识点：获取用户信息
# cs = cc.find_element_by_id("uin_tips")
# print(cs.text)
# attribute = cc.find_elements_by_class_name("inputstyle")[0]
# attribute.send_keys("1030253545@qq.com")
# print(attribute.get_attribute("value"))

#知识点：生成用户名
for i in range(5):
    ueser_email = ''.join(random.sample('1234567890',5))+"qq.com"
    print(ueser_email)






















sleep(15)
cc.close()