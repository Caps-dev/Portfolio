import reflex as rx
from Portfolio.styles.styles import Spacer
from Portfolio.styles.colors import color
from Portfolio.components.constants import LINKEDIN_URL


def contact() -> rx.component:
    return rx.center(rx.vstack(rx.heading("Contacto"), rx.box(rx.center(rx.hstack(rx.vstack(rx.text("Email", margin_bottom="14px"), rx.text("campisa26@gmail.com")), rx.vstack(rx.text("LinkedIn"), rx.link(rx.image(src="icon/linkedin.svg", width="40px"), href=LINKEDIN_URL)), spacing=Spacer.DOUBLEBIG.value))), max_width="600px", width="100%",), margin=Spacer.BIG.value, background_color=color.secondary.value, width="100%", padding=Spacer.MEDIUM.value)
