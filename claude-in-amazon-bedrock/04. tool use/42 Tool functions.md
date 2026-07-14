# Learn From This Page

## Source

* Page: **Tool functions** (Claude with Amazon Bedrock course)
* Reference: Active browser page content [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

# Key Concepts

## 1. Why Tool Functions Are Needed

LLMs such as Claude have limitations when interacting with the real world:

* May know the current date but not the exact current time.
* Can struggle with complex date arithmetic.
* Cannot directly perform actions such as setting reminders.
* Need external functions ("tools") to access real-world capabilities. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

### Example Reminder System

To create a reminder feature, three tools are needed:

1. **Get Current Date Time**
   * Returns current date/time.
2. **Add Duration to Date Time**
   * Calculates future date/time.
3. **Set Reminder**
   * Creates the reminder action. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## 2. How Tool Functions Work

Tool use follows a specific workflow:

```text
User Request
      ↓
Claude decides a tool is needed
      ↓
Claude generates tool call
      ↓
Application runs tool function
      ↓
Tool result returned
      ↓
Claude generates final response
```

Steps described in the course:

1. Write the tool function.
2. Create a JSON Schema specification.
3. Send schema to Claude.
4. Claude requests tool execution.
5. Run the tool.
6. Send results back to Claude.
7. Claude uses results in its response. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## 3. Writing Tool Functions

Tool functions are standard Python functions executed when Claude needs extra information. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

### Best Practices

#### Use Descriptive Argument Names

Good:

```python
def add_duration_to_date(date, days):
```

Bad:

```python
def add(x, y):
```

#### Validate Inputs

Reject invalid values and raise clear errors.

#### Return Meaningful Errors

If a tool fails, Claude may attempt another call with corrected parameters. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## 4. Example Tool

### Get Current Datetime

```python
from datetime import datetime, timedelta

def get_current_datetime(
        date_format="%Y-%m-%d %H:%M:%S"
):
    return datetime.now().strftime(date_format)
```

This tool:

* Has a descriptive name.
* Uses a meaningful parameter.
* Provides a default value.
* Returns exactly what it promises. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## 5. JSON Schema for Tools

A JSON Schema describes the tool to Claude. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

### Purpose

JSON Schema helps:

* Define required parameters.
* Explain when to use the tool.
* Describe outputs.
* Validate data structures. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

### Example Structure

```json
{
  "name": "get_current_datetime",
  "description": "Returns the current date and time",
  "input_schema": {
    "type": "object",
    "properties": {
      "date_format": {
        "type": "string"
      }
    }
  }
}
```

***

## 6. JSON Schema Best Practices

### Tool Description

Include:

* What the tool does.
* When it should be used.
* What it returns.
* Typical scenarios. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

### Parameter Descriptions

Provide detailed guidance for each parameter so Claude can select correct values. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

### Recommended Detail Level

* Aim for 3–4 explanatory sentences in tool descriptions.
* Use detailed parameter descriptions. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

# Architecture Mindmap

```text
Tool Use
├── Problem
│   ├── No exact time
│   ├── Weak date arithmetic
│   └── Cannot perform real actions
│
├── Tools
│   ├── Get Current Datetime
│   ├── Add Duration
│   └── Set Reminder
│
├── Flow
│   ├── Define Function
│   ├── Define Schema
│   ├── Send to Claude
│   ├── Tool Call
│   ├── Execute
│   ├── Return Result
│   └── Generate Response
│
└── Best Practices
    ├── Clear Names
    ├── Input Validation
    ├── Useful Errors
    ├── Detailed Descriptions
    └── Strong Schema
```

***

# Q\&A

### Q1. Why are tool functions needed?

Tool functions allow Claude to access capabilities and information it does not inherently possess, such as exact current time, date calculations, and external actions. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

### Q2. What are the three tools needed for a reminder system?

1. Get current datetime
2. Add duration to datetime
3. Set reminder [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

### Q3. What is a tool function?

A tool function is a Python function that executes when Claude needs additional information or capabilities to help a user. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

### Q4. Why should tool inputs be validated?

Validation prevents incorrect or harmful inputs and helps ensure reliable tool execution. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

### Q5. What is JSON Schema used for?

JSON Schema describes how a tool should be called, including its parameters, requirements, and intended usage. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

### Q6. Why are detailed tool descriptions important?

Detailed descriptions help Claude decide accurately:

* When to use a tool
* How to provide parameters
* What results to expect [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

# Quiz

## Question 1

Which limitation is specifically mentioned for Claude?

A. Cannot generate text

B. Cannot understand English

C. Does not always know the exact current time

D. Cannot answer questions

✅ **Answer: C** [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## Question 2

Which tool would calculate a future date?

A. Set reminder

B. Get current datetime

C. Add duration to datetime

D. Generate message

✅ **Answer: C** [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## Question 3

What is the first step in the tool workflow?

A. Run the tool

B. Write the tool function

C. Return results

D. Ask the user again

✅ **Answer: B** [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## Question 4

A tool function is typically written as:

A. HTML

B. SQL

C. Python Function

D. XML Document

✅ **Answer: C** [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## Question 5

Why should tool arguments be descriptive?

A. Reduce server costs

B. Help Claude understand the tool

C. Increase model size

D. Improve internet speed

✅ **Answer: B** [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## Question 6

What does JSON Schema describe?

A. UI Layout

B. Database Design

C. Tool Inputs and Usage

D. Cloud Infrastructure

✅ **Answer: C** [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## Question 7

If a tool returns a meaningful error, Claude may:

A. Stop immediately

B. Delete the tool

C. Try calling it again with corrected inputs

D. Reboot itself

✅ **Answer: C** [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)

***

## Key Takeaway

**Tool Use = Extending Claude with real-world capabilities.**

A high-quality tool implementation requires:

* Clear Python functions
* Robust input validation
* Helpful error handling
* Well-written JSON Schemas
* Detailed descriptions that tell Claude when and how to use the tool effectively. [\[Tool functions\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276757)
