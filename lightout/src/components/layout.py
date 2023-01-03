import dash_bootstrap_components as dbc
from dash import Dash, html
from src.components import (drivers_dropdown, gp_dropdown, line_chart,
                            session_dropdown, year_dropdown)

from ..data.source import DataSource


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title,className="text-center"),
            html.Hr(),
            dbc.Container(
                dbc.Row(
                    className="dropdown-container g-4 lg-3 md-6",
                    children=[
                        year_dropdown.render(app),
                        gp_dropdown.render(app),
                        session_dropdown.render(app),
                        drivers_dropdown.render(app),
                    ],
                ),
            ),
            html.Hr(),
            line_chart.render(app),
        ],
    )
