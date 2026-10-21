# Platform reference checks

Checked 21 October 2026. These links document product capabilities and setup; they do not establish that a particular participant's tenant has enabled them. The workflows are original NavAIgate instructions. Synthetic examples contain no customer data.

| Primary source | Why it matters |
|---|---|
| [Claude: use plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) | Custom plugin upload, Cowork and Claude Code availability; organisation controls. |
| [Claude Code: create a marketplace](https://code.claude.com/docs/en/plugin-marketplaces) | Marketplace manifest and installation route. |
| [Claude Code: skills](https://code.claude.com/docs/en/skills) | SKILL.md discovery and plugin skill names. |
| [Claude: connect Microsoft 365](https://support.claude.com/en/articles/15183774-connect-to-microsoft-365) | Work account, tenant consent, Outlook and document access; write tools depend on setup. |
| [Claude: admin setup for Microsoft 365](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector) | Entra and organisation configuration. |
| [ChatGPT: Projects and chats](https://learn.chatgpt.com/docs/projects?surface=app) | Project instructions and uploaded sources; local filesystem access is separate. |
| [ChatGPT: manage your inbox](https://learn.chatgpt.com/use-cases/manage-your-inbox) | Connected Outlook and human-written sent email for writing context. |
| [Salesforce: sObject Describe](https://developer.salesforce.com/docs/platform/api-rest/guide/resources-sobject-describe.html) | Discover actual object and field metadata before proposing mappings. |
| [Salesforce: working with records](https://developer.salesforce.com/docs/platform/api-rest/guide/using-resources-working-with-records.html) | Record retrieval and update operations; actual permissions still apply. |

The pack does not require a custom Microsoft Graph application. If an organisation builds its own connector, its administrators own the permissions and security review. Never paste credentials into a skill or publish authentication files.
