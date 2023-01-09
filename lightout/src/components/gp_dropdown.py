import i18n
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data import grand_prix
from ..data.data_sqlite import load_gp_data
from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.Grand_Prix, "options"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
        ],
    )
    def select_gp(years: str):
        if years is None: return ['']
        result = load_gp_data(years)
        return result

    return html.Div(
        children=[
            #html.H6(i18n.t("general.driver")),
            html.H6("Grand Prix"),
            dcc.Dropdown(
                id=ids.Grand_Prix,
                multi=False,
                placeholder="Match",
            ),
        ]
    )