import reflex as rx
from Portfolio.styles.styles import Size,Spacing
def header() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.vstack(
                rx.heading("Allan Picado",
                           font_family="system-ui",
                           color="#black",
                           text_shadow="-1px -1px 0 white, 1px -1px 0 white, -1px 1px 0 white, 1px 1px 0 white"),
                rx.text("Student Software Developer",
                        color="white"),
                rx.text("hi!, thanks for visiting my portfolio site, I'm a student software developer, I'm currently studying computer science at the University of Costa Rica, I'm passionate about software development and I'm always looking for new challenges to learn and grow as a developer. I have experience in web development, mobile development, and desktop development, I have worked with technologies like React, React Native, Flutter, Django, and Java",
                        color="white"),
                background="#303030",
                padding_inline=Size.MEDIUM.value,
                padding_block=Size.MEDIUM.value, 
                height="100%",          
                ),
            rx.image(src="https://picsum.photos/200",height="100%",width="auto"),
            spacing=Spacing.DEFAULT.value,
             width="60%",
             height="300px",
        ),
        width="100%"
    )   