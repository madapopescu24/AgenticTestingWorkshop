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

## 🔗 Useful links

<div class="link-grid" markdown>

<a class="link-card" href="https://github.com/UiPath/skills" target="_blank" rel="noopener"><span class="f-icon">🧩</span><span class="f-title">UiPath/skills</span><span class="f-text" markdown="span">The skill repository. Read the `SKILL.md` of `uipath-test` and `uipath-rpa`.</span></a>
<a class="link-card" href="https://uibank.uipath.com" target="_blank" rel="noopener"><span class="f-icon">🏦</span><span class="f-title">UiBank</span><span class="f-text" markdown="span">The demo banking application under test</span></a>
<a class="link-card" href="https://meera-uipath.github.io/software-testing-ilt-guide" target="_blank" rel="noopener"><span class="f-icon">🎓</span><span class="f-title">Test Cloud & Agentic Testing ILT Guide</span><span class="f-text" markdown="span">The click-by-click Test Manager and Studio course: Object Repository, data-driven testing, publishing, and executing test cases</span></a>
<a class="link-card" href="https://docs.uipath.com/test-manager" target="_blank" rel="noopener"><span class="f-icon">📋</span><span class="f-title">Test Manager documentation</span><span class="f-text" markdown="span">Requirements, test cases, test sets, executions, and Autopilot for Testers</span></a>

</div>
