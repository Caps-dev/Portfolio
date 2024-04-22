"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from Portfolio.styles.styles import BASE_STYLE

import reflex as rx
from Portfolio.pages.index import index




class State(rx.State):
    """The app state."""




app = rx.App(style=BASE_STYLE)

