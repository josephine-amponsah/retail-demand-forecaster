import pandas as pd
import numpy as np
import plotly.express as pe
import seaborn as sns


def summaryCard(df, value, agg, group):
    data = data.groupby(group)[value].agg()
    