from dataclasses import dataclass
from enum import Enum


class PokemonType(Enum):
    """Enumeration of all 18 Pokémon types.

    Each type represents a distinct Pokémon elemental category with unique
    offensive and defensive effectiveness characteristics.
    """
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    ELECTRIC = "Electric"
    GRASS = "Grass"
    ICE = "Ice"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DRAGON = "Dragon"
    DARK = "Dark"
    STEEL = "Steel"
    FAIRY = "Fairy"


@dataclass(frozen=True)
class TypeRelationship:
    """Represents a directional type effectiveness relationship.

    Models how effective one Pokémon type is when attacking another type
    using a damage multiplier. Frozen to ensure immutability of reference data.

    Attributes:
        attacker: The attacking Pokémon type
        defender: The defending Pokémon type
        multiplier: Damage multiplier (2.0=super effective, 0.5=not very effective, 0.0=immune)
    """
    attacker: PokemonType
    defender: PokemonType
    multiplier: float


# todo: evaluate if useful as an additional data integrity check (cons: if tables are updated in any way, this func also needs to be updated for the tests not to fail integrity test)
def check_relationships_for_number_of_entries(relations: list[TypeRelationship]) -> None:
    """Counts the number of entries per type (super effective, not very effective and immunities.

    Args:
        relations: List of TypeRelationship

    Raises:
        ValueError: If the amount of entries is not correct
    """
    ...


def check_relationships_for_duplicates(relations: list[TypeRelationship]) -> None:
    """Validates that no duplicate (attacker, defender) pairs exist in the relationships list.

    This function ensures data integrity by detecting duplicate type matchups
    that could result from copy-paste errors during data entry. Uses a set for
    O(1) lookup performance.

    Args:
        relations: List of TypeRelationship objects to validate

    Raises:
        ValueError: If duplicate (attacker, defender) pair is found
    """
    seen = set()

    for relation in relations:
        current_tuple = (relation.attacker, relation.defender)
        if current_tuple in seen:
            raise ValueError(f"Duplicate entry found: ({relation.attacker}, {relation.defender}).")
        seen.add(current_tuple)

