from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:\\chromedriver_win32\\chromedriver.exe')
webbrowser=webdriver.Chrome(service=s)
url='https://nimsts.edu.in/AHIMSG5/hissso/loginLogin.action'
browser.get(url)