# 用户名：2486974634
# 密码：halamadrid
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

username = '2486974634'  # 输入你的4399账号
password = 'halamadrid'  # 输入你的4399密码
path = "F:\\driver\\chromedriver_win32\\chromedriver.exe"
#browser = Chrome( executable_path=path)
s = Service(path)
driver = webdriver.Chrome(service=s)
#driver = webdriver.Chrome(executable_path=path)
wait = WebDriverWait(driver, 10)
driver.get('http://www.4399.com/')
# 找到登录入口，并点击
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login_tologin'))).click()
# 切入frame
driver.switch_to.frame('popup_login_frame')
# 找到输入框，输入账号密码
wait.until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(username)
wait.until(EC.presence_of_element_located((By.ID, 'j-password'))).send_keys(password)
# 点击登录按钮
wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, '#login_form > fieldset > div.login_hor.ux_login.clearfix > input'))).click()
time.sleep(2)
driver.quit()