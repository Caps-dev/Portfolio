import reflex as rx
from Portfolio.styles.styles import Spacer
from Portfolio.styles.colors import color


def header() -> rx.component:
    return rx.center(rx.responsive_grid(rx.vstack(rx.heading("Allan Picado"), rx.text("Estudiante de Ingeniería Software"), rx.text("¡Hola! ¡Gracias por visitar mi portafolio! Soy estudiante de Ingeniería de Software en la Universidad de Costa Rica. Mi formación como Técnico Medio en Informática en Redes y cursos de analista de datos, junto con proyectos autodidactas, me impulsan a crear soluciones innovadoras."), rx.button(rx.image(
        src="icon/cv.svg", width="50px", height="50px", margin_top="20px"
    ), on_click=rx.download(url="/logo.png"), background_color="transparent", _hover={}), background_color=color.secondary.value, width="100%", padding_inline="30px", padding_block="70px"), rx.avatar(name="Allan Picado", size="full", src="yo.jpeg", width="100%"), max_width="890px", width="100%", spacing=Spacer.BIG.value, columns=[1, 1, 2]))


def header_about(img: str) -> rx.component:
    return rx.center(rx.hstack(rx.image(src=img), rx.vstack(rx.heading("¡Hola!"), rx.text("En un mundo donde la tecnología trasciende las barreras, me encuentro en constante búsqueda de conocimiento y exploración. Soy Allan Picado, y esta página es un vistazo a mi viaje en el reino de la informática. Desde mis cimientos como Técnico Medio en Informática en Redes hasta mi actual formación en Ingeniería de Software en la Universidad de Costa Rica, he descubierto mi pasión por crear soluciones tecnológicas impactantes. Te invito a descubrir más sobre mí y mi compromiso con el aprendizaje continuo y la innovación."))), background_color=color.secondary.value, width="100%", max_width="1000px")
