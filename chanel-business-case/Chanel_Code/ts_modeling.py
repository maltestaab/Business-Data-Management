import pandas as pd
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.stattools import adfuller

def test_stationarity(series: pd.Series) -> None:
    """
    Perform ADF test to check for stationarity.
    """
    result = adfuller(series.dropna())
    print(f"ADF Statistic: {result[0]}")
    print(f"p-value: {result[1]}")
    for key, value in result[4].items():
        print(f"Critical Value ({key}): {value}")

def train_ar_model(series: pd.Series, lags: int) -> AutoReg:
    """
    Train an AutoRegressive (AR) model on the time series data.
    """
    model = AutoReg(series, lags=lags).fit()
    return model

def forecast_with_model(model: AutoReg, steps: int) -> pd.Series:
    """
    Forecast future values using the AR model.
    """
    forecast = model.predict(start=len(model.model.endog), end=len(model.model.endog) + steps - 1)
    return forecast