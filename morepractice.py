from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
# get first name <input>

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

first_name.send_keys("Zach")
last_name.send_keys("Shelley")
email.send_keys("zachshelley19@gmail.com")

button = driver.find_element(By.CLASS_NAME, value="btn-primary")
button.send_keys(Keys.ENTER)