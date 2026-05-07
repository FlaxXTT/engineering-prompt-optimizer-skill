# Modular RAG and Agent Guide

Use this reference when a prompt package controls a RAG system, retrieval workflow, tool-using agent, multi-step planner, or evidence-grounded answerer.

## Why Split Modules

RAG and Agent failures cascade. Bad query rewriting causes bad retrieval. Bad retrieval causes bad reasoning. Bad reasoning creates confident summaries from weak evidence. The final answer alone is too late to catch the error.

## Required Modules

### query_rewrite

Purpose: turn the user's raw request into precise retrieval or tool queries.

Define:
- Inputs: raw user request, known constraints, memory.
- Outputs: normalized intent, query variants, excluded meanings.
- Metric: preserves user intent, removes ambiguity, includes key entities.
- Veto failures: changes the task, drops constraints, invents entities.

### retrieval

Purpose: fetch or select evidence.

Define:
- Inputs: rewritten queries, source list, filters.
- Outputs: ranked evidence, source metadata, missing-evidence flags.
- Metric: relevance, freshness, authority, coverage, diversity.
- Veto failures: no citations when required, stale or irrelevant evidence, hidden source gaps.

### reasoning

Purpose: align evidence to claims and detect conflicts.

Define:
- Inputs: evidence set, task signature, metric.
- Outputs: supported claims, unsupported claims, conflicts, confidence.
- Metric: evidence-to-claim alignment, contradiction handling, explicit uncertainty.
- Veto failures: unsupported claim, causal overreach, ignores contradictory evidence.

### summarization

Purpose: produce the user-facing answer or artifact.

Define:
- Inputs: supported claims, output format, audience.
- Outputs: final answer, citations, caveats, next actions.
- Metric: correctness, completeness, usability, citation quality.
- Veto failures: hides uncertainty, omits required format, cites sources not used.

## Cascade Checks

Add a check between modules:
- After query rewrite: ask whether the rewritten query still matches the user's intent.
- After retrieval: stop if evidence is missing, stale, or off-topic.
- After reasoning: list unsupported claims before summarization.
- After summarization: judge against the metric and veto failures.

## Golden Cases For RAG / Agent

Include cases for:
- Ambiguous query needing rewrite.
- Good query but poor retrieval.
- Conflicting sources.
- Missing evidence requiring refusal or caveat.
- Tool error or timeout.
- Final answer that sounds fluent but is unsupported.
