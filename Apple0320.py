from selenium import webdriver
from PIL import Image # pillow 安裝 Anaconda 時已自動安裝
import time
from time import sleep
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# 取出 綱頁圖中的驗證圖片，存入 檔
# 請調整解析度
url = "https://www.apple.com/tw/shop/buy-iphone/iphone-12"
driver = webdriver.Chrome()
driver.get(url)

#time.sleep(1)
#driver.maximize_window()
#time.sleep(1)
#driver.find_element_by_id("btn-confirm").click() # 按我同意
#driver.find_element_by_link_text("iPhone").click()
#driver.find_element_by_css_selector(".chapternav-item-iphone-12 .chapternav-icon").click()
# 5 | click | css=.ac-ln-button | 
#time.sleep(1)
#driver.find_element_by_css_selector(".ac-ln-button").click()

#time.sleep(2)
###########################################################

# 6 | click | id=Item1-dimensionScreensize-6_1inch | 
driver.find_element_by_id("Item1-dimensionScreensize-6_1inch").click()
time.sleep(1)
# 7 | runScript | window.scrollTo(0,200) | 
driver.execute_script("window.scrollTo(0,200)")
# 8 | click | css=.white > .ir | 
time.sleep(1)
driver.find_element_by_css_selector(".white > .ir").click()
# 9 | click | css=#Item364gb_label > .form-selector-title | 
time.sleep(1)
driver.find_element_by_css_selector("#Item364gb_label > .form-selector-title").click()
# 10 | runScript | window.scrollTo(0,850) | 
driver.execute_script("window.scrollTo(0,850)")
# 11 | click | css=.label | 
WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.label')))
driver.find_element_by_css_selector(".label").click()
sleep(4)
driver.find_element_by_name("proceed").click()
sleep(3)
# 13 | click | id=shoppingCart.actions.navCheckout | 
driver.find_element_by_id("shoppingCart.actions.navCheckout").click()
# 14 | mouseOver | id=guest-checkout | 
sleep(3)
driver.find_element_by_id("signIn.guestLogin.guestLogin").click()
#WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.ID,'signIn.guestLogin.guestLogin')))
# 16 | click | css=#guest-checkout > span | 
sleep(3)
driver.find_element_by_css_selector(".as-svgicon-applestorepickup").click()
# 17 | click | css=.as-buttongroup-item:nth-child(1) .form-icon-label | 
sleep(3)
driver.find_element_by_css_selector(".as-storelocator-searchitem:nth-child(1) .as-storelocator-available-quote").click()
# 18 | click | css=.form-selector-right-col | 
sleep(3)
driver.find_element_by_css_selector(".rs-pickup-slot:nth-child(3) .form-selector-label").click()
# 19 | click | id=rs-checkout-continue-button-bottom | 

driver.find_element_by_id("2021-03-31timeWindows").click()
dropdown = driver.find_element_by_id("2021-03-31timeWindows")
dropdown.find_element_by_xpath("//option[. = '下午 2:15 – 下午 2:30']").click()
driver.find_element_by_id("2021-03-31timeWindows").click()
# 20 | runScript | window.scrollTo(0,0) | 
driver.find_element_by_id("rs-checkout-continue-button-bottom").click()
sleep(3)
driver.find_element_by_css_selector(".large-6:nth-child(1) .rs-pickup-optionstitle").click()
sleep(1)
driver.find_element_by_name("lastName").click()
# 22 | type | id=recon-0-153 | 林
driver.find_element_by_name("lastName").send_keys("林")
# 23 | click | id=recon-0-154 | 
driver.find_element_by_name("firstName").click()
# 24 | type | id=recon-0-154 | 肇勳
driver.find_element_by_name("firstName").send_keys("肇勳")
# 25 | click | id=recon-0-163-city | 
driver.find_element_by_name("emailAddress").click()
driver.find_element_by_name("emailAddress").send_keys("remremtan0202@gmail.com")
driver.find_element_by_name("mobilePhone").click()
driver.find_element_by_name("mobilePhone").send_keys("0970404388")


###############
driver.find_element_by_id("rs-checkout-continue-button-bottom").click()
time.sleep(3)
driver.find_element_by_css_selector("#checkout\\.billing\\.billingOptions\\.options\\.0-selector .row").click()
time.sleep(3)

driver.find_element_by_name("cardNumber").click()
driver.find_element_by_name("cardNumber").send_keys("4705 3803 1455 4425")

driver.find_element_by_name("expiration").click()
driver.find_element_by_name("expiration").send_keys("10/25")

driver.find_element_by_name("securityCode").click()
driver.find_element_by_name("securityCode").send_keys("002")




driver.find_element_by_name("lastName").click()
driver.find_element_by_name("lastName").send_keys("林")

driver.find_element_by_name("firstName").click()
driver.find_element_by_name("firstName").send_keys("肇勳")



dropdown.find_element_by_xpath("//option[. = '新北市']").click()
driver.find_element_by_id("city").click()

driver.find_element_by_name("street").click()
driver.find_element_by_name("street").send_keys("板橋區實踐路93巷57號4樓")
#postalCode
driver.find_element_by_name("postalCode").click()
driver.find_element_by_name("postalCode").send_keys("220")

driver.find_element_by_css_selector(".form-selector-group:nth-child(5) .form-selector-label").click()
driver.find_element_by_css_selector(".form-selector-group:nth-child(5) .row .row").click()
driver.find_element_by_id("recon-0-229").click()
driver.find_element_by_id("recon-0-229").send_keys("1221")
driver.find_element_by_id("recon-0-230").click()
driver.find_element_by_id("recon-0-230").send_keys("1221")
driver.find_element_by_css_selector(".rs-fapiao").click()
driver.find_element_by_css_selector("#rs-checkout-continue-button-bottom > span").click()
driver.find_element_by_id("rs-checkout-continue-button-bottom").click()


