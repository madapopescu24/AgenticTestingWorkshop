Intro + theoretical aspects
{: .eyebrow }

# 🤝 Agentic Testing & Coding Agents
Learn what testing with UiPath Test Cloud looks like, what Agentic Testing adds, how coding agents work, and where the two meet in your test lifecycle.

## 🧪 Testing and UiPath Test Cloud

### 🔬 Testing in a nutshell

Testing is an investigation that gives stakeholders information about the quality of the product under test. It happens at four levels:

<div class="circles" markdown>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**Unit**

Individual units of the system, to confirm each one's code behaves as expected. Created and run by developers.

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**Integration**

Units combined and tested as a group, to find faults in how they interact

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**System / End-to-End**

The complete, integrated system, against its end-to-end specification

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**Acceptance**

The system against the business requirements, to judge whether it's ready for delivery

</div>
</div>

</div>

UiPath Test Cloud brings the most value in the middle: **integration** and **end-to-end** testing, which is exactly what the UiBank test cases in this session are. Two more ideas you'll use all day:

- **Black-box testing.** Application testing checks that the software meets its requirements from the outside, through inputs and expected outputs, without access to its code. That's how every UiBank test works.
- **Test early.** A defect found while testing costs far less than a hot-fix after it reaches production. Automation doesn't replace people: it takes the repetitive checks, so testers can focus on exploratory and usability testing.

### ☁️ What UiPath Test Cloud is

**UiPath Test Cloud** is UiPath's offering for application testers: a dedicated interface of Automation Cloud, focused on application testing, and available in the cloud and on-premises.

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">📋</span>
<span class="f-title" markdown="span">Test Manager</span>

Plan, run, manage, and analyze testing: requirements, test cases, test sets, executions, results

</div>

<div class="feature" markdown>
<span class="f-icon">🛠️</span>
<span class="f-title" markdown="span">Studio</span>

Build automated test cases with a visual designer, or as code

</div>

<div class="feature" markdown>
<span class="f-icon">⚙️</span>
<span class="f-title" markdown="span">Orchestrator</span>

Execute and manage test automation at scale, on robots

</div>

<div class="feature" markdown>
<span class="f-icon">✨</span>
<span class="f-title" markdown="span">Agentic Testing</span>

AI agents that speed up test design and execution: Autopilot for Testers, and agents you build yourself

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">Agent Builder</span>

Build those custom agents. Included with the App Tester license

</div>

</div>

### 🧱 The building blocks in Test Manager

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">📁</span>
<span class="f-title" markdown="span">Project</span>

The container for everything below

💡 Every object key starts with the project's **prefix**, for example `UIB:1`. Its **default folder** in Orchestrator is where automated and autonomous runs happen.

</div>

<div class="feature" markdown>
<span class="f-icon">📋</span>
<span class="f-title" markdown="span">Requirement</span>

What the application must do, and its acceptance criteria

💡 Requirements can also come from **Jira**, **ServiceNow**, or **Redmine**

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Test case</span>

A scenario with manual steps, linked to the requirement it covers

💡 It can be linked to an automation in Studio, or run autonomously by Autopilot

</div>

<div class="feature" markdown>
<span class="f-icon">📦</span>
<span class="f-title" markdown="span">Test set</span>

The test cases you execute together

💡 Test cases are assigned **statically** (picked by hand) or **dynamically** (by label). You can enforce an order only for statically assigned ones.

</div>

<div class="feature" markdown>
<span class="f-icon">▶️</span>
<span class="f-title" markdown="span">Execution</span>

One run of a test case or test set

💡 **Manual**, **Automated**, **Autonomous**, or **Pending**, each with a log, a result, and evidence per test case. See [Executions](executions.md).

</div>

</div>

The links between them are what Test Manager calls **traceability**: from a requirement you can see which test cases cover it and how they did in their latest run.

### 🛠️ Test automation projects in Studio

A **test automation project** is the Studio project type for application testing. Only users with the **App Tester Developer** license create and publish them.

- **Test cases and data-driven test cases.** A project holds many test cases. A data-driven test case runs once per row of test data.
- **Given / When / Then.** Every test case has three parts: set up, act, and verify. Verifications go in **Then**.
- **Testing activities included.** **Verify Expression**, **Verify Expression With Operator**, and **Verify Control Attribute** check the expected results, and can attach a screenshot to each result.
- **Object Repository.** UI targets captured from the application, shared by every test case in the project.
- **Test Explorer.** Runs and debugs test cases while you build. Its results last only for your Studio session.
- **VB or C#.** Both expression languages are supported, and test cases can also be written as code.
- **Publishing.** Publishing the project to the **Orchestrator Tenant Process Feed** creates the matching process in Orchestrator. Test Manager runs the latest published version.

