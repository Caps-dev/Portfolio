from enum import Enum
import reflex as rx
from Portfolio.styles.colors import color as color


MAX_WIDTH = "80%"


class Spacer(Enum):
    VERY_SMALL = "0.2em"
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    DOUBLEBIG = "4em"


BASE_STYLE = {
    "background_color": color.Background.value,
    "color": color.tercery.value,
    rx.Link: {
        "text_decoration": "none",
        "_hover": {},
        "color": color.tercery.value
    },
    rx.Text: {
        "color": color.tercery.value
    }
}

HOVER_STYLE = {
    "_hover": {"background_color": color.forthy.value},
}
