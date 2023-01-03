import dash_bootstrap_components as dbc  # BOOTSTRAP
import flask
import i18n
from dash import Dash
from src.components.layout import create_layout
from src.data.f1_data import load_lap_data
from src.data.loader import load_transaction_data
from src.data.source import DataSource

LOCALE = "en"
DATA_PATH = "./data/transactions.csv"

"""
def main() -> None:

    # set the locale and load the translations
    i18n.set("locale", LOCALE)
    i18n.load_path.append("locale")
    server = flask.Flask(__name__)

    # load the data and create the data manager
    data = load_transaction_data(DATA_PATH, LOCALE)
    data = DataSource(data)

    app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP],server=server,)
    app.title = i18n.t("general.app_title")
    app.layout = create_layout(app, data)
    app.run(host="0.0.0.0", port=8080, debug=True)
"""

data = load_transaction_data(DATA_PATH, LOCALE)
data = DataSource(data)

dash_app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP],)
i18n.set("locale", LOCALE)
i18n.load_path.append("locale")
#server = flask.Flask(__name__)

# load the data and create the data manager
dash_app.title = i18n.t("general.app_title")
dash_app.layout = create_layout(dash_app)
app = dash_app.server
if __name__ == "__main__":
    #main()
    
    dash_app.run_server()