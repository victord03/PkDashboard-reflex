import reflex as rx


def search_box() -> rx.Component:
    return rx.input(
        placeholder="Pokemon Type (e.g. 'Fire', 'Psychic', etc)",

        # typography
        font_size="22px",

        # sizing
        width="900px",
        max_width="900px",
        height="60px",

        # padding & margin
        padding_x="20px",
        padding_y="12px",
        margin_top="16em",

        # border
        border_radius="8px",
        border="1px solid gray",
        # box_shadow = "0 4px 6px rgba(0,0,0,0.1)",

    )
