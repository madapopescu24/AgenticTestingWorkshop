简介 + 理论知识
{: .eyebrow }

# 🤝 智能体测试与编码智能体 { #agentic-testing-coding-agents }
了解使用 UiPath Test Cloud 进行测试是什么样的，智能体测试带来了什么，编码智能体如何工作，以及两者在你的测试生命周期中的交汇点。

## 🧪 测试与 UiPath Test Cloud { #testing-and-uipath-test-cloud }

### 🔬 测试概览 { #testing-in-a-nutshell }

测试是一项调查活动，为利益相关方提供被测产品的质量信息。测试分为四个层级：

<div class="circles" markdown>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**单元测试**

针对系统的单个单元，确认每个单元的代码行为符合预期。由开发人员编写和运行。

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**集成测试**

将多个单元组合在一起作为整体测试，发现它们交互中的缺陷

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**系统 / 端到端测试**

针对完整、集成的系统，依据其端到端规格进行测试

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**验收测试**

依据业务需求测试系统，判断它是否可以交付

</div>
</div>

</div>

UiPath Test Cloud 在中间层级价值最大：**集成**测试和**端到端**测试，而本次课程中的 UiBank 测试用例正属于这一类。还有两个你一整天都会用到的理念：

- **黑盒测试。** 应用测试从外部检查软件是否满足需求，通过输入和预期输出进行验证，无需访问代码。每个 UiBank 测试都是这样进行的。
- **尽早测试。** 在测试阶段发现缺陷的成本，远低于缺陷进入生产环境后再做热修复。自动化并不取代人：它承担重复性的检查，让测试人员可以专注于探索性测试和可用性测试。

### ☁️ 什么是 UiPath Test Cloud { #what-uipath-test-cloud-is }

**UiPath Test Cloud** 是 UiPath 面向应用测试人员的产品：它是 Automation Cloud 中专注于应用测试的专用界面，支持云端和本地部署。

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">📋</span>
<span class="f-title" markdown="span">Test Manager</span>

规划、运行、管理和分析测试：需求、测试用例、测试集、执行、结果

</div>

<div class="feature" markdown>
<span class="f-icon">🛠️</span>
<span class="f-title" markdown="span">Studio</span>

使用可视化设计器或代码构建自动化测试用例

</div>

<div class="feature" markdown>
<span class="f-icon">⚙️</span>
<span class="f-title" markdown="span">Orchestrator</span>

在机器人上大规模执行和管理测试自动化

</div>

<div class="feature" markdown>
<span class="f-icon">✨</span>
<span class="f-title" markdown="span">智能体测试</span>

加速测试设计和执行的 AI 智能体：Autopilot for Testers，以及你自己构建的智能体

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">Agent Builder</span>

用于构建这些自定义智能体。包含在 App Tester 许可证中

</div>

</div>

### 🧱 Test Manager 中的基本构件 { #the-building-blocks-in-test-manager }

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">📁</span>
<span class="f-title" markdown="span">项目</span>

以下所有内容的容器

💡 每个对象的键都以项目的**前缀**开头，例如 `VC1:1`。前缀在租户中必须唯一。项目在 Orchestrator 中的**默认文件夹**是自动化运行和自主运行发生的地方。

</div>

<div class="feature" markdown>
<span class="f-icon">📋</span>
<span class="f-title" markdown="span">需求</span>

应用必须做什么，以及它的验收标准

💡 需求也可以来自 **Jira**、**ServiceNow** 或 **Redmine**

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">测试用例</span>

包含手动步骤的场景，关联到它所覆盖的需求

💡 它可以关联到 Studio 中的自动化，也可以由 Autopilot 自主运行

</div>

<div class="feature" markdown>
<span class="f-icon">📦</span>
<span class="f-title" markdown="span">测试集</span>

一起执行的一组测试用例

💡 测试用例可以**静态**分配（手动挑选）或**动态**分配（按标签）。只有静态分配的测试用例才能强制执行顺序。

</div>

<div class="feature" markdown>
<span class="f-icon">▶️</span>
<span class="f-title" markdown="span">执行</span>

测试用例或测试集的一次运行

💡 **Manual**、**Automated**、**Autonomous** 或 **Pending**，每个测试用例都有日志、结果和证据。参见[执行](executions.md)。

