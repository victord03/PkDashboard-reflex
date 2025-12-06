import reflex as rx
from src.components.search_box import search_box
from src.components.experimentation_page import test_page


def index() -> rx.Component:
    return rx.container(

        rx.flex(

            # SEARCH BOX
            search_box(),

            # LINK
            rx.link(
                "Go to the test page",

                # url link
                href="/testPage",

                # typography
                color="white",

                # position
                align_self="flex-start",

                # hover interaction
                _hover={
                    "color": "blue",
                    "font_style":"underlined",
                    "cursor": "pointer",
                },
            ),

            # FLEX COMPONENT PARAMETERS
            flex_direction="column",
            justify_content="space-between",
            align_items="center",
            min_height="100vh",
        ),
        width="100%"
    )


app = rx.App()
app.add_page(index)


app.add_page(test_page, route="/testPage")
