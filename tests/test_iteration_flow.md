# Test: Iteration Flow

Self-test input:

```text
[6][客服, 退款, 工单][帮我写个能自动处理退款工单的提示词]
```

## Expected parse

- `round_total`: 6
- `domain_keywords`: 客服, 退款, 工单
- `prompt_v0`: 帮我写个能自动处理退款工单的提示词

## Expected round plan

1. 需求理解与缺口扫描
2. 逻辑漏洞审查
3. 事实准确性与外部资料风险审查
4. 结构与语气 / 执行稳定性优化 + 长任务不中断机制
5. DSPy 范式重构 + 复杂任务组件化
6. 最终合成与交付

## Expected first round

The first round must:

- state no Material Capsules exist yet;
- identify missing refund policy, ticket fields, risk rules, output format, examples, and metric;
- produce `prompt_v1` with an initial DSPy Signature draft;
- ask for Material Capsules.

## User补料 example

Use `examples/material_capsule_example.md` as `MC-001`.

## Expected second round

The second round must:

- read `MC-001` Info Header;
- read `MC-001` Raw Material only because it resolves the logic conflict around "automatic handling";
- update Todo-list;
- update evidence_map for "only suggestions, no real refund action".

