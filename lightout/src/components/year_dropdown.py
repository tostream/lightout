import i18n
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data import grand_prix
from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options

years = ['2020','2021','2022']

def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.H6(i18n.t("general.year")),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=to_dropdown_options(years),
                multi=False,
                placeholder="Season",
            ),
        ]
    )
