Hands-on · Part 2 of 4
{: .eyebrow }

# 🧪 Test Cases

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">Generate them, automate one by hand, then let the agents do the rest</div>

## 🤖 Ask Autopilot in Test Manager to create test cases

The **Test Case Generation Agent** writes test cases from a requirement, with manual steps and expected results.

1. In Test Manager, under **Requirements**, open a requirement, for example **Login & Initial State Check**.
2. Ask Autopilot to generate test cases for it. To steer it, pick a prompt from the **Prompt Library**: **Valid E2E Scenario Testing** for valid end-to-end scenarios, or **Boundary-Value Testing** for edge cases.
3. Review the suggestions. Keep the happy path, and name it **Login & Initial State Check**. Keep one or two negative cases too, such as a wrong password. Discard the rest.
4. Open **Login & Initial State Check** and read its manual steps. Each one needs an action and an expected result you could check on screen.

!!! tip "Prompt Library"
    The Prompt Library holds predefined prompts, such as **Valid E2E Scenario Testing**, **End-to-End Flow Verification**, **Rapid Test Idea Generation**, **Elusive Issue Detection**, and **Boundary-Value Testing**, plus the custom ones your team saves. A prompt that works well for one requirement usually works for the next, so save the good ones.

## ✍️ Implement the Login test case by hand

Before any agent automates a test for you, build one yourself. It takes longer, and that's the point: you'll know exactly what to check when an agent does it in five minutes.

<div style="background: #16213e; border-left: 10px solid #FA4616; padding: 22px 28px; margin: 1.2rem 0 1.4rem;">
  <div style="font-size: 19px; font-weight: 700; color: #ffffff; line-height: 1.35;">Every UiPath test case has three parts: Given, When, Then.</div>
  <div style="font-size: 15px; font-style: italic; color: #f6c3ab; margin-top: 9px;">Set up what the test needs. Do the one thing under test. Check what the application shows.</div>
</div>

**Create the test case**

1. In **Studio**, find **Login & Initial State Check** among your Test Manager test cases, and create a Studio test case linked to it. Name the file `T0_LoginAndInitialStateCheck.xaml`, the same name as in the trainer's reference package.
2. The new test case opens with three sequences: **Given**, **When**, and **Then**.

**Given: set up**

3. Nothing to add for this test: it needs only your registered ParaBank user and your credential asset. Leave **Given** empty. The credential is read in **When**, inside the browser card that types it.

**When: log in and read Accounts Overview**

4. Open `https://parabank.parasoft.com/parabank/index.htm` in Chrome.
5. Add a **Use Application/Browser** activity and indicate the ParaBank home page.
6. Inside the **Use Application/Browser** card, before any **Type Into**, add a **Get Credential** activity. Set the asset name to `{YourName}_ParaBankCredential` and the folder to `{{ training_folder }}`. Store the outputs in `var_Username` (String) and `var_Password` (SecureString).
7. In the **Customer Login** panel, add **Type Into** for the **Username** field with `var_Username`, and **Type Into** for the **Password** field with `var_Password` as secure text.
8. Add **Click** on **Log In**.
9. Add **Check App State** on the **Accounts Overview** heading. ParaBank opens **Accounts Overview** right after Log In, so this heading proves the login worked. Store the result in `var_OverviewShown` (Boolean).
10. Add **Get Text** on the *"Welcome <First Name> <Last Name>"* text in the left panel, and store it in `var_WelcomeText`.
11. Add **Extract Table Data** on the **Accounts Overview** table (**Account**, **Balance\***, **Available Amount**), and store it in `dt_InitialAccounts`. Store the first account number in `var_FundingAccountId`.

**Then: verify**

12. Add **Verify Expression** with `var_OverviewShown`.
13. Add **Verify Expression** that checks `var_WelcomeText` contains your first and last name.
14. Add **Verify Expression** that checks `dt_InitialAccounts` has at least one account. Every new ParaBank user gets a default checking account.
15. On each verification, turn on the screenshot option, so the evidence is attached to the result.

