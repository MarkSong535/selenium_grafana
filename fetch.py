from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime
import json

config = json.load(open('conf.json'))

# Get the current timestamp for the image name
# today = datetime.now()
image_name = config['filename']

# Set the path where the screenshot will be saved
path = os.path.dirname(os.path.abspath(__file__))

# Configure Chrome WebDriver options
options = Options()
options.add_argument("--window-size=800,480")
options.add_argument("--start-maximized")
options.add_argument("--headless")  # Use headless mode for running in the background
options.add_argument("--disable-gpu")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome('/usr/bin/chromedriver',options=options)
driver.maximize_window()

driver.get(f'{config['base_url']}/login')
driver.maximize_window()

time.sleep(1)

driver.find_element(By.XPATH, "//input[@placeholder='email or username']").send_keys(config['username'])
driver.find_element(By.XPATH, "//input[@placeholder='password']").send_keys(config['password'])
driver.find_element(By.CLASS_NAME, config['button_class']).click()

time.sleep(1)

# Navigate to the URL you want to capture
driver.get(config['dashboard_url'])

# Wait for the page to load (you can adjust the sleep time as needed)
time.sleep(1)

# Use JavaScript to get the full width and height of the webpage
# width = driver.execute_script("return Math.max( document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth );")
# height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

# Set the window size to match the entire webpage
driver.set_window_size(800, 480)

# Find the full page element (usually 'body') and capture the screenshot
full_page = driver.find_element(By.TAG_NAME, "body")
full_page.screenshot(f"{image_name}.png")

# Close the browser window
driver.quit()