---
name: oprp-prompt-optimizer
description: 把用户简陋的口语化提示词，通过多轮“生成→评估→补料→重写”的 OPRO/Self-Refine 自迭代循环，编译成 DSPy 范式（Signature/Module/Metric/Loop/Few-shot）的强提示词，目标是让大模型能长时间自主、分阶段、尽量不中断地工作。只要用户想优化/打磨/重写提示词、想要能驱动长任务或复杂任务的 prompt、提到 DSPy 或提示词工程、或给出一个粗糙 prompt 想让它“变强”，就使用本 Skill——即便用户没明说“优化提示词”或“DSPy”。
---

# 工程化提示词优化

## Purpose

Use this skill to run an Optimization-oriented Prompt Refinement Pipeline, abbreviated OPRP. Turn a rough, conversational, incomplete prompt into a robust DSPy-style prompt architecture for complex and long-running LLM work.

The skill is a multi-round workflow, not a one-shot prompt rewriter. Each round performs role-specific evaluation, targeted material reading, rewrite, version logging, Todo updates, and asks the user for structured material.

## When to use

Use this skill when the user wants to optimize, harden, rewrite, critique, or generate prompts for complex tasks, including thesis writing, literature reviews, Codex development workflows, multi-file programming, data analysis, report generation, architecture design, RAG, agent loops, long document generation, or any prompt meant to drive long-running work.

Also use it when the user provides a rough prompt and asks to make it stronger, even if they do not mention DSPy, OPRO, Self-Refine, or prompt engineering.

## Honest scope

- Do not claim the conversation is actually running the DSPy compiler. Real DSPy compilation requires the `dspy` package, callable LMs, labeled data, metrics, and repeated model calls.
- Position OPRP as a same-model, multi-role optimization loop that simulates compile-like refinement: generate, evaluate, request materials, rewrite, stress test, and synthesize.
- You may optionally output a runnable `dspy` Python skeleton. State that the user must install `dspy`, configure an LM, prepare train/dev data, and implement metrics before real compilation.
- Do not promise the resulting prompt will absolutely never interrupt. Instead design mechanisms that reduce interruption risk: Todo-list, checkpoints, context compression, resumable logs, evidence maps, failure recovery, and stop conditions.

## Invocation format

The first valid user input must contain exactly three top-level bracket groups:

```text
[执行轮次][2-5个领域关键词][用户口语化初始提示词]
```

Example:

```text
[8][复杂编程, Codex, 自动化测试][我想让 Codex 帮我重构一个 Python 项目，要求能自动读文件、发现问题、修复代码、跑测试并给报告。]
```

If the current user message does not satisfy this contract and no OPRP session is already active, output only the content of `templates/invocation_error.md` and stop.

## Input validation

Parse only top-level bracket groups. Treat nested brackets inside the third group as part of the prompt only if the three top-level groups are still unambiguous.

Validation rules:

- Group 1 is `N`, the total round count. It must be an integer and `N >= 4`. Recommend 6-12.
- Group 2 is the domain keyword list. Split by Chinese comma, English comma, ideographic comma, semicolon, or Chinese semicolon. Require 2-5 non-empty keywords.
- Group 3 is `prompt_v0`. It must be non-empty after trimming whitespace.
- On any validation failure, output only `templates/invocation_error.md`.

## State machine

Run the workflow as an explicit state machine:

1. `WAIT_INVOCATION`: wait for the three-bracket invocation and validate it.
2. `INIT_SESSION`: parse `N`, keywords, and `prompt_v0`; create initial context files; generate the round plan; state the honest DSPy boundary.
3. `ROUND_PLAN`: select the current role and define what this round will and will not inspect.
4. `MATERIAL_INTAKE`: classify user replies as `[补料]`, `[修正]`, `[约束]`, `[示例]`, `[继续]`, or `[停止]`; extract Material Capsule Info Headers.
5. `TARGETED_READING`: read Info Headers first; read Raw Material only when the current role needs it.
6. `EVALUATE`: evaluate the current prompt version from this round's role only.
7. `REWRITE`: rewrite the prompt while strengthening Signature, Modules, Metric, Loop, Demonstrations, Search, and Predict.
8. `ASK_FOR_MATERIAL`: ask for the next Material Capsules or confirmation to continue.
9. `FINAL_SYNTHESIS`: produce the final optimized prompt, evidence summary, and optional DSPy Python skeleton.

Read `templates/interaction_protocol.md` when executing or explaining the full interaction protocol.

## Workflow

