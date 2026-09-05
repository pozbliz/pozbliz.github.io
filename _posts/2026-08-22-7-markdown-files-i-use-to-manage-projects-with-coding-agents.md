---
layout: post
title: "7 Markdown files I use to manage projects with coding agents"
date: 2026-08-22
excerpt: "The 7 Markdown files that keep my AI coding agent on track across multiple sessions."
categories: [agents]
tags: [ai-agents, agent-workflows, codex, context-engineering, project-management]
---

When I started using AI coding agents, I managed most projects through conversation. That works well for tasks that
fit into one session. It becomes harder when a project spans several sessions and a new agent needs to recover
previous decisions, preferences, and unfinished work. I used to handle this with handover prompts. Those help, but
important decisions still get buried, discovered tasks get lost, and the reason behind rejected approaches often
disappears. I discuss the tradeoffs between handoffs, fresh sessions, and compaction in [Managing agent context - Part 2](/posts/managing-agent-context-part-2-full-context-windows-compaction/).

My current solution is a small set of Markdown files that can grow with the project:

- `README.md`
- `GLOSSARY.md`
- `DESIGN.md`
- `PLAN.md`
- `TASKS.md`
- `DECISION_LOG.md`
- `LEARNINGS.md`

In Codex, I use the `AGENTS.md` file to tell the agent what each file is for and when it must be updated. I also have
an `init-project` skill that creates the initial project brief in `README.md`. The other documents are created later
by the workflows that need them rather than being scaffolded upfront.

This introduces a lightweight kind of project management into my agent workflow. The agent helps maintain the
project state while it works, instead of leaving me to reconstruct everything from old conversations.

## When to use this workflow

I do not create all seven files for every project. A short script or single-session task usually does not need a
design, plan, task list, and decision history.

Instead, I start with the README and let the rest of the set appear as the project needs it. As a project grows,
recording its current state and history on disk becomes more useful.

## The role of each file

I use separate files so [the agent can load only what it needs](/posts/managing-agent-context-part-1-understanding-the-context-window/) and distinguish current state from plans, decisions,
and tasks.

Each file answers a different question:

| File | Question it answers                                    |
|---|--------------------------------------------------------|
| `README.md` | What is this project and how do I use it?              |
| `GLOSSARY.md` | What do project-specific terms mean?                   |
| `DESIGN.md` | What are we building, and why is it designed this way? |
| `PLAN.md` | In which order are we building it?                     |
| `TASKS.md` | What is open right now?                                |
| `DECISION_LOG.md` | What changed, and why did we choose this approach?     |
| `LEARNINGS.md` | What non-obvious facts should future sessions know?    |

The boundaries are not always perfect. A design decision may affect the plan, create new tasks, and reveal a
learning at the same time. In those cases, I record each fact in the file that owns it.

## README.md: the current entry point

The `README.md` explains the project, its goals and scope, and how to get started.
It is the entry point for both humans and agents.

## GLOSSARY.md: the project's shared language

The `GLOSSARY.md` file records project-specific domain language. It defines terms in one or two sentences
without mixing in behavior, architecture, or implementation details. When several names could describe the same
thing, it chooses one canonical term and lists the alternatives I want the agent to avoid. For example, the glossary
prevents the agent from calling the same concept an "account," "customer," and "subscriber" across different
sessions.

