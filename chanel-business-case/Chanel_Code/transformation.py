import pandas as pd
import requests

def clean_cartier_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the Cartier DataFrame by dropping unnecessary columns and rows with missing values.
    """
    df = df.drop([
        "country", "is_new", "image_url",
        "price_difference", "price_percent_change",
        "price_changed", "price_before"
    ], axis=1)
    df = df.dropna(subset=['price', 'collection'])
    return df


def convert_prices_to_eur(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts 'price' to EUR based on the latest exchange rates and updates the 'currency' column.
    """
    url = 'https://v6.exchangerate-api.com/v6/4eb043dba172cec94fe70b22/latest/EUR'
    response = requests.get(url)
    data = response.json()
    conversion_rates = data["conversion_rates"]
    cr = pd.DataFrame(list(conversion_rates.items()), columns=["Currency", "Exchange Rate"])
    df = df.merge(cr, left_on="currency", right_on="Currency", how="left")
    df["price"] = df["price"] / df["Exchange Rate"]
    df["currency"] = "EUR"
    df = df.drop(columns=["Exchange Rate", "Currency"])
    return df



