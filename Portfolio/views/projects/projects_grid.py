import reflex as rx
from Portfolio.components.projects import project
from Portfolio.styles.colors import color
from Portfolio.styles.styles import HOVER_STYLE
from Portfolio.components import constants as const


def projects_important_grid() -> rx.component:
    return rx.vstack(rx.heading("Proyectos descatados"), rx.responsive_grid(
        rx.box(project(const.CONNECT_4)), rx.box(
            project(const.SPOTIFY_TOP_100)),

        columns=[1, 2, 4],
        spacing="4",
    ), rx.link(rx.button("Ver más", background=color.forthy.value), href="https://github.com/Caps-dev?tab=repositories", is_external=True), background_color=color.secondary.value, padding="20px", id="proyectos")
