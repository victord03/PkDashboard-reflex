# Lessons Learned

## Static Reference Data vs Runtime Parameters

**Context:** When designing functions that operate on datasets, the choice between module-level constants and function parameters depends on data mutability.

### Static Reference Data → Module-Level Constants

**When to use:**
- Data is hardcoded and never changes at runtime
- Data represents game mechanics, configuration, or reference tables
- Expensive to compute but only needed once

**Pattern:**
```python
# Precompute at module import
REFERENCE_INDEX = build_index(STATIC_DATA)

def query_function(key):
    return REFERENCE_INDEX[key]  # Uses global constant
```

**Benefits:**
- Built once on import, zero runtime overhead
- Cleaner API (consumers don't manage data)
- Common Python idiom for expensive constant initialization
- Appropriate use of global state (immutable reference data)

**Examples:** Django settings, NumPy constant tables, game stat databases

---

### Runtime-Modified Data → Function Parameters

**When to use:**
- Data changes during program execution
- Multiple different datasets need to be queried
- Distributed systems or dependency injection needed
- Testing requires custom/mock datasets

**Pattern:**
```python
def query_function(index, key):
    return index[key]  # Explicit dependency

# Caller manages data
index = build_index(dynamic_data)
result = query_function(index, key)
```

**Benefits:**
- Pure functions with explicit dependencies
- Highly testable (inject custom data)
- Supports multiple concurrent datasets
- Functional programming alignment

**Examples:** User-generated data, API responses, streaming data

---

### Decision for PkDashboard

**Choice:** Module-level constant (`OFFENSIVE_INDEX = build_offensive_index()`)

**Rationale:** Pokemon type effectiveness is static game mechanics that never changes at runtime, making it ideal for precomputed module-level constants.

---

## Query Result Mutability: Lists vs Immutable Collections

**Context:** When query functions return collections (e.g., `get_super_effective_against()`), should they return mutable (`list`) or immutable (`tuple`/`frozenset`) types?

### Current Decision: Mutable Lists (with intent to refactor)

**Choice:** Return `list[PokemonType]` from query functions

**Rationale:**
- **Flexibility during discovery phase:** Requirements for sorting, filtering, and display ordering are still evolving
- **Custom ordering needs:** UI likely requires specific type ordering (e.g., Normal, Fire, Water... matching canonical charts) rather than alphabetical
- **Ease of manipulation:** Lists support slicing, indexing, and easy transformation without conversion overhead
- **Conventional Python:** Most query functions return lists (familiar pattern)

**Known Tradeoff:** Lists are mutable, which could allow accidental modification by callers (though each query creates a new list, so source data is protected)

### Future Refactoring Consideration

**When to reconsider:**
- Once UI display requirements are finalized
- When sorting/ordering logic is stable
- During code hardening phase (Phase 3)

**Potential refactor targets:**
- `tuple[PokemonType, ...]` - If deterministic ordering is established, provides immutability with indexing
- `frozenset[PokemonType]` - If order truly doesn't matter and set operations are needed

**Action item:** Revisit during Phase 3 (Polish) to assess complexity of refactoring vs benefits of immutability.
