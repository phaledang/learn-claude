# Learn from This Page: Controlling Model Output (Claude with Amazon Bedrock)

**Source:**  
Anthropic Partners Learning – *Controlling model output*  
Page: *Controlling model output* (Claude with Amazon Bedrock) [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

# Key Concepts

## Why Control Model Output?

Prompt engineering is powerful, but sometimes you need more precise control over:

* How the model starts its response
* What direction the response takes
* When the model should stop generating text
* The structure and length of output

Two important techniques are introduced:

1. **Prefilled Assistant Messages**
2. **Stop Sequences** [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

# 1. Prefilled Assistant Messages

## What Is It?

A technique where you provide the beginning of the assistant's response before Claude generates the rest.

Instead of allowing Claude to decide how to start, you give it a starting phrase. Claude continues from that point. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## How It Works

Conversation structure:

1. Add the user message.
2. Add an assistant message containing the desired starting text.
3. Claude continues from that text. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

Example:

```python
messages = []

add_user_message(
    messages,
    "Is coffee or tea better for breakfast?"
)

add_assistant_message(
    messages,
    "Coffee is better because"
)

chat(messages)
```

Possible response:

```text
it has more caffeine.
```

Combined result:

```text
Coffee is better because it has more caffeine.
```

 [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Why It Works

Claude sees the assistant message and assumes it has already started responding.

It therefore continues the answer instead of creating a completely new response. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Steering the Response

Different prefixes guide the model in different directions:

### Example 1

```text
Coffee is better because
```

Leads Claude toward a coffee-supporting answer.

### Example 2

```text
Tea is better because
```

Leads Claude toward a tea-supporting answer.

### Example 3

```text
They are the same because
```

Encourages a balanced response. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Benefits

* Controls response tone and direction
* Produces more predictable outputs
* Useful for templates and structured responses
* Helps enforce desired answer formats [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

# 2. Stop Sequences

## What Is It?

A stop sequence is a string that forces Claude to stop generating output immediately when that string appears. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## How It Works

The API is configured with one or more stop sequences.

Example:

```python
def chat(
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[]
):
    params = {
        "modelId": model_id,
        "messages": messages,
        "inferenceConfig": {
            "temperature": temperature,
            "stopSequences": stop_sequences
        },
    }
```

 [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Simple Example

Prompt:

```text
Count from 1 to 10
```

Call:

```python
chat(
    messages,
    stop_sequences=["5"]
)
```

Output:

```text
1, 2, 3, 4,
```

Generation stops before including "5". [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Multiple Stop Sequences

Example:

```python
chat(
    messages,
    stop_sequences=[
        "5",
        "3, 4"
    ]
)
```

Claude stops when it encounters the first matching stop sequence. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Common Uses

### Response Length Control

Prevent responses from becoming too long.

### Structured Output

Stop generation after a section is completed.

### Delimiter-Based Processing

Stop after special markers or separators.

### Template Enforcement

Avoid unwanted content after desired output. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

# Comparison

| Technique                   | Purpose                         | How It Works                                 |
| --------------------------- | ------------------------------- | -------------------------------------------- |
| Prefilled Assistant Message | Control how the response begins | Provide the starting text of Claude's answer |
| Stop Sequence               | Control where the response ends | Stop when a specified token/string appears   |

Based on the lesson content. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

# Practical Scenarios

## Scenario 1: JSON Generation

Use:

```text
{
```

as a prefilled assistant message.

This encourages Claude to continue producing JSON. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Scenario 2: Report Sections

Use stop sequences such as:

```text
END_REPORT
```

to stop generation at a specific boundary. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Scenario 3: Opinion Steering

Prompt:

```text
Is tea or coffee better?
```

Assistant prefill:

```text
Tea is better because
```

Claude continues supporting tea. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

# Q\&A

### Q1. What are the two main techniques discussed?

**Answer:**  
Prefilled Assistant Messages and Stop Sequences. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

### Q2. What is a prefilled assistant message?

**Answer:**  
A predefined beginning of Claude's response that guides how the answer continues. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

### Q3. Does Claude repeat the prefilled text?

**Answer:**  
No. Claude continues from where the prefilled text ends. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

### Q4. Why use stop sequences?

**Answer:**  
To force Claude to stop generating when a specified string is encountered. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

### Q5. Is the stop sequence included in the final output?

**Answer:**  
No. The stop sequence itself is omitted. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

### Q6. Can multiple stop sequences be configured?

**Answer:**  
Yes. Claude stops at whichever matching sequence appears first. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

# Quiz

## Question 1

What is the primary purpose of a prefilled assistant message?

A. Increase token limit  
B. Control response direction and starting point  
C. Encrypt prompts  
D. Reduce API cost

✅ **Answer: B** [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Question 2

Claude sees a prefilled assistant message and assumes:

A. The conversation is finished  
B. The user is an administrator  
C. The response has already begun and should continue  
D. The prompt is invalid

✅ **Answer: C** [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Question 3

What happens when Claude encounters a stop sequence?

A. Restarts generation  
B. Ignores the sequence  
C. Stops generating immediately  
D. Generates a warning

✅ **Answer: C** [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Question 4

If the stop sequence is:

```text
5
```

and Claude is counting from 1 to 10, what might the output be?

A. 1,2,3,4,5  
B. 1,2,3,4  
C. 5,6,7,8  
D. 1–10

✅ **Answer: B** [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

## Question 5

Which technique is best for controlling where the response ends?

A. Temperature  
B. System Prompt  
C. Prefilled Assistant Message  
D. Stop Sequence

✅ **Answer: D** [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

***

# Exam Tips

Remember:

* **Prefilled Assistant Message = Control the Beginning**
* **Stop Sequence = Control the Ending**
* Prefilling steers content.
* Stop sequences limit output.
* Combining both provides precise output control for production AI applications. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)

# References

* Anthropic Partners Learning Portal — *Claude with Amazon Bedrock: Controlling model output* [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)
* Topics covered: Prefilled Assistant Messages, Stop Sequences, Output Control Strategies. [\[Controllin...del output\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276723)
