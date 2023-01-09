
import pandas as pd
from sqlalchemy import create_engine


def getSqliteClient(url:str = "lightsout_tempo.db"):
    #client = sqlite3.connect(url)
    client = create_engine(f'sqlite:///{url}')
    return client

def load_lap_data(year: int,gp: str, session:str,driver: str, locale: str='en') -> pd.DataFrame:
    # load the data from the CSV file
    client= getSqliteClient()
    dirvers = ','.join(driver)
    command = f'select Driver,LapNumber,LapTime from Laps_Times where year={year} \
        and gp = "{gp}" and sessions="{session}" and drivernumber in ({dirvers}) '
    print(command)
    result = pd.read_sql(command,client)

    return result

def load_gp_data(year: str):
    client= getSqliteClient()
    command = f'select eventname from GP_INFO where year={year}'
    result = pd.read_sql(command,client)
    return (result.EventName.to_list())


def load_driver_data(year: int,gp: str,session:str = 'race', locale: str='en'):
    client= getSqliteClient()
    command = f'select Abbreviation,DriverNumber from Driver_INFO where year={year} and GP = "{gp}"'
    data_from_db = pd.read_sql(command,client)
    result = [{'label':i['Abbreviation'],'value':i['DriverNumber']} for i in data_from_db.to_dict('r')]
    return result


print(load_lap_data(2019,'Austrian Grand Prix','Race',['44']).to_dict('r'))
print(load_gp_data(2019))

