from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px
import numpy as np
from dash_bootstrap_templates import ThemeSwitchAIO
from pages.default_fig import default_fig
from views.data import CARSA, df, df_c, df_d


# themes
template_theme2 = "flatly"
template_theme1 = "darkly"

register_page(__name__)


# selecting variables for histograms
layout = html.Div(
    [
        dcc.Graph(id="histograms-graph", figure=default_fig),
        "Select an argument (x_axis)",
        dcc.Dropdown(df_d.columns[:7], df_d.columns[0],
                 placeholder="Argument selection for Histogram", id='hist'),
    ]
)


# hist-graph printing
@callback(
    Output('histograms-graph', 'figure'),
    Input('hist', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    )
def update_figure(hist, toggle):
    template = template_theme1 if toggle else template_theme2
    nb = int(1 + 1.44 * np.log(CARSA.shape[0]))  # structures
    try: # for robostness of the web
        fig = px.histogram(CARSA,
                        x=hist,
                        title="Histogram",
                        histnorm='density',
                        nbins=nb,
                        template=template)
    except ValueError:
        fig = default_fig
    return fig
