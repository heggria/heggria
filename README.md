<div align="center">

# Heggria

### Agent Infrastructure Engineer · Developer Tools Builder

I build governed, inspectable, and recoverable systems for AI agents.

[GitHub](https://github.com/heggria) · [Bilibili](https://space.bilibili.com/20296120)

</div>

## What I work on

Most agent systems optimize for completing the current turn. I am interested in the engineering that makes their work trustworthy after the turn is over:

- explicit task graphs instead of orchestration hidden in prompts;
- scoped authority and approval before consequential actions;
- receipts, evidence, and replayable state after execution;
- deterministic recovery when work fails or inputs change;
- small, searchable tool surfaces instead of loading every integration at once.

My primary stack is **TypeScript, Python, Node.js, and Vue**. I work at **MiniMax** in Beijing.

## Selected work

| Project | What it proves | Status |
| --- | --- | --- |
| [Hermit](https://pypi.org/project/hermit-agent/) | A local-first governed agent kernel with approvals, scoped authority, receipts, proof export, and rollback-aware recovery. | [PyPI](https://pypi.org/project/hermit-agent/) |
| [taskflow](https://github.com/heggria/taskflow) | A compiler and runtime for verifiable multi-agent DAGs across Pi, Codex, Claude Code, OpenCode, and Grok. Supports resume, replay, budgets, and incremental recomputation. | [Docs](https://heggria.github.io/taskflow/) · [Releases](https://github.com/heggria/taskflow/releases) · [CI](https://github.com/heggria/taskflow/actions) |
| [Home Compass](https://github.com/heggria/home-compass) | A decision-support product that turns Beijing housing trade-offs and mortgage constraints into an explainable scorecard. | [Source](https://github.com/heggria/home-compass) |
| [SBTI Lab](https://github.com/heggria/sbti-lab) | A shipped personality-testing web product and a compact example of product-focused TypeScript work. | [Source](https://github.com/heggria/sbti-lab) |

## How I build

```text
define the contract
      ↓
verify before model spend
      ↓
execute with bounded authority
      ↓
persist receipts and evidence
      ↓
resume, replay, or roll back
```

I value:

- **claim-to-implementation parity** — documentation should describe what the current release actually does;
- **fail-closed boundaries** — permissions, secrets, paths, and provider behavior must be explicit;
- **reproducible releases** — tests, package smoke checks, provenance, and published artifacts are one release contract;
- **dogfooding** — real workflows should expose reliability problems before users do.

## Contact

The best way to discuss a project is through its GitHub Issues or Discussions. For other conversations, use the public email listed on this profile.
