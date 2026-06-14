# Test: Input Parsing

## Valid three-bracket input

Input:

```text
[6][客服, 退款, 工单][帮我写个能自动处理退款工单的提示词]
```

Expected:

- parse three top-level groups;
- `N = 6`;
- keywords = `客服`, `退款`, `工单`;
- `prompt_v0` non-empty;
- enter `INIT_SESSION`.

## Missing round count

Input:

```text
[客服, 退款][帮我写提示词]
```

Expected: output only `templates/invocation_error.md`.

## Round count less than 4

Input:

```text
[3][客服, 退款][帮我写提示词]
```

Expected: reject and output only invocation guidance.

## Fewer than 2 keywords

Input:

```text
[6][客服][帮我写提示词]
```

Expected: reject.

## More than 5 keywords

Input:

```text
[6][客服, 退款, 工单, 审批, 风控, 售后][帮我写提示词]
```

Expected: reject.

## Empty initial prompt

Input:

```text
[6][客服, 退款][   ]
```

Expected: reject.

