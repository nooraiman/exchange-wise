from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Set Chrome options
# Headless mode is a browser mode that runs without a GUI. This means that the browser is not visible to the user.
options = Options()
options.add_argument("--headless")

# Create a new instance of the Chrome driver
driver = webdriver.Firefox(options=options)

# Array of URLs to scrape
urls = [
    'https://wise.com/gb/currency-converter/usd-to-myr-rate',
    'https://wise.com/gb/currency-converter/sgd-to-myr-rate',
    'https://wise.com/gb/currency-converter/thb-to-myr-rate',
    'https://wise.com/gb/currency-converter/idr-to-myr-rate',
]

# Create an empty dictionary to store the data
data = {}

print("Scraping data from Wise...")

# Loop through each URL
for url in urls:
    driver.get(url)

    # Wait for the page to fully load
    wait = WebDriverWait(driver, 10)

    # Wait for the specific element to be visible
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3.cc__source-to-target.hidden-xs')))

    # Get the text of the element
    text = element.text  # '1 USD = 4.71725 MYR'

    # Split the text into parts
    parts = text.split()  # ['1', 'USD', '=', '4.71725', 'MYR']

    # Get the currency pair and the exchange rate
    currency_pair = parts[1] + parts[4]  # 'USDMYR'
    exchange_rate = float(parts[3])  # '4.71725'

    # Calculate the reverse exchange rate
    reverse_exchange_rate = 1 / exchange_rate

    # Add the data to the dictionary
    data[currency_pair] = exchange_rate
    data[parts[4] + parts[1]] = reverse_exchange_rate

# Close the browser
driver.quit()
print("Scraping complete.")

# Convert the dictionary to a JSON object
json_object = json.dumps(data)

# Write the JSON object to a file
with open('/data/wise.json', 'w') as f:
    f.write(json_object)

print("Data saved to /data/wise.json")