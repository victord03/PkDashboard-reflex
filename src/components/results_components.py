import reflex as rx
from typing import Union
from src.styles.results_page_styles import (
    result_box_style,
    results_vstack_style,
    results_text_style,
    results_title_style
)

def _effectiveness_section(
        title: str,
        types_list: Union[list[str], rx.Var]
) -> rx.Component:

    return rx.vstack(

        _section_title(title),

        _result_box(types_list),

        **results_vstack_style
    )

def _result_box(items: list[str]) -> rx.Component:

    return rx.box(
        rx.foreach(
            items,
            lambda t: rx.text(
                t,
                **results_text_style,
            ),
        ),
        **result_box_style
    )

def _section_title(text: str) -> rx.Component:

    return rx.text(
        text,
        **results_title_style,
    )