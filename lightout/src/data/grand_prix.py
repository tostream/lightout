import datetime as dt
from functools import partial, reduce
from typing import Callable

import babel.dates
import i18n
import pandas as pd
from pandas import Timedelta

import fastf1


class DataSchema:
    RoundNumber = "RoundNumber"
    Country = "Country"
    OfficialEventName = "EventName"



Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]

def create_round_num(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.RoundNumber] = df[DataSchema.RoundNumber]
    return df


def create_country(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.Country] = df[DataSchema.Country]
    return df


def create_event_name(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.OfficialEventName] = df[DataSchema.OfficialEventName]
    return df


def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)
    

def load_gp_data(year: str, locale: str='en') -> pd.DataFrame:
    # load the data from the CSV file
    schedule = fastf1.get_event_schedule(int(year))
    
    fastf1.Cache.enable_cache("C:\\source\\lightout\\lightout\\cache\\in")  
    preprocessor = compose(
        create_round_num,
        create_country,
        create_event_name,
    )
    #preprocessor(lap).to_csv("C:\\source\\lightout\\lightout\\cache\\in\\laps\\temp_laps.csv", encoding='utf-8')
    return preprocessor(schedule)

    
all_grand_prix = ["Abu Dhabi Grand Prix","Sao Paulo Grand Prix",
    "Mexico City Grand Prix","United States Grand Prix"]
test_grand_prix = ["Abu Dhabi Grand Prix","Sao Paulo Grand Prix",
    "Mexico City Grand Prix","United States"]