"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from Portfolio.components.navbar import navbar
from Portfolio.components.footer import footer
from Portfolio.views.header.header import header, header_about
from Portfolio.views.contact.contact import contact
from Portfolio.styles import styles
from Portfolio.styles.colors import color
from Portfolio.views.charts.charts import chart_radar
from Portfolio.views.about.about import about
from Portfolio.views.projects.projects_grid import projects_important_grid

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


def index() -> rx.Component:
    return rx.box(navbar(),
                  rx.center(rx.vstack(header(), projects_important_grid(), about(), contact(), max_width=styles.MAX_WIDTH, width="100%",
                            margin_top=styles.Spacer.SMALL.value, margin_bottom=styles.Spacer.BIG.value)),
                  footer(),)


# Create app instance and add index page.
app = rx.App(style=styles.BASE_STYLE)
app.add_page(index)
