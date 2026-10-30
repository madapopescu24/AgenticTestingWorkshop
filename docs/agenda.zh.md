议程
{: .eyebrow }

# 🗓️ 议程 { #agenda }
**从一份设计文档出发，借助 Autopilot 和编码智能体，依次得到需求、测试用例、测试集和执行。中间有两次休息和午餐。**

## 👋 欢迎 { #welcome }

<div class="timeline" markdown>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

👋 欢迎、自我介绍，以及今天的安排 <span class="pill navy">演示讲解</span>

</div>
</div>

</div>

## 💡 1. 简介 + 理论知识 { #1-intro-theoretical-aspects }

<div class="timeline" markdown>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

💡 <strong style="color: var(--md-primary-fg-color);"><a href="../what-is-a-coding-agent/" style="color: inherit;">简介 + 理论知识</a></strong>：UiPath Test Cloud 和 Test Manager、Autopilot for Testers、Autopilot for Developers、使用 `uip` CLI 和 UiPath 技能的编码智能体，以及何时使用哪一种 <span class="pill navy">演示讲解</span>

</div>
</div>

</div>

## 🙌 2. 动手实践 { #2-hands-on }

动手实践部分紧接在简介之后，从环境准备开始：大家一起准备好虚拟机、登录账号和租户。

### ⚙️ 环境准备 { #setup }

<div class="timeline" markdown>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

通过 Azure Bastion <a href="../setup/#1-connect-to-your-vm">连接到你的虚拟机</a> <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

使用你的工作坊账号<a href="../setup/#2-sign-in-to-the-training-environment">登录培训环境</a> <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

在 Studio Web 中<a href="../setup/#3-confirm-the-tenant">确认租户</a> <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

在虚拟机上<a href="../setup/#4-open-the-terminal">打开终端</a> <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../setup/#5-authenticate-with-your-tenant">让 `uip` CLI 通过你的租户认证</a>，并确认有机器人可以运行你的测试 <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../setup/#6-connect-studio-to-the-training-tenant">将 Studio 连接</a>到培训租户，并检查 Autopilot 面板 <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../setup/#7-register-your-uibank-test-user">注册你的 UiBank 测试用户</a>，并创建凭据资产 <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../setup/#8-download-the-design-document">下载设计文档</a>到你的工作坊文件夹 <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../agentic-testing-hands-on/#create-a-new-project-in-test-manager">在 Test Manager 中创建新项目</a>（例如项目名称 `{YourName}_UIB_Test`，以及一个你自己独有的前缀，比如姓名首字母加一个数字） <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

在 Studio 中<a href="../agentic-testing-hands-on/#create-a-new-test-automation-project-in-uipath-studio-desktop">创建新的测试自动化项目</a>，并<a href="../agentic-testing-hands-on/#connect-it-to-test-manager">将其连接到 Test Manager</a> <span class="pill orange">动手实践</span>

</div>
</div>

</div>

### 📋 需求 { #requirements }

<div class="timeline" markdown>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../requirements/#ask-autopilot-in-studio-desktop-to-create-the-requirements">打开 Studio 和 Test Manager，让 Autopilot in Studio Desktop 创建需求</a>，来源为 .docx 文件 <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

在 Test Manager 中<a href="../requirements/#discuss-the-requirements-in-test-manager">讨论生成的需求</a> <span class="pill amber">讨论</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../requirements/#evaluate-improve-and-re-evaluate-with-autopilot-in-test-manager">用 Test Manager 中的 Autopilot 评估需求质量</a>，采纳部分建议，然后重新评估 <span class="pill orange">动手实践</span>

</div>
</div>

</div>

### ☕ 休息 { #break }

### 🧪 测试用例 { #test-cases }

<div class="timeline" markdown>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../test-cases/#ask-autopilot-in-test-manager-to-create-test-cases">让 Test Manager 中的 Autopilot 创建测试用例</a>，针对某一条具体需求 <span class="pill orange">动手实践</span>

</div>
</div>

</div>

## 🍽️ 午餐 { #lunch }

离开屏幕休息一下。如果你的编码智能体还在构建，就让它在你吃饭时继续运行。

## 🙌 2. 动手实践（续） { #2-hands-on-continued }

### 🧪 测试用例（续） { #test-cases-continued }

<div class="timeline" markdown>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

在 Studio 中<a href="../test-cases/#implement-the-login-test-case-by-hand">手动实现 Login 测试用例</a> <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

在 Studio Desktop 中<a href="../test-cases/#generate-the-next-test-case-with-autopilot-or-a-coding-agent">让 Autopilot in Studio Desktop 或 Codex 生成一个测试用例</a> <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

在 Test Manager 中<a href="../test-cases/#run-autonomously-in-test-manager">自主运行一个测试用例</a>，并实时观看 <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../test-cases/#implement-a-few-more-test-cases">再实现几个测试用例</a> <span class="pill orange">动手实践</span>

</div>
</div>

</div>

### ☕ 休息 { #break_1 }

### ▶️ 执行 { #executions }

<div class="timeline" markdown>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

在 Test Manager 中<a href="../executions/">浏览 Executions 选项卡</a> <span class="pill orange">动手实践</span>

</div>
</div>

</div>

### 📦 测试集 { #test-sets }

<div class="timeline" markdown>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

将<a href="../test-sets/#publish-your-testing-project-to-the-tenant-feed">你的测试项目发布</a>到租户 feed <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../test-sets/#ask-autopilot-in-studio-desktop-to-create-test-sets">让 Autopilot in Studio Desktop 根据测试用例创建测试集</a> <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../test-sets/#run-the-test-sets">运行测试集</a> <span class="pill orange">动手实践</span>

</div>
</div>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../test-sets/#look-into-the-executions-of-the-test-sets">查看测试集的执行</a> <span class="pill orange">动手实践</span>

</div>
</div>

</div>

### 🚀 后续步骤 { #next-steps }

<div class="timeline" markdown>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

<a href="../agentic-testing-hands-on/#next-steps">你构建了什么，接下来可以尝试什么</a> <span class="pill amber">讨论</span>

</div>
</div>

</div>

## 🧩 3. SAP 测试 { #3-sap-testing }

<div class="timeline" markdown>

<div class="tl-item" markdown>
<div class="tl-time"></div>
<div class="tl-body" markdown>

🧩 <a href="../sap-testing/">SAP 测试</a> <span class="pill navy">演示讲解 + 演示</span>

</div>
</div>

</div>

## 💬 问答 { #qa }

带上你对今天任何内容的问题。

## 📝 反馈 { #feedback }

告诉我们哪些地方效果好，哪些地方需要改进。

!!! info "今天的安排如何进行"
    - **计划是灵活的。** 我们可以在工作坊期间调整安排，包括休息时间。
    - **智能体构建的时间就是你审阅的时间。** 当 Autopilot 或你的编码智能体在工作时，看看它正在生成什么，或者提前阅读下一个选项卡。
    - **休息时间也可以用来追赶进度。** 如果休息开始时你的编码智能体还在构建，就让它继续运行，你先去休息。
    - **测试集有备用方案。** 讲师会在共享文件夹中发布 `DemoUiBankTests` 包。如果你自己的测试用例没能及时完成自动化，在创建和运行测试集时使用讲师的包即可——你仍然会运行一个测试集并查看它的执行。

!!! tip "培训环境"
    在 **[{{ training_url }}]({{ training_url }})** 登录，使用租户 **{{ training_tenant }}**。