# Critical matchups ("super effective" and "not very effective")
RELATIONSHIPS = [

    # Normal
    TypeRelationship(attacker=PokemonType.NORMAL, defender=PokemonType.ROCK, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.NORMAL, defender=PokemonType.GHOST, multiplier=0.0),

    # Fire
    TypeRelationship(attacker=PokemonType.FIRE, defender=PokemonType.FIRE, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FIRE, defender=PokemonType.WATER, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FIRE, defender=PokemonType.GRASS, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FIRE, defender=PokemonType.ICE, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FIRE, defender=PokemonType.BUG, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FIRE, defender=PokemonType.ROCK, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FIRE, defender=PokemonType.DRAGON, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FIRE, defender=PokemonType.STEEL, multiplier=2.0),

    # Water
    TypeRelationship(attacker=PokemonType.WATER, defender=PokemonType.FIRE, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.WATER, defender=PokemonType.WATER, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.WATER, defender=PokemonType.GRASS, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.WATER, defender=PokemonType.GROUND, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.WATER, defender=PokemonType.ROCK, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.WATER, defender=PokemonType.DRAGON, multiplier=0.5),

    # Electric
    TypeRelationship(attacker=PokemonType.ELECTRIC, defender=PokemonType.WATER, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.ELECTRIC, defender=PokemonType.ELECTRIC, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.ELECTRIC, defender=PokemonType.GRASS, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.ELECTRIC, defender=PokemonType.GROUND, multiplier=0.0),
    TypeRelationship(attacker=PokemonType.ELECTRIC, defender=PokemonType.FLYING, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.ELECTRIC, defender=PokemonType.DRAGON, multiplier=0.5),

    # Grass
    TypeRelationship(attacker=PokemonType.GRASS, defender=PokemonType.FIRE, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.GRASS, defender=PokemonType.WATER, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.GRASS, defender=PokemonType.GRASS, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.GRASS, defender=PokemonType.POISON, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.GRASS, defender=PokemonType.GROUND, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.GRASS, defender=PokemonType.FLYING, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.GRASS, defender=PokemonType.BUG, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.GRASS, defender=PokemonType.ROCK, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.GRASS, defender=PokemonType.DRAGON, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.GRASS, defender=PokemonType.STEEL, multiplier=0.5),

    # Ice
    TypeRelationship(attacker=PokemonType.ICE, defender=PokemonType.FIRE, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.ICE, defender=PokemonType.WATER, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.ICE, defender=PokemonType.GRASS, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.ICE, defender=PokemonType.ICE, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.ICE, defender=PokemonType.GROUND, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.ICE, defender=PokemonType.FLYING, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.ICE, defender=PokemonType.DRAGON, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.ICE, defender=PokemonType.STEEL, multiplier=0.5),

    # Fighting
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.NORMAL, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.ICE, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.POISON, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.FLYING, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.PSYCHIC, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.BUG, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.ROCK, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.GHOST, multiplier=0.0),
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.DARK, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.STEEL, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FIGHTING, defender=PokemonType.FAIRY, multiplier=0.5),

    # Poison
    TypeRelationship(attacker=PokemonType.POISON, defender=PokemonType.GRASS, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.POISON, defender=PokemonType.POISON, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.POISON, defender=PokemonType.GROUND, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.POISON, defender=PokemonType.ROCK, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.POISON, defender=PokemonType.GHOST, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.POISON, defender=PokemonType.STEEL, multiplier=0.0),
    TypeRelationship(attacker=PokemonType.POISON, defender=PokemonType.FAIRY, multiplier=2.0),

    # Ground
    TypeRelationship(attacker=PokemonType.GROUND, defender=PokemonType.FIRE, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.GROUND, defender=PokemonType.ELECTRIC, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.GROUND, defender=PokemonType.GRASS, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.GROUND, defender=PokemonType.GROUND, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.GROUND, defender=PokemonType.FLYING, multiplier=0.0),
    TypeRelationship(attacker=PokemonType.GROUND, defender=PokemonType.BUG, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.GROUND, defender=PokemonType.ROCK, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.GROUND, defender=PokemonType.STEEL, multiplier=2.0),

    # Flying
    TypeRelationship(attacker=PokemonType.FLYING, defender=PokemonType.ELECTRIC, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FLYING, defender=PokemonType.GRASS, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FLYING, defender=PokemonType.FIGHTING, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FLYING, defender=PokemonType.BUG, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FLYING, defender=PokemonType.ROCK, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FLYING, defender=PokemonType.STEEL, multiplier=0.5),

    # Psychic
    TypeRelationship(attacker=PokemonType.PSYCHIC, defender=PokemonType.FIGHTING, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.PSYCHIC, defender=PokemonType.POISON, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.PSYCHIC, defender=PokemonType.PSYCHIC, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.PSYCHIC, defender=PokemonType.DARK, multiplier=0.0),
    TypeRelationship(attacker=PokemonType.PSYCHIC, defender=PokemonType.STEEL, multiplier=0.5),

    # Bug
    TypeRelationship(attacker=PokemonType.BUG, defender=PokemonType.FIRE, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.BUG, defender=PokemonType.GRASS, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.BUG, defender=PokemonType.FIGHTING, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.BUG, defender=PokemonType.POISON, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.BUG, defender=PokemonType.FLYING, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.BUG, defender=PokemonType.PSYCHIC, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.BUG, defender=PokemonType.GHOST, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.BUG, defender=PokemonType.DARK, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.BUG, defender=PokemonType.STEEL, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.BUG, defender=PokemonType.FAIRY, multiplier=0.5),

    # Rock
    TypeRelationship(attacker=PokemonType.ROCK, defender=PokemonType.FIRE, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.ROCK, defender=PokemonType.ICE, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.ROCK, defender=PokemonType.FIGHTING, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.ROCK, defender=PokemonType.GROUND, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.ROCK, defender=PokemonType.FLYING, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.ROCK, defender=PokemonType.BUG, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.ROCK, defender=PokemonType.STEEL, multiplier=0.5),

    # Ghost
    TypeRelationship(attacker=PokemonType.GHOST, defender=PokemonType.NORMAL, multiplier=0.0),
    TypeRelationship(attacker=PokemonType.GHOST, defender=PokemonType.PSYCHIC, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.GHOST, defender=PokemonType.GHOST, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.GHOST, defender=PokemonType.DARK, multiplier=0.5),

    # Dragon
    TypeRelationship(attacker=PokemonType.DRAGON, defender=PokemonType.DRAGON, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.DRAGON, defender=PokemonType.STEEL, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.DRAGON, defender=PokemonType.FAIRY, multiplier=0.0),

    # Dark
    TypeRelationship(attacker=PokemonType.DARK, defender=PokemonType.FIGHTING, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.DARK, defender=PokemonType.PSYCHIC, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.DARK, defender=PokemonType.GHOST, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.DARK, defender=PokemonType.DARK, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.DARK, defender=PokemonType.FAIRY, multiplier=0.5),

    # Steel
    TypeRelationship(attacker=PokemonType.STEEL, defender=PokemonType.FIRE, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.STEEL, defender=PokemonType.WATER, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.STEEL, defender=PokemonType.ELECTRIC, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.STEEL, defender=PokemonType.ICE, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.STEEL, defender=PokemonType.ROCK, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.STEEL, defender=PokemonType.STEEL, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.STEEL, defender=PokemonType.FAIRY, multiplier=2.0),

    # Fairy
    TypeRelationship(attacker=PokemonType.FAIRY, defender=PokemonType.FIRE, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FAIRY, defender=PokemonType.FIGHTING, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FAIRY, defender=PokemonType.POISON, multiplier=0.5),
    TypeRelationship(attacker=PokemonType.FAIRY, defender=PokemonType.DRAGON, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FAIRY, defender=PokemonType.DARK, multiplier=2.0),
    TypeRelationship(attacker=PokemonType.FAIRY, defender=PokemonType.STEEL, multiplier=0.5),

]


# Validate data integrity on module import (fail-fast for duplicates)
check_relationships_for_duplicates(RELATIONSHIPS)
