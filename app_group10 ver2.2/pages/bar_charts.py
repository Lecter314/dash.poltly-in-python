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
        dcc.Dropdown(df_d.columns[:4], df_d.columns[0],
                placeholder="Quantitative Argument selection", id="bary"),
        dcc.Graph(id="bar_chart", figure=default_fig),
    ]
)


# bar charts printing
@callback(
    Output('bar_chart', 'figure'),
    Input('category', 'value'),
    Input('bary', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
# get the mean instead of aggregate values
def update_bar_chart(category, bary, toggle):
    template = template_theme1 if toggle else template_theme2
    try: # for robostness of the web
        fig = px.bar(
            data_frame=df.groupby([category]).mean().reset_index(), 
            x=category, 
            y=bary,
            color=bary,
            title="Bar chart",
            labels={bary: "mean_" + str(bary)},
            template=template,
            )
    except TypeError:
        fig = default_fig
    # print(category, bary)
    return fig

