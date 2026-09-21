# Coding Agents + UiPath: Hands-On Session

**Build a Coded Agent, an RPA workflow, and a Coded App — all from your coding agent, all wired into one recruitment pipeline.**

!!! tip "Here is our plan for this session:"

    1. Get the mental model for coding agents, skills, tools, and plugins —
       see [What's a Coding Agent?](what-is-a-coding-agent.md).
    2. Build a **Coded Agent** that researches jobs and matches candidates.
    3. Build an **RPA** workflow that registers those candidates on a web form.
    4. Build a **Coded App** dashboard that shows the whole pipeline.
    5. Optionally bring all three together in **Maestro** — a homework deep dive.

## Goal

By the end of the session you'll have three deployed components talking to each other through **Data Service**: a Python agent that finds jobs and scores candidates, an XAML workflow that registers each candidate on a website with no API, and a React dashboard the recruiter actually uses. You'll have generated all three by prompting a coding agent — not by dragging activities onto a canvas or scaffolding React by hand.

!!! tip "Training Environment"
    Log in at **[{{ training_url }}]({{ training_url }})** and remember using tenant **{{ training_tenant }}** for this session.

## The agenda

One connected scenario, mostly hands-on. Pick the format that fits your group.

=== "Two days"

    **Day 1 — Foundations and the agent** · 3h

    | Part | Focus | Duration | Format |
    | :--- | :--- | ---: | :--- |
    | 💡 <strong style="color: var(--md-primary-fg-color);">Intro</strong> | Coding agents, skills, tools, plugins. The mental model. | 0.5h | Presentation |
    | ✅ <strong style="color: var(--md-primary-fg-color);">Environment check</strong> | Confirm the `uip` CLI, the skills, and your tenant login all work | 0.5h | Hands-on |
    | 🤖 <strong style="color: var(--md-primary-fg-color);">Coded Agent</strong> | Research jobs, generate JDs, match candidates | 1.5h | Hands-on |
    | 💬 <strong style="color: var(--md-primary-fg-color);">Recap and Q&A</strong> | What the agent does, what breaks, what comes next | 0.5h | Discussion |

    **Day 2 — Automation and the dashboard** · 3.5h + 0.5h optional

    | Part | Focus | Duration | Format |
    | :--- | :--- | ---: | :--- |
    | ⚙️ <strong style="color: var(--md-primary-fg-color);">RPA Workflow</strong> | Register candidates on UiBank | 1.5h | Hands-on |
    | 📊 <strong style="color: var(--md-primary-fg-color);">Coded App</strong> | Dashboard of jobs, matches, and registered candidates | 2h | Hands-on |
    | 🔗 <strong style="color: var(--md-primary-fg-color);">Integrate in Maestro</strong> <em style="color: #6a6a6a; font-weight: 400;">(optional)</em> | Bring the agents, RPA, and apps together end-to-end | 0.5h | Homework |

=== "One day"

    **Five and a half hours**, plus breaks and lunch — the Maestro part is optional on top.

    | Part | Focus | Duration | Format |
    | :--- | :--- | ---: | :--- |
    | 💡 <strong style="color: var(--md-primary-fg-color);">Intro</strong> | Coding agents, skills, tools, plugins. The mental model. | 0.5h | Presentation |
    | 🤖 <strong style="color: var(--md-primary-fg-color);">Coded Agent</strong> | Research jobs, generate JDs, match candidates | 1.5h | Hands-on |
    | ⚙️ <strong style="color: var(--md-primary-fg-color);">RPA Workflow</strong> | Register candidates on UiBank | 1.5h | Hands-on |
    | 📊 <strong style="color: var(--md-primary-fg-color);">Coded App</strong> | Dashboard of jobs, matches, and registered candidates | 2h | Hands-on |
    | 🔗 <strong style="color: var(--md-primary-fg-color);">Integrate in Maestro</strong> <em style="color: #6a6a6a; font-weight: 400;">(optional)</em> | Bring the agents, RPA, and apps together end-to-end | 0.5h | Homework |

!!! info "The Maestro integration is optional"
    The three labs stand on their own — you finish with a working agent, workflow, and app. Wiring them into a single **Maestro** orchestration is a deep dive for anyone who wants to take it further, and it works well as homework after the session.

## The scenario

<div style="font-family: inherit; margin: 1.5rem 0 2rem;">

  <div style="background: #16213e; border-left: 10px solid #FA4616; padding: 26px 32px; margin-bottom: 22px;">
    <div style="font-size: 20px; font-weight: 700; color: #ffffff; line-height: 1.35;">A staffing agency is digitizing its recruitment pipeline.</div>
    <div style="font-size: 15px; font-style: italic; color: #f6c3ab; margin-top: 10px; line-height: 1.45;">Three problems: find jobs, register candidates, and give recruiters a view of everything.</div>
  </div>

  <div style="display: flex; flex-wrap: wrap; gap: 18px; align-items: stretch;">
  <div style="flex: 1 1 260px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 5px solid #FA4616; padding: 20px 22px 22px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 18px;">
      <img src="../coding-agents-hands-on.images/icon-search.png" alt="" style="width: 46px; height: 46px; box-shadow: none; border: none;">
      <span style="font-size: 34px; font-weight: 700; color: #f6c3ab; line-height: 1;">01</span>
    </div>
    <div style="font-size: 17px; font-weight: 700; color: #16213e; margin-bottom: 12px;">Coded Agent</div>
    <div style="font-size: 13.5px; color: #4a4a4a; line-height: 1.55; margin-bottom: 18px;">Searches the web for open jobs, generates structured JDs, matches against a candidate pool.</div>
    <div style="font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12.5px; color: #FA4616; font-weight: 600;">&rarr; Writes to Data Service</div>
  </div>
  <div style="flex: 1 1 260px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 5px solid #FA4616; padding: 20px 22px 22px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 18px;">
      <img src="../coding-agents-hands-on.images/icon-register.png" alt="" style="width: 46px; height: 46px; box-shadow: none; border: none;">
      <span style="font-size: 34px; font-weight: 700; color: #f6c3ab; line-height: 1;">02</span>
    </div>
    <div style="font-size: 17px; font-weight: 700; color: #16213e; margin-bottom: 12px;">RPA Workflow</div>
    <div style="font-size: 13.5px; color: #4a4a4a; line-height: 1.55; margin-bottom: 18px;">Reads candidate CSV, registers each one on <code>uibank.uipath.com/register-account</code>.</div>
    <div style="font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12.5px; color: #FA4616; font-weight: 600;">&rarr; Writes status back to Data Service</div>
  </div>
  <div style="flex: 1 1 260px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 5px solid #FA4616; padding: 20px 22px 22px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 18px;">
      <img src="../coding-agents-hands-on.images/icon-dashboard.png" alt="" style="width: 46px; height: 46px; box-shadow: none; border: none;">
      <span style="font-size: 34px; font-weight: 700; color: #f6c3ab; line-height: 1;">03</span>
    </div>
    <div style="font-size: 17px; font-weight: 700; color: #16213e; margin-bottom: 12px;">Coded App</div>
    <div style="font-size: 13.5px; color: #4a4a4a; line-height: 1.55; margin-bottom: 18px;">Recruiter dashboard: open jobs, generated descriptions, matched candidates, registration status.</div>
    <div style="font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12.5px; color: #FA4616; font-weight: 600;">&rarr; Reads from Data Service</div>
  </div>
  </div>

</div>

One connected story across all three labs — each one hands its output to the next through Data Service.

## <img src="../coding-agents-hands-on.images/icon-search.png" alt="" style="width: 1.05em; height: 1.05em; vertical-align: -0.12em; margin-right: 0.4em; border: none; box-shadow: none;">Lab 1 — the Coded Agent { .lab-title }

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">Jobs research + candidate matching</div>

**75 min build + 15 min review**

### What's a Coded Agent?

Not to be confused with the *coding* agent you're typing into. A Coded Agent is a Python agent you write yourself and run on UiPath infrastructure. You pick the framework, use the UiPath SDK, package it with one CLI command, and deploy it to Orchestrator.

<div style="font-size: 13px; font-weight: 700; letter-spacing: 0.09em; color: #FA4616; margin: 1.4rem 0 0.8rem;">SUPPORTED FRAMEWORKS</div>

<div style="display: flex; flex-wrap: wrap; gap: 14px; align-items: stretch; margin-bottom: 1.5rem;">
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="font-size: 17px; font-weight: 700; color: #16213e; margin-bottom: 9px;">LangGraph</div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Graph-based, stateful agent flows</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="font-size: 17px; font-weight: 700; color: #16213e; margin-bottom: 9px;">LlamaIndex</div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">RAG and document-grounded agents</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="font-size: 17px; font-weight: 700; color: #16213e; margin-bottom: 9px;">OpenAI Agents SDK</div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">OpenAI's official agent framework</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="font-size: 17px; font-weight: 700; color: #16213e; margin-bottom: 9px;">Plain Python</div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Simple function-based agents</div>
  </div>
</div>

### What the hiring agent does

The four nodes run in order — each one feeds the next, and `Persist` closes the loop by writing to Data Service for Lab 2 to pick up.

<div style="font-size: 13px; font-weight: 700; letter-spacing: 0.09em; color: #FA4616; margin: 1.4rem 0 0.8rem;">WHAT THE AGENT DOES</div>

<div style="display: flex; flex-wrap: wrap; gap: 14px; align-items: stretch; margin-bottom: 1.5rem;">
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Search</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">01</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Web search for current openings in the target roles</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Generate</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">02</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Structured job description: title, must-haves, nice-to-haves, level</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Match</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">03</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Score the candidate pool against each job description</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Persist</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">04</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Write jobs and matches to Data Service</div>
  </div>
</div>

**Your objectives:**

1. Prompt your coding agent to scaffold a LangGraph agent.
2. Wire the WebSearch tool into the graph.
3. Add a Data Service write step using the UiPath SDK.
4. Run an eval set, then deploy to your tenant.

**What you need:**

- A list of target job titles (for example, "RPA Developer", "AI Engineer").
- `candidates.csv` (provided).
- Your Anthropic or OpenAI API key.

### The prompt

This is real text you can paste:

```text
Build a UiPath Coded Agent in LangGraph that:

1. Takes the name of a job as input
2. For each role, generates a structured JD with must-haves and nice-to-haves
3. Scores a list of candidates (generate the JSON list locally and use it as
   part of the solution; it should contain at least one profile for Forward
   Deployed Engineer) against each JD
4. Writes jobs and top-3 matches per role to Data Service

Include an eval set with 5 cases. The name of the agent should be
{YourName}JobMatchingAgent. Use the UiPath SDK.
```

Here's what the coding agent does with that:

1. Loads the `uipath-agents` skill.
2. Generates `agent.py` with four nodes.
3. Builds Pydantic models for jobs and matches.
4. Adds the Data Service write via the UiPath SDK.
5. Creates `evals/` with five cases.
6. Asks you to review before publishing.

### What it generates

```python
from langgraph.graph import StateGraph
from uipath import UiPath

sdk = UiPath()

def search_jobs(state):
    # Built-in WebSearch tool -> recent postings per role
    state["jobs"] = [web_search(t) for t in state["titles"]]
    return state

def generate_jd(state):
    # LLM call -> structured JD (Pydantic model)
    ...

def match_candidates(state):
    candidates = sdk.buckets.read("candidates.csv")
    # LLM scoring -> top-3 per role
    ...

def persist(state):
    sdk.entities.bulk_create("Jobs", state["jobs"])
    sdk.entities.bulk_create("Matches", state["matches"])
```

### Publish the agent

This assumes the `uip` CLI is installed and you're logged into the right org. Replace the project path and tenant name with your own.

```bash
# 1. Install Python 3.13 (Windows)
winget install -e --id Python.Python.3.13 --accept-package-agreements --accept-source-agreements

# 2. Open a fresh shell and point PATH at the real Python 3.13 install
#    (PowerShell example -- adjust the path to your install)
$env:PATH="$env:LOCALAPPDATA\Programs\Python\Python313;$env:LOCALAPPDATA\Programs\Python\Python313\Scripts;$env:PATH"
python --version

# 3. Install uv
python -m pip install uv

# 4. Install the UiPath runtime packages the coded agent needs
python -m pip install uipath uipath-langchain uipath-dev langgraph langchain-community pandas

# 5. Go to the agent project
cd job-matching-agent

# 6. Point the UiPath wrapper at the Python runtime
uip codedagent setup --force

# 7. Select the target tenant
uip login tenant set {{ training_tenant }} --output json
uip login status --output json

# 8. Initialize the coded agent project
uip codedagent init

# 9. Publish to the tenant feed
uip codedagent deploy --tenant
```

## <img src="../coding-agents-hands-on.images/icon-register.png" alt="" style="width: 1.05em; height: 1.05em; vertical-align: -0.12em; margin-right: 0.4em; border: none; box-shadow: none;">Lab 2 — the RPA Workflow { .lab-title }

**75 min build + 15 min review**

### Why RPA for this part?

UiBank exposes registration only through a web form. There's no API.

- **RPA is the right tool.** Browser-based UI automation is exactly what RPA was built for — faster and more reliable than scraping.
- **Generated, not drawn.** You'll prompt your coding agent to build the XAML. No hand-dragging activities onto a canvas.
- **Connected to Lab 1.** You read candidates from Data Service (written by the Coded Agent) and write registration status back.

### What the workflow does

| Stage | What happens |
| :--- | :--- |
| **Read** | Pull candidates from Data Service (matched in Lab 1) |
| **Loop** | For each candidate, open the registration page |
| **Fill** | Type each field, submit, wait for success |
| **Update** | Write registration status back to Data Service |

**Your objectives:**

1. Prompt your coding agent to generate the XAML workflow.
2. Let it discover the project first, so it sees the existing packages.
3. Review the generated workflow in **Studio Desktop**.
4. Run against the sample CSV and verify the registrations.

**Your target:** `uibank.uipath.com/register-account`, the sample candidates CSV (provided), and UiPath Studio Desktop with the default packages.

### The sample candidate data

```csv
first_name,last_name,middle_name,sex,title,employment_status,date_of_birth,marital_status,num_dependents,username,email,password
Alice,Nguyen,,Female,Ms,Full-time,1/15/1990,Single,0,alice.nguyen,alice.nguyen@example.com,Welcome2026!
Ben,Carter,J.,Male,Mr,Full-time,3/22/1985,Married,2,ben.carter,ben.carter@example.com,Welcome2026!
Clara,Osei,,Female,Ms,Full-time,7/4/1992,Single,1,clara.osei,clara.osei@example.com,Welcome2026!
```

Three things to tell the workflow about this data:

- An empty `middle_name` is valid. The form should skip the field, not type an empty string.
- The date format is `MM/DD/YYYY`, which matches the form's picker.
- All test passwords are demo-grade. In production, pull them from a vault.

### The prompt

```text
Build a UiPath workflow that registers each candidate from candidates.csv at
uibank.uipath.com/register-account. The name of the workflow should be
{YourName}RegisterInUiBank. candidates.csv contains first_name, last_name,
middle_name, sex, title, employment_status, date_of_birth, marital_status,
num_dependents, username, email, and password.
```

### How the workflow skill thinks

The `uipath-rpa` skill is discovery-first. It reads before it writes:

```text
Let me inspect the project first...
  -> Reading project.json
  -> Found packages: UiPath.UIAutomation.Activities,
     UiPath.Excel.Activities, UiPath.WebAPI.Activities
  -> Inspected candidates.csv header

I'll create RegisterCandidates.xaml with:
  - Excel.ReadCsv -> DataTable
  - For Each Row in candidates
  - Open browser at registration URL
  - Type Into each form field (skip empty middle name)
  - Click Submit, wait for success element
  - Write Status back to Data Service (Candidates entity)
  - Try/Catch with screenshot on failure

Created RegisterCandidates.xaml (validated)
```

Four things worth noticing in that output:

| What it did | Why it matters |
| :--- | :--- |
| **Reads first** | Discovers packages and CSV structure before writing any code. |
| **Picks the right activities** | Knows `Excel.ReadCsv` exists and reaches for UI Automation activities. |
| **Handles edge cases** | Empty middle name handled, screenshot on failure. |
| **Closes the loop** | Writes status back to Data Service for the Coded App to read. |

## <img src="../coding-agents-hands-on.images/icon-dashboard.png" alt="" style="width: 1.05em; height: 1.05em; vertical-align: -0.12em; margin-right: 0.4em; border: none; box-shadow: none;">Lab 3 — the Coded App { .lab-title }

**100 min build + 20 min review**

### What's a Coded App?

A custom web app in TypeScript and React, for when the canvas-based **UiPath Apps** builder isn't enough. You build it in your IDE with the UiPath TypeScript SDK, deploy it to Orchestrator, and the platform governs it.

- **Your stack.** TypeScript, React, your design system, your favourite libraries.
- **Platform access.** `@uipath/uipath-typescript` gives you Cases, Tasks, Processes, Entities, and Buckets.
- **Enterprise-grade.** OAuth, IP restrictions, audit logs, and RBAC — all inherited from UiPath.

### What you'll build

A recruiter dashboard that reads the Jobs, Matches, and Candidates entities from Data Service:

- Jobs list, sorted by recency.
- Click into any job for the full description.
- Candidate matches with their scores.
- Registration status badges.
- A button that triggers the Coded Agent on demand.

### The prompt

```text
Build a Coded App using UiPath TypeScript SDK called recruiter-dashboard.
It should:

1. Read Jobs from the UiPath Data Service Jobs entity
2. For each job, show the JD and matched candidates
3. Show registration status from the Candidates entity
4. Add a button that triggers the Coded Agent

The name of the app should be {YourName}RecruiterApp. Use uipath-coded-apps
for the table component.
```

And the structure it generates:

```text
recruiter-dashboard/
├── package.json
├── uipath.json
├── src/
│   ├── App.tsx
│   ├── pages/
│   │   ├── JobsList.tsx
│   │   └── JobDetail.tsx
│   ├── hooks/
│   │   ├── useJobs.ts
│   │   └── useCandidates.ts
│   └── api/uipath.ts
└── README.md
```

### The Data Service hook

Here's how the dashboard reads jobs and matches:

```typescript
import { UiPath } from '@uipath/uipath-typescript/core'
import { Entities } from '@uipath/uipath-typescript/entities'
import { useQuery } from '@tanstack/react-query'

const sdk = new UiPath({ /* env-based config */ })

export function useJobs() {
  return useQuery({
    queryKey: ['jobs'],
    queryFn: async () => {
      const entities = new Entities(sdk)
      return entities.list('Jobs', { orderBy: 'createdAt desc' })
    },
  })
}
```

### Publishing the Coded App

Fifteen steps, and most of the pain is in steps 4 to 6. Work through them in order.

#### 1. Prerequisites

```bash
winget install OpenJS.NodeJS
npm install -g @uipath/cli
uip tools install @uipath/codedapp-tool
uip tools install @uipath/orchestrator-tool

uip login
uip login status --output json
```

You also need your UiPath org name, tenant name, workspace folder key, an External App client ID, and the Data Service entity IDs.

#### 2. Create the app

```bash
npm create vite@latest recruiter-dashboard -- --template react-ts
cd recruiter-dashboard
npm install
npm install @uipath/uipath-typescript --@uipath:registry=https://registry.npmjs.org
npm install path-browserify tailwindcss@3 postcss autoprefixer
```

#### 3. Configure Vite

Set `base: './'` in `vite.config.ts`. UiPath hosts coded apps under a mounted path, not the domain root, so an absolute base breaks every asset URL.

#### 4. Create the UiPath app config

Add `uipath.json`:

```json
{
  "scope": "DataFabric.Schema.Read DataFabric.Data.Read OR.Execution.Read OR.Jobs.Write",
  "clientId": "YOUR_EXTERNAL_APP_CLIENT_ID"
}
```

Use the External App client ID, and keep the scope string aligned with what the app actually calls. Prefer the narrow scopes you need over broad ones.

#### 5. Create `.env`

```bash
VITE_UIPATH_CLIENT_ID=YOUR_EXTERNAL_APP_CLIENT_ID
VITE_UIPATH_SCOPE=DataFabric.Schema.Read DataFabric.Data.Read OR.Execution.Read OR.Jobs.Write
VITE_UIPATH_ORG_NAME=your-org
VITE_UIPATH_TENANT_NAME=your-tenant
VITE_UIPATH_BASE_URL=https://staging.api.uipath.com
VITE_JOBS_ENTITY_ID=YOUR_JOBS_ENTITY_ID
VITE_MATCHES_ENTITY_ID=YOUR_MATCHES_ENTITY_ID
VITE_CANDIDATES_ENTITY_ID=YOUR_CANDIDATES_ENTITY_ID
VITE_AGENT_PROCESS_NAME=job-matching-agent
VITE_AGENT_FOLDER_PATH=your.name@example.com's workspace
```

!!! warning "VITE_UIPATH_BASE_URL must be the API host"
    Not the portal host. Use `https://staging.api.uipath.com` for staging and `https://api.uipath.com` for production. Pointing it at `staging.uipath.com` is the single most common setup mistake.

#### 6. Create the External App correctly

In UiPath Cloud, create a **Non-Confidential** External App. It must include the exact redirect URIs for local dev — both `http://localhost:5173` and `http://localhost:5173/` — and the scopes your app needs.

For this dashboard, the working scope set is:

- `DataFabric.Schema.Read`
- `DataFabric.Data.Read`
- `OR.Execution.Read`
- `OR.Jobs.Write`

If the External App doesn't allow a requested scope, login fails with UiPath Identity `#200` and `invalid_scope`.

#### 7. Initialize auth in code

Create the SDK client only after validating the config, and keep `sdk` nullable until initialization succeeds. Only construct services like `new Entities(sdk)` or `new Processes(sdk)` when `sdk` is real.

That prevents `Invalid SDK instance` errors and service construction before auth is ready.

#### 8. Read Data Service and Orchestrator data

Use subpath imports. Don't import service classes from the package root:

```typescript
import { UiPath } from '@uipath/uipath-typescript/core';
import { Entities } from '@uipath/uipath-typescript/entities';
import { Processes } from '@uipath/uipath-typescript/processes';
```

For Data Service, call `entities.getById(entityId)`, then paginate with `getAllRecords({ pageSize, cursor })`. Don't assume one call returns everything.

#### 9. Build locally

```bash
npm run build
npm run dev   # if you want to test locally first
```

Verify that sign-in works, the app returns to `localhost:5173`, and you see no `invalid_scope` or `Invalid SDK instance` errors.

#### 10. Package the coded app

```bash
uip codedapp pack dist --name recruiter-dashboard --version 0.1.0 --author "Your Name" --description "Recruiter dashboard"
```

This creates `.uipath/recruiter-dashboard.0.1.0.nupkg`.

#### 11. Publish to UiPath

```bash
uip codedapp publish --name recruiter-dashboard --version 0.1.0 --tenant-name {{ training_tenant }} --uipath-dir .uipath
```

Pass `--uipath-dir .uipath` explicitly. The CLI can miss newly packed versions without it.

#### 12. Deploy to a folder

```bash
uip or folders list --output json
uip codedapp deploy --name recruiter-dashboard --folder-key YOUR_FOLDER_KEY
```

#### 13. Verify the deployment

Open the deployed URL and check that login works, the app loads entity data, the trigger buttons call the expected process, and no auth or scope errors appear.

#### 14. The bugfix release flow

When you change config or code: update the files, rebuild, bump the version, repack, republish, redeploy.

```bash
npm run build
uip codedapp pack dist --name recruiter-dashboard --version 0.1.1 --author "Your Name" --description "Recruiter dashboard"
uip codedapp publish --name recruiter-dashboard --version 0.1.1 --tenant-name {{ training_tenant }} --uipath-dir .uipath
uip codedapp deploy --name recruiter-dashboard --folder-key YOUR_FOLDER_KEY
```

#### 15. The lessons worth remembering

- Use `base: './'` in Vite.
- Use `https://staging.api.uipath.com`, not `https://staging.uipath.com`, for SDK API calls.
- Register the correct `localhost` redirect URIs in the External App.
- Keep `uipath.json` and `.env` aligned.
- Keep the External App scopes aligned with `VITE_UIPATH_SCOPE`.
- Prefer exact scopes like `OR.Execution.Read` and `OR.Jobs.Write` over broader strings.
- Pass `--uipath-dir .uipath` on publish.
- Guard SDK initialization so the app fails gracefully instead of crashing.

## Gotchas you'll hit

Things every team learns in the first month.

| Gotcha | What to do |
| :--- | :--- |
| **Trust but verify** | The agent is fast and confident. Always review generated XAML and run the eval set before publishing. |
| **Pin your skill versions** | Skills evolve. Lock to a version in your project so behaviour doesn't shift under you. |
| **Context window matters** | On large projects the agent can miss context. Tell it which files to focus on, or use an `AGENTS.md`. |
| **Auth before everything** | Run `uip login` first. Skills can't deploy if the CLI session expired — this is the usual cause of "it just stopped working". |

## What you built

One end-to-end recruitment pipeline, in three pieces:

| # | Component | What it does |
| ---: | :--- | :--- |
| 01 | **Coded Agent** | LangGraph agent. Searches the web for jobs, generates job descriptions, matches candidates, writes to Data Service. |
| 02 | **RPA Workflow** | XAML workflow. Reads matched candidates, registers each on UiBank, updates status. |
| 03 | **Coded App** | React dashboard. Shows jobs, matches, and registration status, with a trigger button. |

All three talk to each other. All three were built with your coding agent. All in one IDE session.

## Next steps

**This week**

- Install the skills on your laptop and actually use them.
- Pick one current customer use case that fits these patterns.

**Next 30 days**

- Build a customer-specific demo using these patterns.
- Share what worked and what didn't in `#help-coding-agents-preview`.

**Ongoing**

- Contribute new patterns back to `UiPath/skills`.
- Bring your questions. Help customers and partners unlock UiPath through coding agents.

## Resources

| Resource | What's there |
| :--- | :--- |
| [**UiPath/skills**](https://github.com/UiPath/skills) | The skill repository. Read each `SKILL.md`. |
| **Studio + Coding Agents** | Official UiPath page on Studio with Claude Code, Codex, Cursor, and Gemini. |
| [**uipath-typescript**](https://github.com/UiPath/uipath-typescript) | TypeScript SDK reference and sample Coded Apps. |
| [**uipath-langchain-python**](https://github.com/UiPath/uipath-langchain-python) | LangGraph SDK for Coded Agents. |
| **DevCon recording** | The UiPath product team walks through Coded Agents. |
| `#help-coding-agents-preview` | Slack channel. Ask questions, get tips and tricks. |

## Appendix: CLI cheat sheet

Commands you'll run every day with the `uip` CLI.

| Command | What it does | When you'll use it |
| :--- | :--- | :--- |
| `uip skills install` | Install UiPath skills into your coding agent | First-time setup, per project |
| `uip login` | Authenticate with your UiPath tenant | Start of each session |
| `uipath new` | Scaffold a new Coded Agent project | Starting a new agent |
| `uipath run` | Run the agent locally with `input.json` | Testing during development |
| `uipath eval` | Run the evaluation set, score against expectations | Before deploying |
| `uipath publish` | Pack and publish to your tenant | Shipping |
| `uip push` / `uip pull` | Sync a Coded App with Studio Web | Coded App round-trips |
