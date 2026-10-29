# UiPath Agentic Testing with Coding Agents — Site

Hands-on course teaching clients & partners UiPath Agentic Testing with coding agents
(Claude Code) and the `uip` CLI: plan a test case in Test Manager, automate it in
Studio, execute it, and report on it. The scenario is the UiBank test case design
document E2E UiBank Online Banking, which becomes eight requirements and eight independent test cases.

Built on the same MkDocs framework as the
[Agentic Practice Workshop](https://github.com/uipath-practice/AgenticPracticeCourse),
with three additions: a private knowledge base, a configurable training environment,
and a CLI/KB-driven lesson-generation path alongside the screenshot path.

## How it works

```
../knowledge-base/  (private SSOT, NOT in this repo)
        ↓  used as context to generate accurate lessons
docs/*.md  →  MkDocs builds HTML  →  GitHub Actions  →  gh-pages  →  GitHub Pages
```

| Path | Purpose |
|------|---------|
| `docs/` | Published page content — one `.md` per page |
| `mkdocs.yml` | Site config + **published** nav |
| `mkdocs.local.yml` | Local-only nav incl. work-in-progress (gitignored) |
| `main.py` | Environment variables for the training callout |
| `Master/` | Authoring rules & templates (copied from base framework) |
| `.claude/commands/` | Authoring slash commands (copied from base framework) |
| `hooks/`, `scripts/` | Two-column hook; screenshot metadata pipeline (copied) |
| `.github/workflows/deploy.yml` | Auto-deploy to GitHub Pages on push to `main` |

The knowledge base is intentionally kept **outside this public repo** (`../knowledge-base/`)
so internal material is never published.

## First-time setup

```bash
# 1. Pull the reusable framework files from the base repo
./bootstrap-framework.sh

# 2. Install dependencies
pip install -r requirements.txt

# 3. Preview locally (authoring environment + WIP nav)
COURSE_ENV=prod mkdocs serve -f mkdocs.local.yml
# open http://127.0.0.1:8000

# 4. Release-equivalent build check (CI deploys the prod profile)
COURSE_ENV=prod mkdocs build
```

## Publishing to GitHub

This repo is scaffolded locally. To create the remote and deploy:

```bash
cd AgenticTestingWorkshop
git init && git add . && git commit -m "Initial scaffold"
gh repo create madapopescu24/AgenticTestingWorkshop --public --source=. --push
# then enable GitHub Pages on the gh-pages branch (created by the deploy workflow)
```

## Trainer Notes (Internal)

This section is for trainers/facilitators only. It stays in this README rather
than `docs/` because GitHub Pages has no way to restrict access by email —
anything admin-only needs to live in the repo itself, not on the public site.
Do not move this content into `docs/` or reference it from
`mkdocs.yml`/`mkdocs.local.yml`.

### Environment & Tenant Setup

The site's `main.py` defines a `COURSE_ENV` switch with one profile (`prod`)
driving the `{{ training_url }}`, `{{ training_org }}`,
`{{ training_tenant }}`, and `{{ training_folder }}` macros used throughout the
lessons. **The workshop runs on Automation Cloud**, organization `tpenlabs`,
tenant `AgenticTestingWorkshop`. CI deploys with `COURSE_ENV=prod`, and that is
also the default.

| Profile | Organization | URL | Tenant | Used for |
|---|---|---|---|---|
| `prod` | `tpenlabs` | https://cloud.uipath.com/tpenlabs | `AgenticTestingWorkshop` | **The participant environment.** Studio, the `uip` CLI, Test Manager, and Orchestrator all point here. |

_TODO — confirm `tpenlabs` / `AgenticTestingWorkshop` has Test Manager delivered
through Test Cloud, Autopilot for Testers, and Autopilot for Developers enabled._
To run the session on another tenant, change `training_tenant` (and, if needed,
`training_org`) for the `prod` profile in `main.py`.

All exercises operate inside a single shared Orchestrator folder on that tenant.
Test Manager for the tenant is at
`https://cloud.uipath.com/tpenlabs/AgenticTestingWorkshop/testmanager_`.

- **Folder name:** `AgenticTesting` (the `training_folder` macro in `main.py`). It's
  the default Orchestrator folder of every participant's Test Manager project, and
  holds the test packages and the credential assets.
- **Folder key:** _TODO — create or confirm the `AgenticTesting` folder in `AgenticTestingWorkshop`
  and record its key here._

Every deployable artifact (test package, credential asset, Test Manager project) is
named with a `{YourName}` prefix (e.g. `{YourName}UiBankTests`) so
participants sharing the same tenant/folder don't collide with each other's
packages, processes, or Orchestrator entities.

### Inviting Participants

Before a cohort starts, invite each participant to the org
(`tpenlabs` on `cloud.uipath.com`) so they can log in with their own email:

1. In the `tpenlabs` org, go to the **Admin** tab.
2. Go to **Accounts and Local Groups**.
3. Invite each participant using their email address.
4. Make sure each invited participant is added to the **CodingAgentsGroup**
   local group (create it if it doesn't exist) — this is what grants
   them access to the `AgenticTestingWorkshop` tenant, Test Manager, and the `AgenticTesting`
   folder.

### Before Each Training

The agentic testing session (about 8 hours) only works if the platform
prerequisites are ready before it starts:

- [ ] Build and publish the fallback test package `DemoUiBankTests` in the
      **AgenticTesting** folder. Its test entry points `T0_LoginAndInitialAccountState`
      to `T7_LogoutAndEvidenceCollection` automate the eight test cases, one each,
      and pass in any order. Anyone whose own automations from Test Cases
      aren't ready links this one to their test cases in Test Sets.
- [ ] Create a credential asset for the demo package's UiBank user in the folder,
      and do one full dry run: link `DemoUiBankTests` to a Test Manager test case,
      run its test set as automated, and check the screenshots arrive.
- [ ] Give every participant an **App Test Developer** licence, and check an
      **AI Trust Layer** policy allows Autopilot on the tenant.
- [ ] Assign a **robot account with stored credentials** to the **AgenticTesting**
      folder, with a **Testing** or **Production** runtime. Without credentials,
      test set jobs stay Pending with `RobotNoCredentials`, even when the runtime
      shows Connected and Available.
- [ ] Have at least one **Windows** robot in the folder: autonomous test execution
      is supported on Windows only, and needs Test Manager delivered through
      Test Cloud. With only a macOS robot, autonomous runs stay Pending with no
      Orchestrator job.
- [ ] Ask the UiBank owners whether the **Important Notice** privacy dialog can
      show once per user. Today it appears from the second sign-in on, and closing
      it with ✕ logs the user out.
- [ ] Make sure **unattended robots** that can run Chrome browser automation are
      available to the **AgenticTesting** folder — automated test sets AND every
      participant's **Run Autonomously** execution run there. Serverless (the
      "Default Serverless" template has no runtime slots) and participants'
      personal-workspace robots don't pick these jobs up: they stay Pending with
      no error. Stop and re-run any job that went Pending before a robot was
      available. Plan enough capacity for the whole group to run their
      autonomous executions and test sets in the same 10 minutes. This is the most
      likely bottleneck in Test Sets.
- [ ] Confirm **Autopilot** is enabled on the `AgenticTestingWorkshop` tenant for everyone in the
      group: the Autopilot panel in Studio (the hands-on part starts with it
      generating the requirements, and uses it again to create test sets), **Generate Test Case with
      Autopilot** in Test Explorer, the Evaluation Agent, Test Case Generation,
      Prompt Library, **Run Autonomously**, and Generate Insights in Test Manager,
      and Fix / generate in Studio's Expression Editor. Do one dry run of the
      requirements prompt and check it produces eight requirements named
      after the steps. Run one test case autonomously end to end, and check
      the live stream and the per-step screenshots work for participants.
- [ ] Confirm the **CodingAgentsGroup** can create Test Manager projects (the
      hands-on Setup creates one per participant), create credential assets, and upload packages
      in the folder.
- [ ] Check participants can sign Studio in to `cloud.uipath.com/tpenlabs`. Studio signed
      in to another organization or tenant is the most likely Setup failure.
- [ ] The design document is published on the site as
      `docs/resources.assets/E2E UiBank Online Banking.docx` (download buttons on
      the hands-on page and Resources). It's a cleaned copy: leftover images from
      another project, author metadata, and a real username/email were removed.
      If you update the original, clean it the same way before replacing it.
- [ ] Plan time for the [Setup](docs/setup.md) page at the start of the hands-on
      part, right after the intro: participants do it during the session, including the UiBank
      registration and the credential asset. Setup is part of the
      8 hours. Ask Mac users to pair with a Windows user from the Login test case on.

### TODO — fill in before the next cohort

- [ ] Is there a reset/cleanup step needed between cohorts (Test Manager projects,
      packages, credential assets, executions left from the previous run)? Document
      the steps or the script here.
- [ ] UiBank data can be reset at any time. Do participants need to re-register
      before each cohort?
- [ ] Who to contact if a participant needs their credentials/tenant access
      re-issued mid-workshop?

### Timing & Agenda

The session runs for **about 8 hours** (9:00 to 17:00), with a 15-minute break after
Requirements, a 45-minute lunch (12:30) in the middle of Test Cases,
and a 10-minute break before Executions. It ends with SAP Testing, Q&A, and feedback.
The timings are approximate: adapt them during the workshop, including the breaks.
There is no homework. The
participant-facing schedule is on the Agenda page; the trainer view:

| Time | Agenda item | Trainer focus |
|---|---|---|
| 0:00–0:30 | Welcome | Introductions and the plan for the day |
| 0:30–1:45 | 1. Intro + Theoretical Aspects | Present *Agentic Testing & Coding Agents*: Test Cloud, Autopilot for Testers, Autopilot for Developers, coding agents; when to use which. Check Studio is signed in to `tpenlabs` / `AgenticTestingWorkshop` for everyone. |
| 1:45–2:00 | Setup | Everyone works through the Setup page (VM, sign-in, tenant, `uip login`, Studio, UiBank user, credential asset, design document), then creates a Test Manager project (name `{YourName}_UIB_Test`, a unique prefix of 3–5 characters, such as their initials plus a digit: prefixes must be free in the tenant and can't be changed) and sets its default folder, then the Studio test automation project, then connects them; check the Autopilot panel opens for everyone before moving on |
| 2:00–2:15 | Autopilot in Studio creates requirements | Demo the prompt on screen first; check everyone gets eight requirements named after the steps |
| 2:15–2:25 | Discuss the requirements | Traceability, testability, gaps; did Autopilot invent rules? |
| 2:25–2:45 | Evaluate, improve, re-evaluate | Demo the Evaluation Agent on one requirement before people try |
| 2:45–3:00 | Break | |
| 3:00–3:30 | Autopilot in Test Manager creates test cases | Login requirement; show the Prompt Library |
| 3:30–4:15 | Lunch | Help stragglers who are still creating test cases |
| 4:15–4:45 | Implement the Login test case manually | Walk Given / When / Then; make sure targets go into the Object Repository |
| 4:45–5:15 | Autopilot in Studio / Codex generates a test case | Split the room between Autopilot and coding agent; compare results at the end |
| 5:15–5:30 | Run Autonomously | Everyone runs a negative login test case autonomously; point out the live stream and the per-step screenshots |
| 5:30–6:05 | Implement a few more test cases | Point people at the *Given* column: transfer and lookup set up their own data |
| 6:05–6:15 | Break | |
| 6:15–6:25 | Executions tab | Everyone explores their own executions: the autonomous run, its test case log, and the screenshots |
| 6:25–6:35 | Test Sets | Everyone publishes the testing project to the Orchestrator Tenant Process Feed first; then Autopilot creates smoke + regression sets; run; watch robot capacity; Generate Insights |
| 6:35–6:45 | Next Steps | *What you built*, *Gotchas* |
| 6:45–7:45 | SAP Testing | |
| 7:45–7:55 | Q&A | |
| 7:55–8:00 | Feedback | |

The previous recruitment pipeline session (Coded Agent → RPA → Maestro Flow) is
archived locally under `Archive/recruitment-pipeline/`.

**Time-keeping rule:** when a step's time box ends, move on with what you have.
Anyone behind links `DemoUiBankTests` in Test Sets and still runs a test set and reads
its executions.

### Answer Keys / Expected Outputs

_Not yet documented — add reference solutions / expected results here._
