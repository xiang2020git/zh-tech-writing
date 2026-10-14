---
name: zh-tech-writing-en
description: Writing guidelines for Chinese technical documentation. Use when writing or revising Chinese technical documentation and developer documentation (README, design documents, API descriptions, and tutorials).
---

# Writing Chinese Technical Documentation

Goal: Write Chinese technical documentation as a senior engineer would. **Plain**, **specific**, **short sentences**.

## Workflow

**Writing a new document:**

1. Identify the readers and what they should be able to accomplish after reading. Write directly when the available information is sufficient; ask the user when key information that affects content selection is missing.
2. Follow the sections below on “Sentences,” “Tone,” “Paragraphs and Structure,” and “Typography.”
3. Check the entire document against the “AI Style Checklist,” and revise unsuitable wording in context.
4. Run `autocorrect --fix <文件>` to fix spacing and punctuation. If the command is unavailable, skip it and check manually against “Typography.”
5. Manually check what autocorrect does not cover: quotation marks, ellipses, and dashes.

**Revising an existing document:**

1. Read the entire document before revising.
2. If the user only wants feedback, leave the file unchanged and list issues as “Original sentence → Revision → Reason.”
3. Otherwise, edit the file directly and complete the checks in steps 3～5 above. At delivery, explain the main changes in two or three sentences.

Complete all checks and fix the issues found. Retain sentences that quote the original or demonstrate counterexamples according to their purpose.

## Sentences

- Aim to keep each comma-separated segment within 20 characters. Split segments that exceed 30 characters. Keep the entire sentence within 100 characters.
- Express one idea per sentence. Use more simple and coordinate sentences, and separate long attributive phrases.
  - Bad: 那个昨天生病的人没有参加会议。
  - Good: 他昨天生病了，没有参加会议。
- Use affirmative sentences for ordinary explanations, stating the action and completion conditions directly. Change double negatives into explicit requirements or states. Preserve the meaning of safety prohibitions, permission restrictions, and decision conditions.
  - Bad: 不能不检查输出目录。 → Good: 检查输出目录。
  - State description: 请确认装置未接通电源。
  - Bad: 没有删除权限的用户，不能删除此文件。 → Good: 用户必须有删除权限，才能删除此文件。
- When you can specify who does what, state it directly. Reduce unnecessary passive constructions with “被”.
  - Bad: 假如此软件尚未被安装 → Good: 假如还没安装这个软件
- Organize operating instructions around the relationships between actions. Explain parallel actions separately. When a step uses the result of the previous step, identify the result it needs. Use numbered steps for longer procedures.
  - When a sentence mechanically uses “先……，再……”, rewrite the entire sentence, preserving the operating sequence, decision conditions, and order of fields or array elements. Focus the revision on explaining the relationships between actions or data; likewise, use “首先”, “然后”, and “随后” according to the sentence's meaning.
  - Bad: 每对夹指先放换算得到的位置，再放它的相反数。
  - Good: 每对夹指的两项依次为换算后的位置和该位置的相反数。
- Express actions directly with verbs.
  - Bad: 对配置文件进行修改 → Good: 修改配置文件
- In explanations and operating requirements, watch for wording copied from English interrogative clauses, such as “说明还需确认什么”. Express the action and its object naturally according to the sentence's meaning, splitting the sentence when necessary.
  - Bad: 并说明还需确认什么。 → Good: 并列出待确认的内容。
  - When introducing a working principle: 解释这个模块如何工作。 → 说明这个模块的工作原理。
  - Judge words such as “什么” and “如何” in the context of the entire sentence. Questions, question titles, and natural conversational expressions can remain; avoid replacing all of them with vague wording such as “哪些事项” or “相关方式”.
- “这”, “其”, and “该” must each refer to a single, clear object. Repeat the noun if there may be ambiguity.
- Use no more than two layers of modifiers before a noun; split into two sentences if there are more.
- Use common words in modern Chinese.
  - Bad: 这是唯二的方法。 → Good: 只有这两种方法。
- Distinguish “的、地、得”: 开心的笑容、开心地笑、笑得开心。

## Tone

- Explain things as you would to a colleague, using everyday expressions familiar to the reader.
- Address the reader as “你” and the project team as “我们”.
- Use a declarative tone and end sentences with a full stop.
- Describe specific features, operations, or test results. Use the original text or project materials as the authority for numbers, commands, filenames, and error messages. If information that affects the conclusion is missing, list the missing information and explain how to verify it.
  - Bad: p99 延迟从 120 ms 降到 40 ms，性能得到了大幅提升。
  - Good: p99 延迟从 120 ms 降到 40 ms。
- State what is certain directly. If something is uncertain, explain what is uncertain and how to verify it.
- State specific actions, completion criteria, and ways to handle problems. When “不要……” and “避免……” appear repeatedly, replace them with specific actions and combine duplicate reminders. Express explicit requirements and prohibitions according to their original meaning, preserving their applicability conditions and original force.
  - Bad: 不要遗漏报错，不要省略执行命令，不要漏掉 Python 版本。
  - Good: 报告问题时，附上完整报错、执行命令和 Python 版本。
  - Necessary prohibition: 更新固件期间禁止断电。

## Word Choice

- State the object, action, and result clearly. When a general term has an unclear referent, explain the specific content according to the original text.
- Expand general terms such as “事实”, “证据”, and “依据” according to the intended meaning. When explaining features, write the features; when explaining tests, write the test results; when explaining the basis of a judgment, write the logs, documents, or data.
- This project favors specific wording. When words such as “真实”, “真正”, and “实际” only add emphasis, remove the modifiers; when distinguishing objects is necessary, state the specific differences, such as physical hardware versus simulation, or collected data versus generated data. The differences stated should be verifiable from the original text or project materials.
- Rewrite according to the meaning of the whole sentence, retaining the original sources, numbers, reasons, and conditions. Use terms and names according to project conventions, such as 虚拟现实, 实时推理, 数据真实性, `realpath`, and `ground_truth`.
- Retain the original names of functions, fields, products, and established terms. Use technical terms such as “依赖”, “输入输出”, and “上下文窗口” according to their actual meanings.

The following examples show how to revise sentences:

| Original wording | Rewrite according to the intended meaning |
| --- | --- |
| 保留技术事实 | 保留原文的功能说明、参数和操作要求 |
| 用事实代替形容词 | 写清具体功能或已有的测试结果 |
| 日志提供了程序无法打开 `config.yaml` 的证据 | 日志显示，程序无法打开 `config.yaml` |
| 保留依赖关系 | 后一步用到前一步的结果时，指出要用的结果 |
| 保留数据排列 | 保留字段和数组元素的顺序 |
| 全文没有命中上述写法 | 全文未发现上述写法 |
| 使用相机采集的真实图像 | 使用相机采集的图像 |
| 在真实机器人上运行，与仿真结果比较 | 在真机上运行，与仿真结果比较 |

The example of “依赖关系” in the table refers to operating steps. Continue to use the corresponding terms for package dependencies, function calls, and similar contexts.

When checking for translationese, vague emphasis, or successive negatives, read [references/natural-chinese.md](references/natural-chinese.md). It lists examples from online guides and this project's rewrite examples. Judge words such as “真实” in the context of the whole sentence; this project's wording preferences and the external guides are explained separately.

## Paragraphs and Structure

- Put the main point in the first sentence of each paragraph, then add supporting explanation. Discuss one topic per paragraph.
- Prefer no more than 4 lines per paragraph, with a maximum of 7 lines.
- Mainly use second- and third-level headings:
  - Arrange headings in order through the first, second, and third levels.
  - If a heading is the only one at its level, remove that heading level.
  - Subheadings should describe the content of their section.
  - When a fourth-level heading is needed, use `**（1）xxx**` or a list instead.
  - Write headings as short phrases, omitting terminal full stops, commas, and colons.
- Use lists for parallel items that can be scanned individually. Write content with causal or contrasting relationships as paragraphs.
- Reserve bold for warnings or keywords the reader must notice, with at most one or two instances per screen.
- Cite the source when quoting other people's content or images.

## Typography

Rules that apply to every document:

- Add one half-width space between Chinese text and English text or numbers: `在 Linux 上安装 5 个包`.
- Use full-width punctuation in Chinese sentences: `，。：；？（）`. Use half-width punctuation when the entire sentence is in English.
- Do not insert a space when full-width punctuation immediately follows English text or numbers: `他用的是 MacBook Air。`
- Use full-width quotation marks `“ ”`; use `‘ ’` for quotations nested inside quotations.
- Separate coordinate words with the enumeration comma `、`, connecting the final item with “和”: `Google、腾讯和百度`.
- Write ellipses as `……`, not `...` or `。。。`, and do not combine them with “等”.
- Always use half-width digits.

For detailed rules on numbers (thousands separators, units, ranges, and multiples), parentheses, colons, connecting marks, and English abbreviations, see [references/typography.md](references/typography.md). Read it when these appear in the document.

When writing a complete set of product manuals or a documentation site and planning directories and filenames, read [references/manual-structure.md](references/manual-structure.md).

## AI Style Checklist

Check each item during self-review. The left column shows wording to look for; the right column shows how to revise it.

| Look for this wording | Change to |
|---|---|
| Stock openings: “随着……的发展”, “在当今……”, “值得注意的是”, “需要指出的是”, “让我们来看看”, “接下来我们将介绍” | Delete them and state the content directly in the first sentence |
| Stock endings: “总的来说”, “综上所述”, “总而言之”, or a summary paragraph that repeats earlier content | Delete them. If an ending is truly needed, include only new information, such as what to do next |
| Pleasantries: “希望对你有帮助”, “如有问题欢迎交流” | Delete them |
| Contrasting constructions used only for emphasis: “不是 A，而是 B”, “与其说 A，不如说 B” | State the main point directly; preserve technical distinctions and misconceptions that need clarification |
| Progressive constructions: “不仅……而且/更……” | Split into two declarative sentences |
| Operating instructions that mechanically use “先……，再……” or “首先……然后……” | Rewrite according to the rules in “Sentences.” When using the result of the previous step, specify what is needed, preserving the original conditions and sequence |
| Forcing groups of three: three parallel adjectives, or lists that always have three items per group | Write as many items as there are |
| Rhetorical questions answered by the writer: “关键是什么？答案很简单：”, “原因很简单：” | Give the conclusion directly |
| Promotional adjectives: 强大、灵活、无缝、全面、极致、优雅、轻松、一站式 | State specific features or existing test results; when there is only a vague evaluation, remove the evaluation |
| Jargon: 赋能、抓手、闭环、链路、沉淀、对齐、颗粒度、维度、底层逻辑、范式、打通 | Replace with plain language. Retain formal names in code or the business domain (such as “调用链路”) |
| Dashes `——` used to insert explanations | Use commas, colons, parentheses, or split into two sentences. Use at most one or two instances in the entire document |
| Translationese: “进行 + 动词”, “通过……的方式”, “作为一个……”, or multiple instances of “的” in one sentence | Use verbs directly and separate long attributive phrases |
| Explanatory sentences that awkwardly use “说明……什么” or “解释……如何……” | Follow the rules in “Sentences,” using natural word combinations to clarify content, methods, principles, or reasons; retain questions and natural conversational expressions according to their purpose |
| Generalizing different kinds of information with words such as “事实” or “证据” | State specific content as in the examples in “Word Choice,” avoiding fixed word substitutions |
| Modifiers such as “真实”, “真正”, “实际”, and “有效” that only add emphasis | Remove vague emphasis; when distinguishing sources, devices, or states is necessary, explain the differences according to the materials and retain established terms |
| Ordinary explanations organized with repeated “不要”, “避免”, or “不能” | State specific actions and completion conditions, and combine duplicate reminders; preserve the meaning of necessary prohibitions and technical restrictions |
| Excessive vagueness: “在某种程度上”, “在一定情况下可能会” | State what is certain directly; if uncertain, clarify the conditions |
| Exclamation marks, emoji headings, or emoji list markers | Full stops and plain-text headings |
| Bold in every paragraph, splitting even one or two sentences into lists, or subheadings more frequent than paragraphs | Reorganize according to “Paragraphs and Structure” |

