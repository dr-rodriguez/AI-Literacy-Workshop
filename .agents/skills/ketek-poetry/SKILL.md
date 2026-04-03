---
name: ketek-poetry
description: Generates or analyzes Ketek poetry, a word-based palindromic form of poetry from Brandon Sanderson's Stormlight Archive. Use when the user asks for a Ketek, a poem that reads the same forward and backward by word, or asks to format a poem as a Ketek.
---

# Ketek Poetry

A Ketek is a form of holy Vorin poetry characterized by its strict symmetry and complex structure. It is a word-based palindrome divided into five distinct sections.

## Rules of a Ketek

1. **Word-Based Palindrome**: The poem must read the same forward and backward by word (not by letter).
2. **Five Distinct Sections**: The poem must be divisible into five sections, each expressing a complete, distinct thought.
3. **Grammatically Correct**: The entire poem must form a single, grammatically correct sentence.
4. **Poignant**: It should have a deep or meaningful impact.

### Allowances
- **Verb/Word Forms**: You may change the form of a word (e.g., *dying* to *death*, *illuminate* to *illuminating*, *knowing* to *knowledge*) to ensure the grammar works while maintaining the core meaning.
- **Punctuation**: Use punctuation freely to change the meaning or flow between the forward and backward halves.

## Implementation Guidelines

When generating a Ketek:
1. Start with the **pivot** (the third section) and work outwards.
2. Ensure the first and fifth sections mirror each other to provide a sense of "coming home."
3. **Formatting**: Always separate the five sections with forward slashes (`/`).
4. **Output**: Only provide the poem unless the user asks for an explanation.

## Examples

See [references/examples.md](references/examples.md) for classic and fan-made examples.

- Above silence / the illuminating storms / dying storms / illuminate / the silence above.
- Alight / winds approach / deadly / approaching winds / alight.
- Radiant / of birthplace / the announcer comes / to come announce / the birthplace of Radiants.