**Run it**

16. In **Test Explorer**, run the test case. All three verifications must pass.
17. Run it a second time. It must pass again.

!!! warning "Keep the password inside the browser card"
    Workflow Analyzer rule **ST-SEC-008** fails the build when a SecureString is used outside the scope that created it. If **Get Credential** sits in **Given**, or the password is passed to another workflow as an argument, `uip rpa validate` may still pass, but Studio's build and `uip rpa build` fail with *"SecureString variable used outside of the creation scope"*. Read the credential inside the **Use Application/Browser** card that types it.

!!! info "Login fails with *"The username and password could not be verified."*?"
    ParaBank's shared demo database was probably reset. Register your user again with the same username and password, at [register.htm](https://parabank.parasoft.com/parabank/register.htm), then run the test case again. Don't change the test: the failure is in the data.

!!! tip "Use the Object Repository"
    When you indicate a target, save it to the **Object Repository**. The agents you use for the next test case reuse those targets, so the login fields you capture by hand are the ones Autopilot and your coding agent build on.

!!! success "Login test case done"
    `T0_LoginAndInitialStateCheck.xaml` is linked to its Test Manager test case and passes twice, with a screenshot on each verification. Note how long it took. You'll compare with the next test case.

## 🪄 Generate the next test case with Autopilot or a coding agent

Now let an agent automate the next one. Pick a requirement after Login, for example **Open a Checking Account**. First generate its test cases in Test Manager the same way you did for Login, and keep the happy path as **Open a Checking Account**.

!!! warning "Use the test case name Autopilot actually generated"
    Autopilot in Test Manager doesn't always name test cases the same way. Yours may be called **Checking Account Opening**, **Step 1: Open a Checking Account**, or something else. Check the exact name in Test Manager under **Test Cases**, and use it in the prompt below wherever it says **Open a Checking Account**. Otherwise Studio, Autopilot, or your coding agent links the automation to the wrong test case, or doesn't find one.

Then automate it with this prompt. You can give it to Autopilot in Studio Desktop or to a coding agent. The prompt is the same, only where you type it changes:

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

    1. In **Studio**, with your `{YourName}ParaBankTests` project open, open the **Autopilot** panel.
    2. Paste the prompt into **Ask Autopilot anything** and send it.
    3. Review what Autopilot proposes before you accept it: does **Given** log in first? Does **Then** check *"Account Opened!"* and that **Accounts Overview** lists the new account number?
    4. Accept the changes, then run the test case from **Test Explorer**, twice.

=== "Coding agent (Codex, Claude Code)"

    1. In **Studio**, with your `{YourName}ParaBankTests` project open, open the **Terminal** panel at the bottom of the window. It opens in your project folder.
    2. Start your coding agent there:

        ```bash
        claude
        # or
        codex
        ```

    3. Paste the prompt into the terminal and press **Enter**.
    4. Answer its questions, and read each command it proposes before you approve it.
    5. When it's done, run the test case from **Test Explorer**, twice.

    The coding agent loads the `uipath-rpa` skill, reads the project and your Login test case first, then writes the new one. If it can't reach ParaBank in the browser, it doesn't guess selectors: it names the activities it couldn't target `TODO Indicate — …`. Indicate those in Studio, or open ParaBank in Chrome and ask it to try again.

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
    While you review the generated test case, use Autopilot on single expressions. In the **Expression Editor**, select **Fix** (the magic wand) on any expression with a validation error, or type an instruction into the Autopilot box at the bottom, for example *"Build the payee name AutoPayee_ followed by the current time as yyyyMMddHHmm."*

## 🎬 Run Autonomously in Test Manager

Not every test case needs an automation before it can run. In Test Manager, Autopilot can run a test case **autonomously**: it reads the manual steps and carries them out on the application itself, then records a result for each step, with evidence.

Try it on a test case generated from the **Update Contact Info** requirement:

