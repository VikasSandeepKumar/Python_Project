from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://nimsts.edu.in/AHIMSG5/hissso/loginLogin.action")
driver.maximize_window()
driver.find_element_by_name("varUserName").send_keys("77004")
driver.find_element_by_name("varPassword").send_keys("123456")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/input").click()
driver.find_element_by_xpath("//*[@id='Inventory']/a").click()
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='frmMainMenu']"))
driver.find_element_by_id("Issue_2_collapse_wrapper").click()
driver.find_element_by_id("Issue_Desk").click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='Issue Desk_iframe']"))


