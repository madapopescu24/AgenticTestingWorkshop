演示讲解 + 演示
{: .eyebrow }

# 🧩 SAP 测试 { #sap-testing }

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">同一个 Test Cloud，用于 SAP</div>

今天一整天，你测试的是一个小型 Web 应用 UiBank。现在你会看到，同一个 **Test Cloud**——**Test Manager**、**Autopilot for Testers**、机器人和编码智能体——如何测试 SAP，这是企业运行的最关键的业务系统之一。你不需要 SAP 经验：关键术语都列在下面。

## 📖 两分钟了解 SAP { #sap-in-two-minutes }

**SAP** 开发 ERP 软件：企业用来运行财务、销售、采购、人力资源和生产的系统，所有业务共享同一套数据。

| 术语 | 含义 |
|---|---|
| **SAP ECC / SAP S/4HANA** | SAP ERP 的上一代和当前一代产品。许多企业正在从 ECC 迁移到 S/4HANA。 |
| **RISE with SAP** | SAP 提供的、迁移到云端 SAP S/4HANA 的方案。 |
| **SAP GUI / SAP Fiori** | 经典的 Windows 桌面客户端，以及现代的 Web 界面。 |
| **Transaction（事务）** | 在 SAP 中通过代码打开的一项功能，例如用 VA01 创建销售订单。 |
| **Transport（传输）** | 一组 SAP 变更，从开发环境移到测试环境，再到生产环境。每次传输都是需要重新测试的理由。 |
| **Order-to-Cash / Procure-to-Pay** | 端到端业务流程：从客户下单到收款，以及从采购申请到向供应商付款。 |
| **Clean Core** | SAP 的原则：保持标准系统不被修改，把自定义逻辑放到系统外部的扩展和 API 中。 |
| **SAP Cloud ALM** | SAP 用于管理实施项目的工具，包括需求和测试。 |

## 🤔 SAP 测试为什么难：覆盖率假象 { #why-sap-testing-is-hard-the-coverage-illusion }

SAP 团队长期以来报告的是**覆盖率**：已运行的事务或测试用例所占的百分比。但覆盖率衡量的是容易统计的东西，而不是可能出问题的地方。如今出问题的地方往往不在 SAP 内部，而在 SAP 与周边系统的衔接处。

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🧼</span>
<span class="f-title" markdown="span">Clean Core</span>

自定义逻辑从 ERP 中移出，放到扩展、SAP BTP 服务和 API 中。

</div>

<div class="feature" markdown>
<span class="f-icon">☁️</span>
<span class="f-title" markdown="span">SAP 周边的 SaaS</span>

Salesforce、ServiceNow 和 Workday 现在承担了过去在 SAP 中运行的部分业务。

</div>

<div class="feature" markdown>
<span class="f-icon">⏩</span>
<span class="f-title" markdown="span">更快的发布节奏</span>

SAP 每季度发布一次，其他厂商每周发布。流经企业的变更远多于十年前。

</div>

</div>

发布后期的典型故障包括：集成交接单独测试都通过，但同时运行时超时；季度发布后 SAP Fiori 界面发生偏移；权限变更悄无声息地产生错误结果。一份“100% SAP 覆盖率”的报告一个也发现不了。

## 💼 客户在哪些场景用 Test Cloud 测试 SAP { #where-customers-use-test-cloud-for-sap }

<div class="feature-grid cols-4" markdown>

<div class="feature" markdown>
<span class="f-icon">🔁</span>
<span class="f-title" markdown="span">回归测试</span>

跟上 SAP 的季度更新，只运行每次变更所影响的测试。

</div>

<div class="feature" markdown>
<span class="f-icon">🚚</span>
<span class="f-title" markdown="span">S/4HANA 迁移</span>

测试从数据准备到切换上线的每个阶段，并在各批次迁移中复用测试。

</div>

<div class="feature" markdown>
<span class="f-icon">🖥️</span>
<span class="f-title" markdown="span">SAP GUI 和 SAP Fiori</span>

自动化每一种 SAP 界面，界面变化时可以自愈。

</div>

<div class="feature" markdown>
<span class="f-icon">🔗</span>
<span class="f-title" markdown="span">跨系统流程</span>

测试横跨 SAP、Salesforce、Oracle、Workday 和自定义应用的端到端流程。

</div>

</div>

**客户获得的成果：** 3 年 529% 的 ROI，六个月回本；测试执行速度提升 62%，手动工作量减少 52%，测试覆盖率提高 55%。**EDF Renewables** 在五个月内实现了 90% SAP 测试的自动化。

## 🚀 Test Cloud 能为 SAP 做什么 { #what-test-cloud-does-for-sap }

