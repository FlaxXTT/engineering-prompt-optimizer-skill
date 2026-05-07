# Engineering Prompt Optimizer Skill

Verdict: this skill is for prompt systems that can be tested. It is not for polishing decorative phrases like "act as a professional assistant."

`engineering-prompt-optimizer` turns a rough meta-prompt into an evaluation-first engineering prompt package:

- requirement induction
- task signature
- metric
- golden input/output cases
- RAG or Agent module map
- short, standard, and strong-generator prompt variants
- local-model breakpoint plan
- judge prompt
- decision trace summary

It uses a sharp review style by design. It calls out vague requirements, missing metrics, bad architecture assumptions, token waste, and no-foundation vibe coding.

## Repository Layout

If possible, put this repository's contents at the GitHub repository root:

```text
README.md
.gitignore
LICENSE
engineering-prompt-optimizer/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/check_prompt_package.py
promptgen-template/
  memory/
    profile.md
    rubrics.md
    golden-cases.md
    model-strategy.md
```

If you uploaded an outer `list_skill/` folder, the files still work, but GitHub may not show this README on the repository homepage. Move the contents of `list_skill/` to the repository root for a cleaner release.

`promptgen-template/` is a sanitized public template. It is not the real local `.promptgen/` memory directory.

## Install A Compatible Agent

Install one of these first:

- Codex: [OpenAI Codex docs](https://platform.openai.com/docs/codex) and [OpenAI Codex CLI](https://github.com/openai/codex)
- Claude Code: [Anthropic Claude Code quickstart](https://docs.anthropic.com/en/docs/claude-code/quickstart)

## Install The Skill

### Codex

From the repository root:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Path ".\engineering-prompt-optimizer" -Destination "$env:USERPROFILE\.codex\skills\engineering-prompt-optimizer" -Recurse -Force
```

If your files are still inside an outer `list_skill/` folder:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Path ".\list_skill\engineering-prompt-optimizer" -Destination "$env:USERPROFILE\.codex\skills\engineering-prompt-optimizer" -Recurse -Force
```

### Claude Code

From the repository root:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Path ".\engineering-prompt-optimizer" -Destination "$env:USERPROFILE\.claude\skills\engineering-prompt-optimizer" -Recurse -Force
```

If your files are still inside an outer `list_skill/` folder:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Path ".\list_skill\engineering-prompt-optimizer" -Destination "$env:USERPROFILE\.claude\skills\engineering-prompt-optimizer" -Recurse -Force
```

Restart Codex or Claude Code after installation so the skill list reloads.

## Optional Memory Template

The real `.promptgen/` directory is local memory. Do not publish it.

To create a clean local memory structure in your own project:

```powershell
New-Item -ItemType Directory -Force ".\.promptgen\memory" | Out-Null
Copy-Item -Path ".\promptgen-template\memory\*" -Destination ".\.promptgen\memory" -Force
```

If your files are still inside an outer `list_skill/` folder:

```powershell
New-Item -ItemType Directory -Force ".\.promptgen\memory" | Out-Null
Copy-Item -Path ".\list_skill\promptgen-template\memory\*" -Destination ".\.promptgen\memory" -Force
```

Use `.promptgen/memory/` for local preferences, rubrics, public or redacted golden cases, and model strategy. Do not store credentials, customer data, private logs, or unredacted examples there.

## Usage Modes

### Mode 1: Meta-prompt To Prompt Package

Use this when you only have a rough idea.

Example:

```text
Use engineering-prompt-optimizer.

Meta-prompt:
I want a prompt that helps me choose a tech stack for a small RAG app.

Known constraints:
- I may use local models.
- I care about privacy.
- I want the final prompt to be short enough for a weak model.
```

The skill should first induce the real requirement, ask blocking questions if needed, then produce a task signature, metric, golden cases, prompt variants, judge prompt, and breakpoint plan.

### Mode 2: Prompt Review And Failure Diagnosis

Use this when you already wrote a prompt and want it judged harshly.

Example:

```text
Use engineering-prompt-optimizer to review this prompt.

Prompt:
<paste prompt>

Goal:
<what the prompt should accomplish>

Golden examples:
<optional input/output examples>
```

The skill should start with a blunt verdict, name the broken parts, explain how they fail, then provide a fix or a stop condition.

### Mode 3: RAG / Agent Workflow Design

Use this when the prompt controls retrieval, tools, memory, citations, or multi-step agent loops.

The skill must split the system into:

- `query_rewrite`
- `retrieval`
- `reasoning`
- `summarization`

Each module needs inputs, outputs, metrics, and veto failures. This prevents bad retrieval from becoming a fluent but wrong final answer.

### Mode 4: Local Or Weak Model Execution

Use this when privacy, offline execution, cost, or context length matters.

The skill should produce:

- `prompt_short.md`
- `prompt_standard.md`
- `prompt_strong_generator.md`
- `breakpoint_plan.md`
- `decision_trace_summary.md`

Long workflows should be split into clarification, retrieval/context collection, analysis, generation, and review.

## Use Flow

1. Start with a rough meta-prompt or an existing prompt.
2. Add 3 to 10 golden input/output examples if you have them.
3. Let the skill induce the real requirement and ask blocking questions.
4. Confirm or correct the requirement summary.
5. Generate the task signature and metric.
6. Draft at least 10 golden cases; expand to 50 before production use.
7. Generate short, standard, and strong-generator prompt variants.
8. For RAG or Agent workflows, generate the module map.
9. Use the judge prompt to score weak-model outputs.
10. Update local `.promptgen/memory/` only with non-sensitive, reusable knowledge.

## Trigger Conditions

Use this skill when the user asks for:

- prompt optimization, writing, rewriting, scoring, hardening, or generation
- meta-prompt workflows
- Codex, Claude, Cursor, coding agent, RAG, Agent loop, local-model, or weak-model prompt design
- task definition, Metric, golden cases, judge prompt, prompt injection defense, or prompt quality review
- technology stack recommendations inside a prompt workflow
- requirement induction before implementation
- no-foundation vibe coding detection

Do not use it for ordinary coding tasks unless the real task is to design, critique, or evaluate the prompt/workflow that drives the coding task.

## Optional Smithery MCP Links

These MCPs are optional. The skill works without them, but they are useful when you want tool-backed verification, scoring, or injection scanning.

- Technology stack web verification: [Exa Search](https://server.smithery.ai/exa)
- Prompt quality scoring: [Prompt Quality Score - PQS](https://server.smithery.ai/onchaintel/pqs)
- Prompt injection detection: [promptscan](https://server.smithery.ai/nicks-brn/promptscan)

Smithery CLI:

- [Smithery](https://smithery.ai)

Typical discovery flow:

```powershell
smithery mcp search "web search"
smithery mcp search "prompt evaluation"
smithery mcp search "prompt injection"
```

## Validate

Validate the skill structure:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\engineering-prompt-optimizer"
```

Validate a generated prompt package:

```powershell
python -B ".\engineering-prompt-optimizer\scripts\check_prompt_package.py" ".\path\to\prompt-package"
```

The package checker expects at least:

- `task_signature.md`
- `metric.md`
- `golden_cases.md`

For RAG or Agent packages, it also expects `module_map.md` with module-level metrics.

## Privacy Notes

Before uploading, keep these out of the repository:

- real `.promptgen/`
- `.env`
- API keys, tokens, credentials, and private keys
- `__pycache__/`
- `*.pyc`
- local app session folders

This upload bundle intentionally contains only the skill package, public templates, and public documentation.
