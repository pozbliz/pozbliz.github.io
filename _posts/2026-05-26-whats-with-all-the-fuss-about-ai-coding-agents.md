---
layout: post
title: "What's with all the fuss about AI coding agents?"
date: 2026-05-26
excerpt: "An introduction to AI coding agents for readers familiar with ChatGPT, explaining how agents use files, commands, CLIs, and tools to work closer to real workflows."
subtitle: "Why AI coding agents are different from normal chat tools, and why they are worth learning."
categories: [agents]
tags: [coding-agents, ai-agents, cli, codex]
---

This is a post for readers who have used ChatGPT (or similar tools) but are still wondering what makes AI coding agents 
worth learning.
Even though we call them **coding** agents, these tools are not only useful for people writing code. I will start with 
the coding case because it makes the difference easier to see. Later, I will show why the same ideas can also be 
applied to non-coding tasks.

## What is an AI agent?

"An AI agent, also called *agentic AI*, can pursue goals, use tools, and take actions with varying degrees of autonomy. 
In practice, agents usually operate within human-defined objectives, constraints, and available tools."
(See [Wikipedia: AI agent](https://en.wikipedia.org/wiki/AI_agent)).
In simple words: an AI agent works toward a goal using tools and taking actions within limits set by a human.

## What is an AI coding agent?

"Coding agents are a subset of AI agents specifically designed to help developers with coding tasks."
(See [GitHub Resources: What are AI agents?](https://github.com/resources/articles/what-are-ai-agents)).
However, the same features that make these agents useful for coding also make them useful for other 
software work: reading project files, running commands, checking errors, and iterating on the result. 

## Which AI coding agents are people using?

Some examples you might have heard about:

- Claude Code
- Codex
- Cursor
- Windsurf
- Devin
- GitHub Copilot coding agent

This list mixes a few product types: terminal-based agents, AI-first editors, hosted coding agents, and agent features 
inside larger developer tools. The common thread is that they can inspect a project, use tools and make changes with 
a user-defined level of autonomy.

## On CLIs, shells and terminals

When you use software by clicking with your mouse, you use its graphical user interface (GUI). However, that is not the 
only way to control software.

A **command line interface (CLI)** is a text-based alternative to a GUI. You control software by typing 
commands instead of clicking buttons. Examples: `echo hello`, `git status`.

A **shell** is a program that interprets and runs your text commands. Examples: `bash`, `Windows PowerShell`.

A **terminal** is the window that lets you interact with a shell. Example: `Windows Terminal`.

## Why CLIs matter for agents

Most coding-agent workflows did not become useful because they clicked through GUIs like a human. Instead, they work 
through text-based tools: files, commands, logs, tests and CLIs.

*There is a separate area called* computer use *where AI agents interact with a GUI by clicking, typing, and reading 
the screen. That is worth its own post. For this article, I will focus on text-based work through a CLI.*

A CLI gives an AI agent a text-based way to control software without needing to click through the GUI. In some tools, 
the CLI even exposes advanced features that are not available from the GUI. For me, understanding what is 
possible through a CLI made the value of coding agents much easier to understand: they can operate in the same 
text-based environment where many real workflows already happen.

Here is a simple example: comparing ChatGPT as a conversational chat interface with Codex as a CLI tool running 
from the terminal. Let's say we want to summarize a text document and save the summary to a new file.

In a normal ChatGPT chat, I have two options: I can either copy and paste the text into the chat window, or I can 
upload the file so that it becomes available in that chat session. Then I can prompt the AI to create a summary in the 
desired format. I can iterate and have it rewrite the summary until I am happy with the output. Then, I copy and 
paste the summary into a new file and save it. 

On the other hand, I start Codex from the terminal on my PC by typing `codex`. As before, I can write a prompt 
asking it to take the input document, summarize it, and save the summary to a new file. I will need to specify which 
input document it should use. I can point it to the exact file name, or give it part of the file name and ask it 
to find the right file. Let's look at some of the steps the AI might perform in order to find the target file:

_Note: I will use bash commands for my examples._

1. Check which folder we are currently in
   ```
   pwd
   ```

2. List the files in this folder
   ```
   ls
   ```

3. Move into a likely folder
   ```
   cd Documents
   ```

4. Search for text documents with "example" in the filename
   ```
   find . -type f -iname "*example*.txt"
   ```

5. Or search for all text documents if I do not remember the name
   ```
   find . -type f -iname "*.txt"
   ```

Once it finds the right file, it can read it, create the summary, and save the summary to a new file.

Even for a single file, the Codex workflow is simpler because it saves me the manual copy-pasting.
Now, imagine the difference if we want to summarize not just one file, but one hundred files. With Codex, I can 
point it to a folder with all the input files and prompt: "For each file in input/, create a separate summary document 
in output/." Then I can let it work through the folder and review the output when it is done.

## Further possibilities

The example above just showed some basic commands for navigation and file manipulation.
Let's look at what is possible when using other tools and CLIs:

- **AWS CLI**: Deploy or manage AWS resources.
- **PostgreSQL CLI (psql)**: Query a database.
- **Python scripts**: Write and execute scripts.
- **Slack CLI or API tooling**: Send messages to Slack.
- **curl**: Access website content, download files.
- **ffmpeg**: Process video and audio.

With tools like these, an agent is not limited to local files. If it has the right credentials and permissions, it can 
also interact with external systems.
That is the key shift: the useful part is not only that it can write code, but that it can use the same 
text-based tools to execute complex workflows.

Depending on the tool and setup, coding agents can:
- read surrounding files to understand the project context,
- create, move, edit, or delete many files at once,
- run multi-step workflows,
- preserve memory of important knowledge or the current state,
- iterate until a defined result is reached,
- run multiple tasks in parallel,
- connect to external tools through CLIs, APIs, or integrations.

Two ideas I want to unpack in future posts are stateful agents and goal-driven workflows, including the /goal command.

Some personal office productivity use cases I have heard people describe:

- categorizing incoming emails by urgency,
- drafting replies based on previous conversations,
- summarizing Slack threads and extracting action items,
- creating follow-up reminders when there is no reply after a set number of days,
- reviewing writing against specific style, tone, and clarity rules.

## Conclusion

I hope the difference is clearer now. Compared with a normal chat interface, coding agents 
work much closer to the files, tools, and workflows where the actual task happens. There are 
many more useful examples I have not mentioned here. The main pattern is that any workflow that 
can be expressed through files, commands, APIs, or repeatable steps is a good candidate for 
trying an AI agent. For my own AI learning, coding agents have become one of the main areas 
I want to understand better because they have already proved useful in my workflows. These 
tools are also evolving quickly, with new features and slash commands appearing all the time. 
I want to use future posts to unpack the features and workflows that seem genuinely useful: what 
they do, when to use them, and where they might still fall short.
