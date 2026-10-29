动手实践 · 第一步
{: .eyebrow }

# 🧰 环境准备 { #setup }

**这是动手实践部分的第一件事：你的虚拟机、登录、租户和测试数据。从上到下依次完成。每一节都会先自行验证，然后你再继续。**

!!! info "我们一起完成"
    环境准备是课程的一部分：在介绍之后、动手实践开始时，讲师会带全场一起完成。如果某一步失败，请先举手，不要直接往下做。

!!! tip "培训环境"
    在 **[{{ training_url }}]({{ training_url }})** 登录，使用租户 **{{ training_tenant }}**。

## 🖥️ 1. 连接到你的虚拟机 { #1-connect-to-your-vm }

每位学员都会拿到一台已经装好工具的虚拟机（VM）。本页剩下的内容以及整个课程，你都在这台虚拟机里完成。

1. 打开你收到的虚拟机详情。其中显示虚拟机的 **Username** 和 **Password**，并带有复制按钮。
2. 选择 **Connect via Azure Bastion**。它会在浏览器标签页中打开虚拟机，所以你不需要 RDP 客户端。

    ![虚拟机详情：Username 和隐藏的 Password，带复制按钮，以及 Download RDP File 和 Connect via Azure Bastion 按钮](setup.images/vm-connect-options.png){ .screenshot width="320" }

3. 在 **Azure Bastion** 表单中，保持 **Protocol** 为 **RDP**、**Port** 为 **3389**。输入虚拟机的用户名和密码，选择你的 **Keyboard Language**，然后选择 **Login**。

    ![Azure Bastion 登录表单，包含 Protocol RDP、Port 3389、Username、Password、Keyboard Language 和 Login 按钮](setup.images/azure-bastion-login.png){ .screenshot width="420" }

4. 当浏览器询问是否允许访问剪贴板时，选择允许。你一整天都要把提示词粘贴到虚拟机里。
5. 等待虚拟机的 Windows 桌面在浏览器标签页中加载完成。

!!! tip "无法用 Ctrl+V 粘贴到虚拟机？"
    在你自己电脑的 Chrome 浏览器中打开 `chrome://settings/content/clipboard`，确认 Bastion 网站不在 **Not allowed to see your clipboard** 列表中。

## 🔑 2. 登录培训环境 { #2-sign-in-to-the-training-environment }

从这里开始，请**在虚拟机内**操作。

1. 在虚拟机中打开 **Google Chrome**，访问 **[{{ training_url }}]({{ training_url }})**。
2. 选择 **Continue with Microsoft**。

    ![UiPath 登录页面，包含 Continue with Google、Continue with Microsoft、Continue with LinkedIn 和 Continue with Email](setup.images/uipath-sign-in.png){ .screenshot width="420" }

3. 使用工作坊详情中 **Your Workshop Account** 区域里的用户名和密码登录，不要用你自己的账号。输入用户名，选择 **Next**，再输入密码并选择 **Sign in**。

    ![Microsoft 登录页面，包含 Email, phone, or Skype 字段和 Next 按钮](setup.images/microsoft-sign-in.png){ .screenshot width="420" }

## ✅ 3. 确认租户 { #3-confirm-the-tenant }

登录后，打开 **Studio Web**。在右上角确认租户选择器显示的是 **{{ training_tenant }}**。如果显示的是其他租户，请先切换到 **{{ training_tenant }}** 再继续。

## 💻 4. 打开终端 { #4-open-the-terminal }

1. 在虚拟机中打开 Windows 搜索，输入 `terminal`。
2. 选择 **Terminal** 应用。

    ![Windows 搜索中输入了 terminal，最佳匹配为 Terminal 应用](setup.images/windows-terminal-search.png){ .screenshot width="500" }

虚拟机里已经装好了你的编码智能体、`uip` CLI 和 UiPath 技能，无需再安装任何东西。接下来的几节都会用到这个终端。

## 🔐 5. 向你的租户进行身份验证 { #5-authenticate-with-your-tenant }

工作坊运行在 **{{ env_label }}** 上，那里提供最新的 Autopilot for Testers 和 Autopilot for Developers 功能。把 CLI 指向那里：

```bash
uip login --authority {{ training_authority }} --organization {{ training_org }} -t {{ training_tenant }}
```

确认你指向了正确的位置：

```bash
uip login status --output json
```

然后在浏览器中打开一次 **Test Manager**（**[{{ training_url }}]({{ training_url }})**），确认你能看到 **Projects** 页面。如果看不到，请讲师为你开通访问权限。

确认 `{{ training_folder }}` 文件夹中有机器人可以运行你的测试。让你的编码智能体运行：

```bash
uip or folders runtimes {{ training_folder }}
```

它必须显示一个状态为 **Available** 的运行时。之后，测试作业不能一直处于 Pending 状态，且原因为 `RobotNoCredentials`。如果任一检查失败，请告诉讲师。

!!! info "讲师检查清单：租户侧"
    讲师会在课程开始前准备好以下内容。学员无法自行修复：

    - 为每位学员分配 **App Test Developer** 许可证。
    - 一条允许 Autopilot 的 **AI Trust Layer** 策略。
    - **{{ training_folder }}** 文件夹，并具有创建资产和运行测试集的权限。
    - 该文件夹中有一个带 **Testing** 或 **Production** 运行时的机器人，并且有一个**存储了凭据的机器人账号**分配到该文件夹。没有凭据时，即使运行时显示 Connected 和 Available，测试集作业也会一直处于 Pending，原因为 `RobotNoCredentials`。
    - 文件夹中有一个用于 **Run autonomously** 的 **Windows** 机器人：自主运行仅支持 Windows。

## 🔗 6. 将 Studio 连接到培训租户 { #6-connect-studio-to-the-training-tenant }

Autopilot in Studio 作用于 Studio 当前登录的租户。让 Studio 登录到与 CLI 相同的位置：

1. 打开 **Studio**。如果你已登录到其他环境（例如 `cloud.uipath.com`），请先退出登录。
2. 重新登录之前，把云端 URL 改为 `{{ training_authority }}`。在 **UiPath Assistant** 中，它位于 **Preferences** > **Orchestrator Settings** 下，名为 **Service URL**。
3. 登录，然后选择组织 **{{ training_org }}** 和租户 **{{ training_tenant }}**。
4. 确认 Studio 中可以使用 **Autopilot** 面板。如果不能，请先询问讲师再继续，因为动手实践部分就从它开始。

!!! warning "所有工具使用同一个环境"
    Studio、`uip` CLI 和你的浏览器都必须指向 **{{ training_url }}**。如果其中某一个仍在其他环境中，Autopilot 会把需求保存到你的编码智能体看不到的项目里。

## 🏦 7. 注册你的 UiBank 测试用户 { #7-register-your-uibank-test-user }

测试用例会以已注册的 UiBank 用户身份登录。现在就创建你的用户，让测试有账号可用。

1. 访问 **[uibank.uipath.com/register-account](https://uibank.uipath.com/register-account)**。
2. 填写表单：名、中间名和姓，性别，邮箱，用户名和密码。请使用一个你在其他地方都没用过的密码，因为 UiBank 是一个公开的演示网站。
3. 注册后，在 **[uibank.uipath.com/login](https://uibank.uipath.com/login)** 登录，确认账号可以使用。

4. 如果登录后 UiBank 显示 **Important Notice** 对话框，请选择 **I agree to the Privacy Policy**。用 ✕ 关闭它会让你处于未登录状态。请在自动化任何操作之前，现在就手动接受它。

测试不会在项目中存储你的密码，而是从 Orchestrator 的**凭据资产**中读取。请手动创建它：

1. 在 **Orchestrator** 中打开 `{{ training_folder }}` 文件夹，进入 **Assets**。
2. 选择 **Add** > **Credential**，命名为 `{YourName}_UiBankCredential`。
3. 在那里输入你的 UiBank 用户名和密码，然后保存。

!!! warning "不要把密码交给你的编码智能体"
    `uip` CLI 只能在命令行中以 `username:password` 的形式接收凭据，所以编码智能体会在聊天中向你索要。这样密码就会出现在对话记录和命令中。请改为在 Orchestrator 中输入。

!!! warning "记下你的 UiBank 邮箱"
    在动手实践中你会把它用作 `var_LoanEmail`：Step 6 中的个人资料检查会把它与 UiBank 显示的邮箱进行比较。

## 📄 8. 下载设计文档 { #8-download-the-design-document }

创建一个名为 `workshop` 的文件夹，把[设计文档](resources.md#the-design-document)下载到其中。它应该是这样的：

```text
workshop/
└── E2E UiBank Online Banking.docx   ← the design document
```

你会在课程开始时创建 Test Manager 项目和 Studio 项目。

!!! success "环境准备完成"
    你的虚拟机已在浏览器、Studio 和 `uip` CLI 中登录到 {{ training_tenant }}，并且有了 UiBank 测试用户和设计文档。开始测试吧。
