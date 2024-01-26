import reflex as rx
from Portfolio.styles.colors import color, text_color


def navbar() -> rx.component:
    return rx.hstack(rx.image(src="logo.png", width="50px", height="auto"), rx.spacer(), rx.link("Inicio", margin_inline_end="2px", href=""), rx.link("Proyectos", margin_inline_end="2px", href="#proyectos"), rx.link("Sobre mi", margin_inline_end="2px", href="#about"), position="sticky", text_align="right", background=color.navbar.value, width="100%", z_index="999", top="0", padding_inline="1em", padding_block=".5em")
