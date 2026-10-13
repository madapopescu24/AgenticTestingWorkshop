# UiPath Coding Agents Workshop — Site

Hands-on course teaching clients & partners to build UiPath agents and Maestro
orchestrations with coding agents (Claude Code) and the `uip` CLI.

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
| `main.py` | Environment variables (staging vs prod) for the training callout |
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
COURSE_ENV=staging mkdocs serve -f mkdocs.local.yml
# open http://127.0.0.1:8000

# 4. Release-equivalent build check
COURSE_ENV=prod mkdocs build
```

## Publishing to GitHub

This repo is scaffolded locally. To create the remote and deploy:

```bash
cd coding-agents-course
git init && git add . && git commit -m "Initial scaffold"
gh repo create uipath-practice/CodingAgentsCourse --public --source=. --push
# then enable GitHub Pages on the gh-pages branch (created by the deploy workflow)
```

## Trainer Notes (Internal)

This section is for trainers/facilitators only. It stays in this README rather
than `docs/` because GitHub Pages has no way to restrict access by email —
anything admin-only needs to live in the repo itself, not on the public site.
Do not move this content into `docs/` or reference it from
`mkdocs.yml`/`mkdocs.local.yml`.

### Environment & Tenant Setup

The site's `main.py` defines a `COURSE_ENV` switch with two profiles (`staging`
and `prod`) driving the `{{ training_url }}` / `{{ training_tenant }}` macros
used throughout the lessons. In practice, only the cloud environment below is
real — there is no separate staging UiPath org/tenant to author or test
against. Treat the `staging` profile in `main.py` as unused/vestigial.

| Organization | URL | Tenant | Used for |
|---|---|---|---|
| `tpenlabs` | https://cloud.uipath.com/tpenlabs | `CodingAgentsPractice` | The one real environment — both authoring/testing and the live participant-facing environment (CI builds with `COURSE_ENV=prod`) |

All exercises operate inside a single shared Orchestrator folder in this
org/tenant (`tpenlabs` / `CodingAgentsPractice`):

- **Folder name:** `CodingAgentsILT`
- **Folder key:** `c30345cd-5543-46a9-b42b-0354e60b4f15`

Every deployable artifact (agent, coded app, Maestro flow, RPA process) is
named with a `{YourName}` prefix (e.g. `{YourName}LoanUnderwritingAgent`) so
participants sharing the same tenant/folder don't collide with each other's
packages, processes, or Orchestrator entities.

### Inviting Participants

Before a cohort starts, invite each participant to the `tpenlabs` org so they
can log in with their own email:

1. In the `tpenlabs` org, go to the **Admin** tab.
2. Go to **Accounts and Local Groups**.
3. Invite each participant using their email address.
4. Make sure each invited participant is added to the **CodingAgentsGroup**
   local group — this is what grants them access to the `CodingAgentsPractice`
   tenant and the `CodingAgentsILT` folder.

### Before Each Training

- [ ] Confirm the **LoanUnderwriting** storage bucket exists in the
      **CodingAgentsILT** folder in Orchestrator — the RPA lesson (Application
      Intake & Enrichment) uploads results there, and the run fails if it's
      missing.

For the **recruitment pipeline** session (two 90-minute blocks), the time
budget only works if the platform prerequisites are ready before the session:

- [ ] Build and publish the two fallback processes in the **CodingAgentsILT**
      folder, following the contract on the hands-on page:
      `DemoJobMatchingAgent` (input `job_title`, output `job` + `matches`) and
      `DemoRegisterInUiBank` (`in_CandidatesJson` → `out_ResultsJson`).
      Anyone whose Lab 1 or Lab 2 doesn't finish uses these in Lab 3.
- [ ] Do one full dry run of the `{YourName}RecruitmentPipeline` flow with the
      demo processes, including the Action Center approval.
- [ ] Make sure **unattended robots** that can run browser automation are
      available to the **CodingAgentsILT** folder, with enough capacity for
      the whole group to run the RPA step in the same 15 minutes. This is the
      most likely bottleneck in Lab 3.
- [ ] Confirm participants can use the **LLM Gateway** from coded agents in
      the tenant — Lab 1 doesn't ask for a personal Anthropic/OpenAI key.
- [ ] Confirm the **CodingAgentsGroup** has rights to create Maestro flows and
      receive Action Center tasks in the folder.
- [ ] Send the [Setup](docs/setup.md) page at least two days ahead. Setup is
      not part of the 180 minutes. Ask Mac users to pair with a Windows user
      for Lab 2.

### TODO — fill in before the next cohort

- [ ] Is there a reset/cleanup step needed between cohorts (stale processes,
      packages, jobs, Action Center tasks left in the shared folder from the
      previous run)? Document the steps or the script here.
- [ ] Any UiBank API seed-data reset needed, or is `https://uibank-api.uipath.com`
      stable/shared indefinitely across cohorts?
- [ ] Who to contact if a participant needs their credentials/tenant access
      re-issued mid-workshop?

### Timing & Agenda

The recruitment pipeline session runs in **two 90-minute blocks with no
breaks**, and the full use case — including the Maestro orchestration — is
built inside them. There is no homework. The participant-facing schedule is on
the Agenda page; the trainer view:

| Block | Time | Part | Trainer focus |
|---|---|---|---|
| 1 | 0:00–0:20 | Intro | Present *What's a Coding Agent?*; demo one skill loading live |
| 1 | 0:20–0:25 | Ready check | `uip login status`; anyone failing pairs up — don't debug setup live |
| 1 | 0:25–0:30 | Scenario and contract | Walk the data-flow diagram and the contract table — it's what makes Lab 3 work |
| 1 | 0:30–1:20 | Lab 1 — Coded Agent | Everyone pastes the prompt at the same time; narrate the plan the agent shows |
| 1 | 1:20–1:30 | Checkpoint | Compare shortlists; confirm processes exist; point stragglers at `DemoJobMatchingAgent` |
| 2 | 0:00–0:30 | Lab 2 — RPA | Mac users pair; at 0:25 everyone publishes, finished or not |
| 2 | 0:30–1:20 | Lab 3 — Maestro Flow | Watch robot capacity; show one approval in Action Center on screen |
| 2 | 1:20–1:30 | Wrap-up | *What you built*, *Gotchas*, next steps |

Architecture changes from the earlier versions (both archived locally under
`Archive/`):

- **Coded App and Data Service removed.** The Coded App needed an External
  App, OAuth scopes, entity IDs, and a 15-step publish — it didn't fit next to
  the orchestration. The recruiter now reviews the shortlist in an **Action
  Center** approval task, and Maestro passes data between steps, so no
  entities are needed.
- **Maestro moved from homework into Lab 3.** It's the step that turns the
  components into the full use case.
- **A fixed data contract** between components (`job_title` → `job` +
  `matches` → `in_CandidatesJson` → `out_ResultsJson`) so components built in
  separate prompts plug together, and the demo processes can stand in for any
  participant's.
- Lab 1: one job title, provided `candidates.json`, no web search, LLM Gateway
  instead of personal API keys, 3 eval cases.
- Lab 2: candidates come in as an argument instead of a CSV; usernames get a
  per-participant suffix to avoid UiBank collisions.

**Time-keeping rule:** when a lab's time box ends, publish what you have and
move on. Anyone behind switches to the demo processes in Lab 3 and still
finishes the pipeline.

### Answer Keys / Expected Outputs

_Not yet documented — add reference solutions / expected results here._
