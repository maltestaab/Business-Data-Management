from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import bigquery_storage
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from transformation import clean_cartier_data, convert_prices_to_eur


########## DATA IMPORT ###########

# Load environment variables from .env file
load_dotenv()

# Access environment variables
model_target = os.getenv("MODEL_TARGET")
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Print to check if they are loaded correctly
print(f"\nModel Target: {model_target}")
print(f"\nGoogle Credentials Path: {credentials_path}")
print("\n")


# Create credentials and initialize the BigQuery client
credentials = service_account.Credentials.from_service_account_file(credentials_path)
client = bigquery.Client(credentials=credentials, project="edhecbusinessdatamanagement")


############# 2022-2024 Data ############

query = """
    SELECT * 
    FROM `edhec-business-manageme.luxurydata2502.price-monitoring-2022`
    WHERE Brand = 'Cartier'
"""

# Run the query and load results into a Pandas DataFrame
df = client.query(query).to_dataframe()


# Path to your Google Cloud service account key file
key_path = credentials_path

print("\n###2020-2022 DF ###")
# Preview the DataFrame
print(df.head())
########### 2025 Data ##############


# Define SQL query
query = """
SELECT *
FROM `edhecbusinessdatamanagement.cartier_us.cartier_us`
WHERE brand = 'Cartier';
"""

# Run query and store results in a DataFrame
query_job = client.query(query)
df_2025 = query_job.result().to_dataframe()

print("\n### 2025 DF ###")
# Preview the DataFrame
print(df_2025.head())

############# Preprocessing ################

# Preprocessing
df_cleaned = clean_cartier_data(df)
df_converted = convert_prices_to_eur(df_cleaned)

df_2025_cleaned = clean_cartier_data(df_2025)
df_2025_converted = convert_prices_to_eur(df_2025_cleaned)


print("\n### 2020-2022 DF CLEANED AND CONVERTED ###")
# Preview the DataFrame
print(df_converted)


df_converted.columns()

