from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
python_events = {}


for i in range(len(events)):
    python_events[i] = {
        "time" : dates[i].text,
        "event" : events[i].text
    }

# for key, value in python_events.items():
#     print(key, value['time'], value['event'])

print(python_events)

driver.close()