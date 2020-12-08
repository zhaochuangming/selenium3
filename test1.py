#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By
cc = webdriver.Chrome()
cc.get("https://mail.qq.com/")
print(WebDriverWait(cc,10).until(EC.title_is("登录QQ邮箱")))

#知识点：class_name定位出现多个值处理方法
#1.先去console输入代码：document.getElementsByClassName("")，然后找到对应的下标
cc.switch_to.frame(1)
sleep(1)
# cc.find_elements_by_class_name("inputstyle")[0].send_keys("1030253545@qq.com")
# cc.find_elements_by_class_name("inputstyle")[1].send_keys("Cczcmily926520...")
# cc.find_element_by_class_name("login_button").click()

#知识点：判断元素是否可见
kj = (By.CLASS_NAME,"inputstyle")
print(WebDriverWait(cc,1).until(EC.visibility_of_element_located(kj)))
cc.close()

