import datetime as dt
from functools import partial, reduce
from typing import Callable, Collection

import babel.dates
import i18n
import pandas as pd
from pandas import Timedelta
from pymongo import MongoClient


def getMongoClient(url:str = "mongodb://localhost:27017/",instance:str ="admin", dbName:str = ""):
    client = MongoClient(url)
    db = client[instance]
    company= db[dbName]
    return company

def load_lap_data(year: int,gp: str, session:str,driver: str, locale: str='en') -> pd.DataFrame:
    # load the data from the CSV file
    company= getMongoClient(instance ="f1_database", dbName = "matches")
    
    result=pd.DataFrame(columns=['Driver','LapNumber','LapTime'])
    for i in driver:
        data_from_db = company.find_one({'index':'LapTimes',
        'DriverNumber':i,
        'years':year,
        'GP':gp})
        result= pd.concat([result, pd.DataFrame(data_from_db[session])])
    
    return result

def load_gp_data(year: str):
    company= getMongoClient(instance ="f1_database", dbName = "matches")
    data_from_db = company.find_one({'index':'GP','years':year})
    return (data_from_db["GP"])


def load_driver_data(year: int,gp: str,session:str, locale: str='en'):
    client= getMongoClient(instance ="f1_database", dbName = "matches")
    data_from_db = client.find_one({'index':'Drivers','years':year,'GP':gp})
    result = [{'label':i['Abbreviation'],'value':i['DriverNumber']} for i in data_from_db['driver']]
    return result