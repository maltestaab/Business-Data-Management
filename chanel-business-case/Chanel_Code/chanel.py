from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import requests
import os
from dotenv import load_dotenv

import os
from dotenv import load_dotenv

# Handle .env path for both scripts and notebooks
try:
    # For .py scripts
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
except NameError:
    # For Jupyter Notebooks (__file__ not defined)
    project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))

# Load .env from project root
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)

# Access environment variables
model_target = os.getenv("MODEL_TARGET")
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Print to check if they are loaded correctly
print(f"Model Target: {model_target}")
print(f"Google Credentials Path: {credentials_path}")


######## Import of Dataset from BigQuery ############

# Path to your Google Cloud service account key file
key_path = credentials_path

# Create credentials and initialize the BigQuery client
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project="edhecbusinessdatamanagement")

# Big Query SQL Query
query = """
    SELECT * 
    FROM `edhec-business-manageme.luxurydata2502.price-monitoring-2022`
    WHERE Brand = 'Chanel'
"""

# Run the query and load results into a Pandas DataFrame
df = client.query(query).to_dataframe()

# Display the first 5 rows of the dataframe
print(df.head())



######## Data Cleaning ############

# Drop unnecessary columns
df = df.drop(columns=["country", "is_new", "image_url", 
                      "price_difference", "price_percent_change", 
                      "price_changed", "price_before"])

# Drop rows with missing values
df = df.dropna(subset=['price', 'collection'])



######## Preprocessing: Same Exchange rate for all products ############

# API URL for exchange rates (USD as base currency)
url = 'https://v6.exchangerate-api.com/v6/4eb043dba172cec94fe70b22/latest/EUR'

# Making the request
response = requests.get(url)
data = response.json()

# Extract the conversion rates dictionary
conversion_rates = data["conversion_rates"]

# Convert to DataFrame
cr = pd.DataFrame(list(conversion_rates.items()), columns=["Currency", "Exchange Rate"])

# Merge df1 (orders) with cr (exchange rates) based on currency
df_curr = df.merge(cr, left_on="currency", right_on="Currency", how="left")

# Convert price using the exchange rate
df_curr["price_EUR"] = df_curr["price"] / df_curr["Exchange Rate"]

# Drop unnecessary columns
df_curr = df_curr.drop(columns=["Exchange Rate", "Currency"])


print("\nrun correctly!!!")