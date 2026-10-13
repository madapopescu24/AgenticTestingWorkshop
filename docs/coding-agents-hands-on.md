# Coding Agents + UiPath: Hands-On Session

**Build a Coded Agent, an RPA workflow, and a Coded App — all from your coding agent, all wired into one recruitment pipeline.**

!!! tip "Here is our plan for this session:"

    1. Get the mental model for coding agents, skills, tools, and plugins —
       see [What's a Coding Agent?](what-is-a-coding-agent.md).
    2. Build a **Coded Agent** that researches jobs and matches candidates.
    3. Build an **RPA** workflow that registers those candidates on a web form.
    4. Build a **Coded App** dashboard that shows the whole pipeline.
    5. Optionally bring all three together in **Maestro** — a homework deep dive.

## Overview

Every week a recruiter at a staffing agency does the same four things by hand: search job boards, write a description for each role, read through a candidate pool to find who fits, and register the shortlist in the client's portal. Hours of work, done differently by every recruiter, with nowhere to see where anyone stands.

You'll automate all four — by describing what you want in plain English and letting your coding agent build it. Three components, each handing work to the next through **Data Service**. By the end you'll know exactly when code beats drag-and-drop, and why.

## Goal

By the end of the session you'll have three deployed components talking to each other through **Data Service**: a Python agent that finds jobs and scores candidates, an XAML workflow that registers each candidate on a website with no API, and a React dashboard the recruiter actually uses. You'll have generated all three by prompting a coding agent — not by dragging activities onto a canvas or scaffolding React by hand.

!!! tip "Training Environment"
    Log in at **[https://cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)** using tenant **CodingAgentsPractice**.

## What You'll Build

Three components in the session, plus a fourth as homework:

1. **Coded Agent** — a Python LangGraph agent that takes a list of job titles, web-searches current openings, generates a structured job description per role, scores a candidate pool against each one, and writes jobs and top-3 matches to Data Service
2. **RPA Workflow** — a Studio XAML workflow that reads the matched candidates from Data Service, registers each one on the UiBank web form, and writes the registration status back
3. **Coded App** — a React Coded App that reads the Jobs, Matches and Candidates entities and presents them to a recruiter, with a button that triggers the agent on demand
4. **Maestro Process** *(homework)* — a UiPath Flow that runs the agent, pauses for a recruiter to approve the shortlist, triggers the RPA registration, and surfaces the result in the app

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

<div style="background: #16213e; border-left: 10px solid #FA4616; padding: 22px 28px; margin: 1.2rem 0 1.4rem;">
  <div style="font-size: 19px; font-weight: 700; color: #ffffff; line-height: 1.35;">Python agents that run on UiPath infrastructure.</div>
  <div style="font-size: 15px; font-style: italic; color: #f6c3ab; margin-top: 9px;">Not to be confused with the coding agent you're typing into — you write this one yourself.</div>
</div>

You pick the framework, use the UiPath SDK, package it with one CLI command, and deploy it to Orchestrator.

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

<div style="background: #faf8f6; border: 1px solid #eee3dc; border-left: 4px solid #FA4616; padding: 18px 22px; margin: 1.4rem 0;">
  <div style="font-size: 14px; font-weight: 700; letter-spacing: 0.09em; color: #FA4616; margin-bottom: 12px;">YOUR OBJECTIVES</div>
  <ul style="list-style: none; margin: 0 0 16px; padding: 0; font-size: 16px; color: #333; line-height: 1.55;">
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">1</span>
      <span>Prompt your coding agent to scaffold a LangGraph agent.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">2</span>
      <span>Wire the WebSearch tool into the graph.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">3</span>
      <span>Add a Data Service write step using the UiPath SDK.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">4</span>
      <span>Run an eval set, then deploy to your tenant.</span>
    </li>
  </ul>
  <div style="border-top: 1px solid #eee3dc; padding-top: 12px; margin-top: 4px;">
    <div style="font-size: 14px; font-weight: 700; letter-spacing: 0.09em; color: #FA4616; margin-bottom: 9px;">WHAT YOU NEED</div>
    <ul style="margin: 0; padding-left: 18px; font-size: 15px; color: #4a4a4a; line-height: 1.55;"><li style="margin-bottom: 5px;">A list of target job titles (for example, "RPA Developer", "AI Engineer").</li><li style="margin-bottom: 5px;"><code>candidates.csv</code> — provided below, see <a href="#the-sample-candidate-data">The sample candidate data</a>.</li><li style="margin-bottom: 5px;">Your Anthropic or OpenAI API key.</li></ul>
  </div>
</div>

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

<div style="background: #faf8f6; border: 1px solid #eee3dc; border-left: 4px solid #FA4616; padding: 18px 22px; margin: 1.4rem 0;">
  <div style="font-size: 14px; font-weight: 700; letter-spacing: 0.09em; color: #FA4616; margin-bottom: 12px;">WHAT THE CODING AGENT DOES WITH THAT</div>
  <ul style="list-style: none; margin: 0; padding: 0; font-size: 16px; color: #333; line-height: 1.55;">
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">1</span>
      <span>Loads the <code>uipath-agents</code> skill.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">2</span>
      <span>Generates <code>agent.py</code> with four nodes.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">3</span>
      <span>Builds Pydantic models for jobs and matches.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">4</span>
      <span>Adds the Data Service write via the UiPath SDK.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">5</span>
      <span>Creates <code>evals/</code> with five cases.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">6</span>
      <span>Asks you to review before publishing.</span>
    </li>
  </ul>
</div>

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

Both paths do the same thing. Run the commands yourself if you want to see each step, or hand the whole job to your coding agent.

=== "Manually"

    This assumes the `uip` CLI is installed and you're logged into the right org. Replace the project path and tenant name with your own.

    ```bash
    # 1. Go to the agent project
    cd job-matching-agent

    # 2. Point the UiPath wrapper at the Python runtime
    uip codedagent setup --force

    # 3. Select the target tenant
    uip login tenant set {{ training_tenant }} --output json
    uip login status --output json

    # 4. Initialize the coded agent project
    uip codedagent init

    # 5. Publish to the tenant feed
    uip codedagent deploy --tenant
    ```

=== "Using Your Coding Agent"

    Give this prompt to your coding agent — it initializes the project and publishes for you:

    ```text
    Publish the {YourName}JobMatchingAgent coded agent I just built.

    1. Point the UiPath wrapper at my Python runtime with `uip codedagent setup`.
    2. Switch to the {{ training_tenant }} tenant and confirm `uip login status`
       shows the right org and tenant before going further.
    3. Initialize the coded agent project, then publish it to the tenant feed.
    4. Report back the package name and version you published, and stop if any
       step fails rather than retrying blindly.
    ```

    !!! tip "Watch what it runs"
        The agent proposes each command before running it. Read them — publishing writes to your tenant feed, and that is the one step you want to see before it happens.

## <img src="../coding-agents-hands-on.images/icon-register.png" alt="" style="width: 1.05em; height: 1.05em; vertical-align: -0.12em; margin-right: 0.4em; border: none; box-shadow: none;">Lab 2 — the RPA Workflow { .lab-title }

**75 min build + 15 min review**

### Why RPA for this part?

<div style="background: #16213e; border-left: 10px solid #FA4616; padding: 22px 28px; margin: 1.2rem 0 1.4rem;">
  <div style="font-size: 19px; font-weight: 700; color: #ffffff; line-height: 1.35;">UiBank exposes registration only through a web form.</div>
  <div style="font-size: 15px; font-style: italic; color: #f6c3ab; margin-top: 9px;">There's no API. Some systems only have a UI — this is exactly what RPA was built for.</div>
</div>

<div style="display: flex; flex-wrap: wrap; gap: 14px; align-items: stretch; margin-bottom: 1.5rem;">
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">RPA is the right tool</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Browser-based UI automation is faster and more reliable than scraping.</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Generated, not drawn</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">You'll prompt your coding agent to build the XAML. No dragging activities onto a canvas.</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Connected to Lab 1</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Read candidates from Data Service, write registration status back.</div>
  </div>
</div>

### What the workflow does

The four stages run in order — `Read` picks up what Lab 1 wrote, and `Update` hands the status on to the Coded App in Lab 3.

<div style="font-size: 13px; font-weight: 700; letter-spacing: 0.09em; color: #FA4616; margin: 1.4rem 0 0.8rem;">WHAT THE WORKFLOW DOES</div>

<div style="display: flex; flex-wrap: wrap; gap: 14px; align-items: stretch; margin-bottom: 1.5rem;">
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Read</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">01</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Pull candidates from Data Service (matched in Lab 1)</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Loop</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">02</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">For each candidate, open the registration page</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Fill</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">03</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Type each field, submit, wait for success</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Update</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">04</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Write registration status back to Data Service</div>
  </div>
</div>

<div style="background: #faf8f6; border: 1px solid #eee3dc; border-left: 4px solid #FA4616; padding: 18px 22px; margin: 1.4rem 0;">
  <div style="font-size: 14px; font-weight: 700; letter-spacing: 0.09em; color: #FA4616; margin-bottom: 12px;">YOUR OBJECTIVES</div>
  <ul style="list-style: none; margin: 0 0 16px; padding: 0; font-size: 16px; color: #333; line-height: 1.55;">
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">1</span>
      <span>Prompt your coding agent to generate the XAML workflow.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">2</span>
      <span>Let it discover the project first, so it sees the existing packages.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">3</span>
      <span>Review the generated workflow in <strong>Studio Desktop</strong>.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">4</span>
      <span>Run against the sample CSV and verify the registrations.</span>
    </li>
  </ul>
  <div style="font-size: 15px; color: #4a4a4a; border-top: 1px solid #eee3dc; padding-top: 12px;">
    <strong style="color: #16213e;">Your target:</strong> <code>uibank.uipath.com/register-account</code>, the sample <code>candidates.csv</code> <a href="#the-sample-candidate-data">provided below</a>, and UiPath Studio Desktop with the default packages.
  </div>
</div>

### The sample candidate data

```csv
first_name,last_name,middle_name,sex,title,employment_status,date_of_birth,marital_status,num_dependents,username,email,password
Alice,Nguyen,,Female,Ms,Full-time,1/15/1990,Single,0,alice.nguyen,alice.nguyen@example.com,Welcome2026!
Ben,Carter,J.,Male,Mr,Full-time,3/22/1985,Married,2,ben.carter,ben.carter@example.com,Welcome2026!
Clara,Osei,,Female,Ms,Full-time,7/4/1992,Single,1,clara.osei,clara.osei@example.com,Welcome2026!
```

!!! note "Three things to tell the workflow about this data"

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

<div style="display: flex; flex-wrap: wrap; gap: 14px; align-items: stretch; margin-bottom: 1.5rem;">
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Reads first</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">01</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Discovers packages and CSV structure before writing any code.</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Picks the right activities</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">02</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Knows <code>Excel.ReadCsv</code> exists and reaches for UI Automation activities.</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Handles edge cases</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">03</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Empty middle name handled, screenshot on failure.</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 9px;">
      <span style="font-size: 17px; font-weight: 700; color: #16213e;">Closes the loop</span>
      <span style="font-size: 22px; font-weight: 700; color: #f6c3ab; line-height: 1;">04</span>
    </div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">Writes status back to Data Service for the Coded App to read.</div>
  </div>
</div>

## <img src="../coding-agents-hands-on.images/icon-dashboard.png" alt="" style="width: 1.05em; height: 1.05em; vertical-align: -0.12em; margin-right: 0.4em; border: none; box-shadow: none;">Lab 3 — the Coded App { .lab-title }

**100 min build + 20 min review**

### What's a Coded App?

<div style="background: #16213e; border-left: 10px solid #FA4616; padding: 22px 28px; margin: 1.2rem 0 1.4rem;">
  <div style="font-size: 19px; font-weight: 700; color: #ffffff; line-height: 1.35;">When the canvas-based UiPath Apps builder isn't enough.</div>
  <div style="font-size: 15px; font-style: italic; color: #f6c3ab; margin-top: 9px;">A custom web app in TypeScript and React — built in your IDE, governed by the platform.</div>
</div>

<div style="display: flex; flex-wrap: wrap; gap: 14px; align-items: stretch; margin-bottom: 1.5rem;">
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="font-size: 17px; font-weight: 700; color: #16213e; margin-bottom: 9px;">Your stack</div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">TypeScript, React, your design system, your favourite libraries.</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="font-size: 17px; font-weight: 700; color: #16213e; margin-bottom: 9px;">Platform access</div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;"><code>@uipath/uipath-typescript</code> gives you Cases, Tasks, Processes, Entities, and Buckets.</div>
  </div>
  <div style="flex: 1 1 220px; background: #ffffff; border: 1px solid #e8e8e8; border-top: 4px solid #FA4616; padding: 18px 20px; box-sizing: border-box;">
    <div style="font-size: 17px; font-weight: 700; color: #16213e; margin-bottom: 9px;">Enterprise-grade</div>
    <div style="font-size: 14.5px; color: #4a4a4a; line-height: 1.55;">OAuth, IP restrictions, audit logs, and RBAC — all inherited from UiPath.</div>
  </div>
</div>

### What you'll build

A recruiter dashboard that reads the Jobs, Matches, and Candidates entities from Data Service.

<div style="background: #faf8f6; border: 1px solid #eee3dc; border-left: 4px solid #FA4616; padding: 18px 22px; margin: 1.4rem 0;">
  <div style="font-size: 14px; font-weight: 700; letter-spacing: 0.09em; color: #FA4616; margin-bottom: 12px;">WHAT THE DASHBOARD SHOWS</div>
  <ul style="list-style: none; margin: 0 0 16px; padding: 0; font-size: 16px; color: #333; line-height: 1.55;">
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">1</span>
      <span>Jobs list, sorted by recency.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">2</span>
      <span>Click into any job for the full description.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">3</span>
      <span>Candidate matches with their scores.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">4</span>
      <span>Registration status badges.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">5</span>
      <span>A button that triggers the Coded Agent on demand.</span>
    </li>
  </ul>
</div>

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

## 🔗 Homework — Connect it all in Maestro { .lab-title }

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">Optional deep dive · on your own, after the session</div>

<div style="background: #16213e; border-left: 10px solid #FA4616; padding: 22px 28px; margin: 1.2rem 0 1.4rem;">
  <div style="font-size: 19px; font-weight: 700; color: #ffffff; line-height: 1.35;">Three pieces that work. Now make them run as one process.</div>
  <div style="font-size: 15px; font-style: italic; color: #f6c3ab; margin-top: 9px;">No walkthrough for this one — that's the point. You already have every skill you need.</div>
</div>

Each lab left you with a deployed component and a Data Service entity. **Maestro** is what turns them into a single orchestrated process: it calls the agent, waits for the result, hands work to the RPA robot, and routes a human into the loop when one is needed.

<div style="background: #faf8f6; border: 1px solid #eee3dc; border-left: 4px solid #FA4616; padding: 18px 22px; margin: 1.4rem 0;">
  <div style="font-size: 14px; font-weight: 700; letter-spacing: 0.09em; color: #FA4616; margin-bottom: 12px;">YOUR OBJECTIVES</div>
  <ul style="list-style: none; margin: 0; padding: 0; font-size: 16px; color: #333; line-height: 1.55;">
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">1</span>
      <span>Design a <strong>Maestro</strong> process that runs the three components end to end.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">2</span>
      <span>Trigger the Coded Agent to research jobs and write matches to Data Service.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">3</span>
      <span>Call the RPA workflow to register each matched candidate on UiBank.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">4</span>
      <span>Surface the results in the Coded App so a recruiter can review them.</span>
    </li>
    <li style="display: flex; gap: 10px; margin-bottom: 9px; align-items: baseline;">
      <span style="flex: 0 0 auto; background: #FA4616; color: #ffffff; border-radius: 50%; width: 23px; height: 23px; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">5</span>
      <span>Publish the process and run it once, start to finish.</span>
    </li>
  </ul>
</div>

### Which skill to use

`uipath-maestro-flow` — it creates, validates, and debugs UiPath Flow projects in the `.flow` JSON format. You never hand-edit the JSON; you describe the process and let the agent build it, exactly as you did in the three labs.

### A prompt to start from

Treat this as a starting point, not a script. Read what the agent proposes, push back, and iterate.

```text
Build a Maestro Flow called {YourName}RecruitmentPipeline that orchestrates the
three components I already deployed:

1. Start by running my {YourName}JobMatchingAgent coded agent, passing in a list
   of target job titles. Wait for it to finish writing Jobs and Matches to
   Data Service.
2. Then run my {YourName}RegisterInUiBank RPA process for the matched candidates,
   so each one gets registered on UiBank and the status is written back.
3. Add a human approval step before the RPA runs, so a recruiter can confirm
   the shortlist first.
4. Validate the flow, publish it, and tell me the process key.

Discover what's already deployed in my tenant before you start, and ask me
before creating anything new.
```

!!! tip "What 'done' looks like"
    One Maestro run that starts from a list of job titles and ends with registered candidates visible in your Coded App — with no manual step in between except the approval you designed in.

!!! info "Stuck? That's expected"
    This is the part nobody walks you through. Ask your coding agent to explain what it generated, check the run in **Orchestrator**, and send the interesting failures our way with `uip feedback send`.

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
- Do the [Maestro homework](#homework-connect-it-all-in-maestro) — wire the agent, the RPA workflow, and the app into one orchestrated process.

**Next 30 days**

- Rebuild something you already maintain with a coding agent. Compare how long it took, and note where the agent needed correcting.
- Write your own skill for a pattern your team repeats, so the agent gets it right without being told twice.
- Push past the happy path: ask the agent for eval sets, error handling, and the deploy step you'd normally do by hand.

**Ongoing**

- Bring your questions. No question is too basic, especially this early.
- Tell us when something doesn't work. Run `uip feedback send` the moment a skill guesses wrong, a command fails, or a step takes three tries.
- Say what you'd want next. The rough edges you report are what shape the next version of the skills and the CLI.

## Resources

| Resource | What's there |
| :--- | :--- |
| [**UiPath/skills**](https://github.com/UiPath/skills) | The skill repository. Read each `SKILL.md`. |
| **Studio + Coding Agents** | Official UiPath page on Studio with Claude Code, Codex, Cursor, and Gemini. |
| [**uipath-typescript**](https://github.com/UiPath/uipath-typescript) | TypeScript SDK reference and sample Coded Apps. |
| [**uipath-langchain-python**](https://github.com/UiPath/uipath-langchain-python) | LangGraph SDK for Coded Agents. |

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