1. In Test Manager, under **Requirements**, open **Update Contact Info** (`{YourPrefix}:8`, Step 7 in the design document).
2. Ask Autopilot to generate test cases for it, and pick **Rapid Test Idea Generation** from the **Prompt Library**. It returns many short test ideas, fast.
3. Review the ideas and pick one to run autonomously, for example *"Update the phone number and verify that the new number is saved"*. Keep it, and discard the rest.
4. Open the test case and read its manual steps. Each one needs one action and an expected result you can check on screen. Edit any step that's vague.
5. The test case must log in first. Write the password as `{{ '{{' }}credential:{YourName}_ParaBankCredential{{ '}}' }}` instead of typing it into the step.
6. Open the **Manual Steps** tab and select **Run autonomously**. Depending on the release, the button may be labeled **Run with Autopilot**.
7. Enter the target URL `https://parabank.parasoft.com/parabank/index.htm`. **Run** stays disabled until you do.
8. Pick the model the trainer names.
9. Turn on **live streaming** now, before you select **Run**, if you want to watch the test case run as it happens.
10. Select **Run**.
11. When it finishes, open the result. Every step's execution is documented with a screenshot of what Autopilot saw, next to the step's outcome.

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
<span class="f-title" markdown="span">Open a Savings Account</span>

📄 `T2_OpenASavingsAccount.xaml`

**Given:** Log in, read `var_FundingAccountId`

**Then:** *"Account Opened!"*; the Savings account is listed, and the funding account dropped by the opening deposit

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Transfer Funds Between Accounts</span>

📄 `T3_TransferFundsBetweenAccounts.xaml`

**Given:** Log in, open a Checking and a Savings account, read both balances

**Then:** *"Transfer Complete!"*; Checking = before − `var_TransferAmount`; Savings = before + `var_TransferAmount`

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Pay a Bill</span>

📄 `T4_PayABill.xaml`

**Given:** Log in, open a Savings account to pay from

**Then:** *"Bill Payment Complete"* with `var_PayeeName`, `var_BillAmount`, and the Savings account

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Find Transactions & Account Activity</span>

📄 `T5_FindTransactionsAndAccountActivity.xaml`

**Given:** Log in, open a Savings account, transfer `var_TransferAmount` into it, and pay a bill from it

**Then:** **Find by Amount** shows the bill payment; **Find by Date** shows the transfer received

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Request a Loan</span>

📄 `T6_RequestALoan.xaml`

**Given:** Log in, read `var_FundingAccountId`

**Then:** *"Loan Request Processed"*; if approved, `var_LoanAccountId` is listed with balance = `var_LoanAmount`

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Update Contact Info</span>

📄 `T7_UpdateContactInfo.xaml`

**Given:** Log in

**Then:** *"Profile Updated"*; reopening the page shows `var_NewPhone`

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Logout & Evidence Collection</span>

📄 `T8_LogoutAndEvidenceCollection.xaml`

**Given:** Log in

**Then:** The **Customer Login** panel is back; **Account Services** is gone

</div>

</div>

!!! warning "Don't assume the loan is approved"
    ParaBank's loan decision depends on how the demo is configured and on the funds in the source account. Keep `var_LoanAmount` and `var_DownPayment` small, and read the **Status** on screen. If it's **Denied**, the test fails with the reason and a screenshot, as the design document says, so you can see why.

