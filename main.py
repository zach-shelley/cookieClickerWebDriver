import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# Use ID, Name, Class, CSS selector, Xpath to find element(s) to interact with and access attributes
def check_inventory():
    inventory = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    highest_item = None
    highest_price = 0
    total_cookies = int(cookies_element.text.split(' ')[0])
    for item in inventory:
        price = int(item.find_element(By.CLASS_NAME, "price").text)

        if highest_price < price <= total_cookies:
            highest_item = item
            highest_price = price

    if highest_item:
        highest_item.click()

time.sleep(2)
start_time = time.time()

lang_select = driver.find_element(By.ID, "langSelect-EN")
lang_select.click()

cookie = driver.find_element(By.ID, "bigCookie")
cookies_element = driver.find_element(By.ID, "cookies")


last_check = time.time()
game_on = True

while game_on:

    cookie.click()

    current_time = time.time()
     # check if 5 seconds have passed
    if current_time - last_check >= 10:
        check_inventory()
        last_check = current_time

    if current_time - start_time >= 300:
        game_on = False

driver.close()
cookies_per_second = cookies_element.text.split(' ')[-1]
print(f"cookies/sec : {cookies_per_second} ")

# closes tab
# driver.quit() closes browser
