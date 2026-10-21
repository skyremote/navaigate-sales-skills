# NavAIgate Sales Skills

Five reusable workflows for technical-sales teams using Microsoft 365. Prepare for a customer conversation, keep Salesforce accurate, challenge a deal, build your own writing voice and run a useful QBR.

**Start with one task. You do not need to write code.** Each skill explains what to read, what to produce and how to check the result. Your connected tools supply the data; the skill supplies the method.

## Choose your first task

| Skill | Start with this request | What you get |
|---|---|---|
| [Prepare for meetings](skills/meeting-prep/SKILL.md) | “Prepare me for my next meeting with [customer]. Check my calendar and relevant conversations. Give me a one-page brief and show your sources.” | Purpose, people, commitments, questions and an agenda. |
| [Salesforce admin](skills/salesforce-admin/SKILL.md) | “Turn these meeting notes into proposed Salesforce updates. Show me what would change before changing anything.” | A clear record update proposal, next steps and missing evidence. |
| [Black Hat](skills/black-hat/SKILL.md) | “Challenge our plan for this deal. Give me the five strongest ways it could fail, the evidence and the questions we need to ask.” | An honest deal challenge and a small action plan. |
| [Build my voice](skills/build-my-voice/SKILL.md) | “Help me build my writing-voice skill from my own sent Outlook emails. Start with a small sample, then let me correct three drafts.” | A private personal voice skill that improves through your edits. |
| [QBR](skills/qbr/SKILL.md) | “Prepare a QBR for [customer] covering [dates]. Show progress against their goals, gaps in the evidence and a joint 90-day plan.” | A customer review brief, metric table and presentation structure. |

## Get the pack

- **Claude Cowork:** [download the plugin ZIP](https://github.com/skyremote/navaigate-sales-skills/releases/latest/download/navaigate-sales-plugin-v1.0.0.zip) and upload it through Cowork's custom plugin control.
- **Claude Code:** add this repository as a plugin marketplace, then install `navaigate-sales`.
- **ChatGPT online:** [choose a self-contained Markdown workflow](chatgpt/), upload it to a private Project and ask ChatGPT to follow it. No terminal required.

Follow the short [platform setup guide](docs/platforms.md) for the exact route and Microsoft 365 setup. [All downloads](https://github.com/skyremote/navaigate-sales-skills/releases/latest) include individual skills, the complete plugin, ChatGPT files and checksums.

In Claude Code:

```text
/plugin marketplace add skyremote/navaigate-sales-skills
/plugin install navaigate-sales@navaigate-sales-skills
```

## Your first ten minutes

1. Choose one skill and install or upload it using the route above.
2. Tell the assistant which account, meeting or customer you mean. Give it a connected source or an approved file. You can start with a synthetic practice example from the skill's references.
3. Ask for a small result: one meeting brief, one proposed CRM update or three voice test drafts.
4. Inspect the sources and correct what is wrong. Keep the useful result and your corrections in your private workspace.

Do the same task again with a different customer. The reusable instructions are the skill; each customer request is a new run. You do not need to build a custom app first.

## What connects to what?

| Part | Its job |
|---|---|
| Your request | Defines the outcome for this task. |
| Skill | Supplies the repeatable instructions, checks and output format. |
| Connected tool | Retrieves data or performs an available action in an approved service. |
| Source evidence | Lets you check why the result says what it says. |
| Your judgement | Corrects the result and authorises external changes when needed. |

Installing this pack does not connect Outlook or Salesforce. Use your organisation's approved connections. If a source is unavailable, the assistant must say so and work from approved files instead. Salesforce changes need a clear record and action; the other four workflows produce private drafts or files and do not send messages.

The voice skill creates **your own writing profile**, not an audio voice clone. It reviews your own writing, produces three drafts for you to edit and turns those edits into reusable guidance. It does not monitor your mailbox in the background or publish your profile here.

## For facilitators and maintainers

Use [the short practice session](docs/practice-session.md) to teach by doing. Platform differences and source references are in [docs/platforms.md](docs/platforms.md) and [docs/sources.md](docs/sources.md). Packaging checks and behavioural evaluation details are in [docs/validation.md](docs/validation.md).

`skills/` is the maintained source. `chatgpt/` and release ZIPs are generated from it:

```sh
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

The build uses Python's standard library and makes no network calls. All included examples are synthetic. Keep customer data, raw mail, transcripts, credentials and generated voice profiles outside this public repository. MIT licensed; [NavAIgate](https://navaigate.dev).
