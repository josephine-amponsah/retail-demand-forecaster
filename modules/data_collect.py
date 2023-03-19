import requests
import io
import pandas as pd
# import flask_caching
from flask_caching import Cache


sales_url="https://github.com/ladyjossy77/retail-optimization/blob/master/data/sales.csv?raw=true"
# sales=requests.get(sales_url).content
# sales_da =pd.read_csv(io.StringIO(sales.decode('utf-8')))
returns_url="https://github.com/ladyjossy77/retail-optimization/blob/master/data/returns.csv?raw=true"

timeout = 20

# cache = Cache(app.server, config={
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'cache-directory'
# })
@cache.memoize(timeout= timeout)

def sales_data():  # sourcery skip: inline-immediately-returned-variable
    sales=requests.get(sales_url).content
    sales_data =pd.read_csv(io.StringIO(sales.decode('utf-8')))
    return sales_data

def returns_data():  # sourcery skip: inline-immediately-returned-variable
    returns=requests.get(returns_url).content
    returns_data =pd.read_csv(io.StringIO(returns.decode('utf-8')))
    return returns_data