# Codex Workflow Example

## Invocation

```text
[8][复杂编程, Codex, 自动化测试][我想让 Codex 帮我重构一个 Python 项目，要求能自动读文件、发现问题、修复代码、跑测试并给报告。]
```

## Early requirement scan

The first round should identify missing details:

- repository type and language versions;
- test command and expected pass criteria;
- protected files or areas that must not be edited;
- coding standards and formatting tools;
- desired final report format;
- permission policy for dependency installation and network access.

## Suggested Material Capsules

- `MC-001`: repository structure and key files.
- `MC-002`: test commands and known failures.
- `MC-003`: refactor constraints and no-touch zones.
- `MC-004`: desired report format.

## Prompt architecture direction

The final prompt should define components such as:

- RepositoryIntake
- FailureScanner
- PatchPlanner
- TestRunner
- ReportSynthesizer

