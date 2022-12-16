import datetime as dt
from functools import partial, reduce
from typing import Callable

import babel.dates
import i18n
import pandas as pd
from pandas import Timedelta

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
    print('cp5')
    print(year)
    print(gp)
    print(session)
    f1_session = fastf1.get_session(int(year), gp, session)
    print('cp6')
    
    fastf1.Cache.enable_cache("C:\\source\\lightout\\lightout\\cache\\in")  
    f1_session.load()
    return f1_session


def load_lap_data(year: int,gp: str, session:str,driver: str, locale: str='en') -> pd.DataFrame:
    # load the data from the CSV file
    f1_session = get_f1_session(year ,gp ,session)
    print('cp3')
    print(year)
    print(gp)
    print(driver)
    print('cp4')
    laps=f1_session.laps
    print('cp1')
    print(laps)
    print('cp2')
    lap= laps.pick_driver(driver)
    preprocessor = compose(
        create_driver_column,
        create_lapnum_column,
        format_laptime,
    )
    #preprocessor(lap).to_csv("C:\\source\\lightout\\lightout\\cache\\in\\laps\\temp_laps.csv", encoding='utf-8')
    return preprocessor(lap)



def load_driver_data(year: int,gp: str,session:str, locale: str='en') -> pd.DataFrame:
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