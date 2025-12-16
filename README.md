# PkDashboard-reflex

A Pokemon type effectiveness dashboard built with Reflex to visualize strengths, weaknesses, and immunities.

## Overview

Simple web interface to lookup Pokemon type matchups:
- Search/filter by type name
- View offensive effectiveness (very effective, not very effective, immunities)

## Architecture

**Relationship Graph Model**: Type effectiveness is modeled as a directed graph where:
- **Nodes**: Pokemon types (Fire, Water, Grass, etc.)
- **Edges**: Directional effectiveness relationships with multipliers
- **Data structure**: `TypeRelationship` dataclass storing (attacker, defender, multiplier)
- **Indexes**: Bidirectional lookups for both offensive and defensive queries

**Key design decisions:**
- Directional relationships (Fire→Grass is 2.0x, but Grass→Fire is 0.5x)
- Single source of truth (each relationship stored once)
- Dual-type support via multiplier composition
- O(1) lookups via pre-built indexes

## Features

- **Search interface**: Input-based type lookup with submit functionality
- **Type effectiveness tables**:
  - Very effective against (2x damage)
  - Not very effective against (0.5x damage)
  - Immunities (0x damage, if applicable)
- **Polished UI**: Card-based layout with custom background themes and responsive typography

## Tech Stack

- [Reflex](https://reflex.dev/) - Python web framework
- Python 3.x
- **Data structures**: `@dataclass`, `defaultdict`, graph indexing patterns
- **Package manager**: uv

## Setup

```bash
# Install dependencies
uv pip install reflex

# Run app
reflex run
```

## Project Status

**Current Phase**: Polished UI with modular architecture, ready for dual-type calculator and type-ahead search

Completed:
- ✅ Project structure setup (`src/components`, `src/models`, `src/styles`, `tests`)
- ✅ `PokemonType` Enum with all 18 types
- ✅ `TypeRelationship` dataclass (frozen, with attacker/defender/multiplier)
- ✅ Complete RELATIONSHIPS list (~150+ matchups)
- ✅ `build_offensive_index()` function with proper type hints
- ✅ `check_relationships_for_duplicates()` validation function (runs on module import)
- ✅ Module-level `OFFENSIVE_INDEX` constant (precomputed static reference data)
- ✅ Effectiveness lookup functions:
  - `get_offensive_effectiveness()` - Returns damage multiplier for any matchup (including neutral 1.0x)
  - `get_super_effective_against()` - Returns all types that receive 2x damage
  - `get_not_very_effective_against()` - Returns all types that resist with 0.5x damage
  - `get_immune_types()` - Returns all types with complete immunity (0x damage)
- ✅ DRY helper function `_filter_by_multiplier()` to reduce code duplication
- ✅ Comprehensive unit tests (21 tests passing) including edge cases and neutral matchups
- ✅ Data integrity tests for duplicate detection
- ✅ Google-style docstrings for all production and test code
- ✅ **UI Integration:**
  - Search box component with submit button
  - State management with reactive vars
  - Dynamic routing (`/type/[type_name]`)
  - Results page displaying effectiveness data
  - Computed vars that read from URL params
  - `rx.foreach` for rendering type lists
  - Defensive programming (empty state handling)
- ✅ **Visual Styling & Layout:**
  - Professional card-based layout with proper spacing, borders, and shadows
  - Background image support with customizable sky theme
  - Proper color contrast (white text on dark backgrounds, dark text on white cards)
  - Titles positioned above result boxes (not inside)
  - Responsive typography hierarchy
- ✅ **Code Architecture Refactoring:**
  - Functional composition with reusable component functions (`src/components/results_components.py`)
  - Extracted style dictionaries (`src/styles/results_page_styles.py`, `src/styles/background_sky.py`)
  - Modular helper functions: `_effectiveness_section()`, `_result_box()`, `_section_title()`
  - Dict unpacking for clean style application
  - Dramatically improved code readability (90+ lines → 3 function calls)

In Progress:
- 🔨 Homepage navigation icon (pokeball icon created, positioning pending)
- 🔨 Type-ahead search filtering
- 🔨 Dual-type effectiveness calculator
