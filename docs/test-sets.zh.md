动手实践 · 第 4 部分，共 4 部分
{: .eyebrow }

# 📦 测试集 { #test-sets }

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">分组、运行并阅读结果</div>

## 📤 将你的测试项目发布到租户源 { #publish-your-testing-project-to-the-tenant-feed }

Autopilot 根据它在 Orchestrator 中能找到的自动化测试用例来构建测试集，而 Test Manager 从已发布的包中运行它们。所以先发布。

1. 在 **Studio** 中打开你的 `{YourName}UiBankTests` 项目，把测试用例标记为可发布。Studio 创建的测试用例默认是草稿，只有可发布的测试用例才会进入包中。在 **Project** 面板中，右键单击你自动化过的每个测试用例，选择 **Set as Publishable**。它的图标会变成蓝色。
2. 选择 **Publish**。
3. 在 **Publish to** 中选择 **Orchestrator Tenant Process Feed**。
4. 如果之前发布过，请提升版本号，然后选择 **Publish**。
5. 等待包已发布的确认消息。

!!! info "为什么用租户源"
    测试集的自动化运行只包含发布到 **Orchestrator Tenant Process Feed** 的最新包版本中的测试用例。发布到你个人工作区源的包，或者旧版本，都不会被使用。每次修改测试用例后都要重新发布。

## 🪄 让 Autopilot in Studio 创建测试集 { #ask-autopilot-in-studio-to-create-test-sets }

1. 在 **Studio** 中，在你的 `{YourName}UiBankTests` 项目里打开 **Autopilot** 面板。
2. 给 Autopilot 这个提示词：

    ```text
    In my {YourName}_UIB_Test Test Manager project, create two test sets from the
    existing test cases:
    - "UiBank Smoke" with Login and Initial Account State only.
    - "UiBank Regression" with every test case that is automated
      in this Studio project.
    Show me the test cases you'll put in each set before you create them.
    ```

3. 检查它的提议，然后接受。在 Test Manager 中打开 **Test Sets**，确认两个测试集都已存在，并包含正确的测试用例。

!!! tip "为什么需要冒烟测试集？"
    冒烟测试集能快速回答一个问题：应用是否可用，我能否登录？先运行它。如果它失败了，就没必要再等完整的回归测试集了。

## ▶️ 运行测试集 { #run-the-test-sets }

Test Manager 使用你发布到租户源的包，在 `{{ training_folder }}` 文件夹中的机器人上运行自动化测试用例。

1. 在 Test Manager 中打开 **Test Sets**，选择 **UiBank Smoke**，然后选择 **Execute** > **Automated**。
2. 它通过后，用同样的方式运行 **UiBank Regression**。

=== "或者让你的编码智能体来做"

    ```text
    Set every automated test case in {YourName}UiBankTests as Publishable, then
    publish the project to the tenant feed of the {{ training_tenant }}
    tenant if the latest version isn't there yet, check that each automated
    test case is linked to its
    Test Manager test case in my {YourName}_UIB_Test project, then run my
    "UiBank Smoke" and "UiBank Regression" test sets as
    automated executions, wait for them to finish, and give me a report.
    Confirm `uip login status` first, and stop if any step fails.
    ```

    编码智能体会加载 `uipath-test` 技能，并运行 `uip rpa pack`、`uip or packages upload`、`uip tm testcases link-automation`、`uip tm testsets run` 和 `uip tm wait`。

