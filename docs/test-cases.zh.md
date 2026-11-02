动手实践 · 第 2 部分，共 4 部分
{: .eyebrow }

# 🧪 测试用例 { #test-cases }

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">先生成，再手动自动化一个，其余交给智能体</div>

## 🤖 让 Autopilot in Test Manager 创建测试用例 { #ask-autopilot-in-test-manager-to-create-test-cases }

**Test Case Generation Agent** 会根据需求编写测试用例，包含手动步骤和预期结果。

1. 在 Test Manager 的 **Requirements** 下打开一个需求，例如 **Login & Initial State Check**。
2. 让 Autopilot 为它生成测试用例。如需引导生成方向，可以从 **Prompt Library** 中选一个提示词：**Valid E2E Scenario Testing** 用于有效的端到端场景，**Boundary-Value Testing** 用于边界情况。
3. 检查生成的建议。保留正常路径（happy path），并将其命名为 **Login & Initial State Check**。再保留一两个反向用例，例如密码错误。其余的丢弃。
4. 打开 **Login & Initial State Check**，阅读它的手动步骤。每一步都需要一个操作，以及一个你能在屏幕上检查的预期结果。

!!! tip "Prompt Library"
    Prompt Library 中包含预定义的提示词，例如 **Valid E2E Scenario Testing**、**End-to-End Flow Verification**、**Rapid Test Idea Generation**、**Elusive Issue Detection** 和 **Boundary-Value Testing**，以及你的团队保存的自定义提示词。对一个需求效果好的提示词通常也适用于下一个，所以把好用的保存下来。

## ✍️ 手动实现 Login 测试用例 { #implement-the-login-test-case-by-hand }

在让任何智能体为你自动化测试之前，先自己做一个。这会花更多时间，而这正是目的：当智能体五分钟就做完时，你会清楚地知道要检查什么。

<div style="background: #16213e; border-left: 10px solid #FA4616; padding: 22px 28px; margin: 1.2rem 0 1.4rem;">
  <div style="font-size: 19px; font-weight: 700; color: #ffffff; line-height: 1.35;">每个 UiPath 测试用例都有三个部分：Given、When、Then。</div>
  <div style="font-size: 15px; font-style: italic; color: #f6c3ab; margin-top: 9px;">准备测试所需的内容。执行被测的那一个操作。检查应用显示的内容。</div>
</div>

**创建测试用例**

1. 在 **Studio** 中，从你的 Test Manager 测试用例里找到 **Login & Initial State Check**，并创建一个与之关联的 Studio 测试用例。文件命名为 `T0_LoginAndInitialStateCheck.xaml`，与讲师参考包中的名称相同。
2. 新的测试用例打开后包含三个序列：**Given**、**When** 和 **Then**。

**Given：准备**

3. 这个测试无需添加任何内容：它只需要你注册的 ParaBank 用户和你的凭据资产。让 **Given** 保持为空。凭据在 **When** 中读取，位于输入凭据的那个浏览器卡片内。

**When：登录并读取 Accounts Overview**

4. 在 Chrome 中打开 `https://parabank.parasoft.com/parabank/index.htm`。
5. 添加一个 **Use Application/Browser** 活动，并指定 ParaBank 首页。
6. 在 **Use Application/Browser** 卡片内、任何 **Type Into** 之前，添加一个 **Get Credential** 活动。将资产名称设为 `{YourName}_ParaBankCredential`，文件夹设为 `{{ training_folder }}`。把输出保存到 `var_Username`（String）和 `var_Password`（SecureString）。
7. 在 **Customer Login** 面板中，为 **Username** 字段添加 **Type Into**，使用 `var_Username`；为 **Password** 字段添加 **Type Into**，以安全文本方式使用 `var_Password`。
8. 在 **Log In** 上添加 **Click**。
9. 在 **Accounts Overview** 标题上添加 **Check App State**。ParaBank 在 Log In 之后会直接打开 **Accounts Overview**，所以这个标题能证明登录成功。把结果保存到 `var_OverviewShown`（Boolean）。
10. 在左侧面板的 *"Welcome <First Name> <Last Name>"* 文本上添加 **Get Text**，并保存到 `var_WelcomeText`。
11. 在 **Accounts Overview** 表格（**Account**、**Balance\***、**Available Amount**）上添加 **Extract Table Data**，并保存到 `dt_InitialAccounts`。把第一个账号保存到 `var_FundingAccountId`。

**Then：验证**

