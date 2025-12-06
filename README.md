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

- **Auto-filtering search**: Type-ahead search (e.g., "Fi" → "Fire")
- **Type effectiveness tables**:
  - Very effective against (2x damage)
  - Not very effective against (0.5x damage)
  - Immunities (0x damage, if applicable)

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

**Current Phase**: Core data model complete, moving to lookup functions and tests

Completed:
- ✅ Project structure setup (`src/components`, `src/models`)
- ✅ Basic search box UI component
- ✅ `PokemonType` Enum with all 18 types
- ✅ `TypeRelationship` dataclass (frozen, with attacker/defender/multiplier)
- ✅ Complete RELATIONSHIPS list (~150+ matchups)
- ✅ `build_offensive_index()` function with proper type hints

In Progress:
- 🔨 Effectiveness lookup functions
- 🔨 Unit tests for data model and calculator