### 🎫 Licenses

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🎫</span>
<span class="f-title" markdown="span">App Tester</span>

Manual testing, test management, and running (not building) automations. Includes Agent Builder.

</div>

<div class="feature" markdown>
<span class="f-icon">👩‍💻</span>
<span class="f-title" markdown="span">App Tester Developer</span>

Building automated test cases and testing automations, including agents

</div>

<div class="feature" markdown>
<span class="f-icon">🤖</span>
<span class="f-title" markdown="span">App Test Robot</span>

Running automated tests unattended, on a robot

</div>

</div>

### 🔌 Where Test Cloud connects

- **Requirements:** Jira, ServiceNow, Redmine, and other ALM tools through **Test Manager Connect**, which keeps traceability between tests and requirements.
- **Version control:** Git and TFS, through Studio.
- **CI/CD:** Jenkins, Azure DevOps, and GitHub Actions, so test sets run as part of your pipeline.

## ✨ Agentic Testing in UiPath Test Cloud

**UiPath Test Cloud** covers the whole test lifecycle: you plan and design tests in **Test Manager**, automate them in **Studio**, and run them at scale through **Orchestrator**. Agentic testing adds AI agents at each of those steps. They extend what a tester does. They don't replace the tester.

<div class="circles" markdown>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**Plan <span class="pill">Test Manager</span>**

Requirements, test cases with manual steps, test sets

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**Automate <span class="pill">Studio</span>**

Test automation projects, Given / When / Then test cases, the Object Repository

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**Execute <span class="pill">Test Manager + Orchestrator</span>**

Run test sets manually or automated, on robots

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**Analyze <span class="pill">Test Manager</span>**

Results, test case logs, assertions, screenshots, reports

</div>
</div>

</div>

### 🤖 Autopilot for Testers

UiPath ships testing agents out of the box, built into Studio and Test Manager. These are the ones you'll use in the session:

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">📝</span>
<span class="f-title" markdown="span">Autopilot panel <span class="pill ">Studio</span></span>

Generates requirements from a document you give it, and test sets from your test cases, and saves them to the Test Manager project your Studio project is connected to

</div>

<div class="feature" markdown>
<span class="f-icon">🔍</span>
<span class="f-title" markdown="span">Evaluation Agent <span class="pill ">Test Manager</span></span>

Checks a requirement for clarity, completeness, and testability

</div>

<div class="feature" markdown>
<span class="f-icon">🧪</span>
<span class="f-title" markdown="span">Test Case Generation Agent <span class="pill ">Test Manager</span></span>

Generates test cases from a requirement, steered by the **Prompt Library**: Valid E2E Scenario Testing, End-to-End Flow Verification, Rapid Test Idea Generation, Elusive Issue Detection, Boundary-Value Testing, and your own saved prompts

</div>

<div class="feature" markdown>
<span class="f-icon">🎬</span>
<span class="f-title" markdown="span">Run Autonomously <span class="pill ">Test Manager</span></span>

Runs a test case from its manual steps, without an automation. You can watch it live, and each step's execution is documented with a screenshot

</div>

<div class="feature" markdown>
<span class="f-icon">🔎</span>
<span class="f-title" markdown="span">Autopilot Search <span class="pill ">Test Manager</span></span>

Finds requirements, test cases, and other objects from a plain-English question

</div>

<div class="feature" markdown>
<span class="f-icon">📥</span>
<span class="f-title" markdown="span">Import Test Cases <span class="pill ">Test Manager</span></span>

Imports manual test cases from an Excel file, with a prompt that tells Autopilot how to read it

</div>

<div class="feature" markdown>
<span class="f-icon">📊</span>
<span class="f-title" markdown="span">Generate Insights <span class="pill ">Test Manager</span></span>

Builds a report from selected test results: overview, top failing tests, common errors, error patterns, and recommendations

</div>

<div class="feature" markdown>
<span class="f-icon">🪄</span>
<span class="f-title" markdown="span">Generate Test Case with Autopilot <span class="pill ">Studio</span></span>

In **Test Explorer**, turns a manual test case into an automated one, using the project's Object Repository to find the UI elements

</div>

</div>

You can also build your own agents for the parts of your test process that are specific to your team.

### 🪄 Autopilot for Developers

Autopilot for Developers lives in Studio, where you build and fix automations. It uses the workflow's context — variables, data types, and the current expression — to suggest or apply changes:

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🪄</span>
<span class="f-title" markdown="span">Fix</span>

📍 The magic wand at the top of the **Expression Editor**

Corrects an expression with a validation error

</div>

<div class="feature" markdown>
<span class="f-icon">✍️</span>
<span class="f-title" markdown="span">Generate or change an expression</span>

📍 The Autopilot box at the bottom of the **Expression Editor**

