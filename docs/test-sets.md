Hands-on · Part 4 of 4
{: .eyebrow }

# 📦 Test Sets

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">Group, run, and read the results</div>

## 📤 Publish your testing project to the tenant feed

Autopilot builds the test sets from the automated test cases it can find in Orchestrator, and Test Manager runs them from the published package. So publish first.

1. In **Studio**, with your `{YourName}UiBankTests` project open, mark your test cases as publishable. Studio creates test cases as drafts, and only publishable ones go into the package. In the **Project** panel, right-click each test case you automated and select **Set as Publishable**. Its icon turns blue.
2. Select **Publish**.
3. In **Publish to**, select **Orchestrator Tenant Process Feed**.
4. Bump the version if you published before, then select **Publish**.
5. Wait for the confirmation that the package was published.

!!! info "Why the tenant feed"
    Automated runs of test sets include only the test cases published to the **Orchestrator Tenant Process Feed**, in the latest package version. A package published to your personal workspace feed, or an older version, isn't picked up. Republish after every change to your test cases.

## 🪄 Ask Autopilot in Studio to create test sets

1. In **Studio**, open the **Autopilot** panel in your `{YourName}UiBankTests` project.
2. Give Autopilot this prompt:

    ```text
    In my {YourName}_UIB_Test Test Manager project, create two test sets from the
    existing test cases:
    - "UiBank Smoke" with Login and Initial Account State only.
    - "UiBank Regression" with every test case that is automated
      in this Studio project.
    Show me the test cases you'll put in each set before you create them.
    ```

3. Check the proposal, then accept it. In Test Manager, open **Test Sets** and confirm both sets exist with the right test cases.

!!! tip "Why a smoke set?"
    A smoke set answers one question fast: is the application up and can I log in? Run it first. If it fails, there's no point waiting for the full regression set.

## ▶️ Run the test sets

Test Manager runs automated test cases on a robot in the `{{ training_folder }}` folder, from the package you published to the tenant feed.

1. In Test Manager, open **Test Sets**, select **UiBank Smoke**, then **Execute** > **Automated**.
2. When it passes, run **UiBank Regression** the same way.

=== "Or ask your coding agent"

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

    The coding agent loads the `uipath-test` skill and runs `uip rpa pack`, `uip or packages upload`, `uip tm testcases link-automation`, `uip tm testsets run`, and `uip tm wait`.

!!! tip "Not enough automated test cases?"
    Use the trainer's `DemoUiBankTests` package, already published in the `{{ training_folder }}` folder. Its tests are `T0_LoginAndInitialAccountState` to `T7_LogoutAndEvidenceCollection`, one per step. Your test case names come from Autopilot and won't match them exactly, so link them by step:

    1. In Test Manager, open each of your test cases, then its **Automation** section.
    2. Select **Select Automation** > **Tenant Package Feed**.
    3. Pick the `DemoUiBankTests` test for the same step, from T0 to T7.

    Or ask your coding agent to link them by test case key, for example *"Link my test case {YourPrefix}:12 to the test T3_FundsTransferBetweenAccounts in the DemoUiBankTests package."* It runs `uip tm testcases link-automation` with `--test-case-key` and `--test-name`. Then run the test sets. See [Resources](resources.md#trainers-reference-package).

!!! warning "The robot uses your credential asset"
    The robot reads `{YourName}_UiBankCredential` from the `{{ training_folder }}` folder, just like your local runs did. If the asset lives somewhere else, every test fails in **Given**, before it opens a browser.

!!! info "What about manual-only test cases?"
    An automated execution skips test cases without an automation. To include them, execute the test set **Manually**, or run them autonomously.

## 🔎 Look into the executions of the test sets

1. In Test Manager, open the **Execution** tab and find the two executions you just started.
2. Open **UiBank Regression**. Check the result of each test case.
3. Open a failed test case log, if there is one. Read the failed assertion and its screenshot. Is it the test or UiBank?
4. Select the results, then select **Generate Insights**. Autopilot builds a report with an **Overview**, **Top Failing Tests**, **Common Errors**, **Error Patterns**, and **Recommendations**.

!!! success "Test sets done"
    Two test sets created by Autopilot, executed from Test Manager on a robot, with a result and evidence for every automated test case.

## 🛠️ Where it usually breaks

<div class="fix-grid" markdown>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 Run fails with *"Please assign folder to project level"*</span>

<span class="lbl">Cause</span> Your Test Manager project has no default folder

<span class="lbl">Fix</span> Set the project's default folder to `{{ training_folder }}`, then run again

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 Autopilot finds no automated test cases for **UiBank Regression**</span>

<span class="lbl">Cause</span> The project isn't published to the tenant feed yet

<span class="lbl">Fix</span> Publish it to the **Orchestrator Tenant Process Feed**, then ask Autopilot again

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 Some test cases have no result</span>

<span class="lbl">Cause</span> They aren't automated, or aren't in the latest published package

<span class="lbl">Fix</span> Publish again to the **Orchestrator Tenant Process Feed**, and check each Studio test case is linked to its Test Manager test case

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 Every test fails in **Given**</span>

<span class="lbl">Cause</span> The robot can't read the credential asset

<span class="lbl">Fix</span> Check the asset name and folder

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 A test passes alone but fails in the test set</span>

<span class="lbl">Cause</span> It depends on data another test left behind

<span class="lbl">Fix</span> Make its **Given** set up everything it needs

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 Upload fails with *"A testing project should contain at least one entry point"* (error 2006)</span>

<span class="lbl">Cause</span> No test case is marked publishable

<span class="lbl">Fix</span> In the **Project** panel, right-click each test case > **Set as Publishable**, then publish again

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 Upload rejected</span>

<span class="lbl">Cause</span> That package version already exists

<span class="lbl">Fix</span> Bump the project version and publish again

</div>

<div class="fix" markdown>
<span class="f-title" markdown="span">🚨 Execution stays pending</span>

<span class="lbl">Cause</span> No robot is free in the folder

<span class="lbl">Fix</span> Tell the trainer. Robots are shared.

</div>

</div>
