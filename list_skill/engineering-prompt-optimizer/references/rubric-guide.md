# Rubric Guide

## Metric Design

Prefer metrics that expose failure, not metrics that praise style. A good metric is specific enough that two reviewers mostly agree.

Core dimensions for engineering prompt work:
- Correctness: output follows the actual technical facts and task constraints.
- Completeness: output covers all required fields, artifacts, and edge cases.
- Specificity: output names concrete files, APIs, inputs, outputs, and decision points where needed.
- Verifiability: output can be checked by tests, examples, citations, schemas, or review criteria.
- Operational usefulness: a weaker model or engineer can execute it without making hidden decisions.

## Veto Failures

Use veto failures for mistakes that should fail the output regardless of average score:
- Fabricates facts, sources, APIs, library behavior, or current technology claims.
- Recommends a technology stack without current verification when the task requires current information.
- Skips task signature or metric and jumps directly to prompt wording.
- Leaves the implementer to choose core interfaces, data formats, or acceptance criteria.
- Produces vague instructions that cannot be tested.
- Ignores explicit user constraints.

## Golden Cases

Golden cases should be realistic, not toy examples. Cover:
- Happy path.
- Ambiguous input that must trigger questions.
- User with a wrong technical assumption.
- Missing constraints.
- Conflicting constraints.
- Tech-stack recommendation requiring search.
- Prompt polishing request that must be redirected to metric design.
- Weak-model execution output that must be judged.

Default progression:
- Draft 10 cases immediately.
- Expand to 50 before production use.
- Keep failures and expected behavior concise enough to review.

## Strong Model / Weak Model Pattern

Use a strong model for:
- Task signature.
- Metric and veto design.
- Golden-case creation.
- Final judgment and regression review.

Use a weaker or cheaper model for:
- Repetitive generation once the prompt and metric are stable.
- Batch drafting against golden cases.
- Low-risk formatting or transformation.

Do not ask the weak model to decide the core task definition.
