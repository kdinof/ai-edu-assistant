# Module 1: Claude Cowork setup and Google Workspace MCP configuration 2026

**Date:** 2026-03-08
**Model:** sonar-pro
**Questions investigated:** 3

---

## Executive Summary

_[Add your synthesis here after reviewing the findings]_

---

## 1. How to install and configure Claude Desktop Cowork mode on Mac 2026

**Claude Desktop Cowork mode is a feature within the Claude Desktop app for macOS, requiring a Claude Pro ($20/month) or higher subscription like Max ($100-$250/month).** [2][3][5] It enables autonomous AI task handling (e.g., file organization, document creation) in a sandboxed environment, accessible via a tab switch after app installation.[2][3]

### Requirements
- **Hardware/Software:** Apple Silicon Mac (M1/M2/M3 recommended), macOS 14+ (Sonoma or later).[2]
- **Account:** Active Claude Pro or Max subscription; Cowork is not available on free or basic plans.[2][5]
- **Other:** Internet connection; app must stay open during sessions.[2][3]

### Installation Steps
1. Visit claude.ai/download and click **Download for macOS**.[2]
2. Open the downloaded file and drag **Claude.app** to your **Applications** folder.[2]
3. Launch **Claude Desktop** from Applications and sign in with your Pro/Max account.[2][3]

**Note:** This is distinct from Claude Code (a terminal-based tool installed via commands like `claude` after visiting code.claude.com/docs).[1] Cowork is app-exclusive, not a terminal REPL.[2][3][5]

### Configuration and Enabling Cowork Mode
1. Open **Claude Desktop**.[3]
2. At the top of the window, locate the mode selector with tabs like **Chat**, **Cowork** (or **Tasks** in beta), and **Code**.[3][5]
3. Click the **Cowork** tab to switch modes.[3][5]
4. Describe your task in the interface; review Claude's plan, then approve to let it run autonomously on granted folders.[2][3]
5. **Optional enhancements:** Integrate MCP tools (e.g., Desktop Commander from github.com/anthropics/desktop-commander) for Mac automation like file renaming or terminal setup, bridging the sandbox to your system.[4]

Sessions end if the app closes; grant folder access per task for security.[2][3] For advanced use, describe outcomes in plain English rather than code.[4] If on a lower plan, join the waitlist via the app.[5]

**Sources for this section:**
- [1] https://www.youtube.com/watch?v=uPpj6CZ6LLo
- [2] https://aitoolsreview.co.uk/insights/how-to-use-claude-cowork
- [3] https://support.claude.com/en/articles/13345190-get-started-with-cowork
- [4] https://www.youtube.com/watch?v=6bsJdR2naXE
- [5] https://www.datacamp.com/tutorial/claude-cowork-tutorial
- [6] https://www.youtube.com/watch?v=kddjxKEeCuM
- [7] https://www.youtube.com/watch?v=nderH-8EEAk
- [8] https://claudecowork.im

---

## 2. How to set up Google Workspace MCP server for Claude Desktop step by step

## Prerequisites
- A Google account with Google Workspace access (Gmail, Drive, Calendar, etc.).
- Command-line interface (Terminal on macOS/Linux, PowerShell/WSL on Windows).
- Python 3.12+ and `uv` package manager (or Docker for containerized setup).
- Claude Desktop app installed.[1][3]