1. Validate invocation. If invalid, output only `templates/invocation_error.md`.
2. Initialize `context.md`, `context_index.md`, `evidence_map.md`, `prompt_versions.md`, and `todo.md` conceptually or as files when the user asks for file artifacts.
3. Build the round plan from `N`.
4. Round 1 always performs requirement understanding and gap scanning.
5. Every non-final round ends by asking the user to reply with `[补料]`, `[修正]`, `[约束]`, `[示例]`, `[继续]`, or `[停止]`.
6. If the user replies `[继续]`, continue from assumptions and clearly record that external information is missing.
7. If the user replies `[停止]`, synthesize the best current prompt and mark unresolved assumptions.
8. The final round outputs the final prompt using `templates/final_prompt_template.md`.

## Round planning algorithm

Fixed rules:

- `N >= 4`.
- Round 1 is always `需求理解与缺口扫描`.
- Round `N` is always `最终合成与交付`.
- Middle rounds must cover all six core perspectives. If rounds are too few, merge core perspectives.
- Do not repeat the same pure perspective in consecutive rounds.

Core perspectives:

1. `逻辑漏洞审查`
2. `事实准确性与外部资料风险审查`
3. `结构与语气 / 执行稳定性优化`
4. `DSPy 范式重构`
5. `复杂任务组件化`
6. `长任务不中断机制`

Extended perspectives:

7. `反例 / 压力测试`
8. `抗提示注入与歧义鲁棒性`
9. `指标 / Rubric 对齐与自检`
10. `Few-shot 示例质量与精简`
11. `文件工作流与上下文治理`
12. `用户交互 UX 优化`
13. `输出可复用性与迁移性`
14. `自动化测试与验收标准`

Plans:

- `N = 4`: requirement scan; logic + fact + stability; DSPy + componentization + long-task mechanism; final synthesis.
- `N = 5`: requirement scan; logic + fact; stability + long-task mechanism; DSPy + componentization; final synthesis.
- `N = 6`: requirement scan; logic; fact; stability + long-task mechanism; DSPy + componentization; final synthesis.
- `N >= 7`: requirement scan; schedule core perspectives first, merging only if needed; add extended perspectives with remaining slots; final synthesis.

## Round roles

Use these role objectives:

- `需求理解与缺口扫描`: identify user goal, target executor, artifact, inputs, outputs, success criteria, missing data, and initial Signature.
- `逻辑漏洞审查`: find input-output mismatch, conflicts, circular dependencies, missing data sources, absent metrics, and mixed generation/evaluation/repair concerns.
- `事实准确性与外部资料风险审查`: separate model-knowledge facts from user-provided facts, flag unverified facts, conflicts, low-reliability material, and browsing needs.
- `结构与语气 / 执行稳定性优化`: add phases, checkpoints, Todo-list, recovery, file rules, output contracts, context compression, and stop conditions.
- `DSPy 范式重构`: express the prompt as Signature, Modules, Metric, Compiler-like Loop, Demonstrations, Search, and Predict.
- `复杂任务组件化`: require 3-5 independent components with goals, inputs, outputs, dependencies, risks, and acceptance tests.
- `长任务不中断机制`: add progress summaries, intermediate artifacts, assumption logs, uncertainty logs, resumability, failure recovery, and final review checklist.

## Material Capsule protocol

Require user materials to be provided as Material Capsules with an Info Header and Raw Material. Read `templates/material_capsule_template.md` whenever asking the user to provide material.

Every Material Capsule must include:

- `id`, `type`, `source`, `reliability`, `freshness`, `relevance`, `status`
- `summary`, `answers`, `key_terms`, `constraints`, `conflicts`
- `read_when`, `do_not_use_for`, `token_budget`
- `Raw Material`

If the user provides unstructured material, do not silently absorb all of it. Ask them to convert it into one or more Material Capsules, or convert only a small clearly bounded excerpt and mark the rest as not indexed.

## Targeted raw reading

Follow this policy every round:

1. Read all relevant Info Headers first.
2. Decide which capsules are relevant to the current role and current defect list.
3. Read only the Raw Material needed for the current round.
4. If raw is too long, ask the user to split it or identify sections.
5. In the round output, explicitly report:
   - capsules registered;
   - Info Headers read;
   - Raw Material read;
   - indexed capsules whose raw was not read;
   - reading rationale;
   - facts still requiring verification.
6. Never dump all raw material into the final prompt. Preserve traceability through `context_index.md` and `evidence_map.md`.

External-fact policy:

