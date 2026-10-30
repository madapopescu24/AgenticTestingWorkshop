Hands-on · Part 2 of 4
{: .eyebrow }

# 🧪 Test Cases

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">Generate them, automate one by hand, then let the agents do the rest</div>

## 🤖 Ask Autopilot in Test Manager to create test cases

The **Test Case Generation Agent** writes test cases from a requirement, with manual steps and expected results.

1. In Test Manager, under **Requirements**, open a requirement, for example **Login and Initial Account State**.
2. Ask Autopilot to generate test cases for it. To steer it, pick a prompt from the **Prompt Library**: **Valid E2E Scenario Testing** for valid end-to-end scenarios, or **Boundary-Value Testing** for edge cases.
3. Review the suggestions. Keep the happy path, and name it **Login and Initial Account State**. Keep one or two negative cases too, such as a wrong password. Discard the rest.
4. Open **Login and Initial Account State** and read its manual steps. Each one needs an action and an expected result you could check on screen.

!!! tip "Prompt Library"
    The Prompt Library holds predefined prompts, such as **Valid E2E Scenario Testing**, **End-to-End Flow Verification**, **Rapid Test Idea Generation**, **Elusive Issue Detection**, and **Boundary-Value Testing**, plus the custom ones your team saves. A prompt that works well for one requirement usually works for the next, so save the good ones.

## ✍️ Implement the Login test case by hand

Before any agent automates a test for you, build one yourself. It takes longer, and that's the point: you'll know exactly what to check when an agent does it in five minutes.

<div style="background: #16213e; border-left: 10px solid #FA4616; padding: 22px 28px; margin: 1.2rem 0 1.4rem;">
  <div style="font-size: 19px; font-weight: 700; color: #ffffff; line-height: 1.35;">Every UiPath test case has three parts: Given, When, Then.</div>
  <div style="font-size: 15px; font-style: italic; color: #f6c3ab; margin-top: 9px;">Set up what the test needs. Do the one thing under test. Check what the application shows.</div>
</div>

**Create the test case**

1. In **Studio**, find **Login and Initial Account State** among your Test Manager test cases, and create a Studio test case linked to it. Name the file `T0_LoginAndInitialAccountState.xaml`, the same name as in the trainer's reference package.
2. The new test case opens with three sequences: **Given**, **When**, and **Then**.

**Given: set up**

3. Nothing to add for this test: it needs only your registered UiBank user and your credential asset. Leave **Given** empty. The credential is read in **When**, inside the browser card that types it.

**When: log in and open Accounts**

4. Open `https://uibank.uipath.com/login` in Chrome. If it doesn't load, use the [fallback](setup.md#7-register-your-uibank-test-user): `https://purple-dune-0af054403.6.azurestaticapps.net/login`.
5. Add a **Use Application/Browser** activity and indicate the UiBank login page.
6. Inside the **Use Application/Browser** card, before any **Type Into**, add a **Get Credential** activity. Set the asset name to `{YourName}_UiBankCredential` and the folder to `{{ training_folder }}`. Store the outputs in `var_Username` (String) and `var_Password` (SecureString).
7. Add **Type Into** for the **Enter username** field with `var_Username`, and **Type Into** for the **Enter password** field with `var_Password` as secure text.
8. Add **Click** on **Sign In**.
9. Add **Check App State** on the **I agree to the Privacy Policy** button of UiBank's **Important Notice** dialog, with a short timeout. If it appears, **Click** it. If it doesn't, carry on.
10. Add **Check App State** on the **Welcome!** heading above *"Here is your account summary"*. UiBank opens **Accounts** right after Sign In, so this heading proves the login worked. Store the result in `var_WelcomeShown` (Boolean).
11. Add **Get Text** on the account summary area, and store it in `var_AccountSummary`.

**Then: verify**

12. Add **Verify Expression** with `var_WelcomeShown`.
13. Add **Verify Expression** that checks `var_AccountSummary` either contains *"No accounts at this time"* or lists at least one account.
14. On each verification, turn on the screenshot option, so the evidence is attached to the result.

**Run it**

15. In **Test Explorer**, run the test case. Both verifications must pass.
16. Run it a second time. It must pass again.

