# Test: Targeted Raw Reading

## Read only relevant raw

Scenario:

- `MC-001`: refund policy, relevance high.
- `MC-002`: support tone guide, relevance medium.
- `MC-003`: product roadmap, relevance low.

During fact-risk review, expected:

- read Info Headers for all three;
- read raw for `MC-001`;
- do not read raw for `MC-003`;
- read `MC-002` raw only if reply wording is under review.

## Raw too long

If a raw section is too long, expected:

- ask user to split the capsule or identify relevant sections;
- do not consume the entire raw by default.

## Evidence map

Every fact added to the final prompt must map to:

- Material ID;
- evidence type;
- confidence;
- verification status;
- notes.

