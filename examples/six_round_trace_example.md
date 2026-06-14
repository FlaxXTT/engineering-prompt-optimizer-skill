# Six-round Self-test Trace

Self-test input:

```text
[6][客服, 退款, 工单][帮我写个能自动处理退款工单的提示词]
```

## 1. 三括号解析结果

- `round_total`: 6
- `domain_keywords`: 客服, 退款, 工单
- `prompt_v0`: 帮我写个能自动处理退款工单的提示词
- validation: pass

## 2. 轮次规划

1. 需求理解与缺口扫描
2. 逻辑漏洞审查
3. 事实准确性与外部资料风险审查
4. 结构与语气 / 执行稳定性优化 + 长任务不中断机制
5. DSPy 范式重构 + 复杂任务组件化
6. 最终合成与交付

## 3. 第 1 轮输出片段

```markdown
## 第 1 / 6 轮 · 角色：需求理解与缺口扫描

### 0. 本轮资料读取计划
- 已登记资料胶囊：无
- 本轮读取 Info Header：无
- 本轮读取 Raw Material：无
- 本轮未读取但保留索引的资料：无
- 读取理由：用户尚未提供资料，本轮只能从 prompt_v0 做需求归纳。
- 待核验信息：真实退款政策、工单字段、风险规则、人工复核边界、输出格式。

### 1. 本轮角色
本轮只确认任务边界、输入输出、执行对象和缺失信息，不做最终提示词定稿。

### 2. 当前提示词版本 v0
帮我写个能自动处理退款工单的提示词

### 3. 本轮评估
1. “自动处理”含义不清：可能是分类、建议回复、审批建议或真实退款动作。
2. 没有工单字段：无法判断模型可用输入。
3. 没有退款政策：模型会编造业务规则。
4. 没有风险边界：高金额、异常账号、资料缺失等场景无法处理。
5. 没有评价标准：无法判断提示词是否合格。
```

## 4. 一个示例 Material Capsule

```markdown
# Material Capsule: 退款政策草案

## Info Header
- id: MC-001
- type: constraints
- source: 用户本人
- reliability: medium
- freshness: 2026-06-13
- relevance: high
- status: tentative
- summary: 描述退款工单的基础判断规则、自动建议范围和人工复核边界。
- answers:
  - 什么工单可以建议通过退款？
  - 什么工单必须转人工？
- key_terms:
  - 自动建议
  - 人工复核
  - 高金额订单
- constraints:
  - 模型只能输出建议，不能声称已真实退款。
- conflicts:
  - 无
- read_when:
  - 事实风险审查、Metric 设计、最终规则写入时读取。
- do_not_use_for:
  - 不用于执行真实财务退款。
- token_budget: small

## Raw Material
购买 7 天内且未使用的订单，可以建议通过退款；超过 7 天、已经使用、订单金额超过 500 元、异常账号、或资料不完整时，必须转人工复核。模型只能输出建议、理由、缺失字段和下一步动作。
```

## 5. 第 2 轮如何按需读取 Raw

Round 2 is `逻辑漏洞审查`, so it reads:

- Info Header: `MC-001`
- Raw Material: only the policy rule paragraph, because logic defects depend on whether "automatic handling" means real action or recommendation.

It does not read unrelated raw material, if present. Example note:

```markdown
- 本轮读取 Raw Material：MC-001，因为本轮要修复“自动处理”与“真实退款动作”之间的逻辑冲突。
- 本轮未读取但保留索引的资料：MC-002 工单字段样例，因本轮不是字段覆盖率审查。
```

## 6. Todo-list 更新示例

```markdown
## Done
- 已确认模型只能输出退款处理建议，不能执行真实退款。
- 已把“人工复核”加入硬约束。

## Doing
- 第 2 轮逻辑漏洞审查。

## Blocked
- 缺少真实工单字段。
- 缺少客服回复语气规范。
- 缺少验收样例。

## Next
- 要求用户提供 MC-002 工单字段说明和 MC-003 正反例工单。
```

## 7. evidence_map 记录示例

| Claim / Constraint / Design Decision | Source Material ID | Evidence Type | Confidence | Verification Status | Notes |
|---|---|---|---|---|---|
| 模型只能输出退款建议，不能声称已真实退款 | MC-001 | 用户约束 | medium | needs_verification | 来自用户草案，最终仍需业务方确认 |
| 超过 7 天、已使用、高金额或资料不完整需人工复核 | MC-001 | 业务规则 | medium | needs_verification | 未提供正式政策文档 |

