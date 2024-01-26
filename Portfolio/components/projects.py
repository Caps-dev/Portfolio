import reflex as rx
from Portfolio.styles.styles import Spacer
from Portfolio.styles.colors import color


def project(data: dict) -> rx.component:
    if data["area"] == "Programacion":
        margin = "50px"
    elif data["area"] == "Networking":
        margin = "40px"
    else:
        margin = "60px"

    def imagen(img):
        if (img == ""):
            return ""
        else:
            return rx.box(rx.image(src=img, height="30px"))

    return rx.link(rx.box(rx.center(rx.image(src=data["imagen"], height="180px")), rx.box(rx.vstack(rx.heading(data["titulo"]), rx.text(data["descripcion"], margin_left=Spacer.SMALL.value),  rx.flex(rx.spacer(), rx.text(data["area"], background=color.tercery.value, color="#000000 !important", margin_left=margin, padding=Spacer.SMALL.value, margin=Spacer.SMALL.value, border_radius=Spacer.SMALL.value), width="100%"), rx.responsive_grid(
        imagen(data["img1"]), imagen(data["img2"]), imagen(data["img2"]), imagen(data["img2"]), spacing_y=Spacer.VERY_SMALL.value, columns=[4], spacing="2", padding=Spacer.SMALL.value)), background=color.secondary.value, width="100%", margin_bottom=Spacer.SMALL.value)), href=data["url"], is_external=True, margin=Spacer.SMALL.value)
