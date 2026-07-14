# Learn from This Page: Structured Data (Claude with Amazon Bedrock)

**Source:**  
Anthropic Partners Training – *Structured Data*  
Page: **Structured data** (Claude with Amazon Bedrock Course) [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

# Key Concepts

## What is Structured Data?

Structured data is output that follows a predictable format, such as:

* JSON
* Python code
* CSV
* Configuration files
* Bulleted lists

When building applications, developers often need Claude to generate **only the structured content**, without extra explanations. [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

## The Problem with Default Model Responses

Claude is designed to be helpful and often adds:

* Headers
* Explanatory text
* Markdown formatting
* Additional commentary

Example:

````markdown
# EventBridge Rule

```json
{
  "source": ["aws.ec2"]
}
````

This rule captures EC2 events...

````

While useful for documentation, this is inconvenient when users need raw JSON for direct use in applications. 【1-73c277】

---

## Real-World Example

Imagine a web application that generates AWS EventBridge rules.

### User Expectation

User enters:

> Generate an EventBridge rule

Expected output:

```json
{
  "source": ["aws.ec2"]
}
````

### Problem

Claude might return:

* Markdown code blocks
* Explanations
* Additional descriptions

Users must manually copy only the JSON part. [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

# Solution: Assistant Message Prefilling + Stop Sequences

The course introduces a technique to force cleaner output.

### Example

````python
messages = []

add_user_message(
    messages,
    "Generate a very short event bridge rule as json"
)

add_assistant_message(
    messages,
    "```json"
)

text = chat(
    messages,
    stop_sequences=["```"]
)
````
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c83a8776-6567-4369-a1d8-8b6b605f75e2" />

 [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

## How Assistant Prefilling Works

Before Claude generates text, the assistant message is pre-populated with:

````markdown
```json
````

Claude interprets this as:

> "I have already started writing a JSON block."

Therefore Claude:

* Skips introductions
* Skips headers
* Starts writing JSON immediately

 [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

## How Stop Sequences Work

A stop sequence instructs Claude:

> "Stop generating text when this token appears."

Example:

````python
stop_sequences=["```"]
````

Claude naturally tries to close the code block:

```markdown
```

````

Generation stops before the closing delimiter is returned. 【1-73c277】

---

## Behind the Scenes

### Without Control

Claude generates:

```markdown
# EventBridge Rule

```json
{
  ...
}
````

Explanation...

````

### With Prefill + Stop Sequence

Claude generates:

```json
{
  ...
}
````

No explanation.

No markdown wrapper.

Only the desired content. [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

## Processing the Output

After generation:

```python
import json

parsed_data = json.loads(text.strip())
```

Benefits:

* Validates output
* Removes unnecessary whitespace
* Converts JSON into native Python objects

 [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

## Beyond JSON

The technique works for many structured formats:

### Python Code

```python
def hello():
    print("Hello")
```

### CSV

```csv
name,age
John,25
```

### Configuration Files

```yaml
version: 1.0
```

### Bulleted Lists

```text
- item 1
- item 2
```

### Any Structured Format

The key idea is:

1. Prefill Claude with the expected beginning.
2. Stop generation at the desired ending.

 [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

# Architecture Summary

````text
User Request
      │
      ▼
Assistant Prefill
("```json")
      │
      ▼
Claude Generates
(JSON only)
      │
      ▼
Stop Sequence
("```")
      │
      ▼
Clean Structured Output
````

***

# Best Practices

### Use Assistant Prefilling When

* Generating JSON APIs
* Producing machine-readable output
* Creating config files
* Exporting CSV
* Generating code

### Use Stop Sequences When

* You know the natural ending delimiter
* You need precise output formatting
* You want to avoid extra explanations

### Validate Structured Output

Always:

```python
json.loads()
```

for JSON responses before production usage. [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

# Q\&A

### Q1. Why does Claude add explanations by default?

Because Claude is optimized to be helpful and conversational, often adding context and explanations around generated content. [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

### Q2. What is assistant message prefilling?

A technique where you provide the beginning of the expected output so Claude continues from that point. [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

### Q3. What is a stop sequence?

A token or string that immediately stops output generation when encountered. [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

### Q4. Why combine prefilling and stop sequences?

Together they create precise, clean, machine-readable output without additional text. [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

### Q5. Can this technique be used beyond JSON?

Yes. It can be used for code, CSV, YAML, configuration files, and bulleted lists. [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

### Q6. Why validate JSON after generation?

To ensure the generated text is syntactically correct and suitable for downstream applications. [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

***

# Quiz

## Question 1

What problem does structured data generation often face?

A. Slow generation  
B. Excessive token usage  
C. Extra explanatory text around desired output  
D. Missing punctuation

✅ **Answer: C**

***

## Question 2

What is the purpose of assistant message prefilling?

A. Reduce cost  
B. Force a model upgrade  
C. Provide the beginning of the desired response format  
D. Enable streaming

✅ **Answer: C**

***

## Question 3

What does a stop sequence do?

A. Retrains the model  
B. Stops generation when a specific token appears  
C. Compresses output  
D. Removes invalid JSON

✅ **Answer: B**

***

## Question 4

Which stop sequence is used in the example?

A. `</json>`  
B. `STOP`  
C. `}`  
D. ` ``` `

✅ **Answer: D**

***

## Question 5

Which output is best for application integration?

A. JSON with explanation paragraphs  
B. JSON inside markdown plus commentary  
C. Raw JSON only  
D. Screenshot of JSON

✅ **Answer: C**

***

## Question 6

Which Python function can validate generated JSON?

A. `json.dumps()`  
B. `json.loads()`  
C. `json.build()`  
D. `json.validate()`

✅ **Answer: B**

***

## Question 7

Which formats can benefit from prefilling and stop sequences? (Select all that apply)

A. JSON  
B. CSV  
C. Python code  
D. Configuration files

✅ **Answer: A, B, C, D**

***

# References

* Anthropic Partners Training: **Claude with Amazon Bedrock – Structured Data** [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)
* Topics covered:
  * Structured Data Generation
  * Assistant Message Prefilling
  * Stop Sequences
  * JSON Output Control
  * Programmatic Output Validation [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)

# Exam Tip

For Anthropic/Bedrock certification questions, remember:

**"Prefill the desired format + Stop at the closing delimiter = Clean structured output."** ✅ [\[Structured data\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276724)
