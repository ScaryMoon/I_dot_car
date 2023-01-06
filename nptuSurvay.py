
import ddddocr  # 驗證碼
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from time import sleep

# 設定google driver的路徑檔案2
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False})
driver = webdriver.Chrome(
    options=options, service=Service("./chromedriver.exe"))
driver.maximize_window()



# ----------------login-----------------
while True:

    driver.get("https://webap.nptu.edu.tw/Web/Secure/default.aspx")

    sleep(2)
    student = WebDriverWait(driver, 10)
    student = student.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/form/table/tbody/tr[1]/td/table[2]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input"))).click()
    sleep(0.1)
    ac = WebDriverWait(driver, 10)
    ac = ac.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input")))
    sleep(0.1)
    ac = driver.find_element(
        By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input")
    ac.send_keys("")#your account
    sleep(0.1)
    password = driver.find_element(
        By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input")
    password.send_keys("")#your password
    sleep(0.1)
    atho = driver.find_element(
        By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/img")
    atho.screenshot("code.png")

    ocr = ddddocr.DdddOcr()
    with open('code.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    print(res)
    sleep(0.2)
    keyAtho = driver.find_element(
        By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input")
    keyAtho.send_keys(res)
    sleep(0.1)
    Login = driver.find_element(
        By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[3]/input")
    Login.click()
    sleep(1)
    try:
        findSomeThing = WebDriverWait(driver, 7)
        findSomeThing = findSomeThing.until(EC.visibility_of_element_located(
            (By.LINK_TEXT, "公布主題")))
        if findSomeThing != None:
            break
    except:
        pass
                

# 登入後

survay = WebDriverWait(driver, 10)
survay = survay.until(EC.visibility_of_element_located(
    (By.XPATH, "/html/body/form/div[3]/table[9]/tbody/tr/td[2]/a/span")))
sleep(0.5)

mid = WebDriverWait(driver, 10)
mid = mid.until(EC.visibility_of_element_located(
    (By.CLASS_NAME, "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/a"))).click()
                     
#個別填表單 未測試
sleep(0.5)
mids1=driver.find_elements(By.XPATH,"//tr[@class='TRItemStyle']")
mids2=driver.find_elements(By.XPATH,"//tr[@class='TRAlternatingItemStyle']")

for i in range(0,mids1.count):
    try:
        mids= driver.find_element(By.XPATH,f"/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[{2+i*2}]/td[1]/input")

        if mids.is_enabled:
            print("i come in")
            mids.click()
            sleep(4)
            driver.back()
            sleep(1)
    except:pass


sleep(2)

for i in range(0,mids2.count):
    try:
        mids= driver.find_element(By.XPATH,f"/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[{3+i*2}]/td[1]/input")
        if mids.is_enabled:
            print("i come in 2")
            mids.click()
            sleep(4)
            driver.back()
            sleep(1)
    except:pass


# final = WebDriverWait(driver, 10)
# final = final.until(EC.visibility_of_element_located(
#     (By.CLASS_NAME, "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[1]/td/table/tbody/tr[3]/td[1]/a"))).click()
# sleep(0.2)

# fins1=driver.find_elements(By.XPATH,"//tr[@class='TRItemStyle']")
# fins2=driver.find_elements(By.XPATH,"//tr[@class='TRAlternatingItemStyle']")
# sleep(0.3)