!!! warning "Keep the password inside the browser card"
    Workflow Analyzer rule **ST-SEC-008** fails the build when a SecureString is used outside the scope that created it. If **Get Credential** sits in **Given**, or the password is passed to another workflow as an argument, `uip rpa validate` may still pass, but Studio's build and `uip rpa build` fail with *"SecureString variable used outside of the creation scope"*. Read the credential inside the **Use Application/Browser** card that types it.

!!! info "The Important Notice dialog"
    From the second sign-in on, UiBank may show an **Important Notice** with **I agree to the Privacy Policy →** and ✕. Closing it with ✕ leaves you logged out, and every later step fails. Accept it once by hand before you automate, and keep step 9 in every test that logs in.

!!! tip "Use the Object Repository"
    When you indicate a target, save it to the **Object Repository**. The agents you use for the next test case reuse those targets, so the login fields you capture by hand are the ones Autopilot and your coding agent build on.

!!! success "Login test case done"
    `T0_LoginAndInitialAccountState.xaml` is linked to its Test Manager test case and passes twice, with a screenshot on each verification. Note how long it took. You'll compare with the next test case.

## 🪄 Generate the next test case with Autopilot or a coding agent

Now let an agent automate the next one. Pick a requirement after Login, for example **Checking Account Creation**. First generate its test cases in Test Manager the same way you did for Login, and keep the happy path as **Checking Account Creation**.

!!! warning "Use the test case name Autopilot actually generated"
    Autopilot in Test Manager doesn't always name test cases the same way. Yours may be called **Open a Checking Account**, **Step 1: Open a Checking Account**, or something else. Check the exact name in Test Manager under **Test Cases**, and use it in the prompt below wherever it says **Checking Account Creation**. Otherwise Studio, Autopilot, or your coding agent links the automation to the wrong test case, or doesn't find one.

Then automate it with this prompt. You can give it to Autopilot in Studio Desktop or to a coding agent. The prompt is the same, only where you type it changes:

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

    1. In **Studio**, with your `{YourName}UiBankTests` project open, open the **Autopilot** panel.
    2. Paste the prompt into **Ask Autopilot anything** and send it.
    3. Review what Autopilot proposes before you accept it: does **Given** log in first? Does **Then** check the confirmation page and the account summary show the new nickname?
    4. Accept the changes, then run the test case from **Test Explorer**, twice.

=== "Coding agent (Codex, Claude Code)"

    1. In **Studio**, with your `{YourName}UiBankTests` project open, open the **Terminal** panel at the bottom of the window. It opens in your project folder.
    2. Start your coding agent there:

        ```bash
        claude
        # or
        codex
        ```

    3. Paste the prompt into the terminal and press **Enter**.
    4. Answer its questions, and read each command it proposes before you approve it.
    5. When it's done, run the test case from **Test Explorer**, twice.

    The coding agent loads the `uipath-rpa` skill, reads the project and your Login test case first, then writes the new one. If it can't reach UiBank in the browser, it doesn't guess selectors: it names the activities it couldn't target `TODO Indicate — …`. Indicate those in Studio, or open UiBank in Chrome and ask it to try again.

!!! warning "Check, validate, and correct the generated test case"
    Whichever agent built it, the test case is yours to sign off. Before you move on, open it in Studio and check it against its Test Manager test case and the design document:

    - **Given** logs in and sets up everything the test needs, so it runs on its own.
    - **When** does what the manual steps describe, on the right screens and fields.
    - **Then** verifies every expected result, with the right values, and a screenshot on each verification.
    - It runs and passes in **Test Explorer**, twice.

    Where something is wrong or missing, correct it: edit it yourself in Studio, use Autopilot on a single expression, or ask the agent to fix it, telling it exactly what's wrong.

Compare with the Login test case you built by hand:

- How long did it take?
- Is the result as readable as yours? Would you trust its **Then** section without reading it?
- Did it reuse your login targets, or capture new ones?

!!! warning "Make changes in one place at a time"
    Studio, Autopilot, and your coding agent can all edit the same files. Close a file in Studio before your coding agent changes it, and tell your coding agent when you've changed something in Studio, so it re-reads the project instead of overwriting your work.

!!! tip "Autopilot for Developers"
    While you review the generated test case, use Autopilot on single expressions. In the **Expression Editor**, select **Fix** (the magic wand) on any expression with a validation error, or type an instruction into the Autopilot box at the bottom, for example *"Build the nickname AutoChecking_ followed by the current time as yyyyMMddHHmmss."*

## 🎬 Run Autonomously in Test Manager

Not every test case needs an automation before it can run. In Test Manager, Autopilot can run a test case **autonomously**: it reads the manual steps and carries them out on the application itself, then records a result for each step, with evidence.

Try it on one of the negative login test cases you kept when Autopilot generated them:

1. In Test Manager, under **Test Cases**, open a test case that has manual steps but no automation.
2. If a step logs in, write the password as `{{ '{{' }}credential:{YourName}_UiBankCredential{{ '}}' }}` instead of typing it into the step.
3. Open the **Manual Steps** tab and select **Run autonomously**. Depending on the release, the button may be labeled **Run with Autopilot**.
4. Enter the target URL `https://uibank.uipath.com/login`, or `https://purple-dune-0af054403.6.azurestaticapps.net/login` if you use the fallback. **Run** stays disabled until you do.
5. Pick the model the trainer names.
6. Turn on **live streaming** now, before you select **Run**, if you want to watch the test case run as it happens.
7. Select **Run**.
8. When it finishes, open the result. Every step's execution is documented with a screenshot of what Autopilot saw, next to the step's outcome.

!!! warning "Autonomous runs need Test Cloud and a Windows robot"
    Autonomous test execution is available only when Test Manager is delivered through **Test Cloud**, and it's supported on **Windows** environments only. It runs as a job on a Windows robot in the `{{ training_folder }}` folder. With only a macOS robot connected, the run stays **Pending** and no Orchestrator job is created. If yours stays Pending, tell the trainer, and start a new run once a Windows robot is available. See [Why does my execution stay Pending?](executions.md#why-does-my-execution-stay-pending)

Discuss as a group:

- When would you run a test case autonomously instead of automating it? A one-off check of a new feature, or a test case that changes every sprint, are good candidates.
- What makes a manual step easy for Autopilot to follow? The same thing that makes it easy for a person: one action, one expected result, the exact labels on screen.

## ➕ Implement a few more test cases

Pick two or three more requirements and repeat the cycle: generate the test cases in Test Manager, keep the happy path, and automate it with Autopilot in Studio Desktop or your coding agent. Suggested order, with what each test case's **Given** must set up so it runs on its own:

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Savings Account Creation</span>

📄 `T2_SavingsAccountCreation.xaml`

**Given:** Log in

**Then:** Confirmation page and account summary show the Savings nickname

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Funds Transfer Between Accounts</span>

📄 `T3_FundsTransferBetweenAccounts.xaml`

**Given:** Log in, open a Checking and a Savings account, read both balances

**Then:** Checking = before − `var_TransferAmount`; Savings = before + `var_TransferAmount`

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Loan Application Submission</span>

📄 `T4_LoanApplicationSubmission.xaml`

**Given:** Log in

**Then:** Result message captured; Loan ID returned

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Loan Status Lookup</span>

📄 `T5_LoanStatusLookup.xaml`

**Given:** Log in, submit a loan, keep `var_LoanID`

**Then:** Amount and term match

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">User Profile Identity Verification</span>

📄 `T6_UserProfileIdentityVerification.xaml`

**Given:** Log in

**Then:** Username and email match

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Logout and Evidence Collection</span>

📄 `T7_LogoutAndEvidenceCollection.xaml`

**Given:** Log in

**Then:** Session closed; top menu no longer available

</div>

</div>

!!! warning "Don't assume the loan is approved"
    UiBank's loan decision rules aren't documented. The loan tests must pass whether the loan is approved or rejected, as long as a Loan ID comes back and the lookup shows the same amount and term.

!!! tip "A balance check fails?"
    Read the screenshot before you read the code. The usual causes are a balance read as text with a currency sign (`$1,000.00` isn't a number until you parse it), or a balance read before the account summary refreshed. Autopilot in the Expression Editor is quick at the conversion: *"Convert this text, for example "$1,000.00", to a Decimal."*

!!! success "Test cases done"
    At least four automated test cases, each linked to its Test Manager test case and passing on its own: Login built by hand, the rest built by Autopilot or your coding agent. Plus a few manual-only test cases from Autopilot, and one autonomous run.

!!! tip "Your automations don't build yet?"
    You can still do the Test Sets part. Link the trainer's `DemoUiBankTests` package to your test cases, one per step from T0 to T7. See [Not enough automated test cases?](test-sets.md#run-the-test-sets) in Test Sets.
