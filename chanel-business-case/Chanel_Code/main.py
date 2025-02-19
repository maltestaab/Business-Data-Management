from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

########## DATA IMPORT ###########

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

# Path to your Google Cloud service account key file
key_path = credentials_path

# Create credentials and initialize the BigQuery client
credentials = service_account.Credentials.from_service_account_file(key_path)
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

# Preview the DataFrame
print(df_2025.head())

############# Preprocessing ################

# Preprocessing
df_cleaned = clean_cartier_data(df)
df_converted = convert_prices_to_eur(df_cleaned)