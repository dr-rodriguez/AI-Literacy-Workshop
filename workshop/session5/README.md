# Session 5

Introduces command-line AI workflows with copilot-cli and opencode paired with GitLab Duo or GitHub Copilot for open-source contexts. Mostly hands-on time to try the tools.

## Useful Links

You may need to have Homebrew installed for easier installation of these. See the Self-Service app.

- [GitHub Copilot CLI](https://github.com/github/copilot-cli)
  - Command-line tool for interacting with GitHub Copilot
- [About copilot-cli](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli)
- [OpenCode](https://opencode.ai/)
  - Open-source code editor for AI-assisted development (can add GitHub Copilot or GitLab Duo)
- [Cursor CLI](https://cursor.com/cli)
  - Command-line tool by Cursor

## Tasks

1. Install copilot-cli; see https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli

2. Authenticate with Github (/login)

3. Try out some commands:
 - /context
 - /instructions
 - /skills
 - /model
 - /usage

4. Run headless: `copilot -p "hello"`

If testing OpenCode, the concepts are similar but you need to select the provider (/connect)- such as Github copilot or Gitlab Duo.
