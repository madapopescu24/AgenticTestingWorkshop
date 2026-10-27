Before the session
{: .eyebrow }

# 🧰 Setup

**Everything you install before the workshop starts. Work through it top to bottom — each section verifies itself before you move on.**

!!! info "Do this before the session"
    Setup takes about 45 minutes on a clean machine, and some downloads are large. Get it done ahead of time so the session stays hands-on.

!!! tip "Training Environment"
    Log in at **[{{ training_url }}]({{ training_url }})** using tenant **{{ training_tenant }}**.

## 📦 1. Prerequisites

**Node.js (LTS)** — required for the UiPath CLI.

1. Download the LTS version from **[nodejs.org](https://nodejs.org)**
2. Verify with `node --version` and `npm --version`

!!! tip "npm version must be 11.x.x"
    If `npm --version` returns a different version, upgrade it:

    === "Windows"
        ```bash
        npm install --global npm@11
        ```

    === "Mac"
        ```bash
        npm install -g npm@11
        ```

**Google Chrome with the UiPath extension** — the test cases drive UiBank in Chrome.

1. Install **[Google Chrome](https://www.google.com/chrome/)** if you don't have it
2. Install the **UiPath Browser Automation** extension from the Chrome Web Store, or from Studio under **Home** > **Tools** > **UiPath Extensions** > **Chrome**
3. In Chrome, open `chrome://extensions` and check the extension is **enabled**

**.NET SDK 8.0** — required to build and run UiPath Studio projects.

1. Download from **[dotnet.microsoft.com/download/dotnet/8.0](https://dotnet.microsoft.com/download/dotnet/8.0)** — or on Mac, install via Homebrew:
   ```bash
   brew install --cask dotnet-sdk
   ```
2. Verify with `dotnet --list-sdks` — you should see `8.x.x` in the output

!!! tip "Windows — make sure .NET is on your PATH"
    If `dotnet` is not recognised after install, add it to the PATH manually in PowerShell:
    ```bash
    $env:Path = "C:\Program Files\dotnet;$env:Path"
    dotnet --list-sdks
    ```

**UiPath Studio** — required to run and debug the generated test cases, and to capture UI targets with **Indicate** when your coding agent can't. Currently supported on Windows only; Mac support is coming soon.

1. Download from **[uipath.com/start-trial](https://www.uipath.com/start-trial)**
2. Sign in with your UiPath account and verify Studio launches

**Git** — required for the UiPath skills marketplace. Try Method 1 first; if it doesn't work, use Method 2.

=== "Method 1: winget (quickest)"

    1. Open a terminal and run:
       ```bash
       winget install --id Git.Git -e --source winget
       ```
    2. If prompted to accept terms, type `Y` and press Enter.
    3. Wait for "Successfully installed", then close the window.

=== "Method 2: Download the installer"

    1. Go to **[git-scm.com/download/win](https://git-scm.com/download/win)** — the 64-bit installer should download automatically.
    2. Run the downloaded file (e.g. `Git-2.xx.x-64-bit.exe`). Click Yes if Windows asks for admin permission.
    3. Click through the installer accepting all defaults. On the **"Adjusting your PATH environment"** screen, make sure the middle option is selected: *"Git from the command line and also from 3rd-party software"* — this is the default.
    4. Click Finish when done.

!!! warning "Required for both methods"
    PATH changes only take effect in new windows. Close every open terminal, then open a fresh Command Prompt and verify:
    ```bash
    git --version
    ```
    You should see something like `git version 2.45.1.windows.1`.

## 🤖 2. Install a Coding Agent

Pick one — or install more than one:

=== "Claude Code"

    ```bash
    npm install -g @anthropic-ai/claude-code
    ```

    Verify: `claude --version`

    !!! tip "Claude Code installation error?"
        If the install fails with a scripts permission error, run:
        ```bash
        npm config set allow-scripts=@anthropic-ai/claude-code --location=user
        ```
        Then run the install command again:
        ```bash
        npm install -g @anthropic-ai/claude-code
        ```

    !!! tip "npm permission errors on Mac?"
        A global install without write permissions is the usual cause. Point npm at a folder you own:
        ```bash
        mkdir -p ~/.npm-global
        npm config set prefix ~/.npm-global
        echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.zshrc
        source ~/.zshrc
        ```

=== "Codex"

    ```bash
    npm install -g @openai/codex
    ```

    Verify: `codex --version`

    !!! tip "npm permission errors on Mac?"
        A global install without write permissions is the usual cause. Point npm at a folder you own:
        ```bash
        mkdir -p ~/.npm-global
        npm config set prefix ~/.npm-global
        echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.zshrc
        source ~/.zshrc
        ```

=== "Cursor"

    Cursor comes as an editor and as a terminal agent. Install both — you'll review generated files in the editor and run the agent from the terminal.

    1. Download and install the **Cursor** editor from **[cursor.com/downloads](https://cursor.com/downloads)**, then sign in.
    2. Install the **Cursor CLI**:

        Mac:

        ```bash
        curl https://cursor.com/install -fsS | bash
        ```

        Windows (PowerShell):

        ```powershell
        irm 'https://cursor.com/install?win32=true' | iex
        ```

    3. Open a new terminal and sign in:

        ```bash
        cursor-agent login
        ```

    Verify: `cursor-agent --version`

    !!! tip "`cursor-agent` not found?"
        The installer puts the CLI in `~/.local/bin`. Open a new terminal, or add that folder to your `PATH`.

## ⌨️ 3. Install the UiPath CLI

```bash
npm install -g @uipath/cli@latest
```

Verify: `uip --version` — you should see `1.195.1` or later.

## 🧩 4. Install UiPath Skills into Your Coding Agent

=== "Claude Code"

    ```bash
    # 1. Add the marketplace (once)
    claude plugin marketplace add https://github.com/UiPath/skills
    # 2. Install the plugin from it
    claude plugin install uipath@uipath-marketplace
    uip skills install
    ```

=== "Codex"

    ```bash
    # 1. Add the marketplace (once)
    codex plugin marketplace add UiPath/skills --ref main
    uip skills install
    ```

=== "Cursor"

    Cursor reads skills from the project you open, so install them inside your project folder:

    ```bash
    uip skills install --agent cursor --local
    ```

    The skills land in `workshop/.cursor/skills/` when you run it in your workshop folder. Run the command again in every new project folder you use during the session.

You should see output similar to this:

```json
{
  "Result": "Success",
  "Code": "SkillsInstall",
  "Data": {
    "RootDir": "/Users/YourUser",
    "Skills": [
      "uipath-admin",
      "uipath-agents",
      "uipath-aops",
      "uipath-api-workflow",
      "uipath-automation-discovery",
      "uipath-automationhub",
      "uipath-connector-builder",
      "uipath-feedback",
      "uipath-functions",
      "uipath-governance",
      "uipath-human-in-the-loop",
      "uipath-insights",
      "uipath-ixp",
      "uipath-maestro-bpmn",
      "uipath-maestro-case",
      "uipath-maestro-flow",
      "uipath-mcp-servers",
      "uipath-planner",
      "uipath-platform",
      "uipath-process-mining",
      "uipath-review",
      "uipath-rpa",
      "uipath-solution",
      "uipath-tasks",
      "uipath-test",
      "uipath-troubleshoot"
    ],
    "Agents": [
      "claude",
      "codex",
      "cursor"
    ],
    "Installed": 78,
    "Shadowed": [],
    "Conflicts": []
  }
}
```

`Agents` lists the coding agents the skills were installed for. The skill list grows as UiPath adds skills, so yours may be longer than the example.

Confirm these three skills appear in the output — the hands-on session relies on them:

- `uipath-test` — Test Manager: requirements, test cases, test sets, executions, reports
- `uipath-rpa` — Studio test automation projects and XAML test cases
- `uipath-platform` — Orchestrator: packages, folders, credential assets

!!! info "What each skill actually knows"
    See [Agentic Testing & Coding Agents](what-is-a-coding-agent.md) for the full skill catalog and how skills get discovered.

## 🔐 5. Authenticate with Your Tenant

The workshop runs on **{{ env_label }}**, where the newest Autopilot for Testers and Autopilot for Developers features are available. Point the CLI there:

```bash
uip login --authority {{ training_authority }} --organization {{ training_org }} -t {{ training_tenant }}
```

Verify you're pointed at the right place:

```bash
uip login status --output json
```

Then open **Test Manager** once in the browser at **[{{ training_url }}]({{ training_url }})** and check you can see the **Projects** page. If you can't, ask the trainer to give you access before the session.

## 🔗 6. Connect Studio to the Training Tenant

Autopilot in Studio works against the tenant Studio is signed in to. Sign Studio in to the same place as the CLI:

1. Open **Studio**. If you're signed in to another environment, such as `cloud.uipath.com`, sign out.
2. Before signing in again, change the cloud URL to `{{ training_authority }}`. In **UiPath Assistant**, it's under **Preferences** > **Orchestrator Settings**, as the **Service URL**.
3. Sign in, then select the organization **{{ training_org }}** and the tenant **{{ training_tenant }}**.
4. Check that the **Autopilot** panel is available in Studio. If it isn't, ask the trainer before the session — the hands-on part starts with it.

!!! warning "One environment for everything"
    Studio, the `uip` CLI, and your browser must all point at **{{ training_url }}**. If one of them is still on another environment, Autopilot saves requirements to a project your coding agent can't see.

## 🏦 7. Register Your UiBank Test User

The test cases log in as a registered UiBank user. Create yours now, so they have an account to run against.

1. Go to **[uibank.uipath.com/register-account](https://uibank.uipath.com/register-account)**.
2. Fill in the form: first, middle, and last name, sex, email, username, and a password. Use a password you don't use anywhere else — UiBank is a public demo site.
3. Register, then log in at **[uibank.uipath.com/login](https://uibank.uipath.com/login)** to check the account works.

The tests never store your password in the project. It reads it from an Orchestrator **credential asset**. Create an empty workshop folder, start your coding agent in it (see [section 9](#9-start-a-session)), and give it this prompt:

```text
Create a credential asset named {YourName}_UiBankCredential in the
{{ training_folder }} folder on the {{ training_tenant }} tenant, with my UiBank username.
Ask me for the password interactively — don't put it in a command I can see
in my shell history.
```

Prefer to do it by hand? In **Orchestrator**, open the `{{ training_folder }}` folder, go to **Assets**, and add a **Credential** asset with that name.

!!! warning "Write down your UiBank email"
    You'll need it as `var_LoanEmail` in the hands-on session — the profile check in Step 6 compares it with the email UiBank shows.

## 📄 8. Download the Design Document

Download the [design document](resources.md#the-design-document) into your workshop folder. It should look like this:

```text
workshop/
└── E2E UiBank Online Banking.docx   ← the design document
```

You'll create your Test Manager project and your Studio project at the start of the session.

## ▶️ 9. Start a Session

```bash
cd workshop && claude
# or
cd workshop && codex
# or
cd workshop && cursor-agent
```

Using the Cursor editor instead of the terminal? Open the `workshop` folder in Cursor and use the **Agent** chat — it sees the same skills.

Skills are auto-discovered on session start. Ask the agent to create a test case in Test Manager and it will load the right skill automatically.

!!! success "You're set up"
    Node.js, .NET, Studio signed in to {{ training_tenant }}, Chrome with the UiPath extension, Git, a coding agent, the `uip` CLI, the UiPath skills, an authenticated tenant, a UiBank test user, and the design document. Time to test something.
