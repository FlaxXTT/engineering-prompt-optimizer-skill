# Complex Programming Example

## Invocation

```text
[9][复杂编程, 多文件项目, 断点续跑][帮我写一个提示词，让模型能长期维护一个老项目，自己读代码、修 bug、补测试、整理报告。]
```

## Round priorities

- Round 1: discover repo boundaries, tools, test strategy, acceptance criteria.
- Logic round: separate scanning, planning, editing, testing, and reporting.
- Fact-risk round: mark unknown dependencies, runtime versions, and external APIs as `待核验`.
- Stability round: require checkpoints after file reads, patch plan, test runs, and report synthesis.
- DSPy round: express modules and metric.
- Component round: define 3-5 isolated components.
- Stress-test round: simulate failing tests, flaky tests, missing dependencies, and conflicting user instructions.

## Final prompt must include

- Todo-list workflow.
- File read/write rules.
- Patch safety rules.
- Test command discovery.
- Evidence map from code and logs to conclusions.
- Stop conditions for ambiguous destructive actions.

