"""Type effectiveness calculator module.

Provides data transformation functions to build indexes for efficient
Pokémon type matchup lookups.
"""

from .pokemon_types import (
    PokemonType as pkType,
    RELATIONSHIPS as RLS,
    TypeRelationship, PokemonType
)
from collections import defaultdict
from typing import Dict

def build_offensive_index(data: list[TypeRelationship] = RLS) -> dict[pkType, Dict[pkType, float]]:
    """Builds an offensive lookup index from type relationships.

    Transforms a flat list of type relationships into a nested dictionary
    structure optimized for O(1) offensive effectiveness queries.

    Structure of returned index:
        {
            AttackType1: {
                DefendType1: multiplier,
                DefendType2: multiplier,
                ...,
            },

            AttackType2: {
                DefendType1: multiplier,
                ...,
            },

            ...,
        }

    Args:
        data: List of TypeRelationship objects. Defaults to RELATIONSHIPS constant.

    Returns:
        Nested dictionary mapping attacker types to defender types to multipliers.
        Returns empty dict if data is empty.

    Example:
        >> index = build_offensive_index()
        >> index[PokemonType.FIRE][PokemonType.GRASS]
        2.0
    """
    index = defaultdict(dict)

    # each relation is a TypeRelationship object
    for relation in data:
        index[relation.attacker][relation.defender] = relation.multiplier

    return index

# Creating the index as a global
OFFENSIVE_INDEX = build_offensive_index()

def _filter_by_multiplier(attacker: PokemonType, multiplier: float) -> list[PokemonType]:
    """Helper function to filter types by specific damage multiplier.

    Private utility function used by get_super_effective_against,
    get_not_very_effective_against, and get_immune_types to avoid code duplication.

    Args:
        attacker: The attacking Pokémon type
        multiplier: The damage multiplier to filter by (2.0, 0.5, or 0.0)

    Returns:
        List of PokemonType that match the specified multiplier when attacked.
    """
    attacker_type_dict = OFFENSIVE_INDEX.get(attacker)
    return [pk_type for pk_type, mult in attacker_type_dict.items() if mult == multiplier]


def get_offensive_effectiveness(attacker: PokemonType, defender: PokemonType) -> float:
    """Returns the damage multiplier for an attacking type against a defending type.

    Args:
        attacker: The attacking Pokémon type
        defender: The defending Pokémon type

    Returns:
        Damage multiplier (2.0=super effective, 0.5=not very effective,
        0.0=immune, 1.0=neutral)
    """
    attacker_type_dict = OFFENSIVE_INDEX.get(attacker)

    return attacker_type_dict.get(defender, 1.0)

def get_super_effective_against(attacker: PokemonType) -> list[PokemonType]:
    """Returns all types that the attacker is super effective against (2x damage).

    Args:
        attacker: The attacking Pokémon type

    Returns:
        List of PokemonType that receive 2x damage from the attacker.
        Returns empty list if no super effective matchups exist.
    """
    return _filter_by_multiplier(attacker, 2.0)

def get_not_very_effective_against(attacker: PokemonType) -> list[PokemonType]:
    """Returns all types that resist the attacker's moves (0.5x damage).

    Args:
        attacker: The attacking Pokémon type

    Returns:
        List of PokemonType that receive 0.5x damage from the attacker.
        Returns empty list if no resisted matchups exist.
    """
    return _filter_by_multiplier(attacker, 0.5)


def get_immune_types(attacker: PokemonType) -> list[PokemonType]:
    """Returns all types that are immune to the attacker's moves (0x damage).

    Args:
        attacker: The attacking Pokémon type

    Returns:
        List of PokemonType that are immune (0x damage) to the attacker.
        Returns empty list if no immunities exist.
    """
    return _filter_by_multiplier(attacker, 0.0)
