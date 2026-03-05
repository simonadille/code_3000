# Security

## Intended users
This repository is intended for me and my professor for assignments in CSE 3000

## Risk assessment
If this repository fell into the wrong hands, the main risks would be exposing any private information or secrets if they were accidentally committed (such as API keys, credentials, or personal data). Someone could also misuse the code if it contains any sensitive data.

## Steps taken to secure the repo
- I avoid committing secrets (API keys, passwords, tokens) to the repository.
- I use a `.gitignore` (or equivalent) to keep local config files and secrets (like `.env`) out of version control when applicable.
- I use branch protection / pull request rules / CODEOWNERS.
