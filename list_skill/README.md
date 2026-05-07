# Engineering Prompt Optimizer Skill

Verdict: this skill is for people who want prompt systems that can be tested, not decorative prompt wording.

`engineering-prompt-optimizer` turns a rough meta-prompt into an evaluation-first prompt package:

- induced requirements
- task signature
- metric
- golden input/output cases
- RAG or Agent module map
- short, standard, and strong-generator prompt variants
- local-model breakpoint plan
- judge prompt
- decision trace summary

It uses a sharp review style by design. It is blunt about vague requirements, missing metrics, bad architecture assumptions, and no-foundation vibe coding.

## Contents

```text
list_skill/
  README.md
  .gitignore
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

`promptgen-template/` is a sanitized public template. It is not the real local `.promptgen/` memory directory.

## Trigger Conditions

Use this skill when the user asks for:

- prompt optimization, prompt writing, prompt rewriting, prompt scoring, prompt hardening, or prompt generation
- meta-prompt workflows
- Codex, Claude, Cursor, coding agent, RAG, Agent loop, local-model, or weak-model prompt design
- task definition, Metric, golden cases, judge prompt, prompt injection defense, or prompt quality review
- technology stack recommendations inside a prompt workflow
- requirement induction before implementation
- no-foundation vibe coding detection

Do not use it for ordinary coding tasks unless the real task is to design, critique, or evaluate the prompt/workflow that drives the coding task.

## Install

Install a compatible coding agent first:

- Codex: [OpenAI Codex docs](https://platform.openai.com/docs/codex) and [OpenAI Codex CLI](https://github.com/openai/codex)
- Claude Code: [Anthropic Claude Code quickstart](https://docs.anthropic.com/en/docs/claude-code/quickstart)

For Codex:

```powershell
Copy-Item -Path ".\engineering-prompt-optimizer" -Destination "$env:USERPROFILE\.codex\skills\engineering-prompt-optimizer" -Recurse -Force
```

For Claude:

```powershell
Copy-Item -Path ".\engineering-prompt-optimizer" -Destination "$env:USERPROFILE\.claude\skills\engineering-prompt-optimizer" -Recurse -Force
```

Restart the client after installation so the skill list reloads.

## Optional Memory Template

If you want project memory, copy the sanitized template into your own project as `.promptgen/memory/`:

```powershell
New-Item -ItemType Directory -Force ".\.promptgen\memory" | Out-Null
Copy-Item -Path ".\promptgen-template\memory\*" -Destination ".\.promptgen\memory" -Force
```

Do not publish your real `.promptgen/` directory. It is designed to contain local preferences, project facts, examples, and private review history.

## Public Smithery MCP Shortlist

These are optional MCPs. They are public links and safe to document.

- Technology stack web verification: [Exa Search](https://server.smithery.ai/exa)
- Prompt quality scoring: [Prompt Quality Score - PQS](https://server.smithery.ai/onchaintel/pqs)
- Prompt injection detection: [promptscan](https://server.smithery.ai/nicks-brn/promptscan)

The skill does not require these MCPs to run as a Codex or Claude skill. Add them only if you want tool-backed verification, scoring, or injection scanning.

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
