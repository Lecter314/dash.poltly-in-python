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
        "Select a category (x_axis)",
        dcc.Dropdown(df_c.columns, df_c.columns[0],
                    placeholder="Category selection", id="category"),
        "Select a quantitative argument (y_axis)",
        dcc.Dropdown(df_d.columns[1:4], df_d.columns[0],
                    placeholder="Quantitative Argument selection", id="bary"),
        "Select clustered criteria (group)",
        dcc.Dropdown(df_c.columns, df_c.columns[0],
                    placeholder="Cluster selection", id="c"),
        dcc.Graph(id="clustered_bar_chart", figure=default_fig),
        
    ]
)


# clustered bar charts printing
@callback(
    Output('clustered_bar_chart', 'figure'),
    Input('category', 'value'),
    Input('bary', 'value'),
    Input('c', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)



def update_clusterbar_chart(category, bary, cluster, toggle):
    template = template_theme1 if toggle else template_theme2
    fig = px.histogram(
        data_frame=df,
        x=category,
        y=bary,
        color=cluster,
        barmode='group',
        histfunc='avg',
        template=template,
        )
    return fig