I added this file after watching Matt Pocock explain his `grill-me-with-docs` skill in
[one of his YouTube videos](https://www.youtube.com/watch?v=6BB6exR8Zd8). I kept the same idea but named it
`GLOSSARY.md`, which feels more intuitive to me than `CONTEXT.md`.

I am still testing whether this improves agent output. Even if it does not, a short glossary is useful to humans and
cheap for an agent to read.

## DESIGN.md: what we are building and why

`DESIGN.md` is the stable description of what the system should do and why. It covers goals, non-goals,
architecture, data flow, and major feature rules.

My `AGENTS.md` tells the agent to read `DESIGN.md` before changing code and to check proposed changes against it. If a
change conflicts with the design, the agent asks me to resolve the conflict. I may change the implementation or
update the design.

## PLAN.md: the strategic route through the work

`PLAN.md` turns an approved design into concrete implementation slices. Each slice defines what should be built,
what it depends on, and how I will know it is complete. The plan describes the route, while `TASKS.md` contains the
individual actions needed to complete each slice.

## TASKS.md: the live source of truth

`TASKS.md` is the source of truth for open and completed implementation work. The agent updates a task as soon as it
is finished.

```markdown
# Tasks

## Complete feature workflow

- [ ] Add failing tests for the expected transitions.
- [ ] Implement completion of the current step.
- [ ] Transition to the next phase.
- [ ] Verify the complete flow in the application.
- [ ] [HUMAN] Confirm the transition timing feels correct.

## Follow-up fixes

- [ ] Prevent repeated input from triggering the next phase twice.
```

`[HUMAN]` marks a task that requires my judgment. Changes that affect scope or sequencing go back through planning.

## DECISION_LOG.md: preserving the reason, not only the result

Code shows what changed, but often not why. `DECISION_LOG.md` is created when the first non-trivial decision or change
needs an entry. Newest entries go at the top and record:

- what changed,
- why it changed,
- new issues discovered,
- anything that still needs human judgment.

Typo fixes and other simple edits do not need an entry. I only record decisions that a future session
could reasonably question or repeat. If any new action comes up, it is also added to `TASKS.md`.

## LEARNINGS.md: constraints and gotchas that survive the session

`LEARNINGS.md` stores constraints and gotchas that are neither tasks nor design decisions. It records facts a
future session could easily miss by reading the code and design alone. For example, an external API may behave
differently from its documentation.

Each dated entry states the behavior, why it matters, and the workaround. The agent asks before recording each
learning and creates the file only after I confirm the first one. Future learnings are appended so useful history is
not silently removed.

## How the files work together during a task

At the start of implementation, the agent reads `TASKS.md` and only the supporting documents relevant to the work.
Before changing code, the agent states its approach. After implementation, it verifies the work and updates any
affected project documents.

A new session can inspect the repository and recover the important state from files that were updated while the
work happened.

## Where I stay involved

The workflow keeps me involved where judgment is required:

1. **Unclear requirements:** During interactive work, the agent asks before implementing. During unattended work,
   it chooses a reasonable interpretation and records the assumption.
2. **Workflow handoffs:** I approve the design before planning and the plan before task generation.
3. **Approach review:** Before writing code, the agent explains its approach and tradeoffs.
4. **Human decisions:** `[HUMAN]` items and new durable learnings wait for my confirmation.
5. **Final verification:** The agent reports what changed, what remains open, and what it did not do.

I keep these checkpoints for decisions that can change the project direction or behavior. The agent handles routine
implementation choices.

## The AGENTS.md instructions behind the workflow

These are some of the actual rules from my `AGENTS.md`:

```markdown
- When `TASKS.md` exists, it is the source of truth for implementation work and its completion history. Check it before implementation.
- When `GLOSSARY.md` exists, read it before work that defines, changes, disputes, or depends on domain terminology.
- After every non-trivial decision or change, create `DECISION_LOG.md` if needed and add an entry.
- Confirm a learning with the user before recording it. Create `LEARNINGS.md` after the first confirmation; once created, it is append-only — never delete entries, only add.
- `README.md` should always reflect the current state of the project, not the original plan.
```

Coding conventions and other task-specific rules live in separate files. `AGENTS.md` tells Codex when to load each
one.

## Initializing the workflow with a skill

I use an `init-project` skill to gather the project's purpose, users, scope, success criteria, and confirmed
constraints. It creates `README.md` and recommends an initial repository structure. It does not scaffold the other
documents. The relevant workflow creates each one when the project first needs it.

I will write another article about the skills I use to create and maintain these documents.

## This is still an evolving workflow

Stale documentation can be worse than no documentation because an agent may follow it confidently. Updating the
relevant files should be part of the actual implementation tasks and not a cleanup for afterward.
I am still experimenting with this workflow and expect parts of it to change as I use it on more projects.
If you want to try the idea, start with a `README.md` and one `AGENTS.md` rule that keeps it current. If you use a
different way to preserve project state across agent sessions, I would be interested to hear what has worked for
you.
