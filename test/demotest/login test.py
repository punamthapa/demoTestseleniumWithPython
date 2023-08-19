import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
driver.refresh()

driver.find_element(By.XPATH,"//input[@id='gender-female']").click()
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Punam")
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys("Thapa")

dayDropdown=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']"))
dayDropdown.select_by_value("10")
monthDropdown=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']"))
monthDropdown.select_by_value("11")
yearDropdown=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthYear']"))
yearDropdown.select_by_value("1999")
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("abc1213@gmail.com")
driver.find_element(By.XPATH,"//input[@id='Company']").send_keys("Happy")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("12345@Abc")
driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys("12345@Abc")
driver.find_element(By.XPATH,"//button[@id='register-button']").click()

time.sleep(10)

driver.quit()
