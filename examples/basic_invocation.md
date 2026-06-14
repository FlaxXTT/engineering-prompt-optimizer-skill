# Basic Invocation

## Valid input

```text
[6][数据分析, 报告, 图表][帮我写一个提示词，让模型根据 CSV 做分析、画图、解释结果并生成报告。]
```

## Parsed result

- `round_total`: 6
- `domain_keywords`: 数据分析, 报告, 图表
- `prompt_v0`: 帮我写一个提示词，让模型根据 CSV 做分析、画图、解释结果并生成报告。

## Round plan

1. 需求理解与缺口扫描
2. 逻辑漏洞审查
3. 事实准确性与外部资料风险审查
4. 结构与语气 / 执行稳定性优化 + 长任务不中断机制
5. DSPy 范式重构 + 复杂任务组件化
6. 最终合成与交付

## Invalid input examples

```text
[3][数据分析, 报告][帮我优化提示词]
```

Reject because `N < 4`.

```text
[6][数据分析][帮我优化提示词]
```

Reject because keyword count is less than 2.