### 🎯 决定测试什么 { #decide-what-to-test }

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🔥</span>
<span class="f-title" markdown="span">SAP Heatmap</span>

连接生产 SAP 系统，显示用户实际使用了哪些事务，让你优先测试关键业务事务。

</div>

<div class="feature" markdown>
<span class="f-icon">🎯</span>
<span class="f-title" markdown="span">Change Impact Analysis</span>

当一个传输被暂存时，AI 会找出它影响的流程，并给出一份按风险排序的待重跑测试清单，不必全部重跑。

</div>

<div class="feature" markdown>
<span class="f-icon">🕳️</span>
<span class="f-title" markdown="span">Test Gap Analysis</span>

找出还没有任何测试的关键 SAP 流程。

</div>

</div>

![SAP Application Usage Heatmap：SAP 组件和事务以方块显示，大小取决于使用频率](sap-testing.images/sap-usage-heatmap-W.png){ .screenshot .full }
*使用热图：方块越大，表示该 SAP 组件或事务的使用越多。*

![SAP Change Impact Dashboard，包含三个区域：SAP UI 变更、SAP API 变更和 SAP 安全](sap-testing.images/change-impact-analysis-W.png){ .screenshot .full }
*Change Impact Analysis 涵盖 UI 变更、API 变更和安全变更。*

### 🤖 创建测试并实现自动化 { #create-and-automate-the-tests }

<div class="feature-grid cols-4" markdown>

<div class="feature" markdown>
<span class="f-icon">📝</span>
<span class="f-title" markdown="span">生成测试用例</span>

Autopilot 根据需求或 Heatmap 数据为 SAP 事务创建测试用例，就像它为 UiBank 所做的那样。

</div>

<div class="feature" markdown>
<span class="f-icon">🧮</span>
<span class="f-title" markdown="span">生成测试数据</span>

SAP Test Data Agents 按需创建逼真的数据，例如客户、物料和销售订单。

</div>

<div class="feature" markdown>
<span class="f-icon">🛠️</span>
<span class="f-title" markdown="span">低代码或编码方式自动化</span>

业务用户和开发人员都可以构建自动化，在 Studio 中或借助编码智能体，就像你今天做的那样。

</div>

<div class="feature" markdown>
<span class="f-icon">🩹</span>
<span class="f-title" markdown="span">自愈</span>

当 SAP 界面变化时，自动化会实时修复选择器，而不是直接失败。

</div>

</div>

<div class="img-pair" markdown>

![Autopilot 为 VA01 事务建议了十个测试用例，都是创建销售订单的不同变体](sap-testing.images/test-case-creation-suggestions.png){ .screenshot }

![一个生成的测试用例 Verify Sales Order Creation with Standard Material 的手动步骤，从导航到 SAP Easy Access 界面到检查订单号](sap-testing.images/test-case-creation-manual-steps.png){ .screenshot }

</div>

*为 VA01（创建销售订单）生成的测试用例：左侧为建议列表，右侧为其中一个用例的手动步骤。*
{: .img-pair-caption }

### ▶️ 立即运行 { #run-them-right-away }

**Autonomous Test Execution** 根据手动 SAP 测试的自然语言步骤直接运行它——就是你在[测试用例](test-cases.md)中用过的 **Run Autonomously**。你从项目第一天起就可以开始测试，无需先有任何自动化。

![在 Test Manager 中用 Autopilot 运行 SAP-Create Sales Orders 测试用例：左侧是手动步骤，右侧是正在运行的检查](sap-testing.images/autonomous-test-execution-W.png){ .screenshot width="900" }
*在一个 SAP Fiori 测试用例上使用 Run Autonomously。*

### 🔗 融入 SAP 交付流程 { #fit-into-sap-delivery }

Test Cloud 可以连接 **SAP Cloud ALM**：Cloud ALM 管理需求，Test Cloud 在 SAP 和非 SAP 系统中自动化并运行测试，每个结果都会关联回对应的需求。它也能连接 CI/CD 工具。借助 **Maestro**，一条流水线就能测试整个流程——SAP 传输、Fiori 审批、Salesforce 同步以及发票——并给出一个统一的结论。

![SAP Cloud ALM 与 UiPath 如何协同：Cloud ALM 保存流程、需求、用户故事、缺陷和手动测试用例；UiPath 通过 API 提供自动化测试用例、测试数据和执行](sap-testing.images/cloud-alm-integration-W.png){ .screenshot width="900" }
*SAP Cloud ALM 编排测试；UiPath 自动化并运行测试，然后回传结果。请在解决方案设计阶段确认每个项目的集成选项。*

### 📈 负载下测试 { #test-under-load }

