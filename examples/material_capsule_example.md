# Material Capsule Example

# Material Capsule: 退款政策摘要

## Info Header
- id: MC-001
- type: constraints
- source: 用户本人
- reliability: medium
- freshness: 2026-06-13
- relevance: high
- status: tentative
- summary: 这份资料描述退款工单的基本判断规则。它说明 7 天内未使用订单可自动建议退款，超过 7 天或已使用订单需要人工复核。它还规定高金额订单不能直接自动通过。
- answers:
  - 哪些退款可以建议自动通过？
  - 哪些退款必须人工复核？
- key_terms:
  - 7 天内
  - 已使用订单
  - 高金额订单
- constraints:
  - 高金额订单必须人工复核。
  - 缺少订单状态时不能给出最终退款结论。
- conflicts:
  - 无
- read_when:
  - 在事实风险审查、Metric 设计、最终提示词规则写入时读取 Raw Material。
- do_not_use_for:
  - 不用于生成法律承诺或真实财务退款操作。
- token_budget: small

## Raw Material
退款规则草案：购买 7 天内且未使用的订单，可以建议通过退款；超过 7 天、已经使用、订单金额超过 500 元、用户有异常记录、或资料不完整时，需要转人工复核。模型只能输出处理建议，不能声称已经完成真实退款。

