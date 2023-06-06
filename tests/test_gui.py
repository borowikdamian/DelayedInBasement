from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.get("https://delayedinbasement.onrender.com")

text_input = driver.find_element(By.ID, "text")
text_input.send_keys("example")

button = driver.find_element(By.ID, "button")
button.click()

driver.quit()