12. 添加 **Verify Expression**，使用 `var_OverviewShown`。
13. 添加 **Verify Expression**，检查 `var_WelcomeText` 包含你的名和姓。
14. 添加 **Verify Expression**，检查 `dt_InitialAccounts` 至少有一个账户。每个新的 ParaBank 用户都会有一个默认 checking 账户。
15. 在每个验证上打开截图选项，让证据附加到结果中。

**运行它**

16. 在 **Test Explorer** 中运行测试用例。三个验证都必须通过。
17. 再运行一次。它必须再次通过。

!!! warning "把密码保留在浏览器卡片内"
    当 SecureString 在创建它的作用域之外使用时，Workflow Analyzer 规则 **ST-SEC-008** 会让构建失败。如果 **Get Credential** 放在 **Given** 中，或者密码作为参数传给另一个工作流，`uip rpa validate` 可能仍然通过，但 Studio 的构建和 `uip rpa build` 会失败，报错 *"SecureString variable used outside of the creation scope"*。请在输入凭据的那个 **Use Application/Browser** 卡片内读取凭据。

!!! info "登录失败并显示 *"The username and password could not be verified."*？"
    ParaBank 的共享演示数据库很可能被重置了。请在 [register.htm](https://parabank.parasoft.com/parabank/register.htm) 用相同的用户名和密码重新注册你的用户，然后再次运行测试用例。不要修改测试：问题出在数据上。

!!! tip "使用 Object Repository"
    指定目标元素时，把它保存到 **Object Repository**。下一个测试用例中使用的智能体会复用这些目标元素，所以你手动捕获的登录字段，就是 Autopilot 和你的编码智能体在此基础上构建的内容。

!!! success "Login 测试用例完成"
    `T0_LoginAndInitialStateCheck.xaml` 已关联到它的 Test Manager 测试用例，并通过了两次，每个验证都有截图。记下它花了多长时间，你会把它和下一个测试用例进行比较。

## 🪄 用 Autopilot 或编码智能体生成下一个测试用例 { #generate-the-next-test-case-with-autopilot-or-a-coding-agent }

现在让智能体来自动化下一个。选一个 Login 之后的需求，例如 **Open a Checking Account**。先像为 Login 做的那样，在 Test Manager 中为它生成测试用例，并将正常路径保留为 **Open a Checking Account**。

!!! warning "使用 Autopilot 实际生成的测试用例名称"
    Autopilot in Test Manager 给测试用例命名的方式并不总是一样。你的可能叫 **Checking Account Opening**、**Step 1: Open a Checking Account** 或其他名称。请在 Test Manager 的 **Test Cases** 下查看确切名称，并在下面提示词中所有出现 **Open a Checking Account** 的地方使用它。否则 Studio、Autopilot 或你的编码智能体会把自动化关联到错误的测试用例，或者找不到测试用例。

然后用这个提示词来自动化它。你可以把它交给 Autopilot in Studio Desktop，也可以交给编码智能体。提示词相同，只是输入的位置不同：

```text
In this test automation project, which is connected to my
{YourName}_PB_Test Test Manager project, automate the Test Manager test
case "Open a Checking Account" as T1_OpenACheckingAccount.xaml,
linked to that test case.

Use Given / When / Then. Given logs in, reusing the login steps and Object
Repository targets from T0_LoginAndInitialStateCheck.xaml. Read the
credential asset {YourName}_ParaBankCredential from the {{ training_folder }}
folder inside the browser scope that types it, and don't pass the password
as an argument. Given also reads the first account in Accounts Overview into
var_FundingAccountId. When selects Open New Account, picks CHECKING, picks
var_FundingAccountId as the funding account, stores the minimum deposit
shown on the page in var_MinDeposit, and selects Open New Account. Then
verifies "Account Opened!", reads the number after "Your new account
number:" into var_CheckingAccountId, and verifies that Accounts Overview
lists var_CheckingAccountId with a balance of var_MinDeposit, with a
screenshot on every verification.

Capture any new UI targets from the live ParaBank site into the Object
Repository. Don't write selectors by hand. Inspect the project before you
edit it, then validate and build it. Ask me before you run it.
```

=== "Autopilot in Studio Desktop"

    1. 在 **Studio** 中打开你的 `{YourName}ParaBankTests` 项目，然后打开 **Autopilot** 面板。
    2. 把提示词粘贴到 **Ask Autopilot anything** 中并发送。
    3. 在接受之前检查 Autopilot 提出的内容：**Given** 是否先登录？**Then** 是否检查了 *"Account Opened!"*，以及 **Accounts Overview** 是否列出了新账号？
    4. 接受更改，然后在 **Test Explorer** 中运行该测试用例两次。

=== "编码智能体（Codex、Claude Code）"

    1. 在 **Studio** 中打开你的 `{YourName}ParaBankTests` 项目，然后打开窗口底部的 **Terminal** 面板。它会在你的项目文件夹中打开。
    2. 在那里启动你的编码智能体：

        ```bash
        claude
        # or
        codex
        ```

    3. 把提示词粘贴到终端中并按 **Enter**。
    4. 回答它的问题，并在批准之前阅读它提出的每条命令。
    5. 完成后，在 **Test Explorer** 中运行该测试用例两次。

    编码智能体会加载 `uipath-rpa` 技能，先读取项目和你的 Login 测试用例，然后编写新的测试用例。如果它无法在浏览器中访问 ParaBank，它不会猜测选择器，而是把无法定位目标的活动命名为 `TODO Indicate — …`。请在 Studio 中指定这些目标元素，或者在 Chrome 中打开 ParaBank，让它再试一次。

!!! warning "检查、验证并修正生成的测试用例"
    无论是哪个智能体构建的，测试用例都需要你来签字确认。继续之前，在 Studio 中打开它，对照它的 Test Manager 测试用例和设计文档进行检查：

    - **Given** 会登录并准备测试所需的一切，所以它可以独立运行。
    - **When** 按手动步骤所描述的操作，在正确的界面和字段上执行。
    - **Then** 用正确的值验证每一个预期结果，并且每个验证都有截图。
    - 它在 **Test Explorer** 中运行并通过两次。

    如果有错误或遗漏，就修正它：在 Studio 中自己编辑，对单个表达式使用 Autopilot，或者让智能体修复，并准确告诉它哪里有问题。

和你手动构建的 Login 测试用例比较一下：

- 花了多长时间？
- 结果和你做的一样易读吗？你会不读它的 **Then** 部分就信任它吗？
- 它复用了你的登录目标元素，还是捕获了新的？

!!! warning "一次只在一个地方修改"
    Studio、Autopilot 和你的编码智能体都可以编辑同一批文件。在编码智能体修改文件之前，先在 Studio 中关闭该文件；你在 Studio 中改了什么，也要告诉编码智能体，让它重新读取项目，而不是覆盖你的工作。

!!! tip "Autopilot for Developers"
    在检查生成的测试用例时，可以对单个表达式使用 Autopilot。在 **Expression Editor** 中，对任何有验证错误的表达式选择 **Fix**（魔法棒），或者在底部的 Autopilot 框中输入指令，例如 *"Build the payee name AutoPayee_ followed by the current time as yyyyMMddHHmm."*

## 🎬 在 Test Manager 中 Run Autonomously { #run-autonomously-in-test-manager }

并不是每个测试用例都需要先有自动化才能运行。在 Test Manager 中，Autopilot 可以**自主**运行测试用例：它读取手动步骤，直接在应用上执行，然后为每一步记录结果和证据。

在从 **Update Contact Info** 需求生成的测试用例上试一试：

1. 在 Test Manager 的 **Requirements** 下，打开 **Update Contact Info**（`{YourPrefix}:8`，即设计文档中的 Step 7）。
2. 让 Autopilot 为它生成测试用例，并从 **Prompt Library** 中选择 **Rapid Test Idea Generation**。它会快速返回许多简短的测试想法。
3. 查看这些想法，挑选一个用于自主运行，例如 *"Update the phone number and verify that the new number is saved"*。保留它，丢弃其余的。
4. 打开该测试用例，阅读它的手动步骤。每一步都需要一个操作，以及一个可以在屏幕上检查的预期结果。修改任何含糊的步骤。
5. 该测试用例必须先登录。把密码写成 `{{ '{{' }}credential:{YourName}_ParaBankCredential{{ '}}' }}`，而不是直接在步骤中输入密码。
6. 打开 **Manual Steps** 选项卡，选择 **Run autonomously**。根据版本不同，该按钮可能显示为 **Run with Autopilot**。
7. 输入目标 URL `https://parabank.parasoft.com/parabank/index.htm`。在你输入之前，**Run** 一直不可用。
8. 选择讲师指定的模型。
9. 如果你想实时观看测试用例的运行过程，请在选择 **Run** 之前打开 **live streaming**。
10. 选择 **Run**。
11. 完成后打开结果。每一步的执行都有记录，在步骤结果旁边附有 Autopilot 所见内容的截图。

!!! warning "自主运行需要 Test Cloud 和 Windows 机器人"
    只有当 Test Manager 通过 **Test Cloud** 提供时，才能使用自主测试执行，并且仅支持 **Windows** 环境。它会作为作业在 `{{ training_folder }}` 文件夹中的 Windows 机器人上运行。如果只连接了 macOS 机器人，运行会一直处于 **Pending**，并且不会创建 Orchestrator 作业。如果你的运行一直处于 Pending，请告诉讲师，等有 Windows 机器人可用时再发起新的运行。参见[为什么我的执行一直处于 Pending？](executions.md#why-does-my-execution-stay-pending)

以小组形式讨论：

- 什么时候你会选择自主运行测试用例，而不是把它自动化？对新功能的一次性检查，或者每个迭代都会变化的测试用例，都是不错的选择。
- 什么样的手动步骤便于 Autopilot 执行？和便于人执行的一样：一个操作，一个预期结果，使用屏幕上的确切标签。

## ➕ 再实现几个测试用例 { #implement-a-few-more-test-cases }

再选两三个需求，重复这个循环：在 Test Manager 中生成测试用例，保留正常路径，用 Autopilot in Studio Desktop 或你的编码智能体将其自动化。建议顺序如下，并列出每个测试用例的 **Given** 必须准备的内容，以便它独立运行：

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Open a Savings Account</span>

📄 `T2_OpenASavingsAccount.xaml`

**Given：** 登录，读取 `var_FundingAccountId`

**Then：** *"Account Opened!"*；Savings 账户已列出，资金账户扣除了开户存款

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Transfer Funds Between Accounts</span>

📄 `T3_TransferFundsBetweenAccounts.xaml`

**Given：** 登录，开设一个 Checking 账户和一个 Savings 账户，读取两个余额

**Then：** *"Transfer Complete!"*；Checking = 转账前 − `var_TransferAmount`；Savings = 转账前 + `var_TransferAmount`

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Pay a Bill</span>

📄 `T4_PayABill.xaml`

**Given：** 登录，开设一个用于付款的 Savings 账户

**Then：** *"Bill Payment Complete"*，包含 `var_PayeeName`、`var_BillAmount` 和该 Savings 账户

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Find Transactions & Account Activity</span>

📄 `T5_FindTransactionsAndAccountActivity.xaml`

**Given：** 登录，开设一个 Savings 账户，向其转入 `var_TransferAmount`，并从中支付一笔账单

**Then：** **Find by Amount** 显示账单付款；**Find by Date** 显示收到的转账

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Request a Loan</span>

📄 `T6_RequestALoan.xaml`

**Given：** 登录，读取 `var_FundingAccountId`

**Then：** *"Loan Request Processed"*；如果获批，`var_LoanAccountId` 已列出，余额 = `var_LoanAmount`

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Update Contact Info</span>

📄 `T7_UpdateContactInfo.xaml`

**Given：** 登录

**Then：** *"Profile Updated"*；重新打开页面后显示 `var_NewPhone`

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Logout & Evidence Collection</span>

📄 `T8_LogoutAndEvidenceCollection.xaml`

**Given：** 登录

**Then：** **Customer Login** 面板重新出现；**Account Services** 不再显示

</div>

</div>

!!! warning "不要假设贷款会被批准"
    ParaBank 的贷款审批结果取决于演示环境的配置和源账户中的资金。让 `var_LoanAmount` 和 `var_DownPayment` 保持较小，并读取屏幕上的 **Status**。如果是 **Denied**，测试会按设计文档的要求失败，并附上原因和截图，方便你查看原因。

!!! tip "余额检查失败？"
    先看截图，再看代码。常见原因是：余额以带货币符号的文本形式读取（`$1,000.00` 在解析之前不是数字），或者在账户摘要刷新之前就读取了余额。Expression Editor 中的 Autopilot 能快速完成转换：*"Convert this text, for example "$1,000.00", to a Decimal."*

## 🧹 找出过时的测试用例 { #find-obsolete-test-cases }

应用会变化，而测试用例却停留在原地。过时的测试用例会因为错误的原因失败，或者根本无法运行，却仍然被算作覆盖率。更新后的设计文档包含十个回归测试用例，**TC-PB-002** 到 **TC-PB-011**（参见[回归测试用例](agentic-testing-hands-on.md#the-regression-test-cases)）。其中一些已经和 ParaBank 不再匹配。Autopilot in Test Manager 可以把它们找出来。

**把回归测试用例添加到 Test Manager**

1. 在 Test Manager 中，打开每个回归测试用例所属的需求，例如 **Login & Initial State Check**（`{YourPrefix}:1`）。
2. 让 Autopilot 生成测试用例，附上设计文档，并给它以下指令：

    ```text
    Create one test case for each regression test case in section 6 of the attached design document that belongs to this requirement. Name each one with its ID and name, for example "TC-PB-003 Login with Invalid Credentials". Copy its steps and expected results as written. Don't add, merge, fix, or skip any test case.
    ```

3. 检查每个测试用例是否都关联到了它的需求。对表中的其他需求重复这些步骤，或者在小组内分工完成。

!!! tip "或者让你的编码智能体来做"
    借助 `uipath-test` 技能，你的编码智能体可以在你的 Test Manager 项目中创建这些测试用例，并把它们关联到需求：*"Read section 6 of E2E ParaBank Online Banking.docx. In my Test Manager project {YourName}_PB_Test, create one test case per regression test case, named with its ID and name, with its steps, and link each one to the requirement in this table."* 继续之前，先在 Test Manager 中检查结果。

**让 Autopilot 找出过时的测试用例**

1. 在 **Requirements** 下，打开 **Login & Initial State Check**。它有四个回归测试用例，其中至少有一个已经过时。
2. 选择 **Optimize coverage**，然后选择 **Find obsolete tests**。
3. 在 **Add documents** 中，选择设计文档，或者上传它。选择 **Next**。
4. 在 **Provide additional guidance** 中输入：

    ```text
    The application under test is ParaBank at https://parabank.parasoft.com/parabank/index.htm. A test case is obsolete if it uses a screen, button, field, or flow that ParaBank doesn't have, or if its steps no longer match this requirement. For each obsolete test case, name the step that can't be done.
    ```

5. 保留默认模型，或者选择讲师指定的模型，然后选择 **Find obsolete tests**。
6. 等待通知：*Obsolete tests discovered* 或 *No obsolete test cases discovered*。打开该需求查看最新结果。
7. 对 **Request a Loan** 和 **Transfer Funds Between Accounts** 重复这些步骤。

**先检查，再决定**

Autopilot 提出建议，由你来决定。对于它标记的每个测试用例，打开 ParaBank，找一找该测试用例需要的界面或按钮。然后：

- **已过时：** 添加标签 `Obsolete`，并将它从需求中取消分配。不要删除它：可能还有人需要它的历史记录。
- **未过时：** 保留它，并记下 Autopilot 判断错误的原因。

再反过来检查一遍：Autopilot 是否漏掉了你知道无法运行的测试用例？

??? success "讲师核对：哪些测试用例已经过时？"
    有五个测试用例描述的是 ParaBank 不具备的功能：

    - **TC-PB-005 Rename Account Nickname：** **Account Details** 中没有 **Edit Nickname**。
    - **TC-PB-007 Loan Status Lookup by Loan ID：** 没有 **Loan Status** 菜单，`/parabank/loanstatus.htm` 也不存在。
    - **TC-PB-008 Transfer Funds - Review & Confirm：** **Transfer** 会立即转账，没有确认界面。
    - **TC-PB-010 Login with SMS One-Time Password：** ParaBank 没有第二个身份验证因素。
    - **TC-PB-011 Download Account Statement (PDF)：** **Account Details** 中没有 **Statements** 部分，也无法下载 PDF。

    其余五个仍然适用：TC-PB-002、TC-PB-003、TC-PB-004、TC-PB-006 和 TC-PB-009。TC-PB-009 取决于演示环境的贷款规则，所以请在屏幕上检查它的 **Status**。

以小组形式讨论：

- 这些测试用例是怎么进入设计文档的？某个功能曾被计划、后来被移除，或者属于另一家银行的应用。在你的项目中，哪种情况会发生？
- 过时的测试用例会让你付出什么代价：一次失败的运行、一个虚假的覆盖率数字，还是花时间去修复一个针对已不存在功能的测试？

!!! success "测试用例完成"
    至少四个自动化测试用例，每个都关联到对应的 Test Manager 测试用例并能独立通过：Login 是手动构建的，其余由 Autopilot 或你的编码智能体构建。另外还有几个由 Autopilot 生成的仅手动测试用例、一次自主运行，以及已添加标签并取消分配的过时回归测试用例。

!!! tip "你的自动化还无法构建？"
    你仍然可以完成 Test Sets 部分。把讲师的 `DemoParaBankTests` 包关联到你的测试用例，从 T0 到 T8 每个步骤一个。参见 Test Sets 中的[自动化测试用例不够？](test-sets.md#run-the-test-sets)。
