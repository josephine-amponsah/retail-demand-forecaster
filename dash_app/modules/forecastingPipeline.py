# import sktime
# from sktime.forecasting.compose._multiplexer import MultiplexForecaster
# from sktime.forecasting.theta import ThetaForecaster
# # from sktime.forecasting.exp_smoothing import ExponentialSmoothing
# from sktime.forecasting.ets import AutoETS
# from sktime.forecasting.naive import NaiveForecaster
# # from sktime.forecasting.trend import PolynomialTrendForecaster
# from sktime.forecasting.compose import ForecastingPipeline
import pandas as pd
import sklearn 
import joblib
import pickle

with open("modules/forecaster.pkl", 'rb') as f:
    model = joblib.load(f)

# model = joblib.load('')

# def transform(df, columns, values):
#     df = df.groupby(columns)[values].sum()

#     return df

def forecast(fh):
    pred = model.predict(fh)
    final = pred.reset_index()
    return final

