import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

"""chrome driver"""
service_obj = Service("C://Users/hp/Desktop/browerDriver/chromedriver.exe")

"""firefox webdriver"""
service_obj = Service("C://Users/hp/Desktop/browerDriver/geckodriver.exe")

# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Firefox(service=service_obj)
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
time.sleep(2)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
time.sleep(2)
driver.back()
driver.refresh()
driver.forward()
driver.close()
