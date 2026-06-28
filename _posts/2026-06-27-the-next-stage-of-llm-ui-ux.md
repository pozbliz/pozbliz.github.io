---
layout: post
title: "Claude Tag: The next stage of LLM UI/UX"
date: 2026-06-27
categories: []
tags: [ai-agents, claude, opinion, ui-ux]
excerpt: "How LLMs go from individual use to team-wide collaboration."
---

Anthropic announced Claude Tag on 23 June 2026, introducing it as
[a new way for teams to work with Claude](https://www.anthropic.com/news/introducing-claude-tag). The product demos really impressed me because they show new ways
for individuals as well as whole teams to work with Claude outside a terminal or designated chat interface.
I believe they have given us a glimpse into the future where this way of working could be considered normal for
both engineers and non-engineers. Andrej Karpathy, one of the most prominent voices in the AI space, calls it a
[new paradigm for interacting with Claude](https://x.com/karpathy/status/2069547676849557725) and "the 3rd major redesign of LLM UI/UX." At the same time,
he points out that the value only emerges if the supporting tools, integrations, compute environments, memory,
and security are reliable.

Claude Tag is launching first on Slack, in beta for Claude Team and Enterprise customers. The general idea is to
work with Claude the same way you would with a teammate: you tag Claude in a channel and delegate a task using
the context available there.

Let's look at some examples Anthropic showed.

## Execute shared work

### Coding and raising a PR through chat

![Source: x.com @claudeai](/assets/img/posts/the-next-stage-of-llm-ui-ux/coding-request.png)

Source: [@claudeai on X](https://x.com/claudeai/status/2069468696083349701)

You can ask Claude to implement a feature using channel conversations and connected tools it has access to.
In Anthropic's example, Claude builds it, opens a PR, and finally merges it after human approval.

![Source: x.com @claudeai](/assets/img/posts/the-next-stage-of-llm-ui-ux/pr-approval.png)

Source: [@claudeai on X](https://x.com/claudeai/status/2069468693017268244)

It can also notify another relevant channel after a change.

![Source: x.com @claudeai](/assets/img/posts/the-next-stage-of-llm-ui-ux/channel-notification.png)

Source: [@claudeai on X](https://x.com/claudeai/status/2069468693017268244)

### Investigating incidents

If incident alerts appear in a channel Claude can access, it can investigate and, depending on its tools and
permissions, propose or implement a fix.

![Claude investigating an incident from a Slack alert](/assets/img/posts/the-next-stage-of-llm-ui-ux/incident-investigation.png)

Source: [ClaudeDevs on X](https://x.com/ClaudeDevs/status/2069468902216945939)

## Watch and follow up

### Monitoring metrics

You can point Claude at an A/B test and provide a primary metric to watch along with guardrail metrics that
should stay stable. In Anthropic's example, the guardrails are average order value (AOV) and the API error rate.

![Claude monitoring an A/B test and its guardrail metrics](/assets/img/posts/the-next-stage-of-llm-ui-ux/monitoring-ab-tests.png)

Source: [ClaudeDevs on X](https://x.com/ClaudeDevs/status/2069468911700218284)

You can also use it as a background watcher to notify the team when a defined threshold is
crossed. Anthropic shows an example of CI checks that have been failing for a specified time. Compared to a
regular monitoring system, such as a dashboard with alerts, Claude can use the connected code and conversation context
to investigate a failure, identify a likely culprit, and propose a fix in the same thread.

![Claude watching for a CI failure threshold](/assets/img/posts/the-next-stage-of-llm-ui-ux/background-monitoring-ci-1.png)

![Claude reporting the CI failure and likely cause](/assets/img/posts/the-next-stage-of-llm-ui-ux/background-monitoring-ci-2.png)

Source: [ClaudeDevs on X](https://x.com/ClaudeDevs/status/2069468909858873779)

### Queuing execution after another task has completed

You can give Claude work that depends on another event. In Anthropic's example, it waits for the backend work to finish
before starting the related frontend task.

![Claude waiting for a backend deployment before starting dependent frontend work](/assets/img/posts/the-next-stage-of-llm-ui-ux/queuing-execution.png)

Source: [ClaudeDevs on X](https://x.com/ClaudeDevs/status/2069468906214007035)

## Turn conversations into artifacts

### Creating and updating documentation

Claude can create or update documentation based on conversations in channels it can access. Anthropic shows an
example of Claude creating a post-mortem for an incident that was resolved by several team members.

![Claude turning an incident thread into a postmortem](/assets/img/posts/the-next-stage-of-llm-ui-ux/incident-post-mortem.png)

Source: [ClaudeDevs on X](https://x.com/ClaudeDevs/status/2069468908026020170)

## The death of agent CLIs?

I like this way of interacting with Claude. It feels like Claude is a real teammate (a
really smart one who also never gets tired). However, this does not make agent CLIs like Claude Code
obsolete. Anthropic says that
["Claude Code is still the fastest way to do solo, synchronous work. Claude Tag is Claude Code made multiplayer, async, and proactive across your whole team."](https://x.com/ClaudeDevs/status/2069468913264644419)

On the customer side, I believe that many companies will struggle to use Claude Tag as broadly as Anthropic does.
Anthropic provides controls for channel scope, tool access, spend, and activity logging, but customers still need
to decide who may delegate which actions, who is accountable for the result, and which workflows are reliable
enough to let Claude handle them autonomously. On top of that, using Claude across large volumes of conversations
daily plus code and documentation lookups can quickly produce a considerable token bill.
Anthropic claims that [65% of their product team's code, including most of what built Claude Tag itself](https://x.com/ClaudeDevs/status/2069468900216234010),
is now being created with Claude Tag. However, Anthropic is a very favorable environment for Claude Tag:
it controls the product, can integrate it deeply into its workflows, and can improve it when it falls short.
Companies with older systems and less integrated tooling may not see the same results.

Is it just marketing, then? Partly. Anthropic shows a polished Slack demo with features that are
easy to understand and provide clear enterprise value. However, Claude Tag's value can only be realized by having
a strong support system behind it: scoped access controls, reliable tools, clear approval boundaries, an
organized knowledge base, and workflows that an agent can safely continue without constant human supervision.
I am excited by the direction Anthropic is taking and will continue following the team to see how they plan
to make Claude Tag more widely available.