Writes or rewrites the expression from a plain-English instruction, such as *"Change the result of this expression to String"*

</div>

<div class="feature" markdown>
<span class="f-icon">📝</span>
<span class="f-title" markdown="span">Generate from an annotation</span>

📍 The Autopilot options next to a workflow annotation

Generates the activities the annotation describes

</div>

</div>

!!! tip "Prompting Autopilot"
    Be clear, specific, and concise. Say what output you expect and in what format, and set limits where you need them. *"Summarize this."* gets a vague answer. *"Summarize the following text in 100 words, highlighting key findings."* gets a useful one.

## 💻 What's a coding agent?

A coding agent is an AI assistant that reads, writes, and reasons about code — not just autocompletes it. Instead of suggesting the next line, it understands a goal described in plain English, explores the codebase, makes decisions, and generates entire working components. You stay in control: you review what it builds, ask it to adjust, and iterate until it's right.

Several coding agents are available today, each with their own strengths:

- **Claude Code** — Anthropic's CLI-based agent, runs in your terminal, deeply integrated with the file system. This is the one used in this exercise.
- **Codex CLI** — OpenAI's command-line coding agent, similar terminal-first approach
- **Cursor** — an IDE built around AI, tight editor integration with inline generation and multi-file context
- **Gemini CLI** — Google's terminal agent, strong on reasoning and long context
- **GitHub Copilot Agent** — embedded in VS Code and JetBrains, well suited for in-editor workflows

What makes coding agents especially powerful for UiPath work is the skill layer: by loading domain-specific knowledge about UiPath activities, APIs, and project conventions, the agent can generate production-ready test automation — not generic boilerplate. That's exactly what the UiPath skills in this exercise do.

## 🧠 The Mental Model

Five concepts show up in every coding agent:

<div class="circles" markdown>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**Tools**

Built-in actions the agent can take: read a file, run a bash command, search the web, edit code, etc.

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**Skills**

Domain knowledge bundles the agent loads when it sees a matching task. Like a playbook for one thing.

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**Commands**

Manual shortcuts you type: `/commit`, `/test`, `/deploy`. Triggered by you, not the agent.

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**Hooks**

Run automatically at lifecycle events: before an edit, after a commit, on session start. Used for guardrails.

</div>
</div>

<div class="circle-item" markdown>
<span class="num">5</span>
<div class="ci-body" markdown>

**Subagents**

Specialised workers spawned by the main agent. Used to parallelise or isolate complex tasks.

</div>
</div>

</div>

!!! info "Plugins"
    A plugin is a package that bundles any of these together — like a Marketplace app for your coding agent. The UiPath skills used in this exercise are plugins.

## 🔧 Tools, in practice

Claude Code's built-in tools are always available — no setup required:

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">📖</span>
<span class="f-title" markdown="span">Read</span>

Read any file in your project

</div>

<div class="feature" markdown>
<span class="f-icon">✏️</span>
<span class="f-title" markdown="span">Edit / Write</span>

Modify or create files

</div>

<div class="feature" markdown>
<span class="f-icon">⌨️</span>
<span class="f-title" markdown="span">Bash</span>

Execute shell commands

</div>

<div class="feature" markdown>
<span class="f-icon">🔍</span>
<span class="f-title" markdown="span">Glob / Grep</span>

Search across the codebase

</div>

<div class="feature" markdown>
<span class="f-icon">🌐</span>
<span class="f-title" markdown="span">WebSearch / WebFetch</span>

Look things up online

</div>

<div class="feature" markdown>
<span class="f-icon">👥</span>
<span class="f-title" markdown="span">Task</span>

Spawn a subagent

</div>

</div>

!!! info "Extension Tools (MCP)"
    MCP (Model Context Protocol) is the standard way to give your coding agent new tools without changing the agent itself.

    - **GitHub MCP** — read issues, open PRs
    - **Atlassian MCP** — Jira, Confluence
    - **Slack MCP** — read channels, post messages
    - **Custom UiPath MCP** — call Orchestrator, Maestro

## 🧩 Skills, in practice

A skill is a folder — sitting in `.claude/skills/` (or equivalent), with a `SKILL.md` inside.

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🔎</span>
<span class="f-title" markdown="span">Discovered automatically</span>

The agent reads each `SKILL.md`'s description. When your prompt matches, it loads the full skill on demand.

</div>

<div class="feature" markdown>
<span class="f-icon">📦</span>
<span class="f-title" markdown="span">More than just text</span>

Skills can bundle reference docs, code patterns, helper scripts, even compiled binaries the agent can run.

</div>

<div class="feature" markdown>
<span class="f-icon">🔒</span>
<span class="f-title" markdown="span">Scoped permissions</span>

A skill declares which tools it's allowed to use. Bash access can be tightly controlled.

</div>

