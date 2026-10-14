# Examples of Rewriting into Natural Chinese

Consult this when checking for translationese, vague modifiers, and successive negatives. Judge by the meaning of the entire sentence and its context of use; after rewriting, check the operations, states, quantities, and conditions.

## Examples from Online Guides

The following materials come from software localization teams and technical writing guidelines. They explain how to express the original meaning according to Chinese usage; see the next section for this project's preferences on words such as “真实”.

| Source and location | Examples or key points from the guide | How to use them in writing |
| --- | --- | --- |
| [AOSC《大陆简中自由软件本地化工作指南》](https://repo.aosc.io/aosc-l10n/zh_CN_l10n.pdf), version 1.5.4, section 3 | `File is being saved` is translated as “正在保存文件” | Describe the action in Chinese word order, preserving state information such as “正在” |
| Same source, section 2.4 | The translation of `Start` depends on its relationship to words such as `Pause` and `Resume` | Choose words in the context of the interface, code, and surrounding text |
| [Mozilla 正体中文本地化指南](https://mozilla-l10n.github.io/styleguides/zh-TW/), Testing / QA items 1 and 8 | Use different expressions for the name of the installation action and the state of installation in progress; repeated subjects and possessives in a sentence may be omitted according to its meaning | Distinguish actions from states, and remove unnecessary words such as “你” and “你的” |
| [MDN 简体中文翻译指南](https://github.com/mdn/translated-content/blob/main/docs/zh-cn/translation-guide.md#复数形式), Plural forms | `Application Programming Interfaces (APIs)` corresponds to “应用程序接口（API）” | Handle plural forms according to Chinese usage, preserving meaningful quantities in the original |
| [Ant Design 文案](https://ant.design/docs/spec/copywriting-cn/), State information completely and directly; Be friendly and respect users | Interface messages should explain the purpose of actions and guide users to solve problems after errors | State what to do in messages; still state task requirements according to the original |
| [Australian Government Style Manual：Positive sentences](https://www.stylemanual.gov.au/style-manual-resources/government-writing-handbook/editors-tips/positive-sentences) | Usually state directly what readers need to do; use negative instructions when there is sufficient reason | Prioritize actions in ordinary guidance, and retain explicit wording for necessary prohibitions |

Only a few examples are excerpted here, along with summaries of relevant points. The AOSC guide uses the CC BY-NC-SA 3.0 license and credits Aron Xu, Mingye Wang, and others; see the individual sources for the licenses of the other materials. The examples below were written by this project.

## How to Revise Words Such as “真实”

This project favors specific, plain wording. Modifiers such as “真实”, “真正”, “实际”, and “有效” that only add emphasis can usually be removed. When a distinction is needed, explain the specific difference directly.

The presence of these words in a sentence does not by itself indicate that the text was machine translated. When checking, consider whether the word provides information the reader needs and whether its meaning can be verified from the original text or project materials.

| Context | Original wording | Rewrite |
| --- | --- | --- |
| The image source is already stated, and “真实” only adds emphasis | 使用相机采集的真实图像 | 使用相机采集的图像 |
| Explicitly comparing a robot with simulation | 在真实机器人上运行，与仿真结果比较 | 在真机上运行，与仿真结果比较 |
| Only the output of this run needs to be described | 查看本次程序运行的真实输出 | 查看本次程序运行的输出 |
| “真正” only emphasizes the save action | 将录制的视频真正保存到本地 | 将录制的视频保存到本地 |
| There is only a vague evaluation of effectiveness | 本节有效地帮助你理解推理流程 | 本节介绍推理流程 |
| The content describes configuration | 保留技术事实 | 保留原文的功能说明、参数和操作要求 |
| The content is an error message in a log | 日志提供了程序无法打开 `config.yaml` 的证据 | 日志显示，程序无法打开 `config.yaml` |

“真实数据” may mean collected data, production data, or unmodified data. Choose words after confirming the meaning from context; if the source is unclear, retain the known content and ask the user for confirmation when it affects task requirements. Also use “实际”, “真正”, and “实测” according to the sentence's meaning; in particular, “实测” requires a measurement process.

Use established terms according to their original meaning, such as 虚拟现实, 实时推理, and 数据真实性. Retain project spellings for fields, functions, and product names, such as `ground_truth`, `realpath`, and Unreal Engine.

## Other Wording Easily Copied from English

The following are all examples from this project, illustrating how to rewrite.

| Wording to check | Original sentence | Rewrite |
| --- | --- | --- |
| Expressing an action as “进行 + 名词” | 对配置文件进行修改 | 修改配置文件 |
| “拥有……的能力” | 这个函数拥有读取图像的能力 | 这个函数能读取图像 |
| “这允许你……” | 这个按钮允许你导出视频 | 点击这个按钮可导出视频 |
| Repeated subjects or possessive relationships | 你可以在你的输出目录中查看你的结果 | 在输出目录中查看结果 |
| Stacking multiple modifiers before a noun | 检查由相机在本次运行中所采集到的图像 | 检查相机在本次运行中采集的图像 |
| Unnecessary “层面” | 在文件层面对配置进行修改 | 修改配置文件 |

“允许” expressing permission, “有效” describing a validation result, and “实际值” contrasted with “目标值” all have specific meanings. Retain such wording according to its technical meaning.

## Interrogative Expressions in Explanatory Sentences

When encountering English expressions such as `explain what…` and `describe how…`, first determine what the sentence needs to convey, then organize it according to Chinese usage. When explaining objects, methods, principles, or reasons, choose natural verb combinations; when directing readers to perform an operation, state the specific action directly.

The following are this project's rewrite examples. The original wording prompts a check and does not imply that all similar sentences require rewriting.

| Context | Original wording | Rewrite |
| --- | --- | --- |
| Explaining content that needs confirmation | 资料不足时，保留已有信息，并说明还需确认什么。 | 资料不足时，保留已有信息，列出待确认的内容。 |
| Explaining missing information and verification methods | 说明缺少什么、如何确认。 | 列出缺失的信息，并说明核实方法。 |
| Introducing a working principle | 解释这个模块如何工作。 | 说明这个模块的工作原理。 |
| Introducing an execution flow | 本节解释这个模块如何工作。 | 本节介绍这个模块的运行流程。 |
| Analyzing the reason a connection failed | 说明为什么连接失败。 | 说明连接失败的原因。 |
| Writing operating guidance | 说明读者要做什么、做到什么程度。 | 写清具体做法和完成标准。 |

“如何工作” may refer to a working principle or an execution flow, and “如何确认” may refer to checking materials or confirming with others; the specific translation depends on context.

Choose words according to the meaning of the entire sentence. Avoid always replacing “什么” with “哪些事项”, or always replacing “如何” with “相关方式”. When there is a specific object, name it directly; when the original does not provide specific information, mark the content that needs confirmation and retain the original uncertainty.

Interrogative words can be used naturally in questions, question titles, and conversation, such as “如何配置代理？” and “不确定就说清楚哪里不确定、怎么验证。” Focus the check on whether the sentence is natural and its meaning is clear.

## Changing Successive Negatives into Specific Actions

Organize ordinary explanations around what the reader needs to accomplish, stating the actions, results, and necessary conditions. When multiple instances of “不要”, “避免”, or “不能” occur in one paragraph, check whether they can be combined into one explicit requirement.

| Original wording | Rewrite | Requirement preserved |
| --- | --- | --- |
| 不要遗漏报错，不要省略执行命令，不要漏掉 Python 版本。 | 报告问题时，附上完整报错、执行命令和 Python 版本。 | All three pieces of information are included |
| 不要修改已有函数，不要更改参数名，不要删去检查代码，只填写标记区域。 | 保留已有函数、参数名和检查代码，仅在标记区域填写答案。 | The scope of changes remains limited to the marked area |
| 不要把 `config.yaml` 放在其他目录。 | 将 `config.yaml` 放在当前工作目录。 | Assumes that the preceding text has already specified the current working directory |
| 没有删除权限的用户，不能删除此文件。 | 用户必须有删除权限，才能删除此文件。 | Delete permission is a necessary condition |
| 结果尚未保存时，不得关闭程序。 | 关闭程序前必须保存结果。 | Closing is allowed only after saving |

Retain the explicit prohibition in “更新固件期间禁止断电”. Express states such as “装置未接通电源” and “测试未通过” according to their original meaning. Keep the meanings of permissions, prerequisites, and prohibitions consistent, with wording of the same force as the original.

