<!--
  Profile: heggria/heggria
  Rule: evidence first, philosophy second. Every number here must be checkable.
-->

<div align="center">

# Heggria

### I make agent runs verifiable, replayable, and incremental.

Agent infrastructure & product engineering · [OpenDesign](https://github.com/nexu-io/open-design) · Beijing

[![taskflow](https://img.shields.io/npm/v/pi-taskflow?style=flat-square&color=7775FF&label=taskflow)](https://www.npmjs.com/package/pi-taskflow)
[![pi-taskflow downloads](https://img.shields.io/npm/dm/pi-taskflow?style=flat-square&color=1f6feb&label=pi-taskflow%20downloads%2Fmo)](https://www.npmjs.com/package/pi-taskflow)
[![stars](https://img.shields.io/github/stars/heggria/taskflow?style=flat-square&color=444&label=stars)](https://github.com/heggria/taskflow/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/heggria/taskflow/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/heggria/taskflow/actions/workflows/ci.yml)

[`taskflow`](https://github.com/heggria/taskflow)
&nbsp;·&nbsp;
[`docs`](https://heggria.github.io/taskflow/)
&nbsp;·&nbsp;
[`writing`](https://heggria.github.io/writing/)
&nbsp;·&nbsp;
[`bilibili`](https://space.bilibili.com/20296120)
&nbsp;·&nbsp;
[`email`](mailto:bshengtao@gmail.com)

</div>

---

## Current work & collaboration

- **At work — [OpenDesign](https://github.com/nexu-io/open-design):** the open-source, local-first design application where I work.
- **Personal open source — [taskflow](https://github.com/heggria/taskflow):** verifiable, replayable coding-agent workflows.
- **Collaborate:** try a [host guide](https://heggria.github.io/taskflow/en/docs/guides/), bring a reproducible workflow to [Issues](https://github.com/heggria/taskflow/issues), or contribute an example, host fix, or diagnostic improvement via the [contribution guide](https://github.com/heggria/taskflow/blob/main/CONTRIBUTING.md).

---

<details>
<summary>A real run: a verification gate stopped downstream work</summary>

## A run that stopped before paying for the expensive part

Real output from a Pi run — not a mock dashboard:

```text
⊗ taskflow self-improve  6/7 · blocked · $0.095
    ✓ discover            agent   deepseek-v4-flash  10t ↑38k ↓6.7k $0.011
  ┌ ✓ write-runner-tests  agent   claude-sonnet-4-6  10t ↑13  ↓6.6k $0.020
  ├ ✓ write-store-tests   agent   claude-sonnet-4-6  10t ↑11  ↓10k  $0.018
  ├ ✓ write-agents-tests  agent   claude-sonnet-4-6  10t ↑28  ↓13k  $0.030
  └ ✓ fix-stability       agent   claude-sonnet-4-6  10t ↑13  ↓3.9k $0.012
    ✓ verify              gate    BLOCK 3 type errors in test files
    ⊘ report              reduce  skipped · Gate blocked  ↳ fix-stability
```

The layout **is** the DAG: parallel rails are concurrency, long edges are dependencies,
and the gate states why downstream work stopped. No separate control plane needed to read it.

Nine operations answer questions about a graph for **zero model calls** —
`plan` · `verify` · `compile` · `lint` · `ir` · `trace` · `replay` · `why-stale` · `analytics`.
You can price a run before spending on it, and re-ask what happened after it ends.

---

</details>

## Now building — [taskflow](https://github.com/heggria/taskflow)

**The compounding layer for multi-agent work.**
Declarative DAGs, statically verified, executed in isolated subagents,
resumable across sessions, replayable without tokens, recomputed from the smallest stale frontier.

| | |
|---|---|
| **Runs on** | Pi · Codex · Claude Code · OpenCode · Grok Build · Hermes Agent; see the [host support baseline](https://github.com/heggria/taskflow/blob/main/conformance/workspace/host-support-baseline.json) |
| **Surface** | 12 phase types · 18 built-in agents · 20 MCP tools · TypeScript DSL → portable JSON |
| **Compiled identity** | FlowIR + content hash → provenance, stale analysis, cross-run cache |
| **Evidence** | MIT · [CI](https://github.com/heggria/taskflow/actions/workflows/ci.yml) · [releases](https://github.com/heggria/taskflow/releases) · [host support baseline](https://github.com/heggria/taskflow/blob/main/conformance/workspace/host-support-baseline.json) |
| **Distribution** | 10 taskflow packages on npm. The badge above tracks `pi-taskflow` downloads; downloads are not unique users. |

```text
verify before spend  ·  replay without tokens  ·  recompute the stale frontier
```

[repo](https://github.com/heggria/taskflow) · [docs](https://heggria.github.io/taskflow/) · [examples](https://github.com/heggria/taskflow/tree/main/examples) · [changelog](https://github.com/heggria/taskflow/blob/main/CHANGELOG.md)

One project, gone deep. Everything below is smaller by design.

---

## What's next

Following me is a subscription, so here is what it buys.

| Status | What |
|---|---|
| 🧪 published beta | **[taskflow 0.3.0-beta.1.2](https://github.com/heggria/taskflow/releases/tag/v0.3.0-beta.1.2) — Trusted Effects.** Declared filesystem effects and ledger-backed explanations. Beta, not GA or an OS sandbox; read the [scope and limitations](https://github.com/heggria/taskflow#security-boundaries-we-state-plainly). |
| 📋 published baseline | **[Host support matrix](https://github.com/heggria/taskflow/blob/main/conformance/workspace/host-support-baseline.json).** Published filesystem, secret, and service support limits. Adapter availability does not imply a tested enforcement guarantee for every host. |
| 🚧 draft | **[0.3.0-beta.2 Control Plane work](https://github.com/heggria/taskflow/pull/142).** Active development; not a released feature. |
| ⏭ next | **Write up incremental recompute for agent graphs** — what Bazel/Nix/Salsa get right, and what breaks when the "build steps" are nondeterministic. |

Watch [taskflow releases](https://github.com/heggria/taskflow/releases) for the shipping version of this list.

---

## Why I build it this way

<div align="center">
<img src="assets/compound.svg" alt="chat → traces → trust → next decision, looping back as compound interest" width="680" />
</div>

Getting something to run once is only principal. Real completion leaves interest:
a contract for what *done* meant, evidence of what actually happened, and an honest note
about where uncertainty remains. Chat is excellent at momentum, and momentum evaporates —
two weeks later, *why* the fifteenth revision happened is buried under the first fourteen.

So I put the compounding part in artifacts instead of transcripts:
**the interface that creates the work should not be the only place that can understand it.**

Two rulers I actually use when choosing:

```text
01  Evidence outlives confidence.
02  Constraints give a tool its character — omissions as deliberate as features.
```

More: [Work should outlive chat](https://heggria.github.io/writing/work-should-outlive-chat/) ·
[Trust comes from boundaries](https://heggria.github.io/writing/trust-comes-from-boundaries/) ·
[Small tools, sharp edges](https://heggria.github.io/writing/small-tools-sharp-edges/)

---

## Personal tools & labs

Things I built for myself. Listed because they're where the ideas got tested first — not as products, and not all of them public.

- **Hermit** *(private, personal daily driver)* — a governed local kernel for long-running work: permissions with shape, receipts for what happened, recovery after failure. It's how I found out which parts of "bounded authority" survive contact with my own impatience; taskflow's gates and effect model owe it a lot. Built for one user, so the source stays closed by choice — not a product, and not a stalled open-source plan.
- **[home-compass](https://github.com/heggria/home-compass)** — Beijing housing scorecards where "affordable on paper" ≠ "comfortable to live with."
- **[selffield](https://heggria.github.io/selffield/)** — a personal mirror grown from evidence and tension, with no personality labels.
- **cli-lab** *(private)* — local CLI experiments consolidated into one monorepo. The standalone snapshots in my repo list are the archived predecessors: kept for history, not maintained.

---

## About

I work at [OpenDesign](https://github.com/nexu-io/open-design) in Beijing, between agent infrastructure and full-stack products.
Day languages: TypeScript · Python · Node.js · Vue — but the language I care about most is
the one between a system and the person trying to understand it.

Engineering is practice; writing is necessity. What I ship publicly, I back with evidence;
what I keep private, I say is private.

<div align="center">

<sub>
Follow if you work on agent orchestration, incremental computation, or making runs auditable.<br/>
<em>Once is not enough — make the next time cheaper.</em>
</sub>

</div>
