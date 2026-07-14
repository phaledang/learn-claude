# Learn From This Page: JSON Schema for Tools

**Source:** JSON Schema for tools (Anthropic Claude in Amazon Bedrock course) [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

# Key Concepts

## 1. What is a JSON Schema?

A JSON Schema is a standardized way to describe and validate data structures. In tool use scenarios, it tells Claude:

* What inputs a tool accepts
* The expected data types
* Required and optional parameters
* How the tool should be used properly
* Constraints on input values

The schema acts as a **contract** between the AI model and your code. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

## 2. Two Main Parts of a Tool Schema

### A. Tool Metadata

Contains:

* **name**
* **description**

Purpose:

* Helps Claude understand **when** the tool should be used.
* Explains the tool's functionality and expected behavior.

Example:

```json
{
  "name": "get_weather",
  "description": "Gets weather information for a specified location."
}
```

 [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

### B. Input Schema

Contains:

* Parameter definitions
* Data types
* Required fields
* Property descriptions

Purpose:

* Helps Claude understand **how** to call the tool correctly.

 [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

## 3. Creating a JSON Schema: Step-by-Step

### Step 1: Create a Dictionary with Sample Data

Example function:

```python
def process_data(ids, profile, primary_id, value):
    pass
```

Create representative sample data:

```python
{
  "ids": [1, 2, 3],
  "profile": "user profile",
  "primary_id": 1,
  "value": 10
}
```

 [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### Step 2: Convert to JSON

Convert Python dictionary format into JSON.

Example:

```python
True
```

becomes

```json
true
```

JSON must follow proper JSON syntax rules. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### Step 3: Generate Schema Automatically

Use a:

> JSON → JSON Schema converter

Process:

1. Paste sample JSON.
2. Let the converter generate the schema.
3. Remove unnecessary `$schema` declarations if present.

This significantly speeds up schema creation. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### Step 4: Add Descriptions

This is the most important step.

Add descriptions for:

* The tool
* Each parameter

Why?

Because Claude relies heavily on these descriptions to determine:

* When a tool should be used
* How parameters should be populated
* What information to provide

 [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

## 4. Writing Good Tool Descriptions

### Tool Description Best Practices

Include:

* What the tool does
* When to use it
* What it returns
* Examples if applicable

Recommended length:

* 3–4 sentences

 [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

### Property Description Best Practices

Be extremely detailed:

✅ Good:

```text
City and country for weather lookup.
Examples: "Seattle, WA", "Paris, France"
```

❌ Poor:

```text
Location
```

Detailed descriptions improve tool selection accuracy. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

## 5. Using AI to Help Write Descriptions

If descriptions are difficult to write:

1. Paste the function into Claude.
2. Ask Claude to generate:
   * Tool description
   * Property descriptions

This can accelerate development while maintaining clarity. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

## 6. Why JSON Schemas Matter

A well-designed schema enables:

* Reliable tool calling
* Accurate argument generation
* Better reasoning by the model
* Reduced tool errors
* Improved user experience

Without clear schemas, Claude may misunderstand arguments or select incorrect tools. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

# Architecture Overview

```text
Tool
├── Name
├── Description
└── Input Schema
    ├── Properties
    │   ├── Type
    │   ├── Description
    │   └── Constraints
    └── Required Fields
```

Based on the lesson, the schema provides both:

* Semantic guidance (tool descriptions)
* Structural validation (input schema)

 [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

# Q\&A

### Q1. What is the purpose of a JSON Schema?

**Answer:**  
It defines the structure, types, and requirements of tool inputs so Claude can use the tool correctly. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### Q2. What are the two major sections of a tool schema?

**Answer:**

1. Tool name and description
2. Input schema defining arguments

 [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### Q3. Why is the tool description important?

**Answer:**  
It helps Claude determine when the tool should be used and what it does. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### Q4. Why are parameter descriptions important?

**Answer:**  
They help Claude understand how each argument should be populated and interpreted. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### Q5. What shortcut can be used to generate a schema quickly?

**Answer:**  
Convert sample JSON using an online JSON-to-JSON-Schema converter. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### Q6. What should be removed from some generated schemas?

**Answer:**  
The unnecessary `$schema` declarations. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### Q7. What does the schema act as between Claude and code?

**Answer:**  
A contract that defines how tool communication works. [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

# Quiz

## Multiple Choice

### 1. Which section helps Claude determine when to use a tool?

A. InputSchema  
B. Required Fields  
C. Tool Description  
D. Data Types

✅ **Answer: C** [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### 2. What is the main purpose of JSON Schema?

A. Store databases  
B. Validate and describe data structures  
C. Improve network speed  
D. Encrypt data

✅ **Answer: B** [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### 3. Which step is considered the most important?

A. Convert to JSON  
B. Create sample data  
C. Add descriptions  
D. Remove required fields

✅ **Answer: C** [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### 4. A good tool description should include:

A. Tool name only  
B. Only examples  
C. What it does, when to use it, and what it returns  
D. Source code

✅ **Answer: C** [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### 5. What can help automatically generate a schema?

A. Excel  
B. Markdown Converter  
C. JSON-to-JSON Schema Converter  
D. Word Processor

✅ **Answer: C** [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

### 6. Why are detailed property descriptions valuable?

A. They reduce file size  
B. They improve Claude's understanding of arguments  
C. They make JSON faster  
D. They remove validation

✅ **Answer: B** [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

***

# Practical Example

### Function

```python
def get_weather(location, units):
    pass
```

### Schema Concept

```json
{
  "name": "get_weather",
  "description": "Get current weather information for a location.",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "City and country. Example: Paris, France"
      },
      "units": {
        "type": "string",
        "description": "Temperature unit. Either C or F."
      }
    },
    "required": ["location"]
  }
}
```

This example demonstrates the lesson's central idea: **clear descriptions + structured schema = reliable tool use.** [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)

# References

* Anthropic Partners Skilljar – Claude in Amazon Bedrock
* Lesson: **JSON Schema for Tools** [\[JSON Schem...for tools\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276758)
