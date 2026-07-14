# Learn from This Page: Running the Eval (Claude with Amazon Bedrock)

**Source:**  
Page: *Running the eval* (Claude with Amazon Bedrock Course) [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

# Key Concepts

## 1. Purpose of an Evaluation (Eval) Pipeline

An evaluation pipeline systematically tests how well an AI model performs against a predefined dataset. The workflow is:

1. Take a dataset of test cases.
2. Combine each test case with a prompt template.
3. Send the prompt to Claude.
4. Grade the model output.
5. Collect and analyze the results. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

### High-Level Flow

```text
Dataset
   ↓
Prompt Template
   ↓
Claude Model
   ↓
Output
   ↓
Grader
   ↓
Results
```

***

## 2. Core Functions in the Evaluation Pipeline

The implementation is built around three functions:

### Function 1: `run_prompt()`

Purpose:

* Accepts a test case.
* Merges it with a prompt template.
* Sends the prompt to Claude.
* Returns Claude's output. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

Example:

```python
def run_prompt(test_case):
    prompt = f"""
    Please solve the following task:
    {test_case["task"]}
    """

    messages = []
    add_user_message(messages, prompt)
    output = chat(messages)

    return output
```

### Notes

* Uses a very simple prompt.
* No formatting instructions are included.
* Outputs may be overly verbose.
* Prompt improvements come later through iteration. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

### Function 2: `run_test_case()`

Purpose:

* Executes a single test case.
* Calls `run_prompt()`.
* Grades the result.
* Returns structured results. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

Example:

```python
def run_test_case(test_case):

    output = run_prompt(test_case)

    # TODO - Grading
    score = 10

    return {
        "output": output,
        "test_case": test_case,
        "score": score
    }
```

### Current Limitation

The page uses:

```python
score = 10
```

as a placeholder.

Real grading logic will be added later. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

### Function 3: `run_eval()`

Purpose:

* Processes the entire dataset.
* Runs each test case.
* Aggregates results into a list. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

Example:

```python
def run_eval(dataset):

    results = []

    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)

    return results
```

### Responsibilities

* Orchestration
* Iteration through test data
* Result collection [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

## 3. Running the Evaluation

Dataset is loaded and processed:

```python
with open("dataset.json", "r") as f:
    dataset = json.load(f)

results = run_eval(dataset)
```

What happens:

1. Load dataset.
2. Execute each test case.
3. Generate outputs.
4. Score outputs.
5. Store results. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

## 4. Performance Considerations

The page notes that:

* Running evaluations can take time.
* Even Claude Haiku may require 30+ seconds for a full dataset.
* Optimization techniques will be covered later. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

### Practical Takeaway

When designing eval systems:

* Expect latency.
* Plan batch processing.
* Consider optimization strategies as dataset size grows.

***

## 5. Inspecting Results

Results can be displayed as formatted JSON:

```python
print(json.dumps(results, indent=2))
```

Output contains:

* Claude output
* Original test case
* Evaluation score [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

Example:

```json
{
  "output": "...",
  "test_case": {
    "task": "..."
  },
  "score": 10
}
```

***

## 6. What Has Been Achieved

The pipeline now supports:

### Test Execution

* Load evaluation dataset
* Run prompts against Claude

### Result Collection

* Capture model responses
* Store outputs consistently

### Evaluation Framework

* Prepare structure for grading
* Enable future prompt optimization

### Scalability

* Process multiple test cases automatically [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

## 7. Key Insight

The course highlights an important lesson:

> Most evaluation systems are built on a relatively simple orchestration pipeline. The real sophistication comes from grading logic and prompt optimization, not from running the test loop itself. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

# Q\&A

### Q1. What is the goal of an evaluation pipeline?

**Answer:**  
To test model performance by running a dataset of test cases through a prompt and grading the results. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

### Q2. What does `run_prompt()` do?

**Answer:**  
It merges a test case with a prompt template, sends it to Claude, and returns the model response. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

### Q3. What does `run_test_case()` do?

**Answer:**  
It runs a prompt, grades the output, and returns the result along with the score. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

### Q4. What does `run_eval()` do?

**Answer:**  
It iterates through the dataset, executes each test case, and collects all results. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

### Q5. Why is the score always 10?

**Answer:**  
Because grading is not implemented yet; the score is a placeholder. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

### Q6. Why might evaluation runs take a long time?

**Answer:**  
Each test case requires a model invocation, and processing many cases can take 30+ seconds even with Claude Haiku. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

### Q7. What is the most important missing component?

**Answer:**  
An intelligent grading system that can determine whether outputs are correct. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

# Quiz

## Question 1

Which sequence correctly represents the evaluation workflow?

A. Prompt → Dataset → Claude → Result  
B. Dataset → Prompt → Claude → Grader → Results  
C. Claude → Dataset → Prompt → Results  
D. Dataset → Results → Grader

✅ **Answer: B** [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

## Question 2

Which function directly interacts with Claude?

A. run\_eval()  
B. run\_test\_case()  
C. run\_prompt()  
D. main()

✅ **Answer: C** [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

## Question 3

What is the primary role of `run_eval()`?

A. Build prompts  
B. Grade responses  
C. Process the full dataset  
D. Generate datasets

✅ **Answer: C** [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

## Question 4

Why are scores fixed at 10 in this lesson?

A. Claude always scores perfectly  
B. Dataset is small  
C. Grading logic has not yet been implemented  
D. JSON requires a score

✅ **Answer: C** [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

## Question 5

What does the results object typically contain?

A. Only scores  
B. Only outputs  
C. Output, test case, and score  
D. Prompt only

✅ **Answer: C** [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

## Question 6

According to the lesson, where does most evaluation sophistication come from?

A. Python syntax  
B. File loading  
C. Evaluation orchestration  
D. Grading logic and prompt optimization

✅ **Answer: D** [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)

***

# References

* Claude with Amazon Bedrock Course – *Running the eval* lesson. [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)
* Topics covered:
  * Evaluation workflow
  * `run_prompt`
  * `run_test_case`
  * `run_eval`
  * Dataset execution
  * Result collection
  * Evaluation foundations [\[Running the eval\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276736)
