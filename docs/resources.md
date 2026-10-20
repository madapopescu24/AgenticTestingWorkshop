# Resources

**Reference processes and links to keep handy during and after the session.**

!!! tip "Training Environment"
    Log in at **[https://cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)** using tenant **InvokeWorkshop**.

## Trainer's reference processes

The trainer's `DemoJobMatchingAgent` and `DemoRegisterInUiBank` are working versions of the Lab 1 agent and the Lab 2 workflow. They're already published as processes in the `CodingAgentsILT` folder, so you can use them in Lab 3 without downloading anything — see the **Trainer's processes** tab in [the Lab 3 prompt](coding-agents-hands-on.md#lab-3-the-maestro-flow).

The reference solution for Lab 3, `DemoRecruitmentPipeline`, is the Maestro Flow that wires the two together. Download all three to compare with what your coding agent built, or to see a reference solution after the session.

[Download the trainer materials (.zip, 4.7 MB)](resources.assets/trainer-processes/coding-agents-trainer-materials.zip){ .md-button .md-button--primary }

The archive holds the three projects, their published packages in `dist/`, and the `candidates.json` and `test-input.json` used in the labs. The Python environment for `DemoJobMatchingAgent` isn't included — run `uv sync` in that folder to recreate it.

| Process | What it is | Contract | Where |
| :--- | :--- | :--- | :--- |
| `DemoJobMatchingAgent` | Coded Agent — reference solution for Lab 1 | `job_title` → `job`, `matches` | In the archive |
| `DemoRegisterInUiBank` | RPA Workflow — reference solution for Lab 2 | `in_CandidatesJson` → `out_ResultsJson` | In the archive |
| `DemoRecruitmentPipeline` | Maestro Flow — reference solution for Lab 3 | `job_title` → `job`, `out_ResultsJson` | In the archive |

!!! info "Reference, not a shortcut"
    Build your own components first. The point of the session is to see how your coding agent builds them — the reference processes are there for when something blocks you, and for comparing afterwards.

## Useful links

| Resource | What's there |
| :--- | :--- |
| [**UiPath/skills**](https://github.com/UiPath/skills) | The skill repository. Read each `SKILL.md`. |
| **Studio + Coding Agents** | Official UiPath page on Studio with Claude Code, Codex, Cursor, and Gemini. |
| [**uipath-langchain-python**](https://github.com/UiPath/uipath-langchain-python) | LangGraph SDK for Coded Agents. |
