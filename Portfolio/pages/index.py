import reflex as rx
from Portfolio.views.header import header


@rx.page(route="/", title="My portfolio")
def index() -> rx.Component:
    return rx.center(
        header(),
        background_color="black",
        height="100vh",
    )