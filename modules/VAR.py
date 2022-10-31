import itertools
import pandas as pd
import numpy as np
import scipy
import statsmodels as st
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.api import VAR
from statsmodels.tools.eval_measures import rmse, aic
from statsmodels.tsa.vector_ar.vecm import coint_johansen





def cointegration():
    return

def cointegration_test(df, alpha=0.05):
    output = coint_johansen(df, 0 , 1) 
    return

def VAR_model(train, valid, ):
    model = VAR(endog = train )
    model_fit = model.fit()
    pred = model_fit.forecast(model_fit.y, steps=len(valid))
    transform = pd.DataFrame(index=range(len(pred)), columns=[train.columns])
    for j, i in itertools.product(range(len(train.columns) + 1), range(len(pred))):
        transform.iloc[i][j] = pred[i][j]
        
    error =print('rmse value for', i, 'is : ', rmse(transform[i], valid[i]))
    return transform, error
