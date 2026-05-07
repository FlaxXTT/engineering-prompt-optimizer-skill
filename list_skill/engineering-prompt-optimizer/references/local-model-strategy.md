# Local Model Strategy

Use this reference when the user mentions privacy, local models, weak models, offline execution, inference cost, context limits, or long prompts.

## Defaults

Assume the user may prefer local execution and minimal disclosure. Keep prompts small unless a strong model is explicitly available.

## Prompt Tiers

### Short Prompt

Use for small local models or repetitive execution. Include only:
- Task.
- Input.
- Output format.
- Top metric requirements.
- Veto failures.
- Stop-and-ask trigger.

### Standard Prompt

Use when the model can handle more context. Add:
- Task signature summary.
- Examples.
- Module instructions if needed.
- Review checklist.

### Strong Generator Prompt

Use only with the strongest available model. It should generate:
- Short prompt.
- Standard prompt.
- Judge prompt.
- Breakpoint plan.
- Decision trace summary.

## Breakpoints

Split long workflows into stages:
1. Clarification.
2. Retrieval or context collection.
3. Analysis.
4. Generation.
5. Review.

Each breakpoint needs:
- A short prompt.
- A stop condition.
- A handoff artifact.

## Privacy Rules

- Ask what data cannot leave the machine before recommending cloud models or web services.
- Keep sensitive context in local files when possible.
- Use redacted examples if examples contain personal, proprietary, or regulated data.
- Do not recommend current cloud tooling without search and citation when the recommendation may have changed.

## Decision Trace Summary

Provide an audit-friendly summary:
- Key judgments.
- Evidence used.
- Tradeoffs.
- Rejected options.
- Remaining uncertainty.

Do not ask for or expose hidden chain-of-thought.
