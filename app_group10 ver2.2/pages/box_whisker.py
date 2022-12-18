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


# selecting variables for box-whisker diadram
layout = html.Div(
    [    
        "Select a category (x_axis)",
        dcc.Dropdown(df_c.columns, df_c.columns[0],
                 placeholder="Category selection", id='boxx'),
        "Select a quantitative argument (y_axis)",
        dcc.Dropdown(df_d.columns[:4], df_d.columns[0],
                 placeholder="Category selection", id='boxy'),
        dcc.Graph(id="box_whisker", figure=default_fig),
    ]
)


# box-whisker diadram printing
@callback(
    Output('box_whisker', 'figure'),
    Input('boxx', 'value'),
    Input('boxy', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_box_whisker(boxx, boxy, toggle):
    template = template_theme1 if toggle else template_theme2
    try: # for robostness of the web
        fig = px.box(
            CARSA, 
            x=boxx, 
            y=boxy,
            color=boxx,
            title="Box whisker chart",
            notched=True,
            template=template,
            )
    except ValueError:
        fig = default_fig
    return fig

