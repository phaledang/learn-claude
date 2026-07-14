# Learn from This Page: Prompt Engineering (Claude with Amazon Bedrock)

**Source:**  
Prompt Engineering lesson from Claude with Amazon Bedrock course (Anthropic Partners Skilljar)  
Page: *Prompt engineering* [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Key Concepts

## What is Prompt Engineering?

Prompt engineering is the process of **improving prompts iteratively** to obtain:

* More reliable outputs
* Higher-quality responses
* Better consistency
* Measurable performance improvements

Instead of writing a prompt once and hoping it works, you continuously refine and evaluate it. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# The Iterative Improvement Process

Prompt engineering follows a cycle:

```text
Set Goal
   ↓
Write Initial Prompt
   ↓
Evaluate Performance
   ↓
Apply Prompting Technique
   ↓
Re-evaluate
   ↓
Repeat
```

The objective is to make prompt optimization a measurable engineering process rather than relying on intuition. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Example Use Case: Athlete Meal Planner

The lesson uses a practical example:

Generate a **1-day meal plan** for athletes based on:

* Height
* Weight
* Fitness goal
* Dietary restrictions

Example inputs:

```python
{
  "height": "Athlete's height in cm",
  "weight": "Athlete's weight in kg",
  "goal": "Goal of the athlete",
  "restrictions": "Dietary restrictions"
}
```

The model generates a customized meal plan using these parameters. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Setting Up an Evaluation Pipeline

Instead of manually judging responses, the lesson introduces a `PromptEvaluator` class.

Example:

```python
evaluator = PromptEvaluator(
    max_concurrent_tasks=5
)
```

Purpose:

* Generate test cases
* Run prompt evaluations
* Grade model outputs
* Compare prompt versions

Tip:

* Start with low concurrency (e.g., 3)
* Increase gradually to avoid API rate-limit issues [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Generating Test Datasets

Evaluation requires representative test cases.

Example:

```python
dataset = evaluator.generate_dataset(
    task_description=
        "Write a compact, concise 1 day meal plan for a single athlete",

    prompt_inputs_spec={
        "height": "Athlete's height in cm",
        "weight": "Athlete's weight in kg",
        "goal": "Goal of the athlete",
        "restrictions": "Dietary restrictions"
    },

    num_cases=3
)
```

Benefits:

* Standardized testing
* Repeatable benchmarking
* Easier comparison between prompt versions [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Start with a Baseline Prompt

Don't attempt to create the perfect prompt immediately.

Example initial prompt:

```python
What should this person eat?

- Height: ...
- Weight: ...
- Goal: ...
- Dietary restrictions: ...
```

A simple prompt provides a baseline score against which improvements can be measured. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Running Evaluations

The evaluator measures prompt quality against desired criteria.

Example:

```python
results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset.json",
    extra_criteria="""
    The output should include:
    - Daily caloric total
    - Macronutrient breakdown
    - Meals with exact foods,
      portions, and timing
    """
)
```

Evaluation criteria clearly communicate expectations to the grader. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Reviewing Results

The evaluation produces:

```text
output.html
```

The report contains:

* Scores
* Reasoning
* Model outputs
* Per-test-case analysis

This helps identify:

* Weaknesses
* Missing requirements
* Areas for prompt improvement [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Important Mindset: Measure Before Optimizing

A major lesson:

> Low initial scores are expected.

The example baseline prompt scored:

```text
2.3 / 10
```

This is valuable because it establishes a measurable starting point for future improvements. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Prompt Engineering Techniques Mentioned

The lesson previews several optimization strategies:

## 1. Be Clear and Direct

Tell the model exactly what you want.

***

## 2. Be Specific

Define:

* Output format
* Constraints
* Required details

***

## 3. Structure Prompts

Use structured formats such as:

```xml
<requirements>
...
</requirements>
```

***

## 4. Provide Examples

Show desired input/output examples (few-shot prompting).

***

## 5. Re-evaluate

Verify improvement using objective measurements. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Practical Prompt Engineering Framework

```text
1. Define Goal
2. Build Test Dataset
3. Create Baseline Prompt
4. Evaluate
5. Analyze Results
6. Apply Improvement Technique
7. Reevaluate
8. Repeat Until Target Quality Is Reached
```

This is essentially an AI version of:

```text
Plan
→ Test
→ Improve
→ Validate
```

 [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Q\&A

### Q1. What is prompt engineering?

**Answer:**  
Prompt engineering is the process of systematically improving prompts to obtain more reliable and higher-quality AI outputs. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

### Q2. Why should you evaluate prompts?

**Answer:**  
Evaluation provides measurable evidence that prompt changes improve output quality. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

### Q3. Why generate a dataset?

**Answer:**  
To test prompts consistently across multiple representative scenarios. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

### Q4. Why start with a simple prompt?

**Answer:**  
A simple prompt establishes a baseline for comparison and improvement. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

### Q5. Why use extra evaluation criteria?

**Answer:**  
To ensure outputs contain required information and meet quality expectations. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

### Q6. Why shouldn't low initial scores discourage you?

**Answer:**  
Because the goal is continuous improvement, and the baseline provides a measurable starting point. [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

### Q7. What file contains detailed evaluation results?

**Answer:**  
`output.html` [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

***

# Quiz

## Question 1

What is the primary purpose of prompt engineering?

A. Reduce API costs only  
B. Improve prompts to obtain better outputs  
C. Train foundation models  
D. Replace evaluations

✅ **Answer: B**

***

## Question 2

Which step comes immediately after writing an initial prompt?

A. Train a new model  
B. Deploy to production  
C. Evaluate performance  
D. Fine-tune the model

✅ **Answer: C**

***

## Question 3

Why generate a test dataset?

A. To improve model weights  
B. To benchmark prompt performance consistently  
C. To reduce inference latency  
D. To replace human evaluation

✅ **Answer: B**

***

## Question 4

Which is an example of evaluation criteria?

A. Increase GPU memory
B. Daily caloric total
C. Upgrade API version
D. Increase token limit

✅ **Answer: B**

***

## Question 5

The lesson's initial meal-plan prompt scored approximately:

A. 8.5/10  
B. 5.0/10  
C. 2.3/10  
D. 9.2/10

✅ **Answer: C**

***

## Question 6

Which prompt-improvement technique is mentioned?

A. Quantization
B. Distillation
C. XML structuring
D. Transfer learning

✅ **Answer: C**

***

## Question 7

Why use iterative prompt engineering?

A. Because the first prompt is always perfect
B. Because improvements should be measured and validated
C. Because models cannot follow instructions
D. To avoid evaluations

✅ **Answer: B**

***

# References

* Prompt Engineering lesson, Claude with Amazon Bedrock Course [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)
* Topics referenced in the course:
  * Prompt evaluation
  * Dataset generation
  * Model-based grading
  * Structured prompting
  * Examples/few-shot prompting
  * Systematic prompt optimization [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)

## Key Takeaway

**Prompt engineering is not prompt writing—it's prompt improvement.**

The professional workflow is:

```text
Goal
→ Dataset
→ Baseline Prompt
→ Evaluation
→ Improvement
→ Re-evaluation
→ Repeat
```

Treat prompts like software: **measure, test, and iterate.** [\[vinvoice.v...ice-search\]](https://vinvoice.viettel.vn/utilities/invoice-search)
