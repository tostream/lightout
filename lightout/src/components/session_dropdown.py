import i18n
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options


def render(app: Dash) -> html.Div:
    """@app.callback(
        Output(ids.Drivers, "value"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
        ],
    )
    def select_driver(years: list[str], months: list[str], _: int) -> list[str]:
        return source.filter(years=years, months=months).unique_categories
    """
    all_sessions = ["Race","Qualifying","FP1","FP2","FP3"]
    return html.Div(
        children=[
            #html.H6(i18n.t("general.driver")),
            html.H6("Session"),
            dcc.Dropdown(
                id=ids.Sessions,
                options=to_dropdown_options(all_sessions),
                placeholder="Session",
                multi=False,
            ),
        ]
    )