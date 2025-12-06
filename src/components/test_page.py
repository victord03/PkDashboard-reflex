import reflex as rx


def test_page() -> rx.Component:
    return rx.text(
        "Pokemon Type (e.g. 'Fire', 'Psychic', etc)",
        # typography
        font_size="24px",
        font_weight="bold",
        font_style="italic",
        # colors & backgrounds
        color="blue",
        background_color="#7499ee",
        # spacing
        padding="10px",
        # padding_x="1em",
        # padding_y="1em",
        margin="3em",
        # margin_x="auto",
        # sizing
        width="35em",
        height="4em",
        # max_width="900px",
        # min_height="7em",
        # visual effects
        border_radius="8px",
        border="1px solid white",
        box_shadow="0 4px 6px rgba(0,0,0,0.1)",
        # layout
        display="flex",
        justify="center",
        align="center",
        # hover interaction
        _hover={"background_color": "#e66465", "color": "white", "cursor": "pointer"},
    )
