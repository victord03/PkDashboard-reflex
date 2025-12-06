import pytest
from src.models.pokemon_types import (
    TypeRelationship,
    PokemonType,
    check_relationships_for_duplicates as cfd
)
from src.models.type_calculator import (
    build_offensive_index as boi,
    OFFENSIVE_INDEX,
    get_offensive_effectiveness,
    get_super_effective_against,
    get_not_very_effective_against,
    get_immune_types
)

@pytest.fixture
def create_list_of_relationships() -> list[TypeRelationship]:
    """Provides a small sample of valid type relationships for testing.

    Returns:
        List of 6 TypeRelationship objects with varied multipliers for testing
    """
    return [

        # Normal
        TypeRelationship(attacker=PokemonType.NORMAL, defender=PokemonType.ROCK, multiplier=0.5),

        # Fire
        TypeRelationship(attacker=PokemonType.FIRE, defender=PokemonType.ICE, multiplier=2.0),

        # Water
        TypeRelationship(attacker=PokemonType.WATER, defender=PokemonType.GRASS, multiplier=0.5),

        # Electric
        TypeRelationship(attacker=PokemonType.ELECTRIC, defender=PokemonType.DRAGON, multiplier=0.5),

        # Poison
        TypeRelationship(attacker=PokemonType.POISON, defender=PokemonType.STEEL, multiplier=0.0),
        TypeRelationship(attacker=PokemonType.POISON, defender=PokemonType.FAIRY, multiplier=2.0),
    ]

@pytest.fixture
def create_list_with_duplicate() -> list[TypeRelationship]:
    """Provides a list containing a duplicate (attacker, defender) pair for testing validation.

    Returns:
        List with intentional duplicate Water → Grass relationship for testing duplicate detection
    """
    return [

        # Normal
        TypeRelationship(attacker=PokemonType.NORMAL, defender=PokemonType.ROCK, multiplier=0.5),

        # Fire
        TypeRelationship(attacker=PokemonType.FIRE, defender=PokemonType.ICE, multiplier=2.0),

        # Water
        TypeRelationship(attacker=PokemonType.WATER, defender=PokemonType.GRASS, multiplier=0.5),

        # Water duplicate entry
        TypeRelationship(attacker=PokemonType.WATER, defender=PokemonType.GRASS, multiplier=0.5),

    ]

class TestDataIntegrity:
    """Tests for validating data integrity of type relationships."""

    def test_duplicate_in_origin_date_raises_error(self, create_list_with_duplicate: list[TypeRelationship]) -> None:
        """Verify that duplicate (attacker, defender) pairs raise ValueError."""
        with pytest.raises(ValueError):
            cfd(create_list_with_duplicate)

class TestOffensiveIndex:
    """Tests for the offensive type effectiveness index builder."""

    def test_build_offensive_index(self, create_list_of_relationships: list[TypeRelationship]) -> None:
        """Verify that build_offensive_index correctly transforms relationships into nested dict structure."""
        assert boi(create_list_of_relationships) == {
            PokemonType.NORMAL: {PokemonType.ROCK: 0.5},
            PokemonType.FIRE: {PokemonType.ICE: 2.0},
            PokemonType.WATER: {PokemonType.GRASS: 0.5},
            PokemonType.ELECTRIC: {PokemonType.DRAGON: 0.5},
            PokemonType.POISON:
                {
                    PokemonType.STEEL: 0.0,
                    PokemonType.FAIRY: 2.0
                }
        }

    def test_boi_empty_list_returns_empty_dict(self) -> None:
        """Verify that empty input gracefully returns empty dict without crashing."""
        assert boi([]) == {}

    def test_boi_empty_dict_raises_value_error(self) -> None:
        """Placeholder for future test - currently not applicable to this function."""
        ...

class TestCalcFunctions:
    """Tests for type effectiveness lookup and filtering functions."""

    @pytest.mark.parametrize(
        "attacker, defender, result",
        [
            (PokemonType.FIRE, PokemonType.WATER, 0.5),
            (PokemonType.FAIRY, PokemonType.FIGHTING, 2.0),
            (PokemonType.NORMAL, PokemonType.GHOST, 0.0),
            (PokemonType.NORMAL, PokemonType.PSYCHIC, 1.0),
            (PokemonType.PSYCHIC, PokemonType.NORMAL, 1.0)
        ]
    )
    def test_get_offensive_effectiveness(self, attacker: PokemonType, defender: PokemonType, result: float) -> None:
        """Verify offensive effectiveness returns correct multipliers for various matchups including neutral cases."""
        assert get_offensive_effectiveness(attacker, defender) == result

    @pytest.mark.parametrize(
        "attacker, result", [
            (PokemonType.FIRE, [PokemonType.GRASS, PokemonType.ICE, PokemonType.BUG, PokemonType.STEEL]),
            (PokemonType.ELECTRIC, [PokemonType.WATER, PokemonType.FLYING]),
            (PokemonType.NORMAL, []),
        ]
    )
    def test_get_super_effective_against(self, attacker: PokemonType, result: float) -> None:
        """Verify super effective filtering returns all types that receive 2x damage, including empty lists."""
        assert get_super_effective_against(attacker) == result

    @pytest.mark.parametrize(
        "attacker, result", [
            (PokemonType.NORMAL, [PokemonType.ROCK]),
            (PokemonType.FIRE, [PokemonType.FIRE, PokemonType.WATER, PokemonType.ROCK, PokemonType.DRAGON]),
            (PokemonType.ELECTRIC, [PokemonType.ELECTRIC, PokemonType.GRASS, PokemonType.DRAGON]),
            (PokemonType.GRASS, [PokemonType.FIRE, PokemonType.GRASS, PokemonType.POISON, PokemonType.FLYING, PokemonType.BUG, PokemonType.DRAGON, PokemonType.STEEL])
        ]
    )
    def test_get_not_very_effective_against(self, attacker: PokemonType, result: float) -> None:
        """Verify not very effective filtering returns all types that resist with 0.5x damage."""
        assert get_not_very_effective_against(attacker) == result

    @pytest.mark.parametrize(
        "attacker, result", [
            (PokemonType.NORMAL, [PokemonType.GHOST]),
            (PokemonType.ELECTRIC, [PokemonType.GROUND]),
            (PokemonType.FIGHTING, [PokemonType.GHOST]),
            (PokemonType.POISON, [PokemonType.STEEL]),
            (PokemonType.PSYCHIC, [PokemonType.DARK])
        ]
    )
    def test_get_immune_types(self, attacker: PokemonType, result: float) -> None:
        """Verify immune type filtering returns all types that take 0x damage (complete immunity)."""
        assert get_immune_types(attacker) == result