</div>

</div>

它们之间的关联就是 Test Manager 所说的**可追溯性**：从一个需求出发，你可以看到哪些测试用例覆盖了它，以及这些测试用例在最近一次运行中的结果。

### 🛠️ Studio 中的测试自动化项目 { #test-automation-projects-in-studio }

**测试自动化项目**是 Studio 中用于应用测试的项目类型。只有拥有 **App Tester Developer** 许可证的用户才能创建和发布它们。

- **测试用例和数据驱动测试用例。** 一个项目包含多个测试用例。数据驱动测试用例会针对测试数据的每一行运行一次。
- **Given / When / Then。** 每个测试用例都有三个部分：准备、操作和验证。验证放在 **Then** 中。
- **内置测试活动。** **Verify Expression**、**Verify Expression With Operator** 和 **Verify Control Attribute** 用于检查预期结果，并可以为每个结果附加截图。
- **Object Repository。** 从应用中捕获的 UI 目标元素，由项目中的所有测试用例共享。
- **Test Explorer。** 在构建过程中运行和调试测试用例。它的结果只在当前 Studio 会话中保留。
- **VB 或 C#。** 两种表达式语言都受支持，测试用例也可以用代码编写。
- **发布。** 将项目发布到 **Orchestrator Tenant Process Feed** 会在 Orchestrator 中创建对应的流程。Test Manager 运行最新发布的版本。

### 🎫 许可证 { #licenses }

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🎫</span>
<span class="f-title" markdown="span">App Tester</span>

手动测试、测试管理，以及运行（而非构建）自动化。包含 Agent Builder。

</div>

<div class="feature" markdown>
<span class="f-icon">👩‍💻</span>
<span class="f-title" markdown="span">App Tester Developer</span>

构建自动化测试用例，以及测试自动化（包括智能体）

</div>

<div class="feature" markdown>
<span class="f-icon">🤖</span>
<span class="f-title" markdown="span">App Test Robot</span>

在机器人上以无人值守方式运行自动化测试

</div>

</div>

### 🔌 Test Cloud 的集成方式 { #where-test-cloud-connects }

- **需求：** 通过 **Test Manager Connect** 集成 Jira、ServiceNow、Redmine 和其他 ALM 工具，保持测试与需求之间的可追溯性。
- **版本控制：** 通过 Studio 集成 Git 和 TFS。
- **CI/CD：** Jenkins、Azure DevOps 和 GitHub Actions，让测试集作为流水线的一部分运行。

## ✨ UiPath Test Cloud 中的智能体测试 { #agentic-testing-in-uipath-test-cloud }

**UiPath Test Cloud** 覆盖整个测试生命周期：你在 **Test Manager** 中规划和设计测试，在 **Studio** 中实现自动化，再从 **Test Manager** 执行它们，可以手动、自动，或在同一个测试集中混合进行。智能体测试在每个步骤中都加入了 AI 智能体。它们扩展测试人员的能力，而不是取代测试人员。

<div class="circles" markdown>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**规划 <span class="pill">Test Manager</span>**

需求、包含手动步骤的测试用例、测试集

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**自动化 <span class="pill">Studio</span>**

测试自动化项目、Given / When / Then 测试用例、Object Repository

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**执行 <span class="pill">Test Manager</span>**

以手动、自动或混合方式运行测试集

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**分析 <span class="pill">Test Manager</span>**

结果、测试用例日志、断言、截图、报告

</div>
</div>

</div>

