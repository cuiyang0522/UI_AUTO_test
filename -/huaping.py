import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
desired_caps = {}
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
# 重置与否
desired_caps["noReset"] = True

# 连接appium server。前提appium desktop要启动，有监听端口
# 要将desired_caps服务器参数发送给appium server，打开app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#点击同意
# WebDriverWait(driver,200).until(EC.visibility_of_element_located((MobileBy.ID,"cn.com.open.mooc:id/btPositive")))
# driver.find_element_by_id("cn.com.open.mooc:id/btPositive").click()
# # 点击左上角关闭
# WebDriverWait(driver,200).until(EC.visibility_of_element_located((MobileBy.ID,"cn.com.open.mooc:id/left_icon")))
# driver.find_element_by_id("cn.com.open.mooc:id/left_icon").click()
#
loc_1 = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("推荐")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc_1))
# 从右向左滑动
size = driver.get_window_size()
start_x = size["width"] * 0.9
start_y = size["height"] * 0.5
end_x = size["width"] * 0.1
end_y = size["height"] * 0.5
driver.swipe(start_x,start_y,end_x,end_y,100)


# 向上滑动
loc = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("最新")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.swipe(size["width"]*0.5,size["height"]*0.9,size["width"] * 0.5,size["height"] * 0.1,100)
time.sleep(2)
driver.swipe(size["width"]*0.5,size["height"]*0.9,size["width"] * 0.5,size["height"] * 0.1,100)