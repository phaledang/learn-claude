# Using Subagents Effectively

## Sources:
**"Using subagents effectively"**. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# Core Idea

The key decision is:

> **Does the intermediate work matter?**

* If only the **final result** matters → use a **subagent**
* If the process and discoveries matter and influence subsequent steps → keep the work in the **main thread** [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# When Subagents Shine

Subagents are most effective when:

* The exploration is separate from execution
* The main thread only needs the outcome
* Intermediate investigation would clutter context
* A fresh perspective is beneficial
* A custom system prompt is needed [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### Good Characteristics

✅ Need a result, not a step-by-step history

✅ Exploratory work would consume too much context

✅ Task benefits from specialized instructions

✅ Task can be summarized cleanly afterwards [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# Use Case 1: Research Tasks

Research is presented as the **classic subagent use case**. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

Example:

Instead of your main thread:

* Opening dozens of files
* Tracing function calls
* Exploring multiple code paths

A research subagent performs all exploration and returns:

> JWT validation happens in middleware/auth.js line 42, called from the Express router in route/api.js [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### Benefit

Main thread receives:

* Concise findings
* No investigation noise
* Preserved context window [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# Use Case 2: Code Reviews

Subagents can perform better code reviews because they review code from a **separate context**. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

Problem:

* Main thread helped create the code
* Harder to objectively review work it participated in creating

Solution:

* Reviewer subagent runs separately
* Reads git diff
* Reviews changed files
* Applies review criteria independently [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### Additional Advantage

Review standards can be embedded in the subagent's system prompt:

* Coding standards
* Security rules
* Team review policies

Result:

* More consistent reviews across the team [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# Use Case 3: Custom System Prompts

Claude Code's default prompt is optimized for:

* Concise responses
* Technical work
* Coding tasks [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

Sometimes a different prompt is better.

## Example: Copywriting Agent

Custom instructions:

* Tone
* Audience
* Writing style
* Marketing voice

Why?

Default coding-oriented behavior is not ideal for:

* Landing pages
* Product marketing
* Email campaigns [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

## Example: Styling Agent

Custom instructions:

* Design system
* Color variables
* Component patterns
* Spacing conventions

The subagent loads these resources before working. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### Benefit

The subagent already understands:

* Brand styles
* UI conventions
* CSS patterns

before writing code. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# When Subagents Hurt

Launching a subagent creates overhead:

* Less visibility into the process
* Details compressed into summaries
* Potential information loss

Use a subagent only when it provides a real advantage. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# Anti-Pattern 1: "Expert" Subagents

Examples:

* "Python Expert"
* "Kubernetes Specialist"

According to the course, these usually add no value. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

Reason:

Claude already possesses that knowledge.

A separate expert persona typically cannot do anything that the main thread could not do directly. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# Anti-Pattern 2: Sequential Pipelines

Bad example:

1. Reproduce bug agent
2. Debug bug agent
3. Fix bug agent

Problem:

Each step depends on discoveries from the previous step. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

Consequences:

* Information loss during handoff
* Reduced effectiveness
* Broken reasoning chain

The page notes that bug fixing almost always suffers from this issue. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# Anti-Pattern 3: Test Runner Subagents

Example:

A subagent runs tests and returns:

> Tests failed

Problem:

The detailed output is hidden.

Developers often need:

* Stack traces
* Error messages
* Logs
* Full test results

for debugging. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

The course explicitly states that testing showed the test-runner pattern performed worse among configurations evaluated. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# The Decision Rule

Ask:

> Does the intermediate work matter? [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### If NO

Use a subagent.

Examples:

* Research
* Exploration
* Code review
* Specialized writing
* Styling/design tasks [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### If YES

Keep it in the main thread.

Examples:

* Debugging
* Multi-step reasoning
* Test execution analysis
* Any task requiring continuous human observation and adjustment [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# Exam Notes (Important)

### Good Uses of Subagents

✅ Research and exploration

✅ Code reviews

✅ Tasks requiring custom system prompts [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### Bad Uses of Subagents

❌ Expert personas

❌ Sequential agent pipelines

❌ Test runners hiding output [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

***

# Quick Quiz

### Q1

What question should be asked before creating a subagent?

**Answer:** Does the intermediate work matter? [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### Q2

Why are research tasks a strong subagent use case?

**Answer:** The main thread usually needs just the findings, not the entire exploration process. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### Q3

Why can code-review subagents provide better feedback?

**Answer:** They review code from a separate context and are not influenced by the history of creating the code. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### Q4

Why are "expert" subagents discouraged?

**Answer:** Claude already has the expertise, so the extra agent usually adds no real capability. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### Q5

Why are sequential bug-fixing pipelines discouraged?

**Answer:** Important information can be lost when discoveries are passed between agents. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

### Q6

Why are test-runner subagents often harmful?

**Answer:** They hide detailed test output that is needed for debugging. [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)

# One-Sentence Summary

**Use subagents for independent exploration that can be summarized; avoid them when intermediate reasoning, debugging details, or sequential discoveries must remain visible.** [\[Using suba...ffectively\]](https://anthropic.skilljar.com/introduction-to-subagents/450701)
