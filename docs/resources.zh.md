资源
{: .eyebrow }

# 📚 资源 { #resources }

**课程期间及课后值得随时查阅的参考资料和链接。**

!!! tip "培训环境"
    使用租户 **{{ training_tenant }}** 登录 **[{{ training_url }}]({{ training_url }})**。

## 📄 设计文档 { #the-design-document }

整个动手实践部分都从同一份文档开始：**E2E UiBank Online Banking**。下载它，并把 `E2E UiBank Online Banking.docx` 保存到你的工作坊文件夹中。

[下载设计文档 (.docx)](resources.assets/E2E%20UiBank%20Online%20Banking.docx){ .md-button .md-button--primary }

[动手实践页面](agentic-testing-hands-on.md#the-design-document)概述了它的各个步骤、这些步骤对应的需求以及测试数据。

## 🎁 讲师的参考包 { #trainers-reference-package }

讲师的 `DemoUiBankTests` 是一个可正常运行的测试自动化项目，八个测试用例已全部自动化。它已经发布在 `{{ training_folder }}` 文件夹中，因此如果你自己的自动化还没准备好，可以把它关联到你在 Test Manager 中的测试用例，并在[测试集](test-sets.md)中运行。

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🎁</span>
<span class="f-title" markdown="span">`DemoUiBankTests`</span>

测试自动化项目，测试用例部分的参考解决方案

🧪 `T0_LoginAndInitialAccountState` 到 `T7_LogoutAndEvidenceCollection`

📁 `{{ training_folder }}` 文件夹

</div>

</div>

!!! info "是参考，不是捷径"
    先构建你自己的测试用例。本课的重点是观察 Autopilot 和你的编码智能体如何规划、自动化和运行测试用例。参考包用于你遇到阻碍时，以及课后对比。

## ⌨️ CLI 速查表 { #cli-cheat-sheet }

如果你用编码智能体生成测试用例或运行测试集，会看到它通过 `uip` CLI 运行以下命令。每条命令都加上 `--output json`。

| 命令 | 作用 | 何时会看到 |
| :--- | :--- | :--- |
| `uip skills install` | 将 UiPath skills 安装到你的编码智能体中 | 首次环境准备 |
| `uip login` / `uip login status` | 向你的租户进行身份验证 / 检查会话 | 每次会话开始时 |
| `uip tm project list --filter <key>` | 查找 Test Manager 项目 | 任何 Test Manager 操作之前 |
| `uip tm requirements list` / `uip tm testcases list` | 列出需求和测试用例 | 检查覆盖率 |
| `uip rpa tm connect` / `set-default-project` | 将 Studio 项目连接到 Test Manager | 环境准备 |
| `uip rpa validate` / `uip rpa build` | 检查并构建项目 | 每次修改之后 |
| `uip rpa pack` + `uip or packages upload` | 打包并发布到 Orchestrator | 运行测试集之前 |
| `uip tm testcases link-automation` | 将自动化绑定到 Test Manager 测试用例 | 发布之后 |
| `uip tm testsets run` + `uip tm wait` | 执行测试集并等待结果 | 运行测试集 |
| `uip tm report get` / `uip tm result download` | 汇总一次执行 / 下载 JUnit XML | 报告 |
| `uip feedback send` | 报告缺陷或猜错的技能 | 任何出问题的时候 |

## 🔗 实用链接 { #useful-links }

<div class="link-grid" markdown>

<a class="link-card" href="https://github.com/UiPath/skills" target="_blank" rel="noopener"><span class="f-icon">🧩</span><span class="f-title">UiPath/skills</span><span class="f-text" markdown="span">技能仓库。请阅读 `uipath-test` 和 `uipath-rpa` 的 `SKILL.md`。</span></a>
<a class="link-card" href="https://uibank.uipath.com" target="_blank" rel="noopener"><span class="f-icon">🏦</span><span class="f-title">UiBank</span><span class="f-text" markdown="span">被测的演示银行应用</span></a>
<a class="link-card" href="https://meera-uipath.github.io/software-testing-ilt-guide" target="_blank" rel="noopener"><span class="f-icon">🎓</span><span class="f-title">Test Cloud & Agentic Testing ILT Guide</span><span class="f-text" markdown="span">逐步点击操作的 Test Manager 和 Studio 课程：Object Repository、数据驱动测试、发布和执行测试用例</span></a>
<a class="link-card" href="https://docs.uipath.com/test-manager" target="_blank" rel="noopener"><span class="f-icon">📋</span><span class="f-title">Test Manager 文档</span><span class="f-text" markdown="span">需求、测试用例、测试集、执行以及 Autopilot for Testers</span></a>

</div>
