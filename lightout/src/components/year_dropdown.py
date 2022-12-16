import i18n
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data import grand_prix
from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options


def render(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        children=[
            html.H6(i18n.t("general.year")),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=to_dropdown_options(source.unique_years),
                multi=False,
            ),
        ]
    )
