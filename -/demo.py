# coding=utf-8
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
desired_caps = {}
# 自动化测试引擎
desired_caps["automationName"] = "UiAutomator2"
# 平台类型
desired_caps["platformName"] = "Android"
# 平台版本
desired_caps["platformVersion"] = "6.0.1"
# 设备名称
desired_caps["deviceName"] = "Android Emulator"
# app包名
desired_caps["appPackage"] = "cn.com.open.mooc"
# app入口acitivity
desired_caps["appActivity"] = "com.imooc.component.imoocmain.splash.MCSplashActivity"


# 连接appium server。前提appium desktop要启动，有监听端口
# 要将desired_caps服务器参数发送给appium server，打开app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# 运行代码之前：
# 1。appium server启动成功，处于监听状态
# 2。模拟器或者真机必须能够被电脑识别，即adb devices

#点击同意
WebDriverWait(driver,200).until(EC.visibility_of_element_located((MobileBy.ID,"cn.com.open.mooc:id/btPositive")))
driver.find_element_by_id("cn.com.open.mooc:id/btPositive").click()
# 点击左上角关闭
WebDriverWait(driver,200).until(EC.visibility_of_element_located((MobileBy.ID,"cn.com.open.mooc:id/left_icon")))
driver.find_element_by_id("cn.com.open.mooc:id/left_icon").click()
# 点击账户
WebDriverWait(driver,200).until(EC.visibility_of_element_located((MobileBy.ID,"cn.com.open.mooc:id/lav")))
driver.find_element_by_android_uiautomator('text(\"账号\")').click()
# 点击登陆
WebDriverWait(driver,200).until(EC.visibility_of_element_located((MobileBy.ID,"cn.com.open.mooc:id/tvLoginNow")))
driver.find_element_by_id("cn.com.open.mooc:id/tvLoginNow").click()
# 点击用户名密码的登陆方式
WebDriverWait(driver,200).until(EC.visibility_of_element_located((MobileBy.ID,"cn.com.open.mooc:id/tvPassLogin")))
driver.find_element_by_id("cn.com.open.mooc:id/tvPassLogin").click()
# 输入用户名，密码，点击登陆
WebDriverWait(driver,200).until(EC.visibility_of_element_located((MobileBy.ID,"cn.com.open.mooc:id/accountEditChannel2")))
driver.find_element_by_id("cn.com.open.mooc:id/accountEditChannel2").send_keys("13811814444")
driver.find_element_by_id("cn.com.open.mooc:id/passwordEditChannel2").send_keys("5556666666")
driver.find_element_by_id("cn.com.open.mooc:id/login").click()
# toast，xpath文本匹配
loc = (MobileBy.XPATH,'//*[contains(@text,"{}")]'.format("未注册"))
# 等待的时候，要用元素存在的条件，不能用元素可见的条件
try:
    WebDriverWait(driver,5,0.01).until(EC.presence_of_element_located(loc))
    print(driver.find_element_by_xpath('//*[contains(@text,"{}")]'.format("未注册")).text)
except:
    print("没有找到匹配的toast")





