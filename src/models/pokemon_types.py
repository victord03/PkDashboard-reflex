from dataclasses import dataclass
from enum import Enum


class PokemonType(Enum):
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
    attacker: PokemonType
    defender: PokemonType
    multiplier: float


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

