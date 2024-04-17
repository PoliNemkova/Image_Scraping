from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode

# Set the path to the ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Initialize the Chrome browser
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# URL of the e-commerce website
url = 'https://www.revolve.com/clothing/br/3699fc/?navsrc=main'

# Load the webpage
driver.get(url)

# Wait for the page to fully load (adjust this delay as needed)
time.sleep(5)

# Extract the HTML content after page fully loaded
html_content = driver.page_source

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all image elements
image_elements = soup.find_all('img', class_='s-product-grid-card-image')

# Extract image URLs and print them
for img in image_elements:
    img_url = img['src']
    print(img_url)

# Close the browser
driver.quit()
