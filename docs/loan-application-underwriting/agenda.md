# Agenda
**One connected scenario, built end to end in two 90-minute blocks. No breaks, mostly hands-on.**

!!! warning "Setup is not part of the session"
    Complete the [Setup](../setup.md) page before Block 1 starts. The clock starts with the coding agents intro — there's no time to install Node.js, Studio, or the skills during the session.

**Block 1 — Coding agents and the Coded Agent** · 90 min

| Time | Part | Focus | Format |
| :--- | :--- | :--- | :--- |
| 0:00–0:20 | 💡 <strong style="color: var(--md-primary-fg-color);"><a href="../../what-is-a-coding-agent/" style="color: inherit;">Intro</a></strong> | Coding agents, tools, skills, plugins. Where the `uip` CLI fits. | Presentation + live demo |
| 0:20–0:25 | ✅ <strong style="color: var(--md-primary-fg-color);">Ready check</strong> | Run `uip login status` and start your coding agent | Hands-on |
| 0:25–0:30 | 🧭 <strong style="color: var(--md-primary-fg-color);"><a href="../../coding-agents-hands-on/#the-contract-between-the-components" style="color: inherit;">Scenario and contract</a></strong> | The recruitment pipeline, its architecture, and the data each component passes on | Presentation |
| 0:30–1:20 | 🤖 <strong style="color: var(--md-primary-fg-color);"><a href="../../coding-agents-hands-on/#lab-1-the-coded-agent" style="color: inherit;">Coded Agent</a></strong> | Generate a JD, shortlist candidates, publish as a process | Hands-on |
| 1:20–1:30 | 💬 <strong style="color: var(--md-primary-fg-color);">Checkpoint</strong> | Compare shortlists. Confirm every agent is published. | Discussion |

**Block 2 — The RPA workflow and the Maestro Flow** · 90 min

| Time | Part | Focus | Format |
| :--- | :--- | :--- | :--- |
| 0:00–0:30 | ⚙️ <strong style="color: var(--md-primary-fg-color);"><a href="../../coding-agents-hands-on/#lab-2-the-rpa-workflow" style="color: inherit;">RPA Workflow</a></strong> | Register candidates on UiBank, publish as a process | Hands-on |
| 0:30–1:20 | 🔗 <strong style="color: var(--md-primary-fg-color);"><a href="../../coding-agents-hands-on/#lab-3-the-maestro-flow" style="color: inherit;">Maestro Flow</a></strong> | Agent → approval in Action Center → robot. Run it end to end. | Hands-on |
| 1:20–1:30 | 🏁 <strong style="color: var(--md-primary-fg-color);">Wrap-up</strong> | What you built, gotchas, what to try next | Discussion |

!!! info "How the timing holds up without breaks"
    - **The contract keeps the labs independent.** Every component's inputs and outputs are fixed before you build it, so Lab 3 is wiring, not debugging.
    - **Your coding agent's build time is your reading time.** While it works, read the explanation sections of the lab.
    - **Every lab has a fallback.** The trainer publishes `DemoJobMatchingAgent` and `DemoRegisterInUiBank` in the shared folder. If your own component doesn't finish in its time box, use the trainer's in Lab 3 — you still finish the full pipeline.

!!! tip "Training Environment"
    Log in at **[https://cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)** using tenant **CodingAgentsPractice**.
