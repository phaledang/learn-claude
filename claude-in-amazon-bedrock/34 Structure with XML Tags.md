# Learn From This Page: Structure with XML Tags (Claude Prompt Engineering)

**Source:**  
[Structure with XML tags](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276744)

***

# Key Concepts

## What Are XML Tags in Prompts?

XML tags help organize prompt content by creating clear boundaries between different sections of a prompt.

Example:

```xml
<sales_records>
{sales_records}
</sales_records>
```

Instead of providing raw text, XML tags tell Claude:

* What content belongs together
* Where one section starts and ends
* Which content is instructions versus data

***

## Why Structure Matters

When prompts contain:

* Large datasets
* Long documents
* Source code
* Multiple content types

Claude may struggle to determine:

* Which text is instruction
* Which text is context
* How different sections relate to each other

XML tags solve this by creating explicit structure.

### Without Tags

```text
Analyze the following data...

Sales Records:
...
```

Potential issues:

* Ambiguous boundaries
* Confusing instructions with data
* Less consistent outputs

***

### With Tags

```xml
<sales_records>
...
</sales_records>
```

Benefits:

* Clear separation
* Better context understanding
* More reliable responses

***

# Creating Custom XML Tags

You are not limited to official XML standards.

You can create descriptive tags such as:

```xml
<sales_records>
</sales_records>

<customer_feedback>
</customer_feedback>

<meeting_notes>
</meeting_notes>
```

### Best Practice

Use descriptive names.

✅ Good

```xml
<sales_records>
```

❌ Less helpful

```xml
<data>
```

Specific names provide stronger semantic signals to the model.

***

# Practical Example: Debugging Code

## Not Great Approach

Mixing code and documentation together:

```text
Here is my code...

Here is documentation...
```

Claude may have difficulty identifying:

* Code to debug
* Reference documentation

***

## Better Approach

```xml
<my_code>
from datavortex import Pipeline
...
</my_code>

<docs>
# Creating a data source
...
</docs>
```

Benefits:

* Claude immediately knows which section contains source code
* Claude knows which section serves as guidance
* Better debugging results

***

# Example: Meal Plan Generation

Organizing user inputs:

```xml
<athlete_information>
- Height: 180cm
- Weight: 80kg
- Goal: Build muscle
- Dietary restrictions: None
</athlete_information>
```

Advantages:

* Groups related information
* Improves readability
* Reduces misunderstanding
* Produces more relevant outputs

***

# When Should You Use XML Tags?

Use XML tags when:

### 1. Large Context Windows

Examples:

* Reports
* PDFs
* Research papers
* Meeting transcripts

***

### 2. Multiple Content Types

Examples:

```xml
<instructions>
</instructions>

<source_document>
</source_document>

<expected_output>
</expected_output>
```

***

### 3. Retrieval-Augmented Generation (RAG)

```xml
<retrieved_context>
...
</retrieved_context>
```

Helps Claude understand retrieved knowledge versus instructions.

***

### 4. Code Generation and Debugging

```xml
<code>
</code>

<requirements>
</requirements>

<documentation>
</documentation>
```

***

### 5. User Input Variables

```xml
<customer_profile>
...
</customer_profile>
```

Useful for applications that dynamically inject user data into prompts.

***

# Best Practices

### Use Clear Tag Names

✅

```xml
<customer_feedback>
```

❌

```xml
<data>
```

***

### Keep Related Information Together

✅

```xml
<user_preferences>
...
</user_preferences>
```

Rather than scattering information across the prompt.

***

### Separate Instructions From Context

```xml
<instructions>
Summarize key findings.
</instructions>

<context>
...
</context>
```

***

### Structure Complex Prompts

For enterprise-grade prompts:

```xml
<system_rules>
</system_rules>

<user_request>
</user_request>

<context>
</context>

<output_format>
</output_format>
```

This is especially useful when working with Claude on Amazon Bedrock, MCP servers, and RAG solutions.

***

# Q\&A

### Q1: Why are XML tags useful in prompts?

**Answer:**  
They create clear boundaries between different prompt sections, helping Claude better understand context and instructions.

***

### Q2: Do XML tags need to follow official XML standards?

**Answer:**  
No. You can create custom tags that best describe your content.

***

### Q3: Which is better: `<data>` or `<sales_records>`?

**Answer:**  
`<sales_records>` because it provides more meaningful context.

***

### Q4: Are XML tags only useful for large prompts?

**Answer:**  
No. Even smaller prompts can benefit from improved clarity and structure.

***

### Q5: How do XML tags help in debugging?

**Answer:**  
They separate the source code from documentation, enabling Claude to distinguish what should be analyzed versus what should be used as a reference.

***

### Q6: Can XML tags improve RAG systems?

**Answer:**  
Yes. Tags make retrieved context clearly distinguishable from instructions and user requests.

***

### Q7: What is a common enterprise pattern?

**Answer:**

```xml
<instructions>
</instructions>

<context>
</context>

<output_format>
</output_format>
```

This pattern improves consistency and reliability.

***

# Quiz

## Question 1

What is the primary purpose of XML tags in prompts?

A. Increase token limits  
B. Structure and separate content sections  
C. Speed up API calls  
D. Compress context

✅ **Answer: B**

***

## Question 2

Which tag is more descriptive?

A. `<data>`  
B. `<content>`  
C. `<sales_records>`  
D. `<info>`

✅ **Answer: C**

***

## Question 3

When are XML tags most useful?

A. Large context inputs  
B. Multiple content sections  
C. Dynamic prompt variables  
D. All of the above

✅ **Answer: D**

***

## Question 4

Which example follows best practice?

A.

```xml
<data>
customer feedback
</data>
```

B.

```xml
<customer_feedback>
customer feedback
</customer_feedback>
```

✅ **Answer: B**

***

## Question 5

Which use case benefits from XML tags?

A. RAG systems  
B. Code debugging  
C. Document analysis  
D. All of the above

✅ **Answer: D**

***

## Question 6

For a Solution Architect building MCP or Bedrock solutions, which structure is recommended?

A.

```xml
<context>
...
</context>
```

B.

```xml
<instructions>
...
</instructions>

<context>
...
</context>

<output_format>
...
</output_format>
```

✅ **Answer: B**

***

# Practical Template

A reusable enterprise prompt template:

```xml
<instructions>
Perform the requested task.
</instructions>

<context>
Retrieved knowledge, documents, code, or business data.
</context>

<constraints>
- Follow company policies
- Be concise
- Cite sources
</constraints>

<output_format>
Provide:
1. Summary
2. Risks
3. Recommendations
</output_format>
```

### Key Takeaway

**XML tags are one of the simplest and highest-impact prompt engineering techniques.** They help Claude distinguish instructions, context, code, documents, and user inputs, leading to more accurate, consistent, and maintainable prompts—especially for complex Amazon Bedrock, RAG, and MCP-based applications.
