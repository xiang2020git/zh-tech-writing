# zh-tech-writing

用于编写和修改中文技术文档的 Agent Skill，适合 README、设计文档、接口说明和教程。改写保留原文的功能说明、参数和操作要求，文字力求平实、具体。

规则基于阮一峰的[《中文技术文档的写作规范》](https://github.com/ruanyf/document-style-guide)整理，并补充了“AI 腔清单”。可供 Claude Code 和其他支持 Agent Skills 的工具使用。

## 改写示例

原文：

> 随着微服务架构的不断发展，配置管理已经成为一个不容忽视的问题。值得注意的是，ConfigHub 不仅提供了强大的配置管理能力，更实现了与现有系统的无缝集成——让你轻松应对各种复杂场景！

去掉套话和空泛评价后：

> ConfigHub 用于管理服务配置，可与现有系统集成。

具体功能、刷新时间和接入参数以项目资料为准。资料不足时，保留已有信息，列出待确认的内容。

操作说明也要写清动作之间的关系。原文：

> 每对夹指先放换算得到的位置，再放它的相反数。

改写后：

> 每对夹指的两项依次为换算后的位置和该位置的相反数。

改写保留了两项的顺序，直接说明每项的含义。某一步用到前一步的结果时，指出要用的结果。较长流程可用编号步骤。遇到套用“先……，再……”的句子，按整句含义改写，重点是说明动作或数据的关系。

用词也要说明具体内容。例如：

| 原写法 | 改写 |
| --- | --- |
| 保留技术事实 | 保留原文的功能说明、参数和操作要求 |
| 用事实代替形容词 | 写清具体功能或已有的测试结果 |
| 日志提供了程序无法打开 `config.yaml` 的证据 | 日志显示，程序无法打开 `config.yaml` |
| 使用相机采集的真实图像 | 使用相机采集的图像 |
| 在真实机器人上运行，与仿真结果比较 | 在真机上运行，与仿真结果比较 |

这些例子按整句话的意思改写，来源、数字和原因沿用原文。“真实”“真正”“实际”等词仅用于强调时，删去修饰语；有明确区别时，写明设备、数据来源或状态。“实际值”“数据真实性”等术语，以及函数名和字段名，按原义保留。

“说明还需确认什么”这类表达，按句意改成“列出待确认的内容”。介绍工作原理时，“解释这个模块如何工作”可改成“说明这个模块的工作原理”。选择自然的动词搭配，保留原意。提问和自然的口语表达可保留疑问词。

说明和操作指导以具体做法为主。例如：

> 不要遗漏报错，不要省略执行命令，不要漏掉 Python 版本。

改写为：

> 报告问题时，附上完整报错、执行命令和 Python 版本。

技术要求和必要禁令仍须明确。例如“更新固件期间禁止断电”保留禁令，“关闭程序前必须保存结果”保留前提条件。

更多例子和网上指南的出处见[自然中文的改写示例](skills/zh-tech-writing/references/natural-chinese.md)。本项目对“真实”等空泛修饰语的处理是措辞偏好，按上下文判断。

## 安装

用 [skills](https://github.com/vercel-labs/skills) 命令行工具安装到全局：

```bash
npx skills add leter/zh-tech-writing -g
```

手动安装时，将 `skills/zh-tech-writing` 目录复制到 `~/.claude/skills/`：

```bash
git clone https://github.com/leter/zh-tech-writing.git
cp -r zh-tech-writing/skills/zh-tech-writing ~/.claude/skills/
```

## 安装 autocorrect（可选）

[autocorrect](https://github.com/huacnlee/autocorrect) 用于修正中英文间距和标点。安装后，技能会在改稿时调用它。未安装时，按排版规则手动检查。

```bash
# macOS
brew install autocorrect

# Linux：从 Releases 页面下载二进制文件，放到 PATH 里的任意目录
# https://github.com/huacnlee/autocorrect/releases

# 已经装了 Rust 工具链
cargo install autocorrect
```

运行 `autocorrect -V` 查看版本号，确认命令可用。

## 使用

支持自动调用技能的工具，可在写作任务中加载本技能。例如：

```text
帮我给这个项目写一份 README
把 docs/deploy.md 改得更易读一些
```

在 Claude Code 中也可以按名称调用：

```text
/zh-tech-writing 改一下 docs/api.md
```

只需要修改意见时，说明保留文件原样：

```text
/zh-tech-writing 检查 docs/api.md，只列问题，不要改
```

技能会按“原句 → 改后 → 原因”的格式列出问题。

## 写作与检查规则

新文档按以下步骤编写：

1. 明确读者，以及读者看完文档需要完成的事。
2. 按句子、语气、段落结构和排版规则起草。
3. 对照“AI 腔清单”检查全文，修改套话、含糊表达和机械句式。
4. 命令可用时，运行 `autocorrect --fix <文件>`。未安装时，手动检查排版。
5. 核对引号、省略号和破折号。

修改已有文档时，通读全文，按用户要求改稿或提供意见。

主要规则如下：

- 句子：逗号分隔的每一部分尽量在 20 字以内。多用肯定句，直接写明谁在做什么，少用多余的“被”字句。
- 操作顺序：按动作之间的关系组织说明。用到前一步的结果时，写明要用的内容，保留操作顺序、判断条件和数组元素的顺序。
- 用词：直接说明功能、测试结果、日志内容或原文要求。空泛的“真实”“真正”等修饰语按文意处理，已有技术术语保留原名。
- 语气：像给同事讲清楚一件事。数字、命令和报错信息以原文或项目资料为准，缺少的关键信息注明待确认。
- 指导方式：写清做法、完成条件和遇到问题时的处理方式，合并重复的否定提醒，保留必要禁令。
- 结构：每段说明一个主题，第一句写重点。标题逐层安排，加粗和列表按阅读需要使用。
- 自检：逐项检查套话、机械句式、笼统用词、空泛强调和连续否定等问题。

完整规则见 [SKILL.md](skills/zh-tech-writing/SKILL.md)。

## 目录结构

```text
skills/zh-tech-writing/
├── SKILL.md                     主文件：流程、核心规则、AI 腔清单
└── references/
    ├── typography.md            数字、标点、英文缩写的细则
    ├── manual-structure.md      产品手册的目录结构和文件命名
    └── natural-chinese.md       用词、翻译腔和肯定句的改写示例
```

参考文件按需读取。数字、标点和英文缩写的细则见 `typography.md`；产品手册的目录与文件命名见 `manual-structure.md`；用词、翻译腔和连续否定的改写示例见 `natural-chinese.md`。

## 来源与致谢

句子、段落、标题、标点和数字的规则，整理自阮一峰的[《中文技术文档的写作规范》](https://github.com/ruanyf/document-style-guide)。原项目放在公共领域（public domain）。本项目作了以下调整：

- 修正原规范中的两处符号写法：破折号用 `——`，省略号用 `……`。
- 统一在数字和中文之间加空格。原规范允许两种写法，本项目采用与 autocorrect 一致的格式。
- 采用平实、口语化的表达，使用读者熟悉的词语。

原规范参考了华为《产品手册中文写作规范》、LeanCloud《文档风格指南》、[中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines)、Google Developer Documentation Style Guide 和国家标准 GB/T 15835-2011。

本项目补充了“AI 腔清单”、写作检查流程，以及功能说明和测试结果的写法。

自然中文的改写参考了 [AOSC 本地化指南](https://repo.aosc.io/aosc-l10n/zh_CN_l10n.pdf)、[Mozilla 本地化指南](https://mozilla-l10n.github.io/styleguides/zh-TW/)和 [MDN 简体中文翻译指南](https://github.com/mdn/translated-content/blob/main/docs/zh-cn/translation-guide.md)。这些资料说明如何按中文习惯处理语序、代词、状态和复数形式。肯定句的指导参考了 [Ant Design 文案](https://ant.design/docs/spec/copywriting-cn/)和 [Australian Government Style Manual](https://www.stylemanual.gov.au/style-manual-resources/government-writing-handbook/editors-tips/positive-sentences)。各来源的具体位置、适用范围和本项目示例，见[参考文件](skills/zh-tech-writing/references/natural-chinese.md)。

空格和标点的自动修正由 [autocorrect](https://github.com/huacnlee/autocorrect)（MIT 许可）完成。本项目调用该工具，不包含它的代码。

## 许可

[MIT](LICENSE)
