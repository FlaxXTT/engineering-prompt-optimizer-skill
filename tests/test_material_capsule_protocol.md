# Test: Material Capsule Protocol

## Recognize Info Header

Given a capsule containing `## Info Header`, expected fields:

- id
- type
- source
- reliability
- summary
- read_when

## Detect missing Raw Material

If a capsule has Info Header but no `## Raw Material`, mark it incomplete and ask the user to provide raw or confirm header-only use.

## Multiple capsules

When two or more `# Material Capsule:` sections appear, index each separately in `context_index.md`.

## Low reliability

If `reliability: low`, allow indexing but require caution:

- do not treat its facts as confirmed;
- mark derived facts as low confidence;
- prefer asking for corroborating material.

## Unstructured material

If the user pastes a long Markdown document without Info Headers, ask them to convert it to capsules or split it into a small bounded excerpt.

