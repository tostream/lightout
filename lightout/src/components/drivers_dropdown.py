import i18n
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.data_sqlite import load_driver_data
from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options

all_drivers = ["VER","HAM","PER","RUS"]

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.Drivers, "options"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.Grand_Prix, "value"),
            Input(ids.Sessions, "value"),
        ],
    )
    def select_driver(years: str, gp: str, session: str) :
        if years is not None and gp is not  None and session is not None:
            result = load_driver_data(int(years),gp,session)
            return result
            #return ["VER","HAM","PER","RUS"]
        else:
            return ''
    return html.Div(
        children=[
            #html.H6(i18n.t("general.driver")),
            html.H6("Driver"),
            dcc.Dropdown(
                id=ids.Drivers,
                placeholder="Drivers",
                multi=True,
            ),
        ]
    )