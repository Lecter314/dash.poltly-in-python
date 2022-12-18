import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
from dash_bootstrap_templates import ThemeSwitchAIO
from dash import dash_table as tbl
from pages.default_fig import default_fig
from views.data import CARSA, df, df_c, df_d


# themes
template_theme2 = "flatly"
template_theme1 = "darkly"

dash.register_page(__name__)


# create an interativetable table
layout = html.Div([
    html.H4("Selected Table"),
    html.H5("Demand of Rental Bikes"),
    "Total rental bikes range from: ",
    dcc.Input(id='x1', value=str(CARSA['cnt'].min()),
              type='number'),
    "To: ",
    dcc.Input(id='x2', value=str(CARSA['cnt'].max()),
              type='number'),
    html.H5("The Factors of Demand"),
    tbl.DataTable(CARSA.to_dict('records'),
                  [{"name": i, "id": i} for i in CARSA.columns],
                  style_cell={'padding': '5px', # with some style control
                              'textAlign': 'center'},
                  style_data_conditional=[
                                        {'if': {'row_index': 'odd'},
                                        'backgroundColor': 'rgb(220, 220, 220)',
                                        }
                                    ],
                  style_header={
        'backgroundColor': 'rgb(30, 30, 30)',
        'color': 'white'
    },
    id='df'),], className="table-1")


# the same as others
@callback(
    Output('df', 'data'),
    Input('x1', 'value'),
    Input('x2', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)


# table updating
def update_table(x1, x2, toggle):
    template = template_theme1 if toggle else template_theme2
    sel = (CARSA['cnt'] >= float(x1)) & (CARSA['cnt'] <= float(x2))
    table = CARSA[sel].to_dict('records')
    return table
