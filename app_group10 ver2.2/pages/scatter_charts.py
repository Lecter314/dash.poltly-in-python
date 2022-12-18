import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
from dash_bootstrap_templates import ThemeSwitchAIO
from pages.default_fig import default_fig
from views.data import CARSA, df, df_c, df_d


# themes
template_theme2 = "flatly"
template_theme1 = "darkly"


dash.register_page(__name__)

# selecting variables for bar chart
layout = html.Div(
    [    
        "Select an argument (x_axis)",
        dcc.Dropdown(df_d.columns, df_d.columns[0],
                     placeholder="Argument selection", id='x'),
        "Select another (y_axis)",
        dcc.Dropdown(df_d.columns, df_d.columns[0],
                     placeholder="Function selection", id='y'),
        "Select a category",
        dcc.Dropdown(df_c.columns, df_c.columns[0],
                     placeholder="Category selection", id='c'),
        dcc.Graph(id="scatter_chart", figure=default_fig),
    ]
)


# scatter charts printing
@callback(
    Output('scatter_chart', 'figure'),
    Input('x', 'value'),
    Input('y', 'value'),
    Input('c', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    )
def update_figure(x_name, y_name, c_name, toggle):
    template = template_theme1 if toggle else template_theme2
    try: # for robostness of the web
        fig = px.scatter(
            CARSA, 
            x=x_name, 
            y=y_name, 
            color=c_name,
            title="Scatter chart",
            log_x=False,
            template=template,
            )
    except ValueError:
        fig = default_fig
    return fig

