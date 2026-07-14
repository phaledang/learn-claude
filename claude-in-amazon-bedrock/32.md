# Learn from This Page: **Being Clear and Direct** (Claude Prompt Engineering)

## Source

* Course: *Claude with Amazon Bedrock*
* Page: **Being clear and direct**
* URL: [Being clear and direct](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743) [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

# Key Concepts

## Why the First Line Matters

The first line of a prompt is the most important part of the request because it sets the context and direction for everything that follows. A well-written opening line can significantly improve the quality of Claude's response. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Goals of the First Line

* Establish the task immediately.
* Remove ambiguity.
* Tell Claude exactly what needs to be done.
* Make expectations clear from the start. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

## Principle 1: Be Clear

Being clear means:

* Use simple and understandable language.
* State exactly what you want.
* Avoid unnecessary words.
* Lead with a straightforward description of the task. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Weak Example

Instead of:

> "I need to know about those things people put on their roofs that use sun—those solar panel things, I think they're called."

Use:

> "Write three paragraphs about how solar panels work." [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Why It Works

The improved prompt:

* Identifies the topic.
* States exactly what to produce.
* Defines the expected format. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

## Principle 2: Be Direct

Being direct means:

* Use instructions rather than questions.
* Start with action verbs.
* Clearly specify the desired outcome. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Recommended Action Verbs

* Write
* Create
* Generate
* Identify
* Summarize
* Explain
* Analyze [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Weak Example

Instead of:

> "I was reading about renewable energy and geothermal energy sounds neat. What countries use it?"

Use:

> "Identify three countries that use geothermal energy. Include generation stats for each." [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Why It Works

The revised prompt specifies:

* The task (Identify)
* Quantity (three countries)
* Required data (generation statistics) [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

## Practical Example

### Weak Prompt

> "What should this person eat?" [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Improved Prompt

> "Generate a one-day meal plan for an athlete that meets their dietary restrictions." [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Information Provided Clearly

The improved prompt communicates:

| Element     | Value                |
| ----------- | -------------------- |
| Action      | Generate             |
| Output      | Meal plan            |
| Duration    | One day              |
| Audience    | Athlete              |
| Constraints | Dietary restrictions |

This improvement increased the evaluation score from **2.32** to **3.92**. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

# Best Practices Checklist

When writing prompts:

✅ Start with a strong action verb

✅ Use instructions instead of questions

✅ State the exact task

✅ Specify output format

✅ Include constraints and requirements

✅ Remove unnecessary context

✅ Avoid vague language

✅ Make success criteria obvious [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

# Prompt Formula

A useful template:

```text
<Action Verb> + <Specific Task> + <Output Format> + <Constraints>
```

### Examples

```text
Write a 300-word summary of Agile project management.
```

```text
Generate a one-day meal plan for an athlete with a gluten-free diet.
```

```text
Identify three countries that use geothermal energy and include generation statistics.
```

```text
Create a comparison table of Scrum, Kanban, and XP.
```

***

# Q\&A

### Q1. Why is the first line of a prompt important?

Because it sets the direction and expectations for the entire interaction, significantly influencing output quality. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Q2. What does "being clear" mean?

Using simple language and explicitly stating what you want Claude to do. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Q3. What does "being direct" mean?

Giving instructions and starting with clear action verbs rather than asking vague questions. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Q4. Why are action verbs useful?

They immediately communicate the expected task and make the model's job easier. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Q5. Which prompt is better?

A:

> "Can you tell me about solar energy?"

B:

> "Write three paragraphs explaining how solar panels work."

**Answer:** B, because it is clearer and more direct. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Q6. What information should a good prompt contain?

* Task
* Desired output
* Constraints
* Required details
* Format expectations [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

### Q7. What improvement was shown in the example?

The evaluation score increased from 2.32 to 3.92 after making the prompt clearer and more direct. [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

# Quiz

## Question 1

Which prompt follows the "clear and direct" principle best?

A. Tell me about that sun energy stuff.

B. What do you know about solar energy?

C. Write three paragraphs explaining how solar panels work.

D. Solar panels? Thoughts?

**Answer:** ✅ C [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

## Question 2

Which action verb is recommended?

A. Maybe

B. Wonder

C. Generate

D. Curious

**Answer:** ✅ C [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

## Question 3

What should you use instead of questions when possible?

A. Hints

B. Assumptions

C. Instructions

D. Stories

**Answer:** ✅ C [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

## Question 4

Which prompt is more direct?

A.

```text
I was reading about geothermal energy. What countries use it?
```

B.

```text
Identify three countries that use geothermal energy. Include generation statistics.
```

**Answer:** ✅ B [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

## Question 5

What is a key benefit of being clear and direct?

A. Longer prompts

B. Better output quality

C. More complex wording

D. More background information

**Answer:** ✅ B [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

***

## Question 6

Which prompt template is recommended?

A.

```text
Task + Task + Task
```

B.

```text
Question + Question
```

C.

```text
Action Verb + Task + Output Format + Constraints
```

D.

```text
Context only
```

**Answer:** ✅ C

***

# Key Takeaway

> **Start your prompt with a clear action verb, explicitly state the task, define the expected output, and include any constraints. Claude performs best when it receives clear, direct instructions rather than vague or conversational requests.** [\[Being clea...and direct\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276743)

## Quick Reference

```text
❌ What should this person eat?

✅ Generate a one-day meal plan for an athlete that meets their dietary restrictions.
```

```text
❌ What countries use geothermal energy?

✅ Identify three countries that use geothermal energy. Include generation statistics for each.
```

````text
❌ Tell me about solar panels.

✅ Write three paragraphs explaining how solar panels work.
``` 【1-7ddec6】
````
