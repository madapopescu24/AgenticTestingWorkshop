Hands-on · Part 1 of 4
{: .eyebrow }

# 📋 Requirements

<div style="font-size: 15px; font-style: italic; color: #d1603a; margin: -0.6rem 0 1rem;">From a design document to requirements you'd sign off on</div>

<div style="background: #faf8f6; border: 1px solid #eee3dc; border-left: 4px solid #FA4616; padding: 18px 22px; margin: 1.4rem 0;">
  <div style="font-size: 14px; font-weight: 700; letter-spacing: 0.09em; color: #FA4616; margin-bottom: 9px;">WHAT YOU NEED</div>
  <ul style="margin: 0; padding-left: 18px; font-size: 15px; color: #4a4a4a; line-height: 1.55;"><li style="margin-bottom: 5px;">Your <code>{YourName}UiBankTests</code> project open in <strong>Studio</strong>, connected to your <strong>{YourName}_UIB_Test</strong> Test Manager project. See <a href="../agentic-testing-hands-on/#setup">Setup</a>.</li><li style="margin-bottom: 5px;"><strong>Test Manager</strong> open in your browser on the same tenant.</li></ul>
</div>

## 🪄 Ask Autopilot in Studio to create the requirements

The design document goes in, requirements come out, and nobody types them.

1. In Studio, open the **Autopilot** panel.
2. Attach `E2E UiBank Online Banking.docx` to the conversation, then give Autopilot this prompt:

    ```text
    Generate the requirements for the UiBank web application from the
    attached design document. Create one requirement per step in section 3,
    Step 0 to Step 7, in that order.
    ```

3. Review what Autopilot proposes, then accept the requirements so they're saved to your Test Manager project.

!!! warning "Autopilot missing, or can't save the requirements?"
    Two usual causes. Studio is signed in to the wrong environment: the Autopilot features in this session are on **{{ env_label }}**, so sign Studio in to **{{ training_authority }}**, org **{{ training_org }}**, tenant **{{ training_tenant }}**. Or the project isn't connected to your Test Manager project: check the Test Manager settings in Studio, or ask your coding agent to run `uip rpa tm status` in the project folder.

## 💬 Discuss the requirements in Test Manager

In Test Manager, refresh **Requirements**. You should see eight requirements, one per step of the design document, with keys `UIB:1` to `UIB:8`. Autopilot's names and wording may differ from this:

<div class="circles" markdown>

<div class="circle-item" markdown>
<span class="num">0</span>
<div class="ci-body" markdown>

**Login and Initial Account State**

`UIB:1` · Step 0

</div>
</div>

<div class="circle-item" markdown>
<span class="num">1</span>
<div class="ci-body" markdown>

**Checking Account Creation**

`UIB:2` · Step 1

</div>
</div>

<div class="circle-item" markdown>
<span class="num">2</span>
<div class="ci-body" markdown>

**Savings Account Creation**

`UIB:3` · Step 2

</div>
</div>

<div class="circle-item" markdown>
<span class="num">3</span>
<div class="ci-body" markdown>

**Funds Transfer Between Accounts**

`UIB:4` · Step 3

</div>
</div>

<div class="circle-item" markdown>
<span class="num">4</span>
<div class="ci-body" markdown>

**Loan Application Submission**

`UIB:5` · Step 4

</div>
</div>

<div class="circle-item" markdown>
<span class="num">5</span>
<div class="ci-body" markdown>

**Loan Status Lookup**

`UIB:6` · Step 5

</div>
</div>

<div class="circle-item" markdown>
<span class="num">6</span>
<div class="ci-body" markdown>

**User Profile Identity Verification**

`UIB:7` · Step 6

</div>
</div>

<div class="circle-item" markdown>
<span class="num">7</span>
<div class="ci-body" markdown>

**Logout and Evidence Collection**

`UIB:8` · Step 7

</div>
</div>

</div>

Open two or three and discuss them as a group:

- **Traceability.** Can you tell from each requirement which step of the document it comes from?
- **Testability.** Could you write a pass/fail check for every acceptance criterion? Which ones are vague?
- **Gaps.** The document doesn't say what happens if a transfer is larger than the balance, or what the loan approval rules are. Did Autopilot notice, or did it skip them? Did it invent anything the document doesn't say?

!!! tip "Why one requirement per step"
    Eight small requirements are easier to evaluate, cover, and report on than one big one. When a test fails later, you know exactly which step, and which requirement, it affects.

## 🔍 Evaluate, improve, and re-evaluate with Autopilot in Test Manager

Test Manager's **Evaluation Agent** checks a requirement for clarity, completeness, and testability.

1. Under **Requirements**, open **Funds Transfer Between Accounts**.
2. Select **Evaluate Requirement**, next to **Description**. Read Autopilot's findings and its suggestions.

    ![A requirement in Test Manager, Step 3: Transfer Funds Between Accounts, with its description and the Evaluate Requirement button next to Description](requirements.images/test-manager-evaluate-requirement-W.png){ .screenshot width="900" }
    *The funds transfer requirement, with Evaluate Requirement next to Description.*

3. Implement two or three suggestions you agree with by editing the requirement. A typical one is a rule for a transfer larger than the source balance. If the document doesn't answer a question, write it down as an open question instead of making the answer up.
4. Evaluate the requirement again. Did the result improve? Did Autopilot raise anything new?
5. Repeat for **Loan Application Submission**, the requirement with the most undocumented rules.

!!! tip "Add your own prompts"
    Autopilot evaluates requirements with the prompts in the project's **Prompt Library**. Besides the predefined ones, such as **Multifaceted Audit**, **Performance Evaluation**, and **Security Assessment**, you can add custom prompts for your team's own quality rules:

    1. In Test Manager, select **Project Settings** in the project's left menu, then the **Prompt library** tab.
    2. Select **Add prompt**.
    3. In **Create prompt**, fill in:
        - **Name** and **Description**, so others know when to use it.
        - **Mode of use**: **Evaluate requirement quality** for an evaluation prompt. Other modes include **Create tests from requirement**, **Import test cases**, and **Autonomous Exploration**.
        - **Prompt**: the instructions for Autopilot, as specific and detailed as possible.
    4. Select **Create**.

    Your prompt then appears next to the predefined ones when you evaluate or re-evaluate a requirement.

    <video src="../requirements.images/test-manager-add-custom-prompt.mp4" autoplay loop muted playsinline controls aria-label="Adding a custom prompt in Test Manager: Project Settings, Prompt library, Add prompt, filling in Name, Description, Mode of use, and Prompt, then Create" style="display: block; width: 100%; margin: 1.5rem auto; border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);"></video>

!!! success "Requirements done"
    Eight requirements generated by Autopilot from the design document, discussed, and at least two of them evaluated, improved, and re-evaluated.

!!! info "Autopilot drafts, you decide"
    The Evaluation Agent is good at spotting vague wording and missing cases. It can't know your business rules. Every suggestion you accept is a decision about what UiBank must do, so a product owner should agree with it.
