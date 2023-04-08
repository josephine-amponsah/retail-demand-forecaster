import sktime
from sktime.forecasting.compose._multiplexer import MultiplexForecaster
from sktime.forecasting.theta import ThetaForecaster
# from sktime.forecasting.exp_smoothing import ExponentialSmoothing
from sktime.forecasting.ets import AutoETS
from sktime.forecasting.naive import NaiveForecaster
# from sktime.forecasting.trend import PolynomialTrendForecaster
from sktime.forecasting.compose import ForecastingPipeline
import pandas as pd

pipe = ForecastingPipeline(steps =[
    MultiplexForecaster(forecasters=[
    ("ets", AutoETS()),
    ("theta", ThetaForecaster()),
    ("naive", NaiveForecaster())] )
])
def transform(df, columns, values):
    df = df.groupby(columns)[values].sum()
    return df

def forecast(fh, df, start):
    df = transform(df, columns, values)
    pred = model.predict()
    final = pred[[start]]
    return final