</div>

### 📄 What's in a SKILL.md file

Every skill is built around a single `SKILL.md` file. Here's what one looks like:

```yaml
---
name: uipath-test
description: UiPath Test Manager — manage test projects, cases, sets, executions; generate reports...
allowed-tools: Bash, Read, Write, Glob, Grep
---

# UiPath Test Assistant

When the user asks to work with Test Manager:

1. Run `uip login status` and stop if the session isn't valid
2. Ask for the project name or key, then resolve it with `uip tm project list`
3. Use `uip tm` commands, always with `--output json`
4. If a command fails or a name matches more than one object, stop and ask

## References
- references/publish-and-link-guide.md
- references/failure-triage-guide.md
- references/test-result-report-guide.md
```

The file has four parts:

<div class="circles" markdown>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**Frontmatter**

Declares the skill's name, description, and which tools it's allowed to use.

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**Discovery prompt**

The `description` field is what the agent matches against your request — this is how the skill gets loaded automatically.

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**Instructions**

The body of the file: a step-by-step prompt the agent follows when the skill is active.

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**References**

Paths to files in the skill folder the agent can read for deeper context — API docs, code patterns, example projects.

</div>
</div>

</div>

## 🔗 Where UiPath fits in this picture

UiPath ships a plugin for Claude Code. It bundles skills, hooks, and references — giving the agent domain knowledge about UiPath products out of the box.

```bash
npm -g install @uipath/cli
uip skills install
```

The plugin contains three things:

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">20+ skills</span>

Domain knowledge for every UiPath product: `uipath-test`, `uipath-rpa`, `uipath-platform`, `uipath-agents`, `uipath-maestro-flow`, and more.

</div>

<div class="feature" markdown>
<span class="f-icon">🤖</span>
<span class="f-title" markdown="span">1 subagent</span>

`uipath-project-discovery-agent` — auto-runs on first contact with a UiPath project and builds context for the agent.

</div>

<div class="feature" markdown>
<span class="f-icon">🪝</span>
<span class="f-title" markdown="span">Hooks & references</span>

Session-start nudges, activity docs, and allowlists for safe read-only commands.

</div>

</div>

## 📚 The UiPath skill catalog

The plugin includes skills for every part of the UiPath platform. Three of them drive the labs in this exercise:

<div class="feature-grid" markdown>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-test` <span class="pill ">Used today</span></span>

Test Manager: projects, requirements, test cases and steps, test sets, executions, failure triage, and reports. Also links Studio automations to test cases.

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-rpa` <span class="pill ">Used today</span></span>

Generate and edit Studio projects with a discovery-first approach, including test automation projects, Given / When / Then test cases, and data-driven tests

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-platform` <span class="pill ">Used today</span></span>

Auth, Orchestrator management (folders, packages, assets), Integration Service, CLI tools

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-troubleshoot`</span>

Root-cause investigation when a job or a run behaves unexpectedly

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-agents`</span>

Scaffold, build, run, evaluate, and deploy coded and low-code agents

</div>

<div class="feature" markdown>
<span class="f-icon">🧩</span>
<span class="f-title" markdown="span">`uipath-maestro-flow`</span>

Create, validate, and debug UiPath Flow projects

</div>

</div>

!!! tip "Skills used in this exercise"
    The three skills in bold — `uipath-test`, `uipath-rpa`, and `uipath-platform` — are the ones a coding agent uses if you pick it to automate a test case or run test sets in the hands-on session.

## ⚖️ Where the coding agent fits

Autopilot works inside one product at a time, on what's in front of you. A coding agent works from your terminal, across products, through the `uip` CLI:

<div class="vs" markdown>
<div class="vs-side" markdown>
<span class="f-title" markdown="span">🤖 Autopilot for Testers and for Developers</span>

- **Where you use it:** Inside Studio or Test Manager
- **What it sees:** The requirement, expression, or results in front of you
- **Best for:** Requirements and test cases from a document, requirement quality, test case suggestions, fixing an expression, explaining results

</div>
<div class="vs-mid">VS</div>
<div class="vs-side alt" markdown>
<span class="f-title" markdown="span">💻 Coding agent + UiPath skills</span>

- **Where you use it:** Your terminal or editor
- **What it sees:** Files on your machine, your Studio project, Test Manager, and Orchestrator in one session
- **Best for:** Work that spans files and products: checking coverage against a document, a suite of Given / When / Then automations, publish, link, run, and report

</div>
</div>

In the hands-on session, Autopilot leads. Autopilot in Studio writes the requirements and the test sets, and Autopilot in Test Manager evaluates the requirements, generates the test cases, and runs one autonomously. You automate the Login test case by hand, so you know what good looks like. Then you automate the next one with Autopilot in Studio or a coding agent, and compare the two.
