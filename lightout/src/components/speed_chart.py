import i18n
import pandas
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from pandas import DataFrame

import fastf1

from ..data.data_sqlite import load_telemetry
from ..data.loader import DataSchema
from ..data.source import DataSource
from . import ids

def render(app: Dash) -> html.Div:

    @app.callback(
        Output('tele', "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.Grand_Prix, "value"),
            Input(ids.Sessions, "value"),
            Input(ids.Drivers, "value"),
            Input(component_id='tempchart', component_property='clickData'),
        ],
    )
    def update_speed_chart(
        years: int,
        gp: str,
        session: str,
        drivers: str,
        lapnumber,
    ) -> html.Div:
        if lapnumber is None: return html.Div(children=[html.Div()])
        lap = lapnumber['points'][0]['x']
        data_set_DF = load_telemetry(int(years), gp, drivers,lap, session)
        data_set_DF=data_set_DF[data_set_DF['LapNumber']>1]
        return html.Div(children=[
            telemetry(data_set_DF),
            teleChart(configChartPara(data_set_DF,'Speed',ids.SPEED_CHART)),
            teleChart(configChartPara(data_set_DF,'RPM',ids.RPM_CHART)),
            teleChart(configChartPara(data_set_DF,'nGear', ids.GEAR_CHART)),
            teleChart(configChartPara(data_set_DF,'Throttle', ids.THROTTLE_CHART)),
            teleChart(configChartPara(data_set_DF,'Brake', ids.BARKE_CHART)),
            teleChart(configChartPara(data_set_DF,'DRS', ids.DRS_CHART)),
        ]
            )
    return html.Div(id = 'tele',children=[html.Div()],className="line-chart")

def teleChart(para:dict)-> html.Div:
    fig = px.line(
        para['df'],
        x='Distance',
        y=para['y'], 
        color='Driver',
    )
    fig.update_traces(mode="markers+lines")
    fig.update_layout(margin_b=0,margin_t=0,hovermode="x unified",paper_bgcolor="darkgray",plot_bgcolor="darkgray")
    #fig.update_yaxes(type='date',tickformat ="%M:%S.%2f",hoverformat="Lap Time: %M:%S.%3f")
    fig.update_xaxes(visible=False)
    return html.Div(
            dcc.Graph(figure=fig),
            id=para['id'],
            className="bg-dark text-light mb-3")

def configChartPara(df,y,elementId):
    return {
        'df':df,
        'y':y,
        'id':elementId,
    }

def speedchart(df) -> html.Div:
    fig = px.line(
        df,
        x='Distance',
        y='Speed', 
        color='Driver',
    )
    fig.update_traces(mode="markers+lines")
    fig.update_layout(hovermode="x unified",paper_bgcolor="darkgray",plot_bgcolor="darkgray")
    #fig.update_yaxes(type='date',tickformat ="%M:%S.%2f",hoverformat="Lap Time: %M:%S.%3f")
    fig.update_xaxes(visible=False)
    return html.Div(
            dcc.Graph(figure=fig),
            id=ids.SPEED_CHART,
            className="bg-dark text-light mb-3")

def RPMChart(df):
    fig = px.line(
        df,
        x='Distance',
        y='RPM', 
        color='Driver',
    )
    fig.update_traces(mode="markers+lines")
    fig.update_layout(hovermode="x unified",paper_bgcolor="darkgray",plot_bgcolor="darkgray")
    #fig.update_yaxes(type='date',tickformat ="%M:%S.%2f",hoverformat="Lap Time: %M:%S.%3f")
    fig.update_xaxes(visible=False)
    return html.Div(
            dcc.Graph(figure=fig),
            id=ids.RPM_CHART,
            className="bg-dark text-light mb-3")

def gearChart(df):
    fig = px.line(
        df,
        x='Distance',
        y='nGear', 
        color='Driver',
    )
    fig.update_traces(mode="markers+lines")
    fig.update_layout(hovermode="x unified",paper_bgcolor="darkgray",plot_bgcolor="darkgray")
    #fig.update_yaxes(type='date',tickformat ="%M:%S.%2f",hoverformat="Lap Time: %M:%S.%3f")
    fig.update_xaxes(visible=False)
    return html.Div(
            dcc.Graph(figure=fig),
            id=ids.GEAR_CHART,
            className="bg-dark text-light mb-3")

def throttlechart(df):
    fig = px.line(
        df,
        x='Distance',
        y='Throttle', 
        color='Driver',
    )
    fig.update_traces(mode="markers+lines")
    fig.update_layout(hovermode="x unified",paper_bgcolor="darkgray",plot_bgcolor="darkgray")
    #fig.update_yaxes(type='date',tickformat ="%M:%S.%2f",hoverformat="Lap Time: %M:%S.%3f")
    fig.update_xaxes(visible=False)
    return html.Div(
            dcc.Graph(figure=fig),
            id=ids.THROTTLE_CHART,
            className="bg-dark text-light mb-3")

def brakeChart(df):
    fig = px.line(
        df,
        x='Distance',
        y='Brake', 
        color='Driver',
    )
    fig.update_traces(mode="markers+lines")
    fig.update_layout(hovermode="x unified",paper_bgcolor="darkgray",plot_bgcolor="darkgray")
    #fig.update_yaxes(type='date',tickformat ="%M:%S.%2f",hoverformat="Lap Time: %M:%S.%3f")
    fig.update_xaxes(visible=False)
    return html.Div(
            dcc.Graph(figure=fig),
            id=ids.BARKE_CHART,
            className="bg-dark text-light mb-3")

def DRSChart(df):
    fig = px.line(
        df,
        x='Distance',
        y='DRS', 
        color='Driver',
    )
    fig.update_traces(mode="markers+lines")
    fig.update_layout(hovermode="x unified",paper_bgcolor="darkgray",plot_bgcolor="darkgray")
    #fig.update_yaxes(type='date',tickformat ="%M:%S.%2f",hoverformat="Lap Time: %M:%S.%3f")
    fig.update_xaxes(visible=False)
    return html.Div(
            dcc.Graph(figure=fig),
            id=ids.DRS_CHART,
            className="bg-dark text-light mb-3")

def telemetry(df):
    fig = px.scatter(
        df,
        x='X',
        y='Y', 
    )
    fig.update_traces(mode="markers+lines")
    fig.update_layout(paper_bgcolor="darkgray",plot_bgcolor="darkgray")
    fig.update_xaxes(showgrid=False,zeroline=False,showticklabels=False,visible=False)
    fig.update_yaxes(showgrid=False,zeroline=False,showticklabels=False,visible=False)
    return html.Div(
            dcc.Graph(figure=fig),
            id=ids.DRS_CHART,
            className="bg-dark text-light mb-3")
