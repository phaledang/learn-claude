# Learn From This Page

**Source:**  
Anthropic Partners Skilljar – *Claude with Amazon Bedrock > System prompts*  
Page title: **System prompts** [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

# Key Concepts

## 1. What Are System Prompts?

System prompts are instructions provided to Claude **before** any user message is processed. They help transform a general-purpose AI into a specialized assistant with a specific role, behavior, and scope. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Purpose

* Control how the AI responds.
* Keep responses aligned with a specific domain.
* Enforce consistent behavior.
* Reduce the need for repetitive instructions. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

## 2. The Problem with User-Level Instructions

Putting all requirements directly into every user message is inefficient. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Limitations

* Must anticipate every possible scenario.
* Instructions become repetitive and difficult to maintain.
* Users can see internal guidance.
* Requirements may vary across questions. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Example

Instead of repeatedly saying:

* Mention AWS services.
* Do not mention competitors.

for every conversation, use a system prompt once and let Claude consistently follow that role. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

## 3. Benefits of System Prompts

System prompts provide role-based guidance. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Benefits

* Consistent responses.
* Defined expertise and constraints.
* Better brand alignment.
* Less prompt maintenance.
* No need to cover every edge case explicitly. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

## 4. Implementing a System Prompt

Example from the course: [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

```python
system_prompt = """
You are an AWS cloud support specialist.
Your job is to answer user queries related
to cloud hosting services on AWS.
"""

response = client.converse(
    modelId=model_id,
    messages=messages,
    system=[{"text": system_prompt}]
)
```

### Key Points

* The `system` parameter is a list.
* Each element contains a dictionary with a `"text"` key.
* Claude adopts the role before processing user messages. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

## 5. Creating a Reusable Chat Function

The lesson introduces a reusable function that optionally supports system prompts. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

```python
def chat(messages, system=None):
    params = {
        "modelId": model_id,
        "messages": messages
    }

    if system:
        params["system"] = [{"text": system}]

    response = client.converse(**params)

    return response["output"]["message"]["content"][0]["text"]
```

### Advantages

* Flexible.
* Easy to reuse.
* Supports role-based conversations.
* Works with or without a system prompt. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

## 6. System Prompts in Action

### Without a System Prompt

Question:

> How do I host a Postgres database?

Claude may provide:

* AWS options
* Azure options
* Google Cloud options
* Self-hosted approaches [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### With an AWS Support Specialist Prompt

Claude focuses on:

* Amazon RDS
* Amazon Aurora
* EC2 deployments
* AWS-specific guidance

and avoids competitor recommendations. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

## 7. Handling Off-Topic Requests

System prompts influence behavior even when users ask unrelated questions. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

Example:

* Assigned role: AWS Cloud Support Specialist
* User asks: "Give me a bread recipe"

Expected behavior:

* Claude politely declines or redirects while remaining in character. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

## 8. Technical Requirements

Important rules when using system prompts: [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Rule 1

System prompts cannot be empty strings.

### Rule 2

The `system` parameter must be a list of dictionaries containing a `"text"` key.

### Rule 3

System prompts are processed before user messages.

### Rule 4

You can change the system prompt between conversations, but not during an ongoing conversation. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

# Architecture Overview

```text
System Prompt
      ↓
Claude adopts role
      ↓
User Message
      ↓
Role-guided reasoning
      ↓
Specialized Response
```

Based on the lesson, the system prompt establishes behavior first, then user requests are interpreted within that role. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

# Q\&A

### Q1. What is a system prompt?

A system prompt is a special instruction that defines Claude's role and behavior before user messages are processed. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Q2. Why use system prompts instead of user instructions?

They provide consistent behavior, reduce repetition, and hide implementation details from users. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Q3. How is a system prompt passed to Claude?

Through the `system` parameter as a list containing dictionaries with a `"text"` field. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Q4. What happens if no system prompt is provided?

Claude responds as its default assistant persona. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Q5. Can a system prompt be empty?

No. It must contain at least one character. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Q6. When is a system prompt applied?

Before Claude processes any user message. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Q7. Can the system prompt be changed during a conversation?

The lesson states it can be updated between conversations, not mid-conversation. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

### Q8. Why do system prompts improve chatbot design?

They enforce a role, keep responses focused, and simplify prompt management. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

# Quiz

## Multiple Choice

### 1. What is the main purpose of a system prompt?

A. Increase token limits  
B. Define AI behavior and role  
C. Store chat history  
D. Encrypt requests

✅ **Answer: B** [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

### 2. Which parameter is used to provide a system prompt?

A. context  
B. role  
C. system  
D. prompt

✅ **Answer: C** [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

### 3. How is a system prompt represented?

A.

```python
"system": "prompt"
```

B.

```python
system=[{"text": prompt}]
```

C.

```python
system=(prompt)
```

D.

```python
system={prompt}
```

✅ **Answer: B** [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

### 4. What benefit does a system prompt provide?

A. Automatic model switching  
B. Consistent responses  
C. Reduced API cost only  
D. Faster network speed

✅ **Answer: B** [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

### 5. What would an AWS specialist prompt likely do when asked about PostgreSQL hosting?

A. Discuss every cloud provider equally  
B. Focus on AWS services like RDS and Aurora  
C. Refuse the question  
D. Switch models automatically

✅ **Answer: B** [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

### 6. True or False: System prompts are processed after user messages.

✅ **Answer: False** [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

### 7. True or False: System prompts can help keep chatbot responses on-brand.

✅ **Answer: True** [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

### 8. True or False: An empty string is a valid system prompt.

✅ **Answer: False** [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

***

# Key Takeaway

**System prompts are one of the most important prompt-engineering techniques.** They allow you to transform Claude from a general assistant into a domain-specific expert by defining a role, constraints, and behavioral expectations before any user interaction occurs. This results in more consistent, reliable, and focused responses. [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)

# References

* Anthropic Partners Skilljar – Claude with Amazon Bedrock – System Prompts [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)
* Downloadable notebook: `002_System_Messages.ipynb` mentioned on the course page [\[System prompts\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276726)
