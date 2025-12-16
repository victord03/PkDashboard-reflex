# Roadmap

## Phase 1: Core Functionality
- [x] Setup Reflex project structure
- [ ] Create Pokemon type data model using Relationship Graph architecture
  - [x] Define `TypeRelationship` dataclass (attacker, defender, multiplier)
  - [x] Create `PokemonType` Enum for type safety
  - [x] Build RELATIONSHIPS list with all type matchups (~150+ entries)
  - [x] Implement offensive index builder
  - [x] Add data integrity validation (duplicate detection)
  - [x] Write unit tests for offensive index builder
  - [x] Write data integrity tests
  - [x] Add comprehensive docstrings to all code
  - [x] Implement effectiveness lookup functions
    - [x] `get_offensive_effectiveness()` with neutral matchup support
    - [x] `get_super_effective_against()`
    - [x] `get_not_very_effective_against()`
    - [x] `get_immune_types()`
    - [x] DRY helper function `_filter_by_multiplier()`
  - [x] Write unit tests for lookup functions (21 tests passing)
  - [ ] Create dual-type effectiveness calculator
  - [ ] Implement defensive index (optional optimization for meta-analysis)
- [x] Build search box with submit functionality
  - [x] Create search input component
  - [x] Add submit button
  - [x] Implement State management for user input
  - [x] Connect event handlers (on_change, on_click)
  - [x] Resolve circular import issues (pass handlers as props)
- [x] Display effectiveness tables for selected type
  - [x] Implement dynamic routing (`/type/[type_name]`)
  - [x] Create results page with three data boxes
  - [x] Add computed vars to read URL params and call calculator functions
  - [x] Use `rx.foreach` to render type lists
  - [x] Add defensive programming for empty states

## Phase 2: Enhancements
- [x] Add visual styling and layout
  - [x] Professional card-based UI with borders, shadows, rounded corners
  - [x] Background image support (customizable sky theme)
  - [x] Proper color contrast and typography hierarchy
  - [x] Titles positioned above result boxes
  - [ ] Type-specific colors and badges
- [x] Code architecture refactoring
  - [x] Extract reusable component functions (`_effectiveness_section()`, `_result_box()`, `_section_title()`)
  - [x] Create style dictionaries in `src/styles/` for DRY styling
  - [x] Implement functional composition patterns
  - [x] Apply dict unpacking for clean style application
- [ ] Navigation improvements
  - [x] Create pokeball icon component for homepage navigation
  - [ ] Fix icon positioning (absolute positioning in top-left corner)
- [ ] Search enhancements
  - [ ] Implement type-ahead filtering (auto-suggest Pokemon types as user types)
- [ ] Add Offensive/Defensive mode selector (dropdown UI)
  - [ ] Offensive mode: Show how selected type's moves perform against all types
  - [ ] Defensive mode: Advanced defensive analysis for selected type
    - [ ] Display incoming damage from all attacking types
    - [ ] Recommend coverage moves (analyze weakness chains - e.g., Fire→Water weakness, Water→Electric weakness, suggest Electric)
    - [ ] Suggest stat priorities (e.g., Water attackers use Sp.Atk → recommend Sp.Def, Fighting uses Atk → recommend Def)
    - [ ] Requires: Stat distribution knowledge per type (data research needed)
      - **Research TODO**: Find statistical data on type-based stat distributions (e.g., do Water-types have higher Atk or Sp.Atk on average?)
      - **Research TODO**: Find average base power for physical vs special moves per type (e.g., average damage of physical Water moves vs special Water moves)
      - Potential data sources: Bulbapedia, PokeAPI, Smogon usage stats, or manual dataset compilation
- [ ] Implement dual-type Pokemon UI (architecture already supports calculations)

## Phase 3: Polish
- [ ] Add type icons/badges
- [ ] Responsive design
- [ ] Deploy to production

## Future Ideas
- Pokemon lookup by name (auto-determine type)
- Team builder showing collective weaknesses
- Generation-specific mechanics (if type effectiveness changed)
