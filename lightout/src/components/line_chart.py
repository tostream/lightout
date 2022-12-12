import i18n
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from ..data.source import DataSource
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.LINE_CHART, "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CATEGORY_DROPDOWN, "value"),
        ],
    )
    def update_line_chart(
        years: list[str], months: list[str], categories: list[str]
    ) -> html.Div:
        filtered_source = source.filter(years, months, categories)
        if not filtered_source.row_count:
            return html.Div(i18n.t("general.no_data"), id=ids.LINE_CHART)
        df = filtered_source._data
        fig = px.line(
            df,
            x=df.date,
            y=df.amount,
            color="year",
            labels={
                "amount": i18n.t("general.amount"),
                "year": i18n.t("general.year"),
            },
        )
        return html.Div(dcc.Graph(figure=fig), id=ids.LINE_CHART)

    return html.Div(id=ids.LINE_CHART)
