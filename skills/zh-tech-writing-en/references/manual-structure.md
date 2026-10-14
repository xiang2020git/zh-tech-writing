# Product Manual Structure and Filenames

Consult this when writing a complete software manual or documentation site.

## Directory Structure

| Part | English name | Required | Form | Content |
|---|---|---|---|---|
| 简介 | Introduction | Yes | File | Overall description of the product and documentation |
| 快速上手 | Getting Started | No | File | The quickest way to start using it |
| 入门篇 | Basics | Yes | Directory | Beginner usage tutorials |
| ├ 环境准备 | Prerequisite | Yes | File | Conditions that must be met before use |
| ├ 安装 | Installation | No | File | Installation method |
| └ 设置 | Configuration | Yes | File | Configuration instructions |
| 进阶篇 | Advanced | No | Directory | Intermediate and advanced development tutorials |
| API | Reference | No | Directory or file | Describe each API individually |
| FAQ | FAQ | No | File | Frequently asked questions |
| 附录 | Appendix | No | Directory | Definitions of terms (Glossary), practical examples (Recipes), troubleshooting (Troubleshooting), update history (ChangeLog), and ways to provide feedback (Feedback) |

Reference example: [Redux 文档](https://redux.js.org/introduction/getting-started).

## Filenames

- Use only half-width characters, with no Chinese characters or spaces.
- Use lowercase letters. Explanatory files such as `README` and `LICENSE` may be uppercase.
- Connect multiple words with `-`.

```
差：名词解释.md    好：glossary.md
差：TroubleShooting.md    好：troubleshooting.md
差：advanced_usage.md    好：advanced-usage.md
```

