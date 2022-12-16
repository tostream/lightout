import i18n
import pandas
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from pandas import DataFrame

import fastf1

from ..data.f1_data import load_lap_data
from ..data.loader import DataSchema
from ..data.source import DataSource
from . import ids

testing_data=['1:30.006','1:30.002','1:30.008','1:30.003','1:30.004','1:30.001','1:30.005',
'1:30.007','1:30.009']

def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.LINE_CHART, "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.Grand_Prix, "value"),
            Input(ids.Sessions, "value"),
            Input(ids.Drivers, "value"),
        ],
    )
    def update_line_chart(
        years: int,
        gp: str,
        session: str,
        drivers: list[str]
    ) -> html.Div:
        print(drivers)
        if drivers is None or len(drivers)<1: return html.Div(id=ids.LINE_CHART)
        #filtered_source = source.filter(years, months, categories)
        #if not filtered_source.row_count:
        #    return html.Div(i18n.t("general.no_data"), id=ids.LINE_CHART)
        #df = filtered_source._data
        #data_set: DataFrame= dataset()
        #data_set=source
        #data_set.to_csv("C:\\source\\lightout\\lightout\\cache\\in\\laps\\temp_max_laps.csv", encoding='utf-8')
        #print(data_set)
        data_set = load_lap_data(years, gp, session, drivers[0])
        fig = px.line(
            data_set,
            x=data_set.LapNumber,
            y=data_set.LapTime,
            labels={
                "LapTime": "Lap Time",
                "LapNumber": "Lap Number",
            },
            
        )
        return html.Div(
            dcc.Graph(figure=fig),
            id=ids.LINE_CHART,
            className="bg-dark text-light mb-3")
    return html.Div(id=ids.LINE_CHART)

    """
def dataset():
    session = fastf1.get_session(2021, 'French Grand Prix', 'r')
    
    fastf1.Cache.enable_cache("C:\\source\\lightout\\lightout\\cache\\in")  
    session.load()
    laps=session.laps
    laps.to_csv("C:\\source\\lightout\\lightout\\cache\\in\\laps\\temp_laps.csv", encoding='utf-8')
    lap= laps.pick_driver(33)
    lap.to_csv("C:\\source\\lightout\\lightout\\cache\\in\\laps\\temp_max_laps.csv", encoding='utf-8')
    import pandas 
    laptime_type = {"LapTime":'datetime'}
    lap: DataFrame = pandas.read_csv(
        "C:\\source\\lightout\\lightout\\cache\\in\\laps\\temp_max_laps_2.csv",
        parse_dates=['LapTime'],
        date_parser = lambda s : pandas.to_timedelta(s).total_seconds(),
        )
    return lap
    """