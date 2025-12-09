import reflex as rx
from src.styles.search_bar_style import button_style


def search_box(on_change) -> rx.Component:
    return rx.input(
        placeholder="Attacking Pokémon Type (e.g. 'Fire', 'Psychic', etc)",

        style=button_style,

        # sizing
        width="900px",
        max_width="900px",
        height="60px",

        # event trigger
        on_change=on_change

    )


def submit_button(on_click) -> rx.Component:
    return rx.button(
        "Submit",
        style=button_style,
        on_click=on_click,
    )

def search_box_with_button(on_change, on_submit) -> rx.Component:
    return rx.hstack(
        search_box(on_change),
        submit_button(on_submit),

        align_items="center",

    )