!!! tip "自动化测试用例不够？"
    使用讲师的 `DemoUiBankTests` 包，它已经发布在 `{{ training_folder }}` 文件夹中。它的测试是 `T0_LoginAndInitialAccountState` 到 `T7_LogoutAndEvidenceCollection`，每个步骤一个。你的测试用例名称来自 Autopilot，不会与它们完全一致，所以请按步骤关联：

    1. 在 Test Manager 中打开你的每个测试用例，然后打开它的 **Automation** 部分。
    2. 选择 **Select Automation** > **Tenant Package Feed**。
    3. 从 T0 到 T7 中，选择同一步骤对应的 `DemoUiBankTests` 测试。

    或者让你的编码智能体按测试用例键来关联，例如 *"Link my test case {YourPrefix}:12 to the test T3_FundsTransferBetweenAccounts in the DemoUiBankTests package."* 它会使用 `--test-case-key` 和 `--test-name` 运行 `uip tm testcases link-automation`。然后运行测试集。参见[资源](resources.md#trainers-reference-package)。

!!! warning "机器人使用你的凭据资产"
    机器人会从 `{{ training_folder }}` 文件夹读取 `{YourName}_UiBankCredential`，和你的本地运行一样。如果资产在其他位置，每个测试都会在 **Given** 中失败，甚至在打开浏览器之前。

!!! info "仅手动的测试用例怎么办？"
    自动化执行会跳过没有自动化的测试用例。要包含它们，请以 **Manually** 方式执行测试集，或者自主运行它们。

## 🔎 查看测试集的执行 { #look-into-the-executions-of-the-test-sets }

1. 在 Test Manager 中打开 **Execution** 选项卡，找到你刚刚启动的两次执行。
2. 打开 **UiBank Regression**。查看每个测试用例的结果。
3. 如果有失败的测试用例日志，打开它。阅读失败的断言及其截图。问题出在测试上还是 UiBank 上？
4. 选择结果，然后选择 **Generate Insights**。Autopilot 会生成一份报告，包含 **Overview**、**Top Failing Tests**、**Common Errors**、**Error Patterns** 和 **Recommendations**。

!!! success "测试集完成"
    Autopilot 创建了两个测试集，并从 Test Manager 在机器人上执行，每个自动化测试用例都有结果和证据。

## 🛠️ 常见问题出在哪里 { #where-it-usually-breaks }

<div class="fix-grid" markdown>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 运行失败，提示 *"Please assign folder to project level"*</span>

<span class="lbl">原因</span> 你的 Test Manager 项目没有默认文件夹

<span class="lbl">解决</span> 把项目的默认文件夹设为 `{{ training_folder }}`，然后重新运行

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 Autopilot 找不到 **UiBank Regression** 的自动化测试用例</span>

<span class="lbl">原因</span> 项目还没有发布到租户源

<span class="lbl">解决</span> 把它发布到 **Orchestrator Tenant Process Feed**，然后再问一次 Autopilot

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 部分测试用例没有结果</span>

<span class="lbl">原因</span> 它们没有自动化，或者不在最新发布的包中

<span class="lbl">解决</span> 重新发布到 **Orchestrator Tenant Process Feed**，并检查每个 Studio 测试用例都已关联到对应的 Test Manager 测试用例

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 每个测试都在 **Given** 中失败</span>

<span class="lbl">原因</span> 机器人无法读取凭据资产

<span class="lbl">解决</span> 检查资产名称和文件夹

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 测试单独运行能通过，但在测试集中失败</span>

<span class="lbl">原因</span> 它依赖另一个测试留下的数据

<span class="lbl">解决</span> 让它的 **Given** 准备好所需的一切

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 上传失败，提示 *"A testing project should contain at least one entry point"*（错误 2006）</span>

<span class="lbl">原因</span> 没有测试用例被标记为可发布

<span class="lbl">解决</span> 在 **Project** 面板中右键单击每个测试用例 > **Set as Publishable**，然后重新发布

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 上传被拒绝</span>

<span class="lbl">原因</span> 该包版本已存在

<span class="lbl">解决</span> 提升项目版本号，然后重新发布

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 执行一直处于 Pending</span>

<span class="lbl">原因</span> 文件夹中没有空闲的机器人

<span class="lbl">解决</span> 告诉讲师。机器人是共享的。

</div>

</div>