性能测试已内置于 Test Cloud。你可以复用已有的 UI 和 API 自动化，因此一套自动化同时覆盖功能测试和性能测试。

<div class="vs" markdown>
<div class="vs-side" markdown>
<span class="f-title" markdown="span">🧰 专用负载测试工具</span>

- 由性能工程师编写的一套独立脚本
- 协议层面的模拟 HTTP 流量

</div>
<div class="vs-mid">VS</div>
<div class="vs-side alt" markdown>
<span class="f-title" markdown="span">📈 Test Cloud 中的性能测试</span>

- 复用你的功能自动化，由 Autopilot 规划场景
- 通过 UI 体现真实用户体验，包括页面渲染

</div>
</div>

你可以在云端或本地运行负载测试、尖峰测试、压力测试和耐久测试，并由 CI/CD 流水线触发。结果显示在 Test Manager 中，与功能测试结果并列。

![Test Manager 左侧菜单中的 Performance Scenarios，位于 Requirements、Test Cases 和 Test Sets 旁边](sap-testing.images/performance-testing-test-manager-W.png){ .screenshot width="900" }
*Test Manager 中的 Performance Scenarios，就在你熟悉的 Test Cases 旁边。*

## 🎬 演示时间 { #demo-time }

讲师会在 Test Manager 中演示 **SAP Heatmap**，使用从 CSV 文件上传的演示用使用数据，而不是真实的 SAP 系统：

<div class="circles cols-5" markdown>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**加载使用数据**到一个 Heatmap 连接中

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**解读 Heatmap**：方块大小表示测试相关性，颜色表示覆盖率

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**确定优先级**：排名前 10 的事务，例如 Change Purchase Order (ME22N)

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**让方块变绿**：为事务创建测试用例，放进测试集并运行

</div>
</div>

<div class="circle-item" markdown>
<span class="num">5</span>
<div class="ci-body" markdown>

**找出测试缺口**：仍然没有测试用例的重要事务

</div>
</div>

</div>

## 📏 衡量流程，而不是测试用例 { #measure-processes-not-test-cases }

今天你按测试用例报告结果。在 SAP 环境中，业务方关心的是另一个问题：**order-to-cash** 能否从头到尾、在它涉及的每个系统中正常运行？

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🧭</span>
<span class="f-title" markdown="span">按业务流程报告</span>

“430 个测试中通过了 412 个”变成“Order-to-cash：Salesforce 交接环节有两个失败，都源于季度发布。”

</div>

<div class="feature" markdown>
<span class="f-icon">🔺</span>
<span class="f-title" markdown="span">端到端测试变得低成本</span>

生成的测试、自愈和编排运行，让端到端测试成为每次回归的基线。人的时间用于探索智能体无法预测的部分。

</div>

<div class="feature" markdown>
<span class="f-icon">🛡️</span>
<span class="f-title" markdown="span">QA 负责治理，智能体负责执行</span>

智能体生成、运行和分析测试。测试人员决定哪些流程必须保持通过，哪些风险可以接受。

</div>

</div>

## 🔄 与你今天所做内容的对应关系 { #how-it-maps-to-what-you-did-today }

<div class="circles cols-5" markdown>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**决定测试什么：** Heatmap 和 Change Impact Analysis。*今天：来自设计文档的需求。*

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**创建测试用例和数据：** Autopilot 和 Test Data Agents。*今天：Autopilot 生成了测试用例。*

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**立即运行：** Autonomous Test Execution。*今天：Run Autonomously。*

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**自动化并在机器人上运行。** *今天：Autopilot 或编码智能体自动化了测试用例，并由测试集运行它们。*

</div>
</div>

<div class="circle-item" markdown>
<span class="num">5</span>
<div class="ci-body" markdown>

**保持稳定运行并解释结果：** 自愈和测试洞察。*今天：对测试集结果使用 Generate Insights。*

</div>
</div>

</div>

## 📚 了解更多 { #learn-more }

<div class="link-grid" markdown>

<a class="link-card" href="https://www.uipath.com/platform/agentic-testing/sap-testing" target="_blank" rel="noopener"><span class="f-icon">🧩</span><span class="f-title">使用 Test Cloud 进行 SAP 测试</span><span class="f-text" markdown="span">用例、价值和常见问题</span></a>
<a class="link-card" href="https://www.uipath.com/platform/agentic-testing/performance-testing" target="_blank" rel="noopener"><span class="f-icon">📈</span><span class="f-title">性能测试</span><span class="f-text" markdown="span">基于现有自动化的负载、尖峰、压力和耐久测试</span></a>

</div>

!!! tip "培训环境"
    在 **[{{ training_url }}]({{ training_url }})** 登录，使用租户 **{{ training_tenant }}**。
