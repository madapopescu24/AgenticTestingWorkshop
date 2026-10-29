动手实践 · 第 3 部分，共 4 部分
{: .eyebrow }

# ▶️ 执行 { #executions }

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">每次运行留下证据的地方</div>

## 🗂️ 执行类型一览 { #execution-types-at-a-glance }

Test Manager 中的每次运行都是一次**执行**，每次执行都有一个类型。在本课程中你会见到所有类型：

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">✋</span>
<span class="f-title" markdown="span">手动</span>

👤 由人执行，在 **Manual Execution Assistant** 的引导下进行

▶️ 在测试用例或测试集上选择 **Execute** > **Manually**

</div>

<div class="feature" markdown>
<span class="f-icon">🤖</span>
<span class="f-title" markdown="span">自动化</span>

👤 由机器人执行，运行与测试用例关联的自动化

▶️ 测试用例完成自动化并发布后，选择 **Execute** > **Automated**

</div>

<div class="feature" markdown>
<span class="f-icon">🎬</span>
<span class="f-title" markdown="span">自主</span>

👤 由 Autopilot 执行，在应用上按手动步骤操作

▶️ 在测试用例的 **Manual Steps** 选项卡上选择 **Run autonomously**

</div>

<div class="feature" markdown>
<span class="f-icon">⏳</span>
<span class="f-title" markdown="span">Pending</span>

👤 暂时无人执行。每个测试用例的结果都是 *None*，你可以稍后分批或逐个运行它们

▶️ **Execute** > **Pending**

</div>

</div>

!!! info "本地运行与执行"
    在 Studio 的 **Test Explorer** 中运行，是供你在构建过程中使用的。它们只存在于你的 Studio 会话中，关闭后就会消失。Test Manager 中的执行是供团队使用的：它们会被保存，关联到需求，并带有证据。接下来你会通过测试集创建执行。

## 🔎 浏览 Execution 选项卡 { #explore-the-execution-tab }

到目前为止你运行的所有内容都在 Test Manager 中留下了记录。在你的项目中，选择左侧菜单中的 **Execution** 并浏览：

1. **列表。** 找到到目前为止的每一次执行及其类型：你的自主运行，以及任何手动或自动化运行。
2. **一次执行。** 打开你的自主运行。查看每个测试用例的结果、由谁运行以及运行时间。
3. **测试用例日志。** 打开测试用例日志。阅读每一步及其结果，并打开作为证据附加的截图。
4. **从需求出发。** 在 **Requirements** 下，打开你的测试用例所覆盖的需求，找到覆盖它的测试用例的最新结果。这就是你通过需求和测试用例建立起来的可追溯性。

## ✋ 手动运行测试用例 { #run-a-test-case-manually }

在自主执行旁边再添加一次手动执行，这样你可以比较人和 Autopilot 是如何记录同一个测试的。

1. 在 Test Manager 中，打开你自主运行过的那个测试用例。
2. 选择 **Execute** > **Manually**。如果浏览器询问，请允许 Test Manager 弹出窗口：**Manual Execution Assistant** 会在新窗口中打开。
3. 在 UiBank 上亲自执行每一步，并标记为 **Passed** 或 **Failed**。如果某处与预期结果不同，就添加评论。
4. 如果连续几步都通过了，选择 **Set Passed Till Here**，而不用逐个标记。
5. 选择 **Done**。新的手动执行会出现在 **Execution** 选项卡中，位于自主执行旁边。

!!! tip "比较两者"
    把两次执行并排打开。你和 Autopilot 对每一步得出的结果相同吗？如果有分歧，就查看 Autopilot 在那一步的截图：它准确显示了 Autopilot 看到的内容。

## 🧭 筛选、查找和重新执行 { #filter-find-and-re-execute }

1. **筛选。** 在 **Execution** 选项卡中按结果筛选列表，例如只看失败的。
2. **用 Autopilot Search 查找。** 用自然语言查询执行，例如：

    ```text
    executions with failed test cases this week
    ```

3. **重新执行。** 打开一次执行，选择 **More Options** 或 **Tasks**，然后选择 **Execute Manually** 或 **Execute Automated**。Test Manager 会再次运行相同的测试用例，无需你做任何设置。重新执行不显示活动覆盖率。

!!! warning "重新执行会替换之前的结果"
    重新执行会删除该执行之前的结果并替换它们，包括你刚才比较过的自主运行和手动运行。如果想保留它们，请改为重新运行测试集，这会创建一次新的执行。

## ⏳ 为什么我的执行一直处于 Pending？ { #why-does-my-execution-stay-pending }

你以 **Pending** 方式启动的执行，按设计每个测试用例都会显示 *None*。在你执行它之前，什么都不会运行。而一直处于 Pending 的**自动化**或**自主**执行则不同：它没有被任何机器人接手。

!!! warning "自动化和自主运行需要文件夹中有无人值守机器人"
    Test Manager 会把自动化和自主执行作为 Orchestrator 中的作业来运行，位于项目的默认文件夹 **{{ training_folder }}** 中。只有当连接到 Orchestrator 的**无人值守机器人**有权访问该文件夹时，作业才会启动。以下设置看起来已连接，但不会接手作业：

    - **Serverless。** 发送到 **Default Serverless** 机器模板且没有运行时槽位的运行，会一直处于 Pending，且没有任何错误。
    - **你的个人工作区机器人。** Studio 登录时使用的机器人服务于你的个人工作区，而不是 **{{ training_folder }}**。
    - **没有机器人凭据。** 运行时显示 Connected 和 Available，但没有存储了凭据的机器人账号分配到该文件夹。作业会一直处于 Pending，原因为 `RobotNoCredentials`。
    - **没有 Windows 机器人（针对自主运行）。** 自主测试执行仅支持 Windows。如果只有 macOS 机器人，自主运行会一直处于 Pending，且不会创建 Orchestrator 作业。

    **怎么办：**

    1. 告诉讲师：共享文件夹中的机器人是为所有人配置的。
    2. 有机器人可用后，**停止处于 Pending 的执行并重新运行**。Orchestrator 不会重新检查已经处于 Pending 的作业，所以即使有机器人空闲下来，旧的作业也会一直等待。

## 💻 进阶：用你的编码智能体读取执行 { #stretch-read-executions-with-your-coding-agent }

你的编码智能体可以通过 `uip` CLI 读取同样的执行，并把它们整理成摘要或供 CI 流水线使用的文件。在 Studio 的 **Terminal** 面板中启动你的编码智能体，并给它这个提示词：

```text
In my {YourName}_UIB_Test Test Manager project (prefix {YourPrefix}), summarise the
latest execution: its type, the result per test case, and which steps
failed, with links to their screenshots. Then download its JUnit XML
results into ./results. Confirm `uip login status` first.
```

编码智能体会加载 `uipath-test` 技能，并运行 `uip tm executions list`、`uip tm executions testcaselogs list` 和 `uip tm result download` 等命令。

!!! info "出现 \"Tool 'tm' … is not discoverable\"？"
    你的机器上还没有安装 `uip` CLI 的 Test Manager 部分。错误消息中给出了安装命令。让你的编码智能体运行它，然后再试一次提示词。
