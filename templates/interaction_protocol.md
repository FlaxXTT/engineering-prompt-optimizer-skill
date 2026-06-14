# OPRP Interaction Protocol

## Invocation Protocol

The session starts only when the user provides:

```text
[执行轮次][2-5个领域关键词][用户口语化初始提示词]
```

Validation:

- `N` must be an integer.
- `N >= 4`.
- domain keywords must contain 2-5 items.
- the initial prompt must be non-empty.

If invalid, output only `templates/invocation_error.md`.

## User Reply Types

```text
[继续] 没有新资料，按现有信息继续。
[补料] 提供一个或多个 Material Capsule。
[修正] 修改上一轮误解或错误。
[约束] 增加硬约束。
[示例] 提供正例、反例或 few-shot 示例。
[停止] 提前结束并输出当前最优版本。
```

## State Machine

1. `WAIT_INVOCATION`
2. `INIT_SESSION`
3. `ROUND_PLAN`
4. `MATERIAL_INTAKE`
5. `TARGETED_READING`
6. `EVALUATE`
7. `REWRITE`
8. `ASK_FOR_MATERIAL`
9. `FINAL_SYNTHESIS`

## Per-round Output Template

````markdown
## 第 X / N 轮 · 角色：{本轮角色/视角}

### 0. 本轮资料读取计划
- 已登记资料胶囊：
- 本轮读取 Info Header：
- 本轮读取 Raw Material：
- 本轮未读取但保留索引的资料：
- 读取理由：
- 待核验信息：

### 1. 本轮角色
（本轮模型扮演什么审查角色，为什么这个角度此刻重要。本轮只重点检查什么，不重点检查什么。）

### 2. 当前提示词版本 vX
（当前版本摘要或全文。）

### 3. 本轮评估
（只按本轮角度给出具体、可操作的缺陷；编号列出，不允许泛泛而谈。）

### 4. 缺失资料与约束
（明确还缺哪些资料、文件、约束、示例、禁忌、输出格式、评价标准。）

### 5. 建议补充的 Material Capsule
请优先按下面格式补料：

```markdown
# Material Capsule: {资料标题}

## Info Header
- id: MC-XXX
- type:
- source:
- reliability:
- freshness:
- relevance:
- status:
- summary:
- answers:
  -
- key_terms:
  -
- constraints:
  -
- conflicts:
  -
- read_when:
  -
- do_not_use_for:
  -
- token_budget:

## Raw Material
```

### 6. 重写后的提示词 v(X+1)

（基于现有信息，给出更强版本；必须逐步强化 DSPy Signature / Module / Metric / Loop。）

### 7. 变更日志

| Change | Reason | Related Defect | Evidence / Assumption |
| ------ | ------ | -------------- | --------------------- |

### 8. Todo-list

* 已解决：
* 未解决：
* 阻塞：
* 下一轮重点：

### 9. 下一步

请用 `[补料]`、`[修正]`、`[约束]`、`[示例]`、`[继续]` 或 `[停止]` 回复。

→ 收到你的回复后，进入第 X+1 轮。
````

## No New Material Notice

If the user provides no new information, include:

```markdown
本轮缺少外部信息，以下优化基于假设。假设已记录进 context.md，并会在最终提示词中标注为“待核验”或“需用户确认”。
```

## Round-ending Reply Guide

```markdown
你可以用以下任一方式回复：

1. `[补料]` + 一个或多个 Material Capsule  
   用于提供新资料、约束、参考、样例、评价标准。

2. `[修正]` + 你要纠正的地方  
   用于纠正我对任务、资料或目标的误解。

3. `[约束]` + 新增硬约束  
   用于添加必须遵守的规则，例如格式、篇幅、工具、禁止事项。

4. `[示例]` + 正例/反例  
   用于提供 few-shot 示例或你不想要的输出样式。

5. `[继续]`  
   没有新资料，按现有信息继续下一轮。我会明确记录“本轮基于假设继续”。

6. `[停止]`  
   提前结束，并输出当前最优提示词版本。
```

## Early Stop

If the user replies `[停止]`, produce the best current prompt version using the final prompt template. Mark missing information as `需用户确认` and unsupported facts as `待核验`.

