from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import time

# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the website
url = "http://radiohound.ee.nd.edu/Nodes/Periodogram/3414b566471f"
driver.get(url)

# Wait for page elements to load
time.sleep(10)

# CSS selector for the initial button
button_css_selector = '#root > div > div:nth-child(4) > div > div > div > div > div.col-xl-2.col-lg-3.col-md-3.col-sm-4.col-12 > form > div.btn-group > button.btn.btn-primary.btn-sm'
# CSS selector for the repeated click button
button_css_selector2 = '#DisplayOptions-tabpane-details > div > div > button'

# Set the end time to 24 hours from now
end_time = datetime.now() + timedelta(days=1)

# Click the initial button
button = driver.find_element(By.CSS_SELECTOR, button_css_selector)
button.click()

# Loop to click the second button every 5 seconds for a day
while datetime.now() < end_time:
    try:
        button2 = driver.find_element(By.CSS_SELECTOR, button_css_selector2)
        button2.click()
        time.sleep(5)
        print("Button clicked")
    except Exception as e:
        print(f"Error: {e}")

# Close the browser
driver.quit()
