# Test: Round Planning

## N = 4

Expected:

1. 需求理解与缺口扫描
2. 逻辑漏洞 + 事实风险 + 结构稳定性
3. DSPy 范式 + 组件化 + 长任务机制
4. 最终合成与交付

## N = 5

Expected:

1. 需求理解与缺口扫描
2. 逻辑漏洞 + 事实风险
3. 结构稳定性 + 长任务机制
4. DSPy 范式 + 组件化
5. 最终合成与交付

## N = 6

Expected:

1. 需求理解与缺口扫描
2. 逻辑漏洞
3. 事实风险
4. 结构稳定性 + 长任务机制
5. DSPy 范式 + 组件化
6. 最终合成与交付

## N = 8

Expected:

- round 1 requirement scan;
- round 8 final synthesis;
- all six core perspectives covered;
- one extended perspective may be included or one core perspective may be split;
- no consecutive duplicate pure perspective.

## N = 12

Expected:

- all six core perspectives covered;
- extension perspectives added, such as stress testing, injection robustness, rubric alignment, few-shot quality, file workflow, or UX;
- no consecutive duplicate pure perspective.

## Non-repetition rule

Expected: the planner must not schedule `逻辑漏洞审查` twice in a row as pure roles.

