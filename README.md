
# HIERARCHICAL FORECASTING ECOMMERCE

This projects aims at solving the problem of building one model that handles forecasts for different products, categories, and other levels of categorization.
The aim is to build a model that considers the varying behaviours of each item with respect to time.


## Tech Stack

**Languages:** Python

**Web Application:**  Dash, Dash-bootstrap, HTML, CSS

**Libaries:** scikit-hts, sktime, pandas, numpy, scikit-learn, seaborn, matplotlib

**Skills:** data cleaning, time series analysis, machine learning (time-series-forecasting)


## Data

The data used in this project was obtained from Kaggle (https://www.kaggle.com/datasets/felixzhao/productdemandforecasting).


## Roadmap

- Train several other estimators from the sktime library to optimize teh model runtime and accuracy.
- Deploy final model on web application
- Improve the UI design of the web application
- Modularize actions in the web application


## Features

- Interactive dashboard 
- Page in dashboard with input and trigger for running model
- Downloadable data table of resulting forecast
- Cloud deployed application



## Lessons Learned

1. What did you learn while building this project? 

I was newly introduced to hierarchical time series forecasting, learnt new libraries (scikit-hts, sktime), and learnt how to optimize training data for machine learning models.

2. What challenges did you face and how did you overcome them?

a. Intepreting libraries with very few articles/none on its implementation.
- I resolved it by reading the source codes, looking up approaches that were new.
  In cases where, I still couldn't complete intended tasks, I reached out for support from 
  experienced data scientists for support

b. Deploy an application to cloud (Google cloud)

- Failed one my first attempts and realized very little attention was paid.
  Have now learnt how to configure Dockerfiles, create docker images and configure WSGI server.


