import os

import configparser

import streamlit as st

from snowflake.snowpark import functions as F

from snowflake.snowpark.functions import *

import pandas as pd

from sklearn import datasets

from sklearn.ensemble import RandomForestClassifier

import numpy as np

import time

import matplotlib.pyplot as plt

# from snowflake.snowpark.functions import avg, sum, col,lit

from sklearn import datasets

from sklearn.ensemble import RandomForestClassifier


config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

#snowflake config

sfAccount = config['Snowflake']['sfAccount']
sfUser = config['Snowflake']['sfUser']
sfPass = config['Snowflake']['sfPass']
sfDB = config['Snowflake']['sfDB']
sfSchema = config['Snowflake']['sfSchema']
sfWarehouse = config['Snowflake']['sfWarehouse']



conn = snowflake.connector.connect(user = sfUser,
                                    password = sfPass,
                                    account = sfAccount,
                                    warehouse = sfWarehouse,
                                    database = sfDB,
                                    schema = sfSchema
                                    )

cs = conn.cursor()



data_one = pd.read_sql("select count(*) from FLOWER.PUBLIC.IRIS_FLOWER;",conn)

iris = pd.DataFrame(data_one, index=[0])



st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target


clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Flower types and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')

st.bar_chart(prediction_proba)

st.write(prediction_proba)




