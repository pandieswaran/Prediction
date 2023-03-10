# -*- coding: utf-8 -*-
"""Predicition.pynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R4-9T_4YgJKEEWMoq_1IjXYFULvC6Tg1

**Install Pystan 2.14**
"""

!pip install pystan~=2.14

"""**Install fbprophet**"""

!pip install fbprophet

"""**import Pandas Library**"""

import pandas as pd

"""**To insert a csv file to DataFrame**"""

df = pd.read_csv('USD_SILVER.csv')

"""**To check the value for the DataFrame**"""

df.info()

"""**To change the data type for Date Column**"""

df['Date'] =pd.to_datetime(df['Date'])

"""**To sort Date Column Value**"""

df.sort_values(by='Date', inplace = True)

df.info()

"""**To Check the Tail of the Data Frame**"""

df.tail()

"""**To Create a New Empty DataFrame**"""

sdf = pd.DataFrame()

"""**To Copy the One DataFrame to Another DataFrame**"""

sdf = df

"""**Only Date And Close Column**"""

sdf = sdf[['Date' , 'Close*']]

"""**To Change the Column Rename**"""

sdf.columns = ['ds' , 'y']

"""**To Use Prophet Library**"""

from fbprophet import Prophet

"""**To Fit the Data in Prophet Algorithm**"""

prophet = Prophet(daily_seasonality=True)
prophet.fit(sdf)

"""**Future Date Predict for using 365 Days**"""

future_dates = prophet.make_future_dataframe(periods=365)
predicitions =prophet.predict(future_dates)

"""**To view the Predicted Data and view a graph using Plotly**"""

from fbprophet.plot import plot_plotly

plot_plotly(prophet,predicitions)

"""**To insert a csv file to DataFrame**"""

tm = pd.read_csv('TATAMOTORS.NS.csv')

"""**To check the value for the DataFrame**"""

tm.info()

"""**To change the data type for Date Column**"""

tm['Date'] =pd.to_datetime(tm['Date'])

"""**To View the DataFrame Using Head Function**"""

tm.head()

sdf1 = tm

sdf1 = sdf1[['Date' , 'Close']]

sdf1.columns = ['ds' , 'y']

sdf1.info()

"""**To Fit the Data in Prophet Algorithm**"""

prophet1 = Prophet(daily_seasonality=True)
prophet1.fit(sdf1)

"""**Future Date Predict for using 365 Days**"""

future_dates = prophet1.make_future_dataframe(periods=365)
predicitions =prophet1.predict(future_dates)

"""**To view the Predicted Data and view a graph using Plotly**"""

from fbprophet.plot import plot_plotly

plot_plotly(prophet1,predicitions)