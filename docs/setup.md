# Setup

**Everything you install before the workshop starts. Work through it top to bottom — each section verifies itself before you move on.**

!!! info "Do this before the session"
    Setup takes about 35 minutes on a clean machine, and some downloads are large. Get it done ahead of time so the session stays hands-on.

!!! tip "Training Environment"
    Log in at **[https://cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)** using tenant **InvokeWorkshop**.

## 1. Prerequisites

**Node.js (LTS)** — required for the UiPath CLI and the React app build.

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

**Python 3.10+** — required for coded agents.

1. Download from **[python.org/downloads](https://www.python.org/downloads/)** — on Windows, check **Add Python to PATH** during install
2. Verify with `python --version` or `python3 --version`

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

**UiPath Studio** — required to open, run, and debug generated XAML workflows. Currently supported on Windows only; Mac support is coming soon.

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

## 2. Install a Coding Agent

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

## 3. Install the UiPath CLI

```bash
npm install -g @uipath/cli@latest
```

Verify: `uip --version` — you should see `1.195.1` or later.

## 4. Install UiPath Skills into Your Coding Agent

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

    The skills land in `my-project/.cursor/skills/`. Run the command again in every new project folder you use during the session.

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

- `uipath-agents` — Python coded agents
- `uipath-rpa` — Studio XAML workflows
- `uipath-maestro-flow` — Maestro orchestration

!!! info "What each skill actually knows"
    See [What's a Coding Agent?](what-is-a-coding-agent.md) for the full skill catalog and how skills get discovered.

## 5. Authenticate with Your Tenant (TBD)

```bash
uip login --authority https://cloud.uipath.com --organization tpenlabs -t InvokeWorkshop
```

Verify you're pointed at the right place:

```bash
uip login status --output json
```

## 6. Open Your Project and Start a Session

```bash
cd my-project && claude
# or
cd my-project && codex
# or
cd my-project && cursor-agent
```

Using the Cursor editor instead of the terminal? Open `my-project` in Cursor and use the **Agent** chat — it sees the same skills.

Skills are auto-discovered on session start. Ask the agent to build a coded agent and it will load the right skill automatically.

!!! success "You're set up"
    Node.js, Python, .NET, Studio, Git, a coding agent, the `uip` CLI, the UiPath skills, and an authenticated tenant. Time to build something.
