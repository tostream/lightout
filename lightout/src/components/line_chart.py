import i18n
import pandas
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from pandas import DataFrame

import fastf1

from ..data.data_sqlite import load_lap_data
from ..data.loader import DataSchema
from ..data.source import DataSource
from . import ids

testing_data=['1:30.006','1:30.002','1:30.008','1:30.003','1:30.004','1:30.001','1:30.005',
'1:30.007','1:30.009']

def render(app: Dash) -> html.Div:
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
        drivers: str,
    ) -> html.Div:
        if drivers is None: return html.Div(id=ids.LINE_CHART)
        data_set_DF = load_lap_data(int(years), gp, session, drivers)
        fig = px.line(
            data_set_DF,
            x='LapNumber',
            y='LapTime',
            color='Driver',
            
        )
        return html.Div(
            dcc.Graph(figure=fig),
            id=ids.LINE_CHART,
            className="bg-dark text-light mb-3")
    return html.Div(id=ids.LINE_CHART)
