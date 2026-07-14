# Learn From This Page

**Source:**  
Generating test datasets – Claude with Amazon Bedrock Course  
(Active page content) [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

# Key Concepts

## 1. Why Generate Test Datasets?

When building a **prompt evaluation workflow**, the first step is to:

1. Define a clear objective.
2. Create a test dataset.
3. Evaluate prompt performance against the dataset.

In this lesson, the goal is to create a prompt that generates AWS-related code while returning **only the requested code output** without explanations or formatting. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## 2. Define a Clear Goal

The prompt accepts a task description and should return one of these outputs:

* Python code
* JSON configuration
* Regular expression (Regex)

Important requirement:

* No headers
* No footers
* No explanations
* Only the requested code output

Example initial prompt:

```text
Please provide a solution to the following task: {task}
```

Starting with a simple prompt makes evaluation easier and allows iterative improvement later. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## 3. What Is an Evaluation Dataset?

An evaluation dataset is a collection of test cases used to measure prompt quality.

Process:

```text
Dataset Input
    ↓
Prompt Template
    ↓
Claude Response
    ↓
Evaluation
```

Benefits:

* Tests consistency
* Identifies prompt weaknesses
* Enables comparison between prompt versions
* Supports automated evaluation workflows

 [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## 4. Methods for Creating Datasets

### Manual Creation

Write test cases by hand.

Advantages:

* High quality
* Full control

Disadvantages:

* Slow
* Difficult to scale

### Automatic Generation

Use Claude to generate test cases.

Advantages:

* Fast
* Scalable
* Easy to expand

For dataset generation, a smaller/faster model such as **Haiku** is generally suitable because many examples need to be created efficiently. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## 5. Dataset Generation Function

The lesson demonstrates generating AWS-related tasks using Claude.

Example workflow:

```python
def generate_dataset():
    prompt = """
    Generate 3 AWS-related tasks
    that require Python, JSON,
    or Regex solutions.
    """
```

Generated tasks should:

* Be realistic
* Focus on AWS scenarios
* Be solvable with small code snippets
* Require Python, JSON, or Regex outputs

 [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## 6. Prefilled Assistant Response Technique

The dataset generator uses a useful prompting pattern:

````python
add_assistant_message(messages, "```json")
````

Why?

* Forces Claude to continue generating JSON.
* Makes output easier to parse.
* Improves consistency.

Then use a stop sequence:

````python
stop_sequences=["```"]
````

This stops generation at the closing code fence, helping ensure clean JSON output. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

### Pattern

````text
Assistant starts with:
```json

Claude generates:
{
  ...
}

Stop when:
````

````

Result:

- Structured output
- Easier automation
- Reliable parsing

【1-66f97b】

---

## 7. Parsing Generated JSON

After generation:

```python
text = chat(...)
return json.loads(text)
````

Benefits:

* Converts JSON text into Python objects
* Enables automated processing
* Reduces manual work

 [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## 8. Saving the Dataset

Persist generated data:

```python
with open("dataset.json", "w") as f:
    json.dump(dataset, f, indent=2)
```

Why save datasets?

* Avoid regenerating repeatedly
* Ensure reproducible evaluations
* Version datasets alongside prompts

 [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## 9. Example Generated Tasks

Possible generated tasks may include:

* Extract AWS Account IDs from ARNs
* Create JSON schemas for EC2 configurations
* Build regex patterns for S3 bucket names

These tasks help evaluate whether the prompt consistently returns the correct output format. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## 10. Production Considerations

The lesson uses only 3 test cases for demonstration.

For real-world evaluation:

* Use many more examples
* Increase scenario diversity
* Cover edge cases
* Ensure realistic workloads

Larger datasets provide more trustworthy evaluation results. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

# Architecture Mindmap

```text
Prompt Goal
│
├── AWS-related Tasks
│   ├── Python
│   ├── JSON
│   └── Regex
│
├── Generate Dataset
│   ├── Manual Creation
│   └── Claude Generation
│
├── Structured Output
│   ├── Prefilled Assistant
│   ├── JSON Format
│   └── Stop Sequences
│
├── Save Dataset
│   └── dataset.json
│
└── Evaluation
    ├── Run Prompt
    ├── Compare Results
    └── Improve Prompt
```

***

# Q\&A

### Q1: What is the purpose of a test dataset?

**Answer:**  
To evaluate how well a prompt performs across multiple test scenarios consistently. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

### Q2: What outputs must the prompt generate?

**Answer:**

* Python code
* JSON configuration
* Regular expressions

And only the requested code should be returned. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

### Q3: Why start with a simple prompt?

**Answer:**  
It makes evaluation easier and provides a baseline for iterative prompt improvement. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

### Q4: What are the two ways to create evaluation datasets?

**Answer:**

1. Manual creation
2. Automatic generation using Claude

 [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

### Q5: Why use a faster model like Haiku?

**Answer:**  
Because dataset generation often requires producing many examples efficiently. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

### Q6: Why prefill the assistant message with \`\`\`json?

**Answer:**  
To guide Claude toward generating structured JSON output. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

### Q7: What is the purpose of stop sequences?

**Answer:**  
To stop generation at a specific token and obtain clean structured output. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

### Q8: Why save generated datasets?

**Answer:**  
To avoid repeated generation and ensure reproducible evaluations. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

# Quiz

## Question 1

What is the primary purpose of an evaluation dataset?

A. Train a model  
B. Store production code  
C. Measure prompt performance  
D. Deploy applications

✅ **Answer: C** [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## Question 2

Which output types are expected by the prompt?

A. HTML, CSS, JavaScript  
B. Python, JSON, Regex  
C. Java, SQL, XML  
D. YAML, Bash, Terraform

✅ **Answer: B** [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## Question 3

Why is automatic dataset generation useful?

A. It eliminates evaluation  
B. It is faster and scalable  
C. It improves model training  
D. It removes prompts

✅ **Answer: B** [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## Question 4

What technique encourages Claude to output JSON?

A. Sampling  
B. Streaming  
C. Prefilled assistant message  
D. Reranking

✅ **Answer: C** [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## Question 5

What does the stop sequence accomplish?

A. Improves embeddings  
B. Stops generation at a chosen point  
C. Creates datasets  
D. Runs evaluation

✅ **Answer: B** [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## Question 6

Which Python function converts JSON text to Python objects?

A. json.dump()  
B. json.save()  
C. json.write()  
D. json.loads()

✅ **Answer: D** [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)

***

## Key Takeaways

* Always define a clear evaluation goal first.
* Use datasets to validate prompt behavior systematically.
* Claude can generate test datasets automatically.
* Prefilled assistant responses and stop sequences help produce reliable structured outputs.
* Save datasets for repeatable evaluations.
* Production-grade prompt evaluation requires larger and more diverse datasets. [\[Generating...t datasets\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276733)
