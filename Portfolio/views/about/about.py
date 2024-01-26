import reflex as rx
from Portfolio.styles.styles import Spacer
from Portfolio.styles.colors import color
from Portfolio.views.experiencia.experiencia import experiencia


def about_part():
    return rx.box(
        rx.center(rx.vstack(rx.heading("Sobre mi"),
                            rx.box(
            rx.vstack(
                rx.text("Desde que obtuve mi título como Técnico Medio en Informática en Redes en el Colegio, mi pasión por la tecnología ha sido innegable. Mi formación incluyó una práctica profesional en la empresa Centenario Internacional, donde pude aplicar mis conocimientos en un entorno real y adquirir una valiosa perspectiva sobre el mundo laboral."),
                rx.text("Mi recorrido académico continuó al ingresar a la Universidad de Costa Rica en 2023 para estudiar Ingeniería de Software, un emocionante paso que amplió mis horizontes educativos. Simultáneamente, di inicio a mi carrera profesional en el campo tecnológico, lo que ha enriquecido mi comprensión práctica y teórica."),
                rx.text("Además, incursioné en el análisis de datos a través de la plataforma Platzi, explorando cómo estos datos pueden proporcionar ideas valiosas. Cada proyecto en mi portafolio refleja mi dedicación por fusionar la teoría académica con la aplicación práctica, buscando soluciones creativas y eficientes para los desafíos tecnológicos del mundo real."),
                rx.text("Empecé a trabajar en el campo laboral en el transcurso de este último año, ampliando mi experiencia y habilidades más allá del ámbito académico. Cada día, mi entusiasmo crece por las oportunidades que se presentan y las colaboraciones futuras que podré formar. Espero que encuentres inspiración en mi trabajo y que podamos compartir un emocionante viaje hacia el futuro tecnológico juntos."),
                spacing=Spacer.MEDIUM.value), max_width="600px"),
            spacing=Spacer.BIG.value)),

    )


def about() -> rx.component:
    return rx.vstack(rx.mobile_only(about_part(), padding_inline=Spacer.BIG.value, margin_block=Spacer.BIG.value,
                                    background_color=color.secondary.value,
                                    width="100%",
                                    padding_block=Spacer.BIG.value), rx.tablet_and_desktop(about_part(), padding_inline=Spacer.DOUBLEBIG.value, margin_block=Spacer.BIG.value,
                                                                                           background_color=color.secondary.value,
                                                                                           width="100%",
                                                                                           padding_block=Spacer.BIG.value),
                     experiencia(),
                     rx.center(
        rx.responsive_grid(
            rx.box(rx.vstack(
                rx.image(src="data.png", width="150px"),
                rx.heading("Analista de datos"),
                rx.text("""| Excel | Power bi | Tableu | Python | SQL |"""))),
            rx.box(rx.vstack(
                rx.image(src="wifi.png", width="150px"),
                rx.heading("Redes"),
                rx.text("""| CCNA | LINUX | HCIA |"""))),
            rx.box(rx.vstack(
                rx.image(src="ing.png", width="80px"),
                rx.heading("Programacion"),
                rx.text("""| Python | Java | C++ | HTML | CSS |""")), spacing=Spacer.DOUBLEBIG.value), columns=[1, 2, 3], margin_block=Spacer.DOUBLEBIG.value, spacing_y=Spacer.BIG.value)
    ), id="about")
