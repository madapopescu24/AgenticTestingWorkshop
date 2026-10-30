动手实践 · 第 2 部分，共 4 部分
{: .eyebrow }

# 🧪 测试用例 { #test-cases }

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">先生成，再手动自动化一个，其余交给智能体</div>

## 🤖 让 Autopilot in Test Manager 创建测试用例 { #ask-autopilot-in-test-manager-to-create-test-cases }

**Test Case Generation Agent** 会根据需求编写测试用例，包含手动步骤和预期结果。

1. 在 Test Manager 的 **Requirements** 下打开一个需求，例如 **Login and Initial Account State**。
2. 让 Autopilot 为它生成测试用例。如需引导生成方向，可以从 **Prompt Library** 中选一个提示词：**Valid E2E Scenario Testing** 用于有效的端到端场景，**Boundary-Value Testing** 用于边界情况。
3. 检查生成的建议。保留正常路径（happy path），并将其命名为 **Login and Initial Account State**。再保留一两个反向用例，例如密码错误。其余的丢弃。
4. 打开 **Login and Initial Account State**，阅读它的手动步骤。每一步都需要一个操作，以及一个你能在屏幕上检查的预期结果。

!!! tip "Prompt Library"
    Prompt Library 中包含预定义的提示词，例如 **Valid E2E Scenario Testing**、**End-to-End Flow Verification**、**Rapid Test Idea Generation**、**Elusive Issue Detection** 和 **Boundary-Value Testing**，以及你的团队保存的自定义提示词。对一个需求效果好的提示词通常也适用于下一个，所以把好用的保存下来。

## ✍️ 手动实现 Login 测试用例 { #implement-the-login-test-case-by-hand }

在让任何智能体为你自动化测试之前，先自己做一个。这会花更多时间，而这正是目的：当智能体五分钟就做完时，你会清楚地知道要检查什么。

<div style="background: #16213e; border-left: 10px solid #FA4616; padding: 22px 28px; margin: 1.2rem 0 1.4rem;">
  <div style="font-size: 19px; font-weight: 700; color: #ffffff; line-height: 1.35;">每个 UiPath 测试用例都有三个部分：Given、When、Then。</div>
  <div style="font-size: 15px; font-style: italic; color: #f6c3ab; margin-top: 9px;">准备测试所需的内容。执行被测的那一个操作。检查应用显示的内容。</div>
</div>

**创建测试用例**

1. 在 **Studio** 中，从你的 Test Manager 测试用例里找到 **Login and Initial Account State**，并创建一个与之关联的 Studio 测试用例。文件命名为 `T0_LoginAndInitialAccountState.xaml`，与讲师参考包中的名称相同。
2. 新的测试用例打开后包含三个序列：**Given**、**When** 和 **Then**。

**Given：准备**

3. 这个测试无需添加任何内容：它只需要你注册的 UiBank 用户和你的凭据资产。让 **Given** 保持为空。凭据在 **When** 中读取，位于输入凭据的那个浏览器卡片内。

**When：登录并打开 Accounts**

4. 在 Chrome 中打开 `https://uibank.uipath.com/login`。如果无法打开，请使用[备用地址](setup.md#4-register-your-uibank-test-user)：`https://purple-dune-0af054403.6.azurestaticapps.net/login`。
5. 添加一个 **Use Application/Browser** 活动，并指定 UiBank 登录页面。
6. 在 **Use Application/Browser** 卡片内、任何 **Type Into** 之前，添加一个 **Get Credential** 活动。将资产名称设为 `{YourName}_UiBankCredential`，文件夹设为 `{{ training_folder }}`。把输出保存到 `var_Username`（String）和 `var_Password`（SecureString）。
7. 为 **Enter username** 字段添加 **Type Into**，使用 `var_Username`；为 **Enter password** 字段添加 **Type Into**，以安全文本方式使用 `var_Password`。
8. 在 **Sign In** 上添加 **Click**。
9. 在 UiBank **Important Notice** 对话框的 **I agree to the Privacy Policy** 按钮上添加 **Check App State**，并设置较短的超时时间。如果它出现，就 **Click** 它；如果没出现，就继续。
10. 在 *"Here is your account summary"* 上方的 **Welcome!** 标题上添加 **Check App State**。UiBank 在 Sign In 之后会直接打开 **Accounts**，所以这个标题能证明登录成功。把结果保存到 `var_WelcomeShown`（Boolean）。
11. 在账户摘要区域添加 **Get Text**，并保存到 `var_AccountSummary`。

**Then：验证**

12. 添加 **Verify Expression**，使用 `var_WelcomeShown`。
13. 添加 **Verify Expression**，检查 `var_AccountSummary` 要么包含 *"No accounts at this time"*，要么至少列出一个账户。
14. 在每个验证上打开截图选项，让证据附加到结果中。

**运行它**

15. 在 **Test Explorer** 中运行测试用例。两个验证都必须通过。
16. 再运行一次。它必须再次通过。

!!! warning "把密码保留在浏览器卡片内"
    当 SecureString 在创建它的作用域之外使用时，Workflow Analyzer 规则 **ST-SEC-008** 会让构建失败。如果 **Get Credential** 放在 **Given** 中，或者密码作为参数传给另一个工作流，`uip rpa validate` 可能仍然通过，但 Studio 的构建和 `uip rpa build` 会失败，报错 *"SecureString variable used outside of the creation scope"*。请在输入凭据的那个 **Use Application/Browser** 卡片内读取凭据。

!!! info "Important Notice 对话框"
    从第二次登录开始，UiBank 可能会显示一个 **Important Notice**，其中有 **I agree to the Privacy Policy →** 和 ✕。用 ✕ 关闭它会让你处于未登录状态，之后的每一步都会失败。在自动化之前先手动接受一次，并在每个需要登录的测试中保留第 9 步。

!!! tip "使用 Object Repository"
    指定目标元素时，把它保存到 **Object Repository**。下一个测试用例中使用的智能体会复用这些目标元素，所以你手动捕获的登录字段，就是 Autopilot 和你的编码智能体在此基础上构建的内容。

!!! success "Login 测试用例完成"
    `T0_LoginAndInitialAccountState.xaml` 已关联到它的 Test Manager 测试用例，并通过了两次，每个验证都有截图。记下它花了多长时间，你会把它和下一个测试用例进行比较。

## 🪄 用 Autopilot 或编码智能体生成下一个测试用例 { #generate-the-next-test-case-with-autopilot-or-a-coding-agent }

现在让智能体来自动化下一个。选一个 Login 之后的需求，例如 **Checking Account Creation**。先像为 Login 做的那样，在 Test Manager 中为它生成测试用例，并将正常路径保留为 **Checking Account Creation**。

!!! warning "使用 Autopilot 实际生成的测试用例名称"
    Autopilot in Test Manager 给测试用例命名的方式并不总是一样。你的可能叫 **Open a Checking Account**、**Step 1: Open a Checking Account** 或其他名称。请在 Test Manager 的 **Test Cases** 下查看确切名称，并在下面提示词中所有出现 **Checking Account Creation** 的地方使用它。否则 Studio、Autopilot 或你的编码智能体会把自动化关联到错误的测试用例，或者找不到测试用例。

然后用这个提示词来自动化它。你可以把它交给 Autopilot in Studio Desktop，也可以交给编码智能体。提示词相同，只是输入的位置不同：

```text
In this test automation project, which is connected to my
{YourName}_UIB_Test Test Manager project, automate the Test Manager test
case "Checking Account Creation" as T1_CheckingAccountCreation.xaml,
linked to that test case.

Use Given / When / Then. Given logs in, reusing the login steps and Object
Repository targets from T0_LoginAndInitialAccountState.xaml. Read the
credential asset {YourName}_UiBankCredential from the {{ training_folder }}
folder inside the browser scope that types it, and don't pass the password
as an argument. After Sign In, click "I agree to the Privacy Policy" only
if UiBank's Important Notice appears. When applies for a Checking account
with the nickname AutoChecking_<yyyyMMddHHmmss>. Then verifies that the
confirmation page shows that nickname, and that the account is listed in
the account summary with its nickname, with a screenshot on every
verification. UiBank doesn't display the account type after creation, so
don't check it.

Capture any new UI targets from the live UiBank site into the Object
Repository. Don't write selectors by hand. Inspect the project before you
edit it, then validate and build it. Ask me before you run it.
```

=== "Autopilot in Studio Desktop"

    1. 在 **Studio** 中打开你的 `{YourName}UiBankTests` 项目，然后打开 **Autopilot** 面板。
    2. 把提示词粘贴到 **Ask Autopilot anything** 中并发送。
    3. 在接受之前检查 Autopilot 提出的内容：**Given** 是否先登录？**Then** 是否检查确认页面和账户摘要显示了新的昵称？
    4. 接受更改，然后在 **Test Explorer** 中运行该测试用例两次。

=== "编码智能体（Codex、Claude Code）"

    1. 在 **Studio** 中打开你的 `{YourName}UiBankTests` 项目，然后打开窗口底部的 **Terminal** 面板。它会在你的项目文件夹中打开。
    2. 在那里启动你的编码智能体：

        ```bash
        claude
        # or
        codex
        ```

    3. 把提示词粘贴到终端中并按 **Enter**。
    4. 回答它的问题，并在批准之前阅读它提出的每条命令。
    5. 完成后，在 **Test Explorer** 中运行该测试用例两次。

    编码智能体会加载 `uipath-rpa` 技能，先读取项目和你的 Login 测试用例，然后编写新的测试用例。如果它无法在浏览器中访问 UiBank，它不会猜测选择器，而是把无法定位目标的活动命名为 `TODO Indicate — …`。请在 Studio 中指定这些目标元素，或者在 Chrome 中打开 UiBank，让它再试一次。

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
    在检查生成的测试用例时，可以对单个表达式使用 Autopilot。在 **Expression Editor** 中，对任何有验证错误的表达式选择 **Fix**（魔法棒），或者在底部的 Autopilot 框中输入指令，例如 *"Build the nickname AutoChecking_ followed by the current time as yyyyMMddHHmmss."*

## 🎬 在 Test Manager 中 Run Autonomously { #run-autonomously-in-test-manager }

并不是每个测试用例都需要先有自动化才能运行。在 Test Manager 中，Autopilot 可以**自主**运行测试用例：它读取手动步骤，直接在应用上执行，然后为每一步记录结果和证据。

在 Autopilot 生成测试用例时你保留的某个反向登录测试用例上试一试：

1. 在 Test Manager 的 **Test Cases** 下，打开一个有手动步骤但没有自动化的测试用例。
2. 如果某一步需要登录，把密码写成 `{{ '{{' }}credential:{YourName}_UiBankCredential{{ '}}' }}`，而不是直接在步骤中输入密码。
3. 打开 **Manual Steps** 选项卡，选择 **Run autonomously**。根据版本不同，该按钮可能显示为 **Run with Autopilot**。
4. 输入目标 URL `https://uibank.uipath.com/login`；如果你使用备用地址，则输入 `https://purple-dune-0af054403.6.azurestaticapps.net/login`。在你输入之前，**Run** 一直不可用。
5. 选择讲师指定的模型。
6. 如果你想实时观看测试用例的运行过程，请在选择 **Run** 之前打开 **live streaming**。
7. 选择 **Run**。
8. 完成后打开结果。每一步的执行都有记录，在步骤结果旁边附有 Autopilot 所见内容的截图。

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
<span class="f-title" markdown="span">Savings Account Creation</span>

📄 `T2_SavingsAccountCreation.xaml`

**Given：** 登录

**Then：** 确认页面和账户摘要显示 Savings 昵称

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Funds Transfer Between Accounts</span>

📄 `T3_FundsTransferBetweenAccounts.xaml`

**Given：** 登录，开设一个 Checking 账户和一个 Savings 账户，读取两个余额

**Then：** Checking = 转账前 − `var_TransferAmount`；Savings = 转账前 + `var_TransferAmount`

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Loan Application Submission</span>

📄 `T4_LoanApplicationSubmission.xaml`

**Given：** 登录

**Then：** 捕获结果消息；返回 Loan ID

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Loan Status Lookup</span>

📄 `T5_LoanStatusLookup.xaml`

**Given：** 登录，提交贷款，保留 `var_LoanID`

**Then：** 金额和期限一致

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">User Profile Identity Verification</span>

📄 `T6_UserProfileIdentityVerification.xaml`

**Given：** 登录

**Then：** 用户名和邮箱一致

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Logout and Evidence Collection</span>

📄 `T7_LogoutAndEvidenceCollection.xaml`

**Given：** 登录

**Then：** 会话已关闭；顶部菜单不再可用

</div>

</div>

!!! warning "不要假设贷款会被批准"
    UiBank 的贷款审批规则没有文档说明。只要返回了 Loan ID，并且查询显示的金额和期限一致，无论贷款被批准还是被拒绝，贷款测试都必须通过。

!!! tip "余额检查失败？"
    先看截图，再看代码。常见原因是：余额以带货币符号的文本形式读取（`$1,000.00` 在解析之前不是数字），或者在账户摘要刷新之前就读取了余额。Expression Editor 中的 Autopilot 能快速完成转换：*"Convert this text, for example "$1,000.00", to a Decimal."*

!!! success "测试用例完成"
    至少四个自动化测试用例，每个都关联到对应的 Test Manager 测试用例并能独立通过：Login 是手动构建的，其余由 Autopilot 或你的编码智能体构建。另外还有几个由 Autopilot 生成的仅手动测试用例，以及一次自主运行。

!!! tip "你的自动化还无法构建？"
    你仍然可以完成 Test Sets 部分。把讲师的 `DemoUiBankTests` 包关联到你的测试用例，从 T0 到 T7 每个步骤一个。参见 Test Sets 中的[自动化测试用例不够？](test-sets.md#run-the-test-sets)。
