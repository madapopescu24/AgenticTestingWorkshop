# Agenda
**This exercise runs as a single session of about 6–8 hours, including breaks.**

You'll get your environment ready, then build and deploy all four components of the pipeline — the AI agent, the loan officer app, the Maestro flow that ties them together, and the RPA workflow that drives the whole thing — finishing with a full end-to-end run.

| Step | Focus | Duration |
| ---: | :--- | ---: |
| [**Setup**](../setup.md) | Install the prerequisites, a coding agent, the `uip` CLI, and the UiPath skills | 35 min |
| [**What's a Coding Agent?**](../what-is-a-coding-agent.md) | Understand the mental model, tools, skills, and how UiPath fits in | 15 min |
| [**1. AI Underwriting Assessment**](1-underwriting-agent.md) | Build and deploy the Python coded agent that scores a loan application | 70 min |
| *Break* | | 15 min |
| [**2. Loan Officer Review Dashboard**](2-loan-officer-app.md) | Build and deploy the React app a loan officer uses to approve or reject a case | 55 min |
| *Lunch* | | 45 min |
| [**3. Orchestrating with Maestro Flow**](3-maestro-flow.md) | Build the Maestro process that calls the agent and routes by risk band | 75 min |
| *Break* | | 15 min |
| [**4. Application Intake & Enrichment**](4-intake-enrichment.md) | Build the Studio RPA workflow that submits applications and kicks off the flow | 65 min |
| [**You did it!**](you-did-it.md) | Trigger a full end-to-end run and see what's next | 30 min |

!!! tip "Training Environment"
    Log in at **[{{ training_url }}]({{ training_url }})** and use tenant **{{ training_tenant }}** for this exercise. Everything you deploy goes into the shared **CodingAgentsILT** folder in **Orchestrator**.
