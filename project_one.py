import os
import configparser
import streamlit as st
import snowflake.connector
import pandas as pd
from sklearn import datasets
from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from sklearn.ensemble import RandomForestClassifier





config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

#snowflake config

sfAccount = config['Snowflakes']['sfAccount']
sfUser = config['Snowflakes']['sfUser']
sfPass = config['Snowflakes']['sfPass']
sfDB = config['Snowflakes']['sfDB']
sfSchema = config['Snowflakes']['sfSchema']
sfWarehouse = config['Snowflakes']['sfWarehouse']



conn = snowflake.connector.connect(user = sfUser,
                                    password = sfPass,
                                    account = sfAccount,
                                    warehouse = sfWarehouse,
                                    database = sfDB,
                                    schema = sfSchema
                                    )
session = Session.builder.configs(connection_parameters).create() 

dbs = session.sql('show databases ;').collect()
st.write(dbs)


