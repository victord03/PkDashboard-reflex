import reflex as rx

icon_path = '/pokeball_icon.png'
# 595 x 842

def pokeball_icon() -> rx.Component:
    return rx.link(
        rx.image(
            src=icon_path,  # Icon path
            width="40px",
            height="57px",
            cursor="pointer",  # Show it's clickable
            object_fit="contain",
        ),
        href="/",  # Navigation target
        align_self="flex-start"
    )