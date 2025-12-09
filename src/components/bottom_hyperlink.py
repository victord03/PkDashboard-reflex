import reflex as rx

def hyperlink() -> rx.Component:

    return rx.link(
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
        }
    )