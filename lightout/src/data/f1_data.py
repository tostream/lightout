import datetime as dt
from functools import partial, reduce
from typing import Callable, Collection

import babel.dates
import i18n
import pandas as pd
import pymongo
from pandas import Timedelta
from pymongo import MongoClient

import fastf1


class DataSchema:
    DriverNumber = "DriverNumber"
    LapTime = "LapTime"
    LapNumber = "LapNumber"




def create_driver_column(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.DriverNumber] = df[DataSchema.DriverNumber]
    return df


def create_lapnum_column(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.LapNumber] = df[DataSchema.LapNumber]
    return df


Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]

def format_laptime(df: pd.DataFrame) -> pd.DataFrame:
    def format(laptime: Timedelta) -> float:
        return laptime.total_seconds()

    df[DataSchema.LapTime] = df[DataSchema.LapTime].apply(format)
    return df

def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

def get_f1_session(year: int,gp: str, session:str):
    f1_session = fastf1.get_session(int(year), gp, session)
    
    fastf1.Cache.enable_cache("C:\\source\\lightout\\lightout\\cache\\in")  
    f1_session.load()
    return f1_session

def getMongoClient(url:str = "mongodb://localhost:27017/",instance:str ="admin", dbName:str = ""):
    client = MongoClient(url)
    db = client[instance]
    company= db[dbName]
    return company

def load_lap_data(year: int,gp: str, session:str,driver: str, locale: str='en') -> pd.DataFrame:
    # load the data from the CSV file
    company= getMongoClient(instance ="f1_database", dbName = "matches")
    # database
    data_from_db = company.find_one({'driverNum':'44'})
    return pd.DataFrame(data_from_db["laps"])

def load_gp_data(year: str):
    company= getMongoClient(instance ="f1_database", dbName = "matches")
    data_from_db = company.find_one({'index':'GP','years':year})
    print(type(data_from_db["GP"]))
    print(type(data_from_db))
    return (data_from_db["GP"])


def load_driver_data(year: int,gp: str,session:str, locale: str='en') -> pd.DataFrame:
    client= getMongoClient()
    # load the data from the CSV file
    #schedule = fastf1.get_event_schedule(int(year))
    #sessins = fastf1.get_session(2021, gp, session)
    
    
    #fastf1.Cache.enable_cache("C:\\source\\lightout\\lightout\\cache\\in")  
    #sessins.load()
    f1_session = get_f1_session(year ,gp ,session)
    drivers=f1_session.results['Abbreviation']
    #preprocessor = compose(
    #    create_round_num,
    #    create_country,
    #    create_event_name,
    #)
    #preprocessor(lap).to_csv("C:\\source\\lightout\\lightout\\cache\\in\\laps\\temp_laps.csv", encoding='utf-8')
    return drivers