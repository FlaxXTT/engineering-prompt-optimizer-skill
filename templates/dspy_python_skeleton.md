这不是 Skill 对话中自动运行的 DSPy 编译器。它只是把最终提示词中的 Signature / Module / Metric / Loop 映射成可运行的 dspy 程序骨架。用户需要自行安装 dspy、配置 LM、准备数据集和 metric。

```python
import dspy


class PromptOptimizationSignature(dspy.Signature):
    """Optimize a rough prompt into a robust DSPy-style prompt package."""

    domain_keywords = dspy.InputField(desc="2-5 domain keywords")
    rough_prompt = dspy.InputField(desc="The user's initial conversational prompt")
    material_index = dspy.InputField(desc="Material Capsule Info Headers and evidence map")
    constraints = dspy.InputField(desc="Confirmed hard constraints and unresolved assumptions")

    optimized_prompt = dspy.OutputField(desc="Final optimized prompt")
    rubric_report = dspy.OutputField(desc="Scores, veto failures, and improvement notes")


class PromptOptimizationModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.analyze = dspy.ChainOfThought(PromptOptimizationSignature)

    def forward(self, domain_keywords, rough_prompt, material_index, constraints):
        return self.analyze(
            domain_keywords=domain_keywords,
            rough_prompt=rough_prompt,
            material_index=material_index,
            constraints=constraints,
        )


def metric(example, pred, trace=None):
    text = pred.optimized_prompt or ""
    required = [
        "DSPy Signature",
        "DSPy Modules",
        "Metric",
        "Iterative Optimization Loop",
        "Material Capsule",
        "Todo-list",
        "诚实边界",
    ]
    coverage = sum(1 for item in required if item in text) / len(required)
    no_false_claim = "已经真实运行 DSPy 编译器" not in text
    return coverage >= 0.85 and no_false_claim


trainset = [
    dspy.Example(
        domain_keywords="客服, 退款, 工单",
        rough_prompt="帮我写个能自动处理退款工单的提示词",
        material_index="MC-001: 退款政策; MC-002: 工单字段说明",
        constraints="不能承诺自动退款；需要人工复核高风险工单。",
        optimized_prompt="包含 Signature / Modules / Metric / Loop 的强提示词",
        rubric_report="通过核心结构检查",
    ).with_inputs("domain_keywords", "rough_prompt", "material_index", "constraints")
]


student = PromptOptimizationModule()

# Choose one optimizer after installing and configuring DSPy.
optimizer = dspy.BootstrapFewShot(metric=metric)
# optimizer = dspy.MIPROv2(metric=metric, auto="light")

compiled = optimizer.compile(student, trainset=trainset)

prediction = compiled(
    domain_keywords="客服, 退款, 工单",
    rough_prompt="帮我写个能自动处理退款工单的提示词",
    material_index="MC-001: 退款政策 Info Header",
    constraints="缺失真实政策时标注待核验。",
)

print(prediction.optimized_prompt)
```

