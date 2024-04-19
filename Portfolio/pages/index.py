import reflex as rx

@rx.page(route="/", title="My portfolio")
def index() -> rx.Component:
    return rx.center(
        rx.heading("Welcome to my portfolio!"),
    )
