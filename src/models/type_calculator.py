from .pokemon_types import PokemonType as pkType, RELATIONSHIPS as RLS, TypeRelationship
from collections import defaultdict
from typing import Dict

"""

    { 
        "AttackType1" : {
            "DefendType": DamageMultiplier,
            "DefendType2": DamageMultiplier,
            ...,
        },
        "AttackType2" : {
            "DefendType": DamageMultiplier,
            "DefendType2": DamageMultiplier,
            ...,
        },
        ...
    }

"""

def build_offensive_index(data: list[TypeRelationship] = RLS) -> dict[pkType, Dict[pkType, float]]:
    index = defaultdict(dict)

    # each relation is a TypeRelationship object
    for relation in data:
        index[relation.attacker][relation.defender] = relation.multiplier

    return index