Autopilot 是 UiPath 原生的编码智能体：参见[什么是编码智能体？](#whats-a-coding-agent)。接下来的两节介绍它提供哪些能力集，以及每个能力集在哪些 UiPath 产品中可用。

### 🤖 Autopilot for Testers { #autopilot-for-testers }

UiPath 提供开箱即用的测试智能体，内置于 Studio 和 Test Manager 中。以下是你在本次课程中会用到的：

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">📝</span>
<span class="f-title" markdown="span">Autopilot 面板 <span class="pill ">Studio</span></span>

根据你提供的文档生成需求，根据你的测试用例生成测试集，并将它们保存到你的 Studio 项目所连接的 Test Manager 项目中

</div>

<div class="feature" markdown>
<span class="f-icon">🔍</span>
<span class="f-title" markdown="span">Evaluation Agent <span class="pill ">Test Manager</span></span>

检查需求的清晰度、完整性和可测试性

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Test Case Generation Agent <span class="pill ">Test Manager</span></span>

根据需求的详细信息、用户文档或提示词生成结构化的测试用例，并由 **Prompt Library** 引导：Valid E2E Scenario Testing、End-to-End Flow Verification、Rapid Test Idea Generation、Elusive Issue Detection、Boundary-Value Testing，以及你自己保存的提示词

</div>

<div class="feature" markdown>
<span class="f-icon">🎬</span>
<span class="f-title" markdown="span">Run Autonomously <span class="pill ">Test Manager</span></span>

根据测试用例的手动步骤运行它，无需自动化。你可以实时观看，每个步骤的执行都会配有截图记录

</div>

<div class="feature" markdown>
<span class="f-icon">🔎</span>
<span class="f-title" markdown="span">Find with Autopilot <span class="pill ">Test Manager</span></span>

根据用自然语言提出的问题查找需求、测试用例和其他对象

</div>

<div class="feature" markdown>
<span class="f-icon">📥</span>
<span class="f-title" markdown="span">Import Test Cases <span class="pill ">Test Manager</span></span>

从 Excel 文件导入手动测试用例，并用提示词告诉 Autopilot 如何读取该文件

</div>

<div class="feature" markdown>
<span class="f-icon">📊</span>
<span class="f-title" markdown="span">Generate Insights <span class="pill ">Test Manager</span></span>

根据选定的测试结果生成报告：概览、失败最多的测试、常见错误、错误模式和建议

</div>

<div class="feature" markdown>
<span class="f-icon">🪄</span>
<span class="f-title" markdown="span">Generate Test Case with Autopilot <span class="pill ">Studio</span></span>

在 **Test Explorer** 中，将手动测试用例转换为自动化测试用例，并使用项目的 Object Repository 查找 UI 元素

</div>

</div>

Test Manager 中的 Autopilot 还可以使用更多已连接的来源，它们默认全部启用：

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🧹</span>
<span class="f-title" markdown="span">Obsolete Test Detection</span>

查找与需求关联的过时或冗余测试用例

</div>

<div class="feature" markdown>
<span class="f-icon">📈</span>
<span class="f-title" markdown="span">Autopilot Chart</span>

根据你的数据创建柱状图、折线图和饼图

</div>

<div class="feature" markdown>
<span class="f-icon">📚</span>
<span class="f-title" markdown="span">Documentation Search</span>

从 UiPath 文档中检索内容

</div>

<div class="feature" markdown>
<span class="f-icon">🌐</span>
<span class="f-title" markdown="span">Web Reader and Web Search</span>

总结公开网页内容，并回答需要外部来源最新信息的问题

</div>

<div class="feature" markdown>
<span class="f-icon">🔌</span>
<span class="f-title" markdown="span">自定义 MCP 服务器</span>

通过自定义 MCP 服务器集成运行命令，以及外部自动化流程和智能体

</div>

</div>

你也可以为测试流程中团队特有的部分构建自己的智能体。参见 [Test Manager 中的 Autopilot](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-agent-test-manager#connected-sources)。

### 🪄 Autopilot in Studio Desktop { #autopilot-in-studio-desktop }

Autopilot in Studio Desktop，也称为 Autopilot for Developers，是内置于 Studio 中的编码智能体。你在它的聊天窗口中给出任务，它就会在你的项目上工作：

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🏗️</span>
<span class="f-title" markdown="span">构建和编辑工作流</span>

根据自然语言描述创建 XAML 工作流，并在现有工作流中添加、删除、替换或重组活动

</div>

<div class="feature" markdown>
<span class="f-icon">💻</span>
<span class="f-title" markdown="span">生成代码</span>

编写 C# 编码工作流、编码测试用例和工具类源文件

</div>

<div class="feature" markdown>
<span class="f-icon">⚙️</span>
<span class="f-title" markdown="span">配置活动</span>

设置活动属性、变量、参数和控制流

</div>

<div class="feature" markdown>
<span class="f-icon">💬</span>
<span class="f-title" markdown="span">解释和改进</span>

解释或总结活动和代码的作用，并改进工作流的结构和错误处理

</div>

<div class="feature" markdown>
<span class="f-icon">▶️</span>
<span class="f-title" markdown="span">运行、调试和修复</span>

在聊天中运行、调试和验证工作流，分析文件中的 lint 错误，并应用修复

</div>

<div class="feature" markdown>
<span class="f-icon">📦</span>
<span class="f-title" markdown="span">包和活动</span>

查找并安装工作流所需的 NuGet 包，并发现可用的 UiPath 活动

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">自动化测试用例</span>

将从 Test Manager 获取的手动测试用例自动化，并创建和管理测试用例

</div>

<div class="feature" markdown>
<span class="f-icon">🔎</span>
<span class="f-title" markdown="span">搜索、规划和委派</span>

在文档和网络上搜索最佳实践，在需要时请你澄清，制定计划，并将独立的任务交给子智能体

</div>

<div class="feature" markdown>
<span class="f-icon">🔌</span>
<span class="f-title" markdown="span">MCP 工具</span>

调用已在 Studio 中配置并连接的 MCP 服务器上的工具

</div>

</div>

完整列表参见 [Autopilot in Studio Desktop](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-in-studio-desktop)。

对于单个表达式，Autopilot 也可以在 **Expression Editor** 中工作，并使用工作流的上下文——变量、数据类型和当前表达式：

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🪄</span>
<span class="f-title" markdown="span">修复</span>

📍 **Expression Editor** 顶部的魔术棒

修正存在验证错误的表达式

</div>

<div class="feature" markdown>
<span class="f-icon">✍️</span>
<span class="f-title" markdown="span">生成或修改表达式</span>

📍 **Expression Editor** 底部的 Autopilot 输入框

根据自然语言指令编写或重写表达式，例如 *"Change the result of this expression to String"*

</div>

<div class="feature" markdown>
<span class="f-icon">📝</span>
<span class="f-title" markdown="span">根据注释生成</span>

📍 工作流注释旁边的 Autopilot 选项

生成注释中描述的活动

</div>

</div>

!!! tip "给 Autopilot 写提示词"
    要清晰、具体、简洁。说明你期望的输出及其格式，并在需要的地方设定限制。*"Summarize this."* 得到的是含糊的回答。*"Summarize the following text in 100 words, highlighting key findings."* 得到的才是有用的回答。

## 💻 什么是编码智能体？ { #whats-a-coding-agent }

编码智能体是一种能够阅读、编写代码并对代码进行推理的 AI 助手——而不仅仅是自动补全。它不只是建议下一行代码，而是理解你用自然语言描述的目标，探索代码库，做出决策，并生成完整可用的组件。控制权始终在你手中：你审查它构建的内容，要求它调整，并反复迭代直到结果正确。

目前有多种编码智能体可用，各有所长：

- **Autopilot** — UiPath 原生的编码智能体，构建在 UiPath for Coding Agents 基础设施之上。Autopilot 不是固定的流水线，而是基于技能、工具和命令运行。UiPath 官方技能开箱即用。你也可以编写自己的技能，并在其中引用 UiPath 的技能——使用内置技能、你自己的技能，或两者结合。
- **Claude Code** — Anthropic 基于 CLI 的智能体，在你的终端中运行，与文件系统深度集成
- **Codex CLI** — OpenAI 的命令行编码智能体，同样采用终端优先的方式
- **Cursor** — 围绕 AI 构建的 IDE，与编辑器紧密集成，支持行内生成和多文件上下文
- **Gemini CLI** — Google 的终端智能体，擅长推理和长上下文
- **GitHub Copilot Agent** — 嵌入在 VS Code 和 JetBrains 中，非常适合在编辑器内工作

编码智能体之所以特别适合 UiPath 工作，在于技能层：通过加载有关 UiPath 活动、API 和项目约定的领域知识，智能体可以生成可用于生产的测试自动化——而不是通用的样板代码。这正是本练习中 UiPath 技能所做的事情。

## 🧠 心智模型 { #the-mental-model }

每个编码智能体中都会出现五个概念：

<div class="circles" markdown>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**工具**

智能体可以执行的内置操作：读取文件、运行 bash 命令、搜索网络、编辑代码等。

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**技能**

领域知识包，智能体在遇到匹配的任务时加载。就像针对某一件事的操作手册。

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**命令**

你手动输入的快捷方式：`/commit`、`/test`、`/deploy`。由你触发，而不是由智能体触发。

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**钩子**

在生命周期事件时自动运行：编辑之前、提交之后、会话开始时。用于设置防护措施。

</div>
</div>

<div class="circle-item" markdown>
<span class="num">5</span>
<div class="ci-body" markdown>

**子智能体**

由主智能体派生的专门工作者。用于并行处理或隔离复杂任务。

</div>
</div>

</div>

!!! info "插件"
    插件是将上述任意内容打包在一起的包——就像编码智能体的应用市场应用。本练习中使用的 UiPath 技能就是插件。

## 🔧 工具实践 { #tools-in-practice }

Claude Code 的内置工具始终可用——无需任何设置：

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">📖</span>
<span class="f-title" markdown="span">Read</span>

读取项目中的任意文件

</div>

<div class="feature" markdown>
<span class="f-icon">✏️</span>
<span class="f-title" markdown="span">Edit / Write</span>

修改或创建文件

</div>

<div class="feature" markdown>
<span class="f-icon">⌨️</span>
<span class="f-title" markdown="span">Bash</span>

执行 shell 命令

</div>

<div class="feature" markdown>
<span class="f-icon">🔍</span>
<span class="f-title" markdown="span">Glob / Grep</span>

在代码库中搜索

</div>

<div class="feature" markdown>
<span class="f-icon">🌐</span>
<span class="f-title" markdown="span">WebSearch / WebFetch</span>

在线查找信息

</div>

<div class="feature" markdown>
<span class="f-icon">👥</span>
<span class="f-title" markdown="span">Task</span>

派生子智能体

</div>

</div>

!!! info "扩展工具（MCP）"
    MCP（Model Context Protocol）是为编码智能体提供新工具的标准方式，无需修改智能体本身。

    - **GitHub MCP** — 读取 issue，创建 PR
    - **Atlassian MCP** — Jira、Confluence
    - **Slack MCP** — 读取频道，发布消息
    - **自定义 UiPath MCP** — 调用 Orchestrator、Maestro

## 🧩 技能实践 { #skills-in-practice }

技能就是一个文件夹——位于 `.claude/skills/`（或同等位置）中，里面有一个 `SKILL.md` 文件。

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🔎</span>
<span class="f-title" markdown="span">自动发现</span>

智能体会读取每个 `SKILL.md` 的描述。当你的提示词与之匹配时，它会按需加载完整的技能。

</div>

<div class="feature" markdown>
<span class="f-icon">📦</span>
<span class="f-title" markdown="span">不仅仅是文本</span>

技能可以打包参考文档、代码模式、辅助脚本，甚至智能体可以运行的编译好的二进制文件。

</div>

<div class="feature" markdown>
<span class="f-icon">🔒</span>
<span class="f-title" markdown="span">限定权限</span>

技能会声明它允许使用哪些工具。Bash 访问可以受到严格控制。

</div>

</div>

### 📄 SKILL.md 文件的内容 { #whats-in-a-skillmd-file }

每个技能都围绕一个 `SKILL.md` 文件构建。下面是一个示例：

```yaml
---
name: uipath-test
description: UiPath Test Manager — manage test projects, cases, sets, executions; generate reports...
allowed-tools: Bash, Read, Write, Glob, Grep
---

# UiPath Test Assistant

When the user asks to work with Test Manager:

1. Run `uip login status` and stop if the session isn't valid
2. Ask for the project name or key, then resolve it with `uip tm project list`
3. Use `uip tm` commands, always with `--output json`
4. If a command fails or a name matches more than one object, stop and ask

## References
- references/publish-and-link-guide.md
- references/failure-triage-guide.md
- references/test-result-report-guide.md
```

该文件由四个部分组成：

<div class="circles" markdown>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**Frontmatter**

声明技能的名称、描述，以及它允许使用哪些工具。

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**发现提示词**

智能体用 `description` 字段与你的请求进行匹配——技能正是通过这种方式被自动加载的。

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**指令**

文件的正文：技能激活时智能体遵循的分步提示词。

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**参考资料**

指向技能文件夹中文件的路径，智能体可以读取这些文件获取更深入的上下文——API 文档、代码模式、示例项目。

</div>
</div>

</div>

## 🔗 UiPath 在其中的位置 { #where-uipath-fits-in-this-picture }

UiPath 为 Claude Code 提供了一个插件。它打包了技能、钩子和参考资料——让智能体开箱即用地掌握 UiPath 产品的领域知识。

```bash
npm -g install @uipath/cli
uip skills install
```

该插件包含三部分内容：

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">20+ 个技能</span>

覆盖每个 UiPath 产品的领域知识：`uipath-test`、`uipath-rpa`、`uipath-platform`、`uipath-agents`、`uipath-maestro-flow` 等。

</div>

<div class="feature" markdown>
<span class="f-icon">🤖</span>
<span class="f-title" markdown="span">1 个子智能体</span>

`uipath-project-discovery-agent` — 在首次接触 UiPath 项目时自动运行，为智能体构建上下文。

</div>

<div class="feature" markdown>
<span class="f-icon">🪝</span>
<span class="f-title" markdown="span">钩子与参考资料</span>

会话开始时的提示、活动文档，以及安全只读命令的允许列表。

</div>

</div>

## 📚 UiPath 技能目录 { #the-uipath-skill-catalog }

该插件包含覆盖 UiPath 平台各个部分的技能。其中三个用于本练习的实验：

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-test` <span class="pill ">今日使用</span></span>

Test Manager：项目、需求、测试用例及步骤、测试集、执行、失败分析和报告。还可以将 Studio 自动化关联到测试用例。

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-rpa` <span class="pill ">今日使用</span></span>

以发现优先的方式生成和编辑 Studio 项目，包括测试自动化项目、Given / When / Then 测试用例和数据驱动测试

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-platform` <span class="pill ">今日使用</span></span>

身份验证、Orchestrator 管理（文件夹、包、资产）、Integration Service、CLI 工具

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-troubleshoot`</span>

当作业或运行出现意外行为时进行根因调查

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-agents`</span>

搭建、构建、运行、评估和部署编码智能体与低代码智能体

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-maestro-flow`</span>

创建、验证和调试 UiPath Flow 项目

</div>

</div>

!!! tip "本练习中使用的技能"
    标记为今日使用的三个技能——`uipath-test`、`uipath-rpa` 和 `uipath-platform`——是在动手实践环节中，如果你选择用编码智能体来自动化测试用例或运行测试集时，编码智能体会用到的技能。

## ⚖️ 编码智能体的定位 { #where-the-coding-agent-fits }

Autopilot 一次只在一个产品中工作，处理你眼前的内容。编码智能体则在你的终端中，通过 `uip` CLI 跨产品工作：

<div class="vs" markdown>
<div class="vs-side" markdown>
<span class="f-title" markdown="span">🤖 Autopilot for Testers 与 Autopilot for Developers</span>

- **在哪里使用：** 在 Studio 或 Test Manager 中
- **能看到什么：** 你眼前的需求、表达式或结果
- **最适合：** 根据文档生成需求和测试用例、需求质量、测试用例建议、修复表达式、解释结果

</div>
<div class="vs-mid">VS</div>
<div class="vs-side alt" markdown>
<span class="f-title" markdown="span">💻 编码智能体 + UiPath 技能</span>

- **在哪里使用：** 你的终端或编辑器
- **能看到什么：** 在一个会话中同时看到你机器上的文件、你的 Studio 项目、Test Manager 和 Orchestrator
- **最适合：** 跨文件和跨产品的工作：对照文档检查覆盖率、一整套 Given / When / Then 自动化、发布、关联、运行和报告

</div>
</div>

在动手实践环节中，Autopilot 是主角。Studio 中的 Autopilot 编写需求和测试集，Test Manager 中的 Autopilot 评估需求、生成测试用例，并自主运行其中一个。你会手动实现 Login 测试用例的自动化，从而了解好的自动化是什么样子。然后，你再用 Studio 中的 Autopilot 或编码智能体实现下一个测试用例的自动化，并比较两者。
