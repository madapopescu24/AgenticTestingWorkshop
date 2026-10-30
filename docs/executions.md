Hands-on · Part 3 of 4
{: .eyebrow }

# ▶️ Executions

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">Where every run leaves its evidence</div>

## 🗂️ Execution types at a glance

Every run in Test Manager is an **execution**, and every execution has a type. You'll see all of them in this session:

<div class="feature-grid cols-4" markdown>

<div class="feature" markdown>
<span class="f-icon">✋</span>
<span class="f-title" markdown="span">Manual</span>

👤 A person, guided by the **Manual Execution Assistant**

▶️ **Execute** > **Manually** on a test case or test set

</div>

<div class="feature" markdown>
<span class="f-icon">🤖</span>
<span class="f-title" markdown="span">Automated</span>

👤 A robot, running the automation linked to the test case

▶️ **Execute** > **Automated**, once the test case is automated and published

</div>

<div class="feature" markdown>
<span class="f-icon">🎬</span>
<span class="f-title" markdown="span">Autonomous</span>

👤 Autopilot, following the manual steps on the application

▶️ **Run autonomously** on a test case's **Manual Steps** tab

</div>

<div class="feature" markdown>
<span class="f-icon">⏳</span>
<span class="f-title" markdown="span">Pending</span>

👤 Nobody yet. Every test case gets the result *None*, so you can run them later, in chunks, or one by one

▶️ **Execute** > **Pending**

</div>

</div>

!!! info "Local runs vs. executions"
    Runs from Studio's **Test Explorer** are for you while you build. They live in your Studio session and disappear when you close it. Executions in Test Manager are for the team: they're stored, linked to requirements, and carry their evidence. With test sets, you'll create them next.

## 🔎 Explore the Execution tab

Everything you ran so far left a record in Test Manager. In your project, select **Execution** in the left menu and explore it:

1. **The list.** Find every execution so far, with its type: your autonomous run, and any manual or automated runs.
2. **An execution.** Open your autonomous run. Check its result per test case, who ran it, and when.
3. **A test case log.** Open the test case log. Read each step with its result, and open the screenshots attached as evidence.
4. **From a requirement.** Under **Requirements**, open the requirement your test case covers, and find the latest result of the test cases that cover it. That's the traceability you set up with the requirements and test cases.

## ✋ Run a test case manually

Add a manual execution next to your autonomous one, so you can compare how a person and Autopilot record the same test.

1. In Test Manager, open the test case you ran autonomously.
2. Select **Execute** > **Manually**. Allow pop-ups for Test Manager if your browser asks: the **Manual Execution Assistant** opens in a new window.
3. Carry out each step on UiBank yourself, and mark it **Passed** or **Failed**. Add a comment where something looks different from the expected result.
4. If several steps in a row pass, select **Set Passed Till Here** instead of marking them one by one.
5. Select **Done**. The new manual execution appears in the **Execution** tab, next to the autonomous one.

!!! tip "Compare the two"
    Open both executions side by side. Did you and Autopilot reach the same result for every step? Where you disagree, read Autopilot's screenshot for that step: it shows exactly what Autopilot saw.

## 🧭 Filter, find, and re-execute

1. **Filter.** In the **Execution** tab, filter the list by result, for example failed only.
2. **Find with Autopilot.** Open the **Autopilot** panel in Test Manager and ask for executions in plain English, for example:

    ```text
    Show me the executions in my {YourName}_UIB_Test project that have
    failed test cases this week.
    ```

3. **Re-execute.** Open an execution, select **More Options** or **Tasks**, then **Execute Manually** or **Execute Automated**. Test Manager runs the same test cases again without you setting anything up. Re-executions don't show activity coverage.

!!! warning "Re-executing replaces the previous results"
    A re-execution deletes the earlier results of that execution and replaces them, including the autonomous and manual runs you just compared. To keep them, run the test set again instead, which creates a new execution.

## ⏳ Why does my execution stay Pending?

An execution you started as **Pending** shows *None* for every test case by design. Nothing runs until you execute it. An **automated** or **autonomous** execution that stays Pending is different: nothing has picked it up.

!!! warning "Automated and autonomous runs need an unattended robot in the folder"
    Test Manager runs automated and autonomous executions as jobs in Orchestrator, in the project's default folder, **{{ training_folder }}**. A job starts only when an **unattended robot** connected to Orchestrator has access to that folder. Setups that look connected but don't pick it up:

    - **Serverless.** A run sent to the **Default Serverless** machine template, with no runtime slots, stays Pending without any error.
    - **Your personal workspace robot.** The robot Studio signs in with serves your personal workspace, not **{{ training_folder }}**.
    - **No robot credentials.** The runtime shows Connected and Available, but no robot account with stored credentials is assigned to the folder. The job stays Pending with the reason `RobotNoCredentials`.
    - **No Windows robot, for autonomous runs.** Autonomous test execution is supported on Windows only. With only a macOS robot, an autonomous run stays Pending and no Orchestrator job is created.

    **What to do:**

    1. Tell the trainer: robots in the shared folder are set up for everyone.
    2. Once a robot is available, **stop the pending execution and run it again**. Orchestrator doesn't re-check a job that's already Pending, so the old one keeps waiting even after a robot becomes free.

## 💻 Stretch: read executions with your coding agent

Your coding agent can read the same executions through the `uip` CLI, and turn them into a summary or a file for a CI pipeline. In Studio's **Terminal** panel, start your coding agent and give it this prompt:

```text
In my {YourName}_UIB_Test Test Manager project (prefix {YourPrefix}), summarize the
latest execution: its type, the result per test case, and which steps
failed, with links to their screenshots. Then download its JUnit XML
results into ./results. Confirm `uip login status` first.
```

The coding agent loads the `uipath-test` skill and runs commands such as `uip tm executions list`, `uip tm executions testcaselogs list`, and `uip tm result download`.

!!! info "\"Tool 'tm' … is not discoverable\"?"
    The Test Manager part of the `uip` CLI isn't installed on your machine yet. The error message names the install command. Ask your coding agent to run it, then try the prompt again.
