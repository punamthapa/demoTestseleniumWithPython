from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
driver.refresh()

if driver.title == "nopCommerce demo store. Register":
   print('Title is verified')
else:
   print('Wrong Title')

