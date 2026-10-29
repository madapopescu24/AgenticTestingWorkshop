UiPath Partner Success · 工作坊
{: .eyebrow }

# 🧪 使用编码智能体进行 UiPath 智能体测试 { #uipath-agentic-testing-with-coding-agents }

**借助 Autopilot for Testers、Autopilot for Developers 和编码智能体，规划、自动化、执行并报告 UiPath 测试：从一份测试用例设计文档，到 Test Cloud 中一次已执行的测试。**

!!! tip "培训环境"
    在 **[{{ training_url }}]({{ training_url }})** 登录，使用租户 **{{ training_tenant }}**。

![智能体测试生命周期：环境准备、需求、测试用例、执行和测试集，以及每个阶段由谁完成工作](assets/images/testing-lifecycle.svg){ .lifecycle }

## 🎯 你将构建什么 { #what-youll-build }

本工作坊向你展示 AI 智能体如何在 **UiPath Test Cloud** 中为你工作，以及哪些地方仍需要测试人员做决定。

- 🤖 **Autopilot** 在产品内部工作。在 **Studio** 中，它创建需求、测试用例和测试集。在 **Test Manager** 中，它评估需求、生成测试用例，并自主运行测试用例。
- 💻 像 **Codex** 或 **Claude Code** 这样的**编码智能体**在你的终端中工作。借助 **`uip` CLI** 和 **UiPath 技能**，它在你的 Studio 项目中自动化测试用例，并运行测试集。
- 🏦 你从 **UiBank** 演示应用的一份真实设计文档开始。

## 🗺️ 课程安排 { #the-session }

课程从 9:00 持续到 17:00，约 8 小时，中间有两次休息和午餐。在下面两个部分之后，以 SAP 测试、问答和反馈结束。动手实践部分从[环境准备](setup.md)开始，大家在现场一起完成。

<div class="grid cards" markdown>

-   :material-lightbulb-on-outline:{ .lg .middle } **1. 简介 + 理论知识**

    ---

    Test Cloud、Test Manager、Autopilot for Testers、Autopilot for Developers 和编码智能体：各自做什么，以及何时使用哪一种。

    [:octicons-arrow-right-24: 智能体测试与编码智能体](what-is-a-coding-agent.md)

-   :material-hand-back-right-outline:{ .lg .middle } **2. 动手实践**

    ---

    五个部分，各有独立的选项卡，从一个空项目到一个已执行的测试集。议程页面逐步展示了课程的进行方式。

    [:octicons-arrow-right-24: 议程](agenda.md)

</div>

### 动手实践的各个部分 { #the-hands-on-parts }

<div class="grid cards" markdown>

-   :material-rocket-launch-outline:{ .lg .middle } **环境准备**

    ---

    第一个动手步骤：你的虚拟机、登录、`uip` CLI、Studio，以及你的 UiBank 测试用户。

    [:octicons-arrow-right-24: 环境准备](setup.md)

-   :material-cog-outline:{ .lg .middle } **测试环境准备**

    ---

    场景、设计文档和课堂上的准备工作：你的 Test Manager 项目，以及在 Studio 中新建并连接到它的测试自动化项目。

    [:octicons-arrow-right-24: 测试环境准备](agentic-testing-hands-on.md)

-   :material-clipboard-text-outline:{ .lg .middle } **需求**

    ---

    Studio 中的 Autopilot 根据设计文档创建需求，Test Manager 中的 Autopilot 对其进行评估。

    [:octicons-arrow-right-24: 需求](requirements.md)

-   :material-test-tube:{ .lg .middle } **测试用例**

    ---

    Test Manager 中的 Autopilot 生成测试用例。你手动自动化 Login 测试用例，然后由 Studio 中的 Autopilot 或编码智能体自动化后续用例，Autopilot 还会自主运行其中一个。

    [:octicons-arrow-right-24: 测试用例](test-cases.md)

-   :material-play-circle-outline:{ .lg .middle } **执行**

    ---

    每一次运行——手动、自动或自主——及其结果和截图。

    [:octicons-arrow-right-24: 执行](executions.md)

-   :material-package-variant-closed:{ .lg .middle } **测试集**

    ---

    Autopilot 将你的测试用例分组，你运行它们并查看结果。

    [:octicons-arrow-right-24: 测试集](test-sets.md)

</div>

每个部分都附有你将使用的提示词。

## 🔑 关键概念 { #key-concepts }

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">💻</span>
<span class="f-title" markdown="span">编码智能体</span>

一种 AI 助手（例如 Claude Code），根据你的指令，使用 `uip` CLI 和 UiPath 技能构建并运行 UiPath 组件。

</div>

<div class="feature" markdown>
<span class="f-icon">⌨️</span>
<span class="f-title" markdown="span">`uip` CLI</span>

编码智能体用来与 UiPath 平台交互的命令行界面，包括 Test Manager（`uip tm`）和 Studio 项目（`uip rpa`）。

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">UiPath 技能</span>

精心整理的指令包，教编码智能体如何正确地使用 UiPath。本工作坊使用 `uipath-test`、`uipath-rpa` 和 `uipath-platform`。

</div>

<div class="feature" markdown>
<span class="f-icon">📋</span>
<span class="f-title" markdown="span">Test Manager</span>

Test Cloud 中管理需求、测试用例、测试集、执行和结果的中心。

</div>

<div class="feature" markdown>
<span class="f-icon">🤖</span>
<span class="f-title" markdown="span">Autopilot for Testers</span>

UiPath 在 Studio 和 Test Manager 中内置的测试智能体。它们生成并评估需求，生成测试用例和测试集，自主运行测试用例，并解释测试结果。

</div>

<div class="feature" markdown>
<span class="f-icon">🪄</span>
<span class="f-title" markdown="span">Autopilot for Developers</span>

Studio 中用于构建和修复自动化的 Autopilot：它根据工作流的上下文生成和修复表达式。

</div>

</div>
