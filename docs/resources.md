Resources
{: .eyebrow }

# 📚 Resources

**Reference material and links to keep handy during and after the session.**

!!! tip "Training Environment"
    Log in at **[{{ training_url }}]({{ training_url }})** using tenant **{{ training_tenant }}**.

## 📄 The design document

The whole hands-on part starts from the same document: **E2E UiBank Online Banking**. Download it and save `E2E UiBank Online Banking.docx` in your workshop folder.

[Download the design document (.docx)](resources.assets/E2E%20UiBank%20Online%20Banking.docx){ .md-button .md-button--primary }

[The hands-on page](agentic-testing-hands-on.md#the-design-document) summarises its steps, the requirements they become, and the test data.

## 🎁 Trainer's reference package

The trainer's `DemoUiBankTests` is a working test automation project with all eight test cases automated. It's already published in the `{{ training_folder }}` folder, so you can link it to your Test Manager test cases and run it in [Test Sets](test-sets.md) if your own automations aren't ready.

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🎁</span>
<span class="f-title" markdown="span">`DemoUiBankTests`</span>

Test automation project, reference solution for the Test Cases part

🧪 `T0_LoginAndInitialAccountState` to `T7_LogoutAndEvidenceCollection`

📁 `{{ training_folder }}` folder

</div>

</div>

!!! info "Reference, not a shortcut"
    Build your own test cases first. The point of the session is to see how Autopilot and your coding agent plan, automate, and run them. The reference package is there for when something blocks you, and for comparing afterwards.

## ⌨️ CLI cheat sheet

Commands you'll see a coding agent run with the `uip` CLI, if you use one to generate a test case or run test sets. Add `--output json` to each one.

| Command | What it does | When you'll see it |
| :--- | :--- | :--- |
| `uip skills install` | Install UiPath skills into your coding agent | First-time setup |
| `uip login` / `uip login status` | Authenticate with your tenant / check the session | Start of each session |
| `uip tm project list --filter <key>` | Find a Test Manager project | Before any Test Manager work |
| `uip tm requirements list` / `uip tm testcases list` | List requirements and test cases | Checking coverage |
| `uip rpa tm connect` / `set-default-project` | Connect a Studio project to Test Manager | Setup |
| `uip rpa validate` / `uip rpa build` | Check and build the project | After every change |
| `uip rpa pack` + `uip or packages upload` | Package and publish to Orchestrator | Before running test sets |
| `uip tm testcases link-automation` | Bind an automation to a Test Manager test case | After publishing |
| `uip tm testsets run` + `uip tm wait` | Execute a test set and wait for the result | Running test sets |
| `uip tm report get` / `uip tm result download` | Summarise an execution / download JUnit XML | Reporting |
| `uip feedback send` | Report a bug or a skill that guessed wrong | Whenever something breaks |

## 🔗 Useful links

<div class="link-grid" markdown>

<a class="link-card" href="https://github.com/UiPath/skills" target="_blank" rel="noopener"><span class="f-icon">🧩</span><span class="f-title">UiPath/skills</span><span class="f-text" markdown="span">The skill repository. Read the `SKILL.md` of `uipath-test` and `uipath-rpa`.</span></a>
<a class="link-card" href="https://uibank.uipath.com" target="_blank" rel="noopener"><span class="f-icon">🏦</span><span class="f-title">UiBank</span><span class="f-text" markdown="span">The demo banking application under test</span></a>
<a class="link-card" href="https://meera-uipath.github.io/software-testing-ilt-guide" target="_blank" rel="noopener"><span class="f-icon">🎓</span><span class="f-title">Test Cloud & Agentic Testing ILT Guide</span><span class="f-text" markdown="span">The click-by-click Test Manager and Studio course: Object Repository, data-driven testing, publishing, and executing test cases</span></a>
<a class="link-card" href="https://docs.uipath.com/test-manager" target="_blank" rel="noopener"><span class="f-icon">📋</span><span class="f-title">Test Manager documentation</span><span class="f-text" markdown="span">Requirements, test cases, test sets, executions, and Autopilot for Testers</span></a>

</div>
