# Choose where you work

These are the same five workflows packaged in different ways. Choose one product and complete one small task before adding more tools. No paid model API key is required by this repository.

## Claude Code

In Claude Code, run:

```text
/plugin marketplace add skyremote/navaigate-sales-skills
/plugin install navaigate-sales@navaigate-sales-skills
```

Restart the session if the skills do not appear. Then use `/navaigate-sales:meeting-prep` followed by your request. The other names are `salesforce-admin`, `black-hat`, `build-my-voice` and `qbr`.

For local inspection without installing anything globally:

```sh
git clone https://github.com/skyremote/navaigate-sales-skills.git
claude --plugin-dir ./navaigate-sales-skills
```

An organisation may restrict plugin installation. Use its approved distribution route. Installing instructions does not sign you into Outlook or Salesforce.

## Claude Cowork

1. Download `navaigate-sales-plugin-v1.0.1.zip` from [Releases](https://github.com/skyremote/navaigate-sales-skills/releases/latest).
2. Open Cowork, then **Customize > Plugins**, and upload the custom plugin file. Labels may vary by organisation and app version; use the custom plugin upload control.
3. Start a task and select the skill using `/` or the skill picker. Use one of the README starter requests.
4. Enable the organisation-approved Microsoft 365 connection separately. Select a private working folder when saving outputs.

The ZIP includes the five instruction folders and plugin manifest. It contains no executable MCP server, hooks, credentials or automatic connector installation. Individual skill ZIPs are also supplied for environments that allow skill uploads instead of plugins. If plugins are disabled, use the Markdown task file as instructions with approved attachments; this is a manual fallback, not a native plugin installation.

## ChatGPT online

1. Download one file from [`chatgpt/`](../chatgpt/), for example `meeting-prep.md`. Each is self-contained, including its templates and references.
2. Create a private ChatGPT Project for this workflow. Upload the file as a project source.
3. Add project instructions: **“For this project, read and follow the attached [filename] workflow for relevant requests. Check which tools and sources you actually have. Label missing evidence and do not claim an external action completed without a receipt.”** Replace the filename with the one uploaded.
4. Start a chat with the corresponding README starter request. Connect Outlook Email/Calendar or approved apps available to your workspace, or attach approved files.

For a quick trial, attach the Markdown to a normal chat and ask ChatGPT to follow it for the task. A Project makes the instructions easier to reuse. Uploading `SKILL.md` alone does not install a Claude plugin, create a slash command, grant local folder access or connect Microsoft 365. Product, plan and administrator settings determine available apps and actions.

## Connect Microsoft 365 once

Use your organisation's approved account and connector. In Claude, the documented route is **Customize > Connectors > Microsoft 365 > Connect**, after tenant setup. In ChatGPT, choose the approved Outlook apps/plugins available in your workspace. Read [sources](sources.md) for current vendor guides.

Some workshop environments may already expose **Work IQ** or another approved Microsoft 365 MCP in Claude Code. Reuse that connection if it provides the needed tools; a separate integration is not required just because this pack exists. Tool names and the data they can retrieve differ. Ask:

> “Tell me which connected tools you can use for my calendar, Outlook email, sent email and work documents. Verify a small read for the task I name, and tell me what is unavailable. Do not change anything.”

A connection working in one product does not prove it works in another. Skill instructions are portable; authentication, conversation history, file access and connector permissions are separate. Reading Microsoft 365 does not grant access to Salesforce. Ask your admin about a denied connector; do not route company data through a personal account to bypass the restriction.

For the voice builder, verify that your own sent message bodies are actually accessible. Read/search access is enough; no email-send permission is needed for the workflow. A connector may expose broader permissions than this task uses. The workflow limits what it reads, not the OAuth permission grant.

## Keep work organised

Use a private folder outside the public repository:

```text
my-sales-work/
  instructions.md          # Your stable team conventions
  inputs/                  # Approved originals; preserve them
  outputs/                 # Versioned briefs, proposals and QBRs
  evidence/                # Private source ledger and checks
  my-voice/                # Your personal generated voice skill
```

In Claude Code, `AGENTS.md` or `CLAUDE.md` discovery depends on the harness; follow your team's supported setup. You can keep one canonical rules file and reference it from the other where supported. In ChatGPT, place the equivalent rules in Project instructions. A folder name does not itself load instructions, connect a tool or give an agent memory.

Start fresh chats for distinct outcomes. Carry forward the brief, relevant source IDs, decisions and unresolved questions rather than repeatedly attaching your whole mailbox. Checkpoint the result before changing platforms. There are no universal token savings or model-price promises in this pack.
