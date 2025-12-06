# Roadmap

## Phase 1: Core Functionality
- [x] Setup Reflex project structure
- [ ] Create Pokemon type data model using Relationship Graph architecture
  - [x] Define `TypeRelationship` dataclass (attacker, defender, multiplier)
  - [x] Create `PokemonType` Enum for type safety
  - [x] Build RELATIONSHIPS list with all type matchups (~150+ entries)
  - [x] Implement offensive index builder
  - [ ] Implement effectiveness lookup functions
  - [ ] Create dual-type effectiveness calculator
  - [ ] Write unit tests for data model
  - [ ] Implement defensive index (optional optimization for meta-analysis)
- [ ] Build search box with auto-filtering
- [ ] Display effectiveness tables for selected type

## Phase 2: Enhancements
- [ ] Add visual styling (colors per type)
- [ ] Show defensive matchups (weaknesses/resistances when defending)
- [ ] Implement dual-type Pokemon UI (architecture already supports calculations)

## Phase 3: Polish
- [ ] Add type icons/badges
- [ ] Responsive design
- [ ] Deploy to production

## Future Ideas
- Pokemon lookup by name (auto-determine type)
- Team builder showing collective weaknesses
- Generation-specific mechanics (if type effectiveness changed)