!!! tip "A balance check fails?"
    Read the screenshot before you read the code. The usual causes are a balance read as text with a currency sign (`$1,000.00` isn't a number until you parse it), or a balance read before the account summary refreshed. Autopilot in the Expression Editor is quick at the conversion: *"Convert this text, for example "$1,000.00", to a Decimal."*

## 🧹 Find obsolete test cases

Applications change, and test cases stay behind. An obsolete test case fails for the wrong reason, or never runs, and still counts as coverage. The updated design document has ten regression test cases, **TC-PB-002** to **TC-PB-011** (see [The regression test cases](agentic-testing-hands-on.md#the-regression-test-cases)). Some of them no longer match ParaBank. Autopilot in Test Manager can find them.

**Add the regression test cases to Test Manager**

1. In Test Manager, open the requirement each regression test case belongs to, for example **Login & Initial State Check** (`{YourPrefix}:1`).
2. Ask Autopilot to generate test cases, attach the design document, and give it this instruction:

    ```text
    Create one test case for each regression test case in section 6 of the attached design document that belongs to this requirement. Name each one with its ID and name, for example "TC-PB-003 Login with Invalid Credentials". Copy its steps and expected results as written. Don't add, merge, fix, or skip any test case.
    ```

3. Check that each test case is linked to its requirement. Repeat for the other requirements in the table, or split them across your group.

!!! tip "Or ask your coding agent"
    With the `uipath-test` skill, your coding agent can create the test cases in your Test Manager project and link them to the requirements: *"Read section 6 of E2E ParaBank Online Banking.docx. In my Test Manager project {YourName}_PB_Test, create one test case per regression test case, named with its ID and name, with its steps, and link each one to the requirement in this table."* Check the result in Test Manager before you go on.

**Ask Autopilot to find the obsolete ones**

1. Under **Requirements**, open **Login & Initial State Check**. It has four regression test cases, and at least one of them is obsolete.
2. Select **Optimize coverage**, then **Find obsolete tests**.
3. In **Add documents**, select the design document, or upload it. Select **Next**.
4. In **Provide additional guidance**, type:

    ```text
    The application under test is ParaBank at https://parabank.parasoft.com/parabank/index.htm. A test case is obsolete if it uses a screen, button, field, or flow that ParaBank doesn't have, or if its steps no longer match this requirement. For each obsolete test case, name the step that can't be done.
    ```

5. Keep the default model, or pick the one the trainer names, and select **Find obsolete tests**.
6. Wait for the notification: *Obsolete tests discovered* or *No obsolete test cases discovered*. Open the requirement to see the latest results.
7. Repeat for **Request a Loan** and **Transfer Funds Between Accounts**.

**Check, then decide**

Autopilot proposes, you decide. For each test case it flags, open ParaBank and look for the screen or button the test case needs. Then:

- **Obsolete:** add the label `Obsolete`, and un-assign it from the requirement. Don't delete it: someone may still need its history.
- **Not obsolete:** keep it, and note why Autopilot was wrong.

Do the same check the other way round: did Autopilot miss a test case you know can't run?

??? success "Trainer check: which test cases are obsolete?"
    Five test cases describe features ParaBank doesn't have:

    - **TC-PB-005 Rename Account Nickname:** **Account Details** has no **Edit Nickname**.
    - **TC-PB-007 Loan Status Lookup by Loan ID:** there's no **Loan Status** menu, and `/parabank/loanstatus.htm` doesn't exist.
    - **TC-PB-008 Transfer Funds - Review & Confirm:** **Transfer** moves the money at once. There's no review screen.
    - **TC-PB-010 Login with SMS One-Time Password:** ParaBank has no second authentication factor.
    - **TC-PB-011 Download Account Statement (PDF):** **Account Details** has no **Statements** section and no PDF download.

    The other five still fit: TC-PB-002, TC-PB-003, TC-PB-004, TC-PB-006, and TC-PB-009. TC-PB-009 depends on the demo's loan rules, so check its **Status** on screen.

Discuss as a group:

- How did these test cases end up in the design document? A feature was planned, removed, or belongs to another bank's app. Which happens in your projects?
- What does an obsolete test case cost you: a failed run, a false coverage number, or time spent fixing a test for a feature that's gone?

!!! success "Test cases done"
    At least four automated test cases, each linked to its Test Manager test case and passing on its own: Login built by hand, the rest built by Autopilot or your coding agent. Plus a few manual-only test cases from Autopilot, one autonomous run, and the obsolete regression test cases labeled and un-assigned.

!!! tip "Your automations don't build yet?"
    You can still do the Test Sets part. Link the trainer's `DemoParaBankTests` package to your test cases, one per step from T0 to T8. See [Not enough automated test cases?](test-sets.md#run-the-test-sets) in Test Sets.
