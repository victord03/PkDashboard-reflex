import reflex as rx

from src.components.search_box import search_box_with_button
from src.models.type_calculator import (
    get_super_effective_against,
    get_not_very_effective_against,
    get_immune_types,
)
from src.models.pokemon_types import PokemonType

class State(rx.State):
    selected_type: str = ""


    def store_input(self, value):
        self.selected_type = value

    def handle_submit(self):
        return rx.redirect(f"/type/{self.selected_type}")

    @rx.var
    def super_effective_types(self) -> list[str]:
        type_str = self.router.page.params.get("type_name", "")
        if not type_str:
            return []
        type_enum = PokemonType[type_str.upper()]
        results = get_super_effective_against(type_enum)
        return [t.value for t in results]

    @rx.var
    def not_effective_types(self) -> list[str]:
        type_str = self.router.page.params.get("type_name", "")
        if not type_str:
            return []
        type_enum = PokemonType[type_str.upper()]
        results = get_not_very_effective_against(type_enum)
        return [t.value for t in results]

    @rx.var
    def immune_types(self) -> list[str]:
        type_str = self.router.page.params.get("type_name", "")
        if not type_str:
            return []
        type_enum = PokemonType[type_str.upper()]
        results = get_immune_types(type_enum)
        return [t.value for t in results]


def index() -> rx.Component:
    return rx.container(

            # SEARCH BOX WITH SUBMIT BUTTON
            search_box_with_button(
                on_change=State.store_input,
                on_submit=State.handle_submit,
            ),
    )


@rx.page(route="/type/[type_name]")
def results_page() -> rx.Component:

    return rx.vstack(

        # TEXT
        rx.heading(f"Results for: {State.selected_type}"),

        # SUPER EFFECTIVE BOX
        rx.box(
            "Super effective against:",
            rx.foreach(State.super_effective_types, lambda t: rx.text(t)),

        ),

        # NOT VERY EFFECTIVE BOX
        rx.box(
            "Not very effective against:",
            rx.foreach(State.not_effective_types, lambda t: rx.text(t)),

        ),

        # IMMUNITIES BOX
        rx.box(
            f"Types immune to {State.selected_type}:",
            rx.foreach(State.immune_types, lambda t: rx.text(t)),

        )
    )


app = rx.App()
app.add_page(index)
app.add_page(results_page)