- Default to no browsing or minimal browsing.
- Prefer user-provided sources packaged as Material Capsules.
- Browse only when the task requires current facts, the user asks for verification, or system policy requires it; cite sources when browsing is used.
- Mark unsupported facts as `待核验` and missing user decisions as `需用户确认`.

## Context files

Maintain these conceptual files during the session. If asked to write artifacts, use the templates in `templates/`.

- `context.md`: stable user goal, current prompt version, confirmed constraints, assumptions, decisions, risks, and round log.
- `context_index.md`: Info Header table, keyword index, question-to-material map, and material priority. Do not store full raw here.
- `evidence_map.md`: map claims, constraints, and design decisions to material IDs, confidence, and verification status.
- `prompt_versions.md`: preserve `prompt_v0`, `prompt_v1`, and every later version.
- `todo.md`: track Done, Doing, Blocked, and Next across rounds.

Read the corresponding templates before creating these files.

## DSPy-style optimization

The final prompt must include real DSPy-style structure, not decorative naming:

- `Signature`: input and output fields with meanings and constraints.
- `Modules`: submodules such as IntakeAnalyzer, ContextIndexer, GapEvaluator, PromptGenerator, StressTester, and FinalSynthesizer.
- `Metric`: score dimensions, weights or priority, veto failures, evidence requirements, and scoring method.
- `Compiler-like Optimization Loop`: same-model role cycling that simulates generate-evaluate-rewrite.
- `Demonstrations`: few-shot examples or sources for positive and negative examples.
- `Search Strategy`: how candidate prompt variants are generated and compared.
- `Predict Strategy`: how the final prompt should be used to execute the target task.

For optional real DSPy code, read `templates/dspy_python_skeleton.md` and keep the honest disclaimer.

## Component decomposition

Force the final prompt to decompose any complex task into 3-5 independent components. Each component must define:

- name and goal;
- inputs and outputs;
- independent steps;
- dependencies;
- downstream outputs;
- failure risks;
- acceptance criteria.

Then require a synthesis stage that combines component outputs and checks the system-level contract.

## Todo-list mechanism

Each round must update a Todo-list:

- Done: resolved defects or confirmed materials.
- Doing: current round focus.
- Blocked: missing material, unresolved conflicts, unverified facts.
- Next: next role, requested capsules, and decision points.

The final prompt must require the executor model to maintain this Todo-list during long-running work.

## Long-running task stability

Add mechanisms that reduce interruption risk:

- phase checkpoints;
- progress summaries;
- intermediate artifacts;
- assumption and uncertainty logs;
- file naming rules;
- context compression;
- breakpoint resume protocol;
- failure recovery strategy;
- explicit stop conditions;
- final review checklist.

Always phrase this as risk reduction, never as an absolute guarantee.

## Final output format

On the final round, output the structure from `templates/final_prompt_template.md`. Include the optional `dspy` skeleton only if the user asks for code or if it is useful for the target workflow. If included, keep the disclaimer that no real DSPy compiler has been run in the chat.

## Legacy prompt-package resources

The previous `engineering-prompt-optimizer` assets are migrated here for compatibility:

- Read `references/output-templates.md` when the user asks for the older prompt-package file set, such as `task_signature.md`, `metric.md`, `golden_cases.md`, `prompt_short.md`, or `prompt_standard.md`.
- Read `references/rubric-guide.md` when designing detailed metrics, veto failures, or golden cases.
- Read `references/modular-rag-agent.md` when optimizing RAG, retrieval, tool, agent-loop, or external-evidence workflows.
- Read `references/local-model-strategy.md` when the user mentions privacy, offline use, local models, weak models, context limits, inference cost, or short prompts.
- Optionally run `scripts/check_prompt_package.py <package-dir>` when validating an older prompt package directory.

## Failure modes

Stop or ask for correction when:

- invocation format is invalid;
- `N < 4`;
- keyword count is outside 2-5;
- `prompt_v0` is empty;
- the user asks for external facts but provides no source and browsing is unavailable or inappropriate;
- the user provides huge raw material without Info Headers;
- material conflicts cannot be resolved;
- the user asks for a one-shot final prompt before enough rounds but does not use `[停止]`.

Mark unsupported facts as `待核验` and user-missing decisions as `需用户确认`.

## Examples

Read only the example relevant to the user's domain:

- `examples/basic_invocation.md`
- `examples/codex_workflow_example.md`
- `examples/academic_writing_example.md`
- `examples/complex_programming_example.md`
- `examples/material_capsule_example.md`
- `examples/six_round_trace_example.md`
