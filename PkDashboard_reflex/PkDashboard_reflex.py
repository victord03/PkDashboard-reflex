import reflex as rx

from src.components.search_box import search_box_with_button
from src.components.pokeball_icon import pokeball_icon
from src.components.results_components import _effectiveness_section
from src.models.type_calculator import (
    get_super_effective_against,
    get_not_very_effective_against,
    get_immune_types,
)
from src.models.pokemon_types import PokemonType
from src.styles.results_page_styles import results_main_vstack_style
from src.styles.background_sky import sky_background_style


class State(rx.State):
    selected_type: str = ""

    def store_input(self, value) -> None:
        self.selected_type = value

    def handle_submit(self) -> rx.event.EventSpec:
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

        **sky_background_style,
    )


@rx.page(route="/type/[type_name]")
def results_page() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                pokeball_icon(),
                position="absolute",
                top="20px",
                left="20px",
            ),

            # PAGE HEADING
            rx.heading(
                f"Results for: {State.selected_type}",
                font_size="32px",
                font_weight="800",
                margin_bottom="32px",
                color="#ffffff",  # White text for dark background
            ),

            # SUPER EFFECTIVE
            _effectiveness_section(title="Super effective against:", types_list=State.super_effective_types),

            # INEFFECTIVE
            _effectiveness_section(title="Ineffective against:", types_list=State.not_effective_types),

            # IMMUNITIES AGAINST
            _effectiveness_section(title=f"Types that have immunity to {State.selected_type}:", types_list=State.immune_types),

            **results_main_vstack_style,

            **sky_background_style,
        ),
        position="relative",
    )


app = rx.App()
app.add_page(index)
app.add_page(results_page)
