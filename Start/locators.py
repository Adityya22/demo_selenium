from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/hp/Desktop/browerDriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("test@test.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys('987654321')
driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Aditya")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
