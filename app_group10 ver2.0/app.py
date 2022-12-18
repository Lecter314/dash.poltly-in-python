# -*- coding: utf-8 -*-
# Run this app with 'app.py' and
# visit http://127.0.0.1:8050/ in your web browser.

"""
Topic: The Demand of Rental Bikes During year 2012 in Capital Bikeshare System

@author: Group 10: Bai Xinyi & Yu Tianxiong
"""

from dash import Dash, page_registry, page_container
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

# select the Bootstrap stylesheets and figure templates for the theme toggle here:
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY
theme_toggle = ThemeSwitchAIO(
    aio_id="theme",
    themes=[url_theme2, url_theme1],
    icons={"left": "fa fa-sun", "right": "fa fa-moon"},
)

# This stylesheet defines the "dbc" class.  Use it to style dash-core-components
# and the dash DataTable with the bootstrap theme.
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, use_pages=True, external_stylesheets=[url_theme2, dbc_css])


# the overall setting
navbar = dbc.NavbarSimple(
    [   dbc.Button("Home", href="/", color="secondary", className="me-1"), # add home button
        dbc.Button("Dashboard", href="/dashboard", color="secondary", className="me-1"), # add dashboard
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(page["name"], href=page["path"])
                for page in page_registry.values()
                if not (page["module"] == "pages.not_found_404" or page["module"] == "pages.home" or page["module"] == "pages.dashboard") # exclude two pages other than graphing
            ],
            nav=True,
            label="Analytical Graphs",
        ),
    ],
    brand="The Demand of Rental Bikes During year 2012 in Capital Bikeshare System",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [navbar, theme_toggle, page_container], fluid=True, className="dbc"
)


if __name__ == "__main__":
    app.run_server(debug=True)

