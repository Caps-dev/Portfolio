import reflex as rx
import datetime
from Portfolio.styles.styles import Spacer
from Portfolio.components.constants import GITHUB_URL, LINKEDIN_URL


def footer() -> rx.component:
    return rx.hstack(rx.text(f"Portafolio {datetime.date.today().year}"), rx.image(src="icon/location.svg", width="20px", height="20px"), rx.text("San Jose, Costa Rica"), rx.spacer(), rx.link(rx.image(src="icon/linkedin.svg", width="30px", height="30px"), href=LINKEDIN_URL, is_external=True), rx.link(rx.image(src="icon/github.svg", width="30px", height="30px", margin_left=Spacer.SMALL.value), href=GITHUB_URL, is_external=True), padding=Spacer.DEFAULT.value)
