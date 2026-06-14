# 最终优化提示词

## 1. 使用场景

## 2. 角色设定

## 3. 输入材料

### 3.1 必需材料

### 3.2 可选材料

### 3.3 Material Capsule 资料组织方式

## 4. 总目标

## 5. DSPy Signature

### Input Fields

### Output Fields

## 6. DSPy Modules

### Module 1: IntakeAnalyzer

### Module 2: ContextIndexer

### Module 3: GapEvaluator

### Module 4: PromptGenerator

### Module 5: StressTester

### Module 6: FinalSynthesizer

## 7. Metric / Rubric

## 8. Iterative Optimization Loop

## 9. 资料读取策略

### 9.1 先读 Info Header

### 9.2 按需读取 Raw Material

### 9.3 证据映射

### 9.4 待核验标注

## 10. 组件化执行架构（3–5 个独立组件）

### Component A

### Component B

### Component C

### Component D / Optional

### Component E / Optional

## 11. 组件依赖关系

### 11.1 依赖图

### 11.2 接缝处的数据契约

### 11.3 合成输出机制

## 12. Todo-list 工作制度

## 13. 长任务稳定执行机制

### 13.1 阶段检查点

### 13.2 进度摘要

### 13.3 中间产物保存

### 13.4 上下文压缩

### 13.5 失败恢复

### 13.6 断点续跑

### 13.7 停止条件

## 14. 文件与资料处理规范

## 15. 缺失信息处理机制

## 16. 最终输出要求

## 17. 自检清单

## 18. 禁止事项

## 19. 诚实边界

- 不声称已经真实运行 DSPy 编译器。
- 不承诺绝对永不中断。
- 对没有来源的事实标注“待核验”。
- 对用户未提供的信息标注“需用户确认”。

## （可选）20. 可运行的 dspy 程序骨架

说明：这不是本对话中自动运行的 DSPy 编译器，而是把上面的 Signature / Module / Metric / Loop 映射成可运行程序。需要用户本地安装 dspy、配置 LM、准备数据集和 metric 后运行。

