# A typical eval workflow

**Source:**  
[A typical eval workflow](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276732)

***

# Key Concepts

## What is a Prompt Evaluation Workflow?

A prompt evaluation (eval) workflow is a **systematic and objective process** used to measure and improve prompt quality.

### Why use evaluations?

* Avoid relying on subjective opinions.
* Measure prompt performance consistently.
* Compare different prompt versions.
* Continuously improve prompt effectiveness.

***

## Step 1: Draft Your Initial Prompt

Start with a simple baseline prompt.

Example:

```python
prompt = f"""
Please answer the user's question:
{question}
"""
```

### Purpose

* Establish an initial version.
* Create a baseline for comparison.
* Measure future improvements against this version.

***

## Step 2: Create an Evaluation Dataset

Build a collection of test inputs.

Example dataset:

1. What's 2+2?
2. How do I make oatmeal?
3. How far away is the Moon?

### Dataset Characteristics

* Can be created manually.
* Can be generated using Claude.
* Should represent real-world usage scenarios.
* May contain:
  * Tens of examples
  * Hundreds of examples
  * Thousands of examples

### Best Practice

The dataset should:

* Cover common use cases.
* Include edge cases.
* Reflect actual user questions.

***

## Step 3: Feed Through Claude

For each dataset item:

1. Insert the question into the prompt template.
2. Send the complete prompt to Claude.
3. Collect the response.

Example:

**Input**

```text
What's 2+2?
```

**Generated Prompt**

```text
Please answer the user's question:
What's 2+2?
```

**Output**

```text
2 + 2 = 4
```

Repeat for every record in the dataset.

***

## Step 4: Feed Through a Grader

This is the most important evaluation stage.

The grader receives:

* The question
* Claude's answer

Then assigns a quality score.

### Sample Scoring Scale

| Score | Meaning           |
| ----- | ----------------- |
| 10    | Perfect answer    |
| 4     | Needs improvement |
| 1     | Poor or incorrect |

Example scores:

| Question      | Score |
| ------------- | ----- |
| 2+2           | 10    |
| Oatmeal       | 4     |
| Moon Distance | 9     |

### Calculate Overall Performance

```text
(10 + 4 + 9) / 3 = 7.66
```

Result:

**Baseline Score = 7.66**

***

## Step 5: Change Prompt and Repeat

Improve the prompt.

Example:

```python
prompt = f"""
Please answer the user's question:
{question}

Answer the question with ample detail
"""
```

Run the same evaluation pipeline again.

### Compare Results

| Version   | Score |
| --------- | ----- |
| Prompt V1 | 7.66  |
| Prompt V2 | 8.7   |

Result:

✅ Prompt V2 performs better.

***

# Prompt Iteration Cycle

```text
Create Prompt
        ↓
Build Dataset
        ↓
Run Model
        ↓
Grade Responses
        ↓
Calculate Score
        ↓
Improve Prompt
        ↓
Repeat
```

This cycle enables continuous prompt optimization.

***

# Important Takeaways

### Objective Measurement Matters

Instead of asking:

> "Does this prompt feel better?"

Ask:

> "Did the score improve?"

### Evaluation Requires Three Components

1. Prompt
2. Dataset
3. Grader

### Small to Large Scale

You can start with:

* 3 examples

And eventually scale to:

* Hundreds
* Thousands of test cases

### Iteration is Key

Prompt engineering is not a one-time activity.

The process is:

```text
Test
Measure
Improve
Repeat
```

***

# Q\&A

### Q1. What is the goal of a prompt evaluation workflow?

**Answer:**  
To objectively measure and improve prompt performance using test datasets and grading mechanisms.

***

### Q2. Why is an evaluation dataset needed?

**Answer:**  
The dataset provides representative inputs that allow prompt performance to be tested consistently.

***

### Q3. What does the grader do?

**Answer:**  
The grader evaluates response quality and assigns scores to measure performance.

***

### Q4. Why calculate an average score?

**Answer:**  
It provides a single performance metric that can be compared across prompt versions.

***

### Q5. What happens after obtaining a baseline score?

**Answer:**  
The prompt is modified, re-evaluated, and compared against previous results.

***

### Q6. Why is prompt evaluation better than subjective judgment?

**Answer:**  
Because it uses measurable and repeatable scoring rather than personal opinions.

***

### Q7. What made Prompt V2 better in the example?

**Answer:**  
Adding the instruction:

```text
Answer the question with ample detail
```

improved its average evaluation score.

***

# Quiz

### Question 1

What is the first step in a prompt evaluation workflow?

* A. Run a grader
* B. Create an evaluation dataset
* C. Draft an initial prompt
* D. Calculate average scores

✅ **Answer: C**

***

### Question 2

What is the purpose of an evaluation dataset?

* A. Store prompt scores
* B. Provide test inputs
* C. Store model parameters
* D. Generate embeddings

✅ **Answer: B**

***

### Question 3

Which component assigns quality scores?

* A. Claude
* B. Dataset
* C. Prompt template
* D. Grader

✅ **Answer: D**

***

### Question 4

What score represents a perfect answer?

* A. 1
* B. 4
* C. 10
* D. 100

✅ **Answer: C**

***

### Question 5

What was Prompt V1's score?

* A. 4
* B. 7.66
* C. 8.7
* D. 10

✅ **Answer: B**

***

### Question 6

What was Prompt V2's score?

* A. 8.7
* B. 7.66
* C. 4
* D. 10

✅ **Answer: A**

***

### Question 7

Why repeat the evaluation process after modifying a prompt?

* A. To generate more questions
* B. To compare performance improvements
* C. To retrain Claude
* D. To build embeddings

✅ **Answer: B**

***

### Question 8

Which sequence best represents the workflow?

* A. Grade → Prompt → Dataset
* B. Dataset → Prompt → Model
* C. Prompt → Dataset → Model → Grader → Improve
* D. Model → Improve → Dataset

✅ **Answer: C**

***

# Exam Tips (Anthropic / Bedrock)

Remember this formula:

```text
Prompt
 + Dataset
 + Model Run
 + Grader
 + Score
 + Iteration
 = Prompt Evaluation Workflow
```

Key principle:

> **Prompt engineering without evaluation is guessing. Prompt engineering with evaluation is measurement-driven optimization.**
