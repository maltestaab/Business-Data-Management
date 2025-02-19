from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Set up the ChromeDriver path
chromedriver_path = r"C:\Users\kvgku\Downloads\scrapper\scrapper\driver\chromedriver-win64\chromedriver.exe"

# Set up Chrome options (headless mode is optional)
options = Options()
options.add_argument("--headless")  # Uncomment if you want to run it in headless mode
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
data=[]
# List of URLs to scrape
urls = [
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/panthere-de-cartier",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/tank",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/santos-de-cartier",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/ballon-de-cartier",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/baignoire",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/montres-panthere-joaillerie",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/ronde-et-rotonde-de-cartier",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/pasha-de-cartier",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/reflection-de-cartier",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/clash-unlimited",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/cartier-prive",
    "https://www.cartier.com/fr-fr/montres/collection-de-montres/haute-horlogerie"
]

# Loop through each URL
for url in urls:
    driver.get(url)
    
    # Wait for the page to load completely (you can adjust the time if necessary)
    time.sleep(5)

    # Find the product data by inspecting the HTML structure
    products = driver.find_elements(By.TAG_NAME, 'product-slot')

    # Loop through the products and extract relevant details
    for product in products:
        try:
            name = product.get_attribute('data-info').split('"name":"')[1].split('",')[0]
            short_description = product.get_attribute('data-info').split('"shortDescription":"')[1].split('",')[0]
            price = product.get_attribute('data-price').split('"fullPrice":')[1].split(',')[0]
            currency = product.get_attribute('data-price').split('"priceCurrency"')[1].split('"label":"')[1].split('"')[0]  # Extract currency
            reference_number = product.get_attribute('data-refnumber')
            product_url = product.get_attribute('data-url')
            
            # Print the extracted data
            print(f"URL: {url}")
            print(f"Name: {name}")
            print(f"Description: {short_description}")
            print(f"Price: {currency} {price}")
            print(f"Reference Number: {reference_number}")
            print(f"Product URL: {product_url}")
            print("-" * 50)
            
            data.append({
            'Product Name': name,
            'Description': short_description,
            'Price': price,
            'Currency': currency,
            'Reference_number': reference_number,
            'URL':product_url
        })
        except Exception as e:
            print(f"Error extracting data from product: {e}")

# Close the WebDriver
driver.quit()
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
df = df[df['Price'] != 'Price not found']
df.shape
# Reset index after removing rows (optional)
df.reset_index(drop=True, inplace=True)
df.head()
# Optionally, save the DataFrame to a CSV file
df.to_csv("cartier_products.csv", index=False) 
