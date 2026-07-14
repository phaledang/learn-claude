# Learn from This Page: **Being Specific (Prompt Engineering)**

**Source:** Anthropic Partners Skilljar Course – *Claude with Amazon Bedrock → Prompt Engineering → Being specific* [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

# Key Concepts

## Why Being Specific Matters

One of the most effective ways to improve Claude's output is to provide clear and specific instructions rather than leaving everything open to interpretation. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

Example:

**Vague Prompt**

> Write a short story about a character who discovers a hidden talent.

Possible issues:

* Could be 200 words or 2,000 words
* May introduce many characters
* Story structure is unpredictable
* Output quality varies [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

**Specific Prompt**

* Limit length
* Define structure
* Specify required content
* Add process steps

Result:

* More consistent responses
* Higher quality outputs
* Better alignment with user expectations [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

# Two Types of Guidelines

## 1. Quality Guidelines

Quality guidelines describe **what the final output should look like**. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

Common examples:

### Length Constraints

* Keep under 1,000 words
* Generate exactly 5 bullet points
* Write a 200-word summary [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Structural Requirements

* Include a conclusion
* Use headings
* Include a clear action scene [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Content Requirements

* Include supporting characters
* Mention risks and mitigations
* Provide examples [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Key Idea

Quality guidelines control the **shape and quality** of the response. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

## 2. Process Steps

Process steps describe **how Claude should think through the problem**. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

Example process:

1. Brainstorm 3 talents
2. Select the most interesting one
3. Outline the reveal scene
4. Create supporting characters that strengthen the story [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Benefits

* Encourages systematic reasoning
* Reduces skipped steps
* Improves complex problem solving
* Produces more reliable results [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Key Idea

Process steps control **the path Claude takes** to reach the answer. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

# Real-World Example: Meal Planning

The course shows a meal-planning prompt with clear requirements:

### User Inputs

* Height
* Weight
* Goal
* Dietary restrictions [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Quality Guidelines

1. Include daily calories
2. Show protein, fat, and carbohydrates
3. Specify meal timing
4. Use foods that meet restrictions
5. List portions in grams
6. Keep budget-friendly when requested [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Results

The evaluation score improved:

| Prompt Type               | Score |
| ------------------------- | ----- |
| Baseline prompt           | 3.92  |
| Prompt with guidelines    | 7.86  |
| Prompt with process steps | 7.3   |

The guideline-enhanced prompt more than doubled the evaluation score. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

# When to Use Process Steps

Process steps are especially valuable for:

## Troubleshooting

Example:

* Diagnose system failures
* Investigate bugs
* Find root causes [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

## Decision Making

Example:

* Vendor selection
* Architecture choices
* Technology comparisons [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

## Critical Thinking

Example:

* SWOT analysis
* Risk assessment
* Trade-off analysis [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

## Complex Analysis

The course gives an example:

> Analyze why a sales team experienced a 30% decline in performance.

Instead of accepting the first explanation, process steps can force Claude to examine:

* Market conditions
* Individual performance
* Organizational changes
* Customer feedback [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

# Best Practices

### Use Quality Guidelines When

* Formatting matters
* Outputs must meet standards
* Consistency is important
* Creating reports, stories, summaries, or plans [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Use Process Steps When

* The task is complex
* Analysis is needed
* Multiple factors must be evaluated
* You want deeper reasoning [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Use Both Together

The strongest prompts often combine:

1. Desired output requirements
2. Step-by-step reasoning instructions [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

# Prompt Template

```text
Task:
[What you want Claude to do]

Quality Guidelines:
1. ...
2. ...
3. ...

Process Steps:
1. ...
2. ...
3. ...

Output Format:
[table, markdown, JSON, bullets, etc.]
```

***

# Q\&A

### Q1. What is the main idea of being specific in prompts?

**Answer:** Give Claude clear guidance instead of leaving decisions entirely up to the model. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Q2. What are the two types of guidelines?

**Answer:** Quality Guidelines and Process Steps. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Q3. What do Quality Guidelines control?

**Answer:** The desired characteristics of the final output such as structure, length, and content. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Q4. What do Process Steps control?

**Answer:** The reasoning path Claude takes to produce the output. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Q5. When should you use Process Steps?

**Answer:** During troubleshooting, decision making, critical thinking, and complex analysis. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Q6. Why do specific prompts perform better?

**Answer:** They produce more consistent, predictable, and higher-quality results. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Q7. What meal-plan requirements were included in the example?

**Answer:** Calories, macros, meal timing, dietary restrictions, portion sizes, and budget considerations. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

### Q8. Which approach achieved the highest evaluation score?

**Answer:** The prompt using detailed quality guidelines scored 7.86. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

# Quiz

## Multiple Choice

### 1. What is the primary benefit of being specific in prompts?

A. Reduce token cost only  
B. Improve consistency and quality  
C. Increase model size  
D. Improve internet speed

✅ **Answer: B** [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

### 2. Which guideline type controls the final output characteristics?

A. Process Steps  
B. Temperature Settings  
C. Quality Guidelines  
D. Streaming

✅ **Answer: C** [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

### 3. Which guideline type controls the reasoning process?

A. Process Steps  
B. Length Constraints  
C. Examples  
D. System Prompts

✅ **Answer: A** [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

### 4. Which task benefits most from process steps?

A. Generating a simple title  
B. Choosing a font color  
C. Root cause analysis  
D. Translating one sentence

✅ **Answer: C** [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

### 5. What was the improved score achieved using quality guidelines in the meal-plan example?

A. 3.92  
B. 5.10  
C. 7.30  
D. 7.86

✅ **Answer: D** [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

***

# References

1. Anthropic Partners Skilljar – *Claude with Amazon Bedrock* → Prompt Engineering → *Being Specific*. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)
2. Concepts covered:
   * Quality Guidelines
   * Process Steps
   * Prompt Evaluation
   * Systematic Reasoning
   * Prompt Engineering Best Practices [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)

## Exam Tips

Remember:

**Specific Prompt = Task + Quality Guidelines + Process Steps + Output Format**

This formula consistently produces more reliable results and is a core prompt-engineering principle for Claude, Amazon Bedrock, and other LLMs. [\[Being specific\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276745)