## Step 1: Set Up Google Cloud Project and OAuth Credentials
1. Go to [Google Cloud Console](console.cloud.google.com) and create a new project (or select an existing one). Note the project name.[1]
2. Navigate to **APIs & Services > Credentials**.
3. Click **Create Credentials > OAuth client ID**.
4. Select **Desktop application** (no redirect URIs needed for taylorwilsdon's server).[1][3]
5. Download the JSON credentials file containing your **Client ID** and **Client Secret**.[1][3]
6. Set environment variables:
   ```
   export GOOGLE_OAUTH_CLIENT_ID="your-client-id"
   export GOOGLE_OAUTH_CLIENT_SECRET="your-secret"
   ```
   For development/testing, also set:
   ```
   export OAUTHLIB_INSECURE_TRANSPORT=1
   ```
   Optionally, set a default user email:
   ```
   export USER_GOOGLE_EMAIL="your.email@gmail.com"
   ``` [1]

## Step 2: Enable Required Google APIs
In **APIs & Services > Library**, search for and enable:
- Gmail API
- Google Drive API
- Google Calendar API
- Others as needed (e.g., Sheets for full functionality).[1][2]

## Step 3: Clone and Install the Google Workspace MCP Server
Use the production-ready server from taylorwilsdon/google_workspace_mcp, which supports all major Google Workspace services.[1]
```
git clone https://github.com/taylorwilsdon/google_workspace_mcp
cd google_workspace_mcp
uv sync  # Install dependencies with uv
``` [1]

## Step 4: Configure Server Settings (Optional)
Set additional environment variables for customization:
```
export WORKSPACE_MCP_BASE_URI="http://localhost"
export WORKSPACE_MCP_PORT=8000
```
View full config options in the repo's documentation.[1]

## Step 5: Run the MCP Server
Start the server with tool tiers:
```
uv run main.py --tool-tier core  # Essential tools (Gmail, etc.)
uv run main.py --tool-tier extended  # Core + additional
uv run main.py --tool-tier complete  # All tools
```
Or use Docker:
```
docker build -t workspace-mcp .
docker run -p 8000:8000 workspace-mcp --transport streamable-http
```
The server runs on `http://localhost:8000` and handles OAuth flow: it opens your browser for authentication, saves tokens, and enables multi-user support.[1][3]

## Step 6: Configure Claude Desktop to Use the MCP Server
1. Locate Claude Desktop's config file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Adjust path for your OS.[2][3]
2. Add the server entry to the `mcpServers` object (adapt path/env vars):
   ```
   {
     "mcpServers": {
       "google-workspace": {
         "command": "uv",
         "args": ["run", "main.py", "--tool-tier", "complete"],
         "env": {
           "GOOGLE_OAUTH_CLIENT_ID": "your-client-id",
           "GOOGLE_OAUTH_CLIENT_SECRET": "your-secret",
           "USER_GOOGLE_EMAIL": "your.email@gmail.com"
         }
       }
     }
   }
   ``` [1][2][3]
3. Restart Claude Desktop. The server tools (e.g., Gmail read/send, Drive manage, Calendar events) will appear in the interface.[3]

## Verification and Troubleshooting
- On first run, complete OAuth in the browser (scopes include `gmail.modify`, `calendar`, etc.). Tokens save automatically.[1][2]
- Test in Claude: Ask it to "read my recent Gmail" or similar; it should connect via MCP.[3]
- Common issues: Ensure APIs are enabled, env vars are set, and port 8000 is free. For multi-user, use `MCP_ENABLE_OAUTH21=true`.[1]
- Note: Different repos (e.g., epaproditus) use "Web application" with `http://localhost:4100/code` redirect—stick to taylorwilsdon for Desktop app simplicity.[1][2][3]

This setup integrates Google Workspace with Claude Desktop via MCP for AI-driven automation.[1][3]

**Sources for this section:**
- [1] https://github.com/taylorwilsdon/google_workspace_mcp
- [2] https://mcpservers.org/servers/epaproditus/google-workspace-mcp-server
- [3] https://skywork.ai/skypage/en/ai-engineer-guide-google-workspace-servers/1977622808059383808
- [4] https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-google-cloud-run-in-under-10-minutes
- [5] https://www.youtube.com/watch?v=mgARLKganVo
- [6] https://dev.to/googleworkspace/google-workspace-developer-tools-mcp-server-723
- [7] https://pub.towardsai.net/i-used-mcp-servers-to-automate-google-workspace-and-saved-hours-try-this-155d1b569d09
- [8] https://crunchtools.com/my-mcp-server-setup-practical-guide/

---

## 3. CLAUDE.md best practices for office workers configuration 2026

**CLAUDE.md** files serve as managed documentation in Claude Code (Anthropic's code-focused tool integrated into Enterprise plans since August 2025), providing structured instructions, preferences, and context for Claude to follow during coding tasks like code review, generation, and debugging.[1][3][4]

For office workers—such as non-technical staff in sales, legal, HR, or admin roles—configure CLAUDE.md to emphasize **non-coding workflows**, prompt templates for routine tasks (e.g., email drafting, meeting summaries), and company-specific guidelines, adapting developer-focused best practices for broader enterprise use.[1][3][5]

### Recommended 10-Section Structure for Office Worker CLAUDE.md
Draw from established best practices, prioritizing simplicity, role-based cues, and iterative refinement to ensure reliable outputs without deep technical knowledge.[3][4][5]

- **1. Project/Team Overview**: Summarize your department's goals, key processes, and common tasks (e.g., "This CLAUDE.md is for the Sales team at [Company]. Focus on CRM updates, client emails, and pipeline reports.")[5]
- **2. Tech Stack/Tools**: List accessible tools like email clients, CRM (e.g., Salesforce), docs (e.g., Google Workspace), avoiding code-specific details.[5]
- **3. Workflow/Processes**: Define step-by-step routines, e.g., "For meeting summaries: 1) Extract action items; 2) Assign owners; 3) Flag risks; 4) Suggest follow-ups."[1][4]
- **4. Role-Based Guidelines**: Specify user context, e.g., "Assume user is a sales rep unless specified. Use professional, concise tone. Prioritize brevity for busy schedules."[1][3]
- **5. Prompt Templates**: Include reusable examples, e.g., "Draft sales email: [Context] [Key points] Output in bullet format for quick review."[1]
- **6. Output Conventions**: Enforce formats like "Always use tables for comparisons; end with next steps and questions for human review."[5]
- **7. Approval/Escalation Rules**: "Flag high-risk items (e.g., legal/contract language) for human oversight. Use 'Block-at-Submit'—generate full draft first, then validate."[2][4]
- **8. Data Governance**: "Never share confidential info. Reference internal RAG knowledge bases only. Comply with EU AI Act via human-in-loop for sensitive outputs."[1]
- **9. Style Preferences**: "Match company voice: [examples]. Avoid jargon; explain acronyms."[3][5]
- **10. Monitoring/Feedback**: "Track acceptance rates via Anthropic analytics. Update this file quarterly based on team feedback."[1]

### Implementation Best Practices for 2026 Office Configurations
- **Selective Activation**: Use `/context` command to load CLAUDE.md per project/task; don't auto-apply universally to avoid irrelevant guidance.[4]
- **Integration with Enterprise Features**: Leverage Model Context Protocol (MCP) for querying internal systems (e.g., ticket logs, CRM); pair with RAG for company knowledge (boosts recall by up to 67%).[1]
- **Human Oversight**: Shift from full reviews to AI-flagged escalations, e.g., for strategic decisions—aligns with 2026 trends in agentic workflows.[2]
- **Iteration Process**: Practice workflows manually first, document in CLAUDE.md, then scale via Claude Skills for reusable prompts.[3][4]
- **Admin Setup**: Enterprise admins assign "premium" seats with Claude Code access; use SAML/SCIM for SSO and set usage caps.[1]

Place CLAUDE.md in project roots or shared repos for team access; update periodically to incorporate Anthropic's open-source cookbooks (e.g., prompt caching for 2x latency reduction).[1][3] This setup enables office workers to achieve gains like 50% faster onboarding or 2x response speeds, as seen in enterprise cases.[1][2]

**Sources for this section:**
- [1] https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026
- [2] https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf
- [3] https://addyosmani.com/blog/ai-coding-workflow/
- [4] https://dev.to/valgard/claude-code-must-haves-january-2026-kem
- [5] https://uxplanet.org/claude-md-best-practices-1ef4f861ce7c
- [6] https://www.youtube.com/watch?v=sy65ARFI9Bg
- [7] https://github.com/awattar/claude-code-best-practices

---

## All Sources

1. https://www.youtube.com/watch?v=uPpj6CZ6LLo
2. https://aitoolsreview.co.uk/insights/how-to-use-claude-cowork
3. https://support.claude.com/en/articles/13345190-get-started-with-cowork
4. https://www.youtube.com/watch?v=6bsJdR2naXE
5. https://www.datacamp.com/tutorial/claude-cowork-tutorial
6. https://www.youtube.com/watch?v=kddjxKEeCuM
7. https://www.youtube.com/watch?v=nderH-8EEAk
8. https://claudecowork.im
9. https://github.com/taylorwilsdon/google_workspace_mcp
10. https://mcpservers.org/servers/epaproditus/google-workspace-mcp-server
11. https://skywork.ai/skypage/en/ai-engineer-guide-google-workspace-servers/1977622808059383808
12. https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-google-cloud-run-in-under-10-minutes
13. https://www.youtube.com/watch?v=mgARLKganVo
14. https://dev.to/googleworkspace/google-workspace-developer-tools-mcp-server-723
15. https://pub.towardsai.net/i-used-mcp-servers-to-automate-google-workspace-and-saved-hours-try-this-155d1b569d09
16. https://crunchtools.com/my-mcp-server-setup-practical-guide/
17. https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026
18. https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf
19. https://addyosmani.com/blog/ai-coding-workflow/
20. https://dev.to/valgard/claude-code-must-haves-january-2026-kem
21. https://uxplanet.org/claude-md-best-practices-1ef4f861ce7c
22. https://www.youtube.com/watch?v=sy65ARFI9Bg
23. https://github.com/awattar/claude-code-best-practices
