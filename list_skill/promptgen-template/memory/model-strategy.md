# Model Strategy Template

## Default Strategy
- Use the strongest available model as the prompt generator for `meta_prompt + golden examples + metric`.
- Use weaker, cheaper, or local models only after the task signature, metric, prompt variants, and breakpoint plan are stable.
- Use a strong model as judge when evaluating weak-model outputs.
- Provide short, standard, and strong-generator prompt variants when privacy, local models, context limits, or cost are relevant.

## RAG / Agent Strategy
- Split workflows into query rewrite, retrieval, reasoning, and summarization modules.
- Give each module its own inputs, outputs, metric, and veto failures.
- Add cascade checks between modules so bad retrieval or weak evidence does not become a fluent but wrong final answer.

## Public Smithery MCP Shortlist
- Technology stack web verification: Exa Search - https://server.smithery.ai/exa
- Prompt quality scoring: Prompt Quality Score - PQS - https://server.smithery.ai/onchaintel/pqs
- Prompt injection detection: promptscan - https://server.smithery.ai/nicks-brn/promptscan

## Do Not
- Do not ask a weak model to infer missing project requirements.
- Do not accept prompt wording improvements without evidence from metrics or test cases.
- Do not trust current technology recommendations without search or citations.
- Do not request or expose hidden chain-of-thought. Provide a decision trace summary instead.
