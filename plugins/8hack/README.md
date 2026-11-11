# 8hack

The hackathon co-pilot for 14 November 2026: the `8hack` skill, four companion skills
(`hack-rubric-check`, `hack-venture-gates`, `hack-economic-model`, `hack-plain-voice`)
and the Control8 MCP server `hack`.

## Install (Claude Code)

```
claude plugin install 8hack --marketplace kakashi-ventures/hackathon
```

Older Claude Code:

```
claude plugin marketplace add kakashi-ventures/hackathon
claude plugin install 8hack@kva-hackathon
```

Then in Claude Code: `/mcp` → `hack` → Authenticate, and sign in with the email you registered with.
Type `/8hack` to start.

The skill files are generated from Control8 (`skills/8hack`, `skills:hack-sync`): edit them there, not here.
