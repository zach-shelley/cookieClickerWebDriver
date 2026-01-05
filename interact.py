from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

# Hone in on anchor tag to click direct
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount li:nth-of-type(2) a")

# find element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value='search')

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)




