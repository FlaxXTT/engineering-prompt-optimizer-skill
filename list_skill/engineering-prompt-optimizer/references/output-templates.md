# Output Templates

Use these templates when the user has provided enough information to build a full prompt package.

## meta_prompt.md

```markdown
# Meta-prompt

## Raw User Intent
<briefly restate the rough user request>

## Induced Core Demand
<what the user actually appears to need>

## User-Provided Golden Seeds
- Input: <example input>
  Output: <example desired output>

## Confirmed Constraints
- <privacy, local model, cost, latency, stack, language, or output constraints>

## Open Risks
- <facts that still need confirmation>
```

## induction_questions.md

```markdown
# Induction Questions

## Requirement Induction Summary
<core demand, likely audience, likely workflow, likely failure mode>

## Blocking Questions
1. <question about task boundary or failure boundary>
2. <question about metric or examples>
3. <question about privacy, target model, or deployment constraints>

## Stop Rule
Do not generate the final prompt until the blocking questions are answered or explicitly accepted as assumptions.
```

## task_signature.md

```markdown
# Task Signature

## Name
<short task name>

## Purpose
<one sentence describing the real job>

## Inputs
- <input name>: <type, source, required/optional, constraints>

## Outputs
- <output name>: <format, destination, quality bar>

## Constraints
- <technical, time, cost, safety, compatibility, or style constraints>

## Use Context
<who runs it, in which tool, how often, and under what uncertainty>

## Failure Boundary
- <what must not happen>
- <what means the task should stop and ask for clarification>
```

## metric.md

```markdown
# Metric

## Score Dimensions
- Correctness (<weight>%): <how to judge>
- Completeness (<weight>%): <how to judge>
- Specificity (<weight>%): <how to judge>
- Verifiability (<weight>%): <how to judge>
- Usability (<weight>%): <how to judge>

## Veto Failures
- <condition that makes the output fail regardless of score>

## Automated Checks
- <lint, tests, schema validation, exact-match checks, citation checks, or not applicable>

## Human Review Checks
- <expert judgment criteria that cannot be automated yet>

## Pass Threshold
<minimum score and veto-free requirement>
```

## golden_cases.md

```markdown
# Golden Cases

Target: 50 high-quality cases before production use.

## Case 001: <case name>
- Input:
  <realistic input>
- Expected behavior:
  <what a good output must do>
- Common failure:
  <what a weak model is likely to get wrong>
- Metric focus:
  <which score dimensions this case stresses>
```

## module_map.md

```markdown
# Module Map

## query_rewrite
- Input:
- Output:
- Metric:
- Veto failures:

## retrieval
- Input:
- Output:
- Metric:
- Veto failures:

## reasoning
- Input:
- Output:
- Metric:
- Veto failures:

## summarization
- Input:
- Output:
- Metric:
- Veto failures:

## Cascade Risk Checks
- <how to detect bad retrieval before generation>
- <how to stop if evidence is missing or contradictory>
```

## prompt_short.md

Use for local or weak models with tight context.

```markdown
Task: <one-line task>
Input: <required input>
Output: <strict format>
Must pass: <top metric requirements>
Stop and ask if: <clarification trigger>
Never: <veto failures>
```

## prompt_standard.md

Use for normal weak-model execution.

Use concise task instructions. Include:
- Task signature summary.
- Required inputs.
- Output format.
- Metric and veto failures.
- Search or citation requirement if the topic can change.
- Clarification trigger.
- Any module-specific handoff if the workflow is RAG or Agent-based.

Avoid:
- Generic role-play filler.
- Hidden chain-of-thought requests.
- Unverifiable quality words such as "best" without a metric.
- Asking the weak model to invent missing project facts.

## prompt_strong_generator.md

Use this with a strong model to generate or revise the weak executor prompt.

```markdown
You are the prompt generator for this engineering workflow.

Inputs:
- Meta-prompt:
<paste meta_prompt.md>
- Task signature:
<paste task_signature.md>
- Metric:
<paste metric.md>
- Golden input/output seeds:
<paste 3-10 examples>
- Model target:
<weak/local model constraints>

Generate:
1. A short weak-model prompt.
2. A standard weak-model prompt.
3. A judge prompt.
4. A breakpoint plan.
5. A decision trace summary listing key judgments, evidence, tradeoffs, and rejected options.

For each prompt section, state which metric dimension it serves. Do not merely polish wording.
Do not include hidden chain-of-thought.
```

## Judge Prompt

```markdown
Evaluate the candidate output against the metric below.

Return:
1. Score table by dimension.
2. Any veto failure.
3. The top 3 concrete defects.
4. A corrected output if the candidate fails.

Metric:
<paste metric>

Task signature:
<paste signature>

Candidate output:
<paste output>
```

## breakpoint_plan.md

```markdown
# Breakpoint Plan

## 1. Clarification
- Goal:
- Prompt:
- Stop condition:

## 2. Retrieval or Context Collection
- Goal:
- Prompt:
- Stop condition:

## 3. Analysis
- Goal:
- Prompt:
- Stop condition:

## 4. Generation
- Goal:
- Prompt:
- Stop condition:

## 5. Review
- Goal:
- Prompt:
- Stop condition:
```

## decision_trace_summary.md

```markdown
# Decision Trace Summary

## Key Judgments
- <judgment and why it matters>

## Evidence Used
- <source, golden case, metric, memory, or user answer>

## Tradeoffs
- <chosen tradeoff and consequence>

## Rejected Options
- <option rejected and concrete reason>

## Remaining Uncertainty
- <what still needs testing or confirmation>
```
