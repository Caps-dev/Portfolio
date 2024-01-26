import reflex as rx
from Portfolio.components.constants import DATA


def chart_radar() -> rx.Component:

    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="A",
            stroke="#92ffc4",
            fill="#92ffc4"
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(
            data_key="subject"),
        data=DATA, height=150, stroke="#4f4f4f"

    )
