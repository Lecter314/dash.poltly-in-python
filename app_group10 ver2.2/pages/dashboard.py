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
    
    "Select numeric fields (limit of 2)",
    dcc.Dropdown(df_d.columns[:4], df_d.columns[0],
            placeholder="Select numeric fields", id="numeric", multi=True),
    "Select one qualitative",
    dcc.Dropdown(df_c.columns, df_c.columns[0],
            placeholder="Category selection", id="category"),
    "Total rental bikes range from: ",
    dcc.Input(id='x1', value=str(CARSA['cnt'].min()),
              type='number'),
    "To: ",
    dcc.Input(id='x2', value=str(CARSA['cnt'].max()),
              type='number'),
    
    html.H5("The Factors of Demand"),
    
    tbl.DataTable(data=CARSA.to_dict('records'), # how table is initially disigned
                  columns=[{"name": i, "id": i, "deletable": True, "selectable": True} for i in CARSA.columns],
                  editable=True,
                  filter_action="native",
                  sort_action="native",
                  sort_mode="multi",
                  column_selectable="single",
                  row_selectable="multi",
                  row_deletable=True,
                  selected_columns=[],
                  selected_rows=[],
                  page_action="native",
                  page_current= 0,
                  page_size= 10,
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


# options for the dropdown for a limit of 2 numeric inputs
OPTIONS = [
    {"value": df_d.columns[0], "label": df_d.columns[0]},
    {"value": df_d.columns[1], "label": df_d.columns[1]},
    {"value": df_d.columns[2], "label": df_d.columns[2]},
    {"value": df_d.columns[3], "label": df_d.columns[3]},
    #...
]
# a callback that sets the options of the dropdown to the choices that are currently selected if the limit is reached
@callback(
    Output(component_id="numeric", component_property="options"),
    [
        Input(component_id="numeric", component_property="value"),
    ],
)
def update_dropdown_options(values):
    if len(values) == 2:
        return [option for option in OPTIONS if option["value"] in values]
    else:
        return OPTIONS


# for category and numeric rolldown updates, we update the column in the original table
@callback(
    Output('df', 'columns'),
    Input('df', 'columns'),
    Input('category', 'value'),
    Input('numeric', 'value'),
)
def update_columns(columns, category, numeric):
    # print(category, numeric)
    numeric_label = [numeric] if type(numeric) == str else numeric # whether is sth like 'hum' or ['hum'] or ['atemp', 'windspeed'] bsed on user selections
    try: # avoid invalid inputs
        columns = CARSA[[category, "cnt"] + numeric_label].columns if category != "None" and numeric != [] else CARSA.columns # for null input
    except KeyError:
        columns = CARSA.columns
    return [{"name": i, "id": i, "deletable": True, "selectable": True} for i in columns] # update the column


# update the averall table based on row selection
@callback(
    Output('df', 'data'),
    Input('category', 'value'),
    Input('x1', 'value'),
    Input('x2', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
# table updating
def update_table(category, x1, x2, toggle):
    template = template_theme1 if toggle else template_theme2
    try:
        sel = (CARSA['cnt'] >= float(x1)) & (CARSA['cnt'] <= float(x2))
    except TypeError:
        sel = []
    table = CARSA[sel].to_dict('records')
    return table
