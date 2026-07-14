# Learn From This Page: Handling Tool Use Responses (Claude with Amazon Bedrock)

**Source:**  
[Handling tool use responses](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276764)

***

# Key Concepts

## 1. What is Tool Use?

When Claude decides to use a tool, it does **not** return only text.

Instead, it returns a **special response structure** that contains instructions for the application to execute a tool.

Why this matters:

* Claude cannot directly execute your functions.
* Your application must:
  * Detect the tool request
  * Execute the function
  * Return the results back to Claude
  * Continue the conversation

***

## 2. Tool Choice Configuration

The `toolChoice` parameter controls when Claude uses tools.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/508b94e9-5e25-4e43-9614-ef5e7fa98026" />

### Auto

```json
"toolChoice": "auto"
```

* Default behavior
* Claude decides whether a tool is needed

### Any

```json
"toolChoice": "any"
```

* Claude must use a tool
* Claude chooses which tool

### Specific Tool

```json
"toolChoice": {
  "tool": "get_current_time"
}
```

* Forces Claude to call a specific tool
* Useful for testing

### Summary

| Option        | Behavior               |
| ------------- | ---------------------- |
| auto          | Claude decides         |
| any           | Must use a tool        |
| specific tool | Forced tool invocation |

***

## 3. Multi-Part Message Structure

A normal response:

```text
The weather today is sunny.
```

A tool-use response contains multiple content parts:

### Part 1: Text

Human-readable explanation

```text
I can help you find the current time.
Let me check that for you.
```

### Part 2: ToolUse

Structured request:

```json
{
  "toolUseId": "...",
  "name": "get_current_time",
  "input": {}
}
```

***

## 4. ToolUse Part Components

Every tool request contains:

### toolUseId

Unique identifier

```json
"toolUseId": "tooluse_123"
```

Purpose:

* Used to correlate tool results with requests

***

### name

Tool Claude wants to execute

```json
"name": "get_current_time"
```

***

### input

Arguments for the tool

```json
"input": {
  "timezone": "UTC"
}
```

***

## 5. Conversation Flow with Tools
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ef993370-d136-44dd-bb83-fb0a5cec24fd" />

### Step 1

User sends request

```text
What time is it now?
```

### Step 2

Claude responds with:

* Text part
* ToolUse part

***

### Step 3

Application extracts:

```json
toolUseId
name
input
```

***

### Step 4

Application executes tool

```python
current_time()
```

***

### Step 5

Application sends back ToolResult

Along with:

* Original user message
* Original assistant tool request
* Tool result

***

### Step 6

Claude generates final answer

```text
The current time is 10:35 UTC.
```

***

## 6. Complete Message History is Critical

A common mistake:

❌ Sending only the tool result

Correct approach:

✅ Send:

1. User message
2. Assistant tool request
3. Tool result

This maintains context and allows Claude to continue reasoning.

***

## 7. Flexible Message Handling

The lesson recommends supporting:

### Simple Text

```python
add_user_message(messages, "Hello")
```

### Multi-Part Content

```python
add_user_message(messages, content_parts)
```

Example:

```python
def add_user_message(messages, content):
    if isinstance(content, str):
        ...
    else:
        ...
```

Benefit:

* Works for both normal conversations
* Works for tool workflows

***

## 8. Returning Full Content Parts

Instead of only returning text:

```python
return text
```

Return:

```python
return text, parts
```

Where:

```python
parts = response["output"]["message"]["content"]
```

This gives access to:

* Text responses
* Tool requests
* Future multimodal content

***

## 9. Checking Stop Reasons

The model includes a `stopReason`.

Important value:

```json
"tool_use"
```

When detected:

```python
if stopReason == "tool_use":
    execute_tool()
```

Meaning:

> Claude is waiting for your application to run a tool.

***

## 10. Practical Architecture

```text
User
  ↓
Claude
  ↓
Tool Request
  ↓
Application
  ↓
Execute Tool
  ↓
Tool Result
  ↓
Claude
  ↓
Final Response
```

This is the core architecture of tool-enabled AI agents.

***

# Q\&A

## Q1. What is a ToolUse response?

**Answer:**  
A structured response from Claude requesting the application to execute a tool.

***

## Q2. What does `toolUseId` do?

**Answer:**  
It uniquely identifies a tool request and is used when returning the tool result.

***

## Q3. What is stored in the `name` field?

**Answer:**  
The exact tool Claude wants to call.

***

## Q4. What is stored in the `input` field?

**Answer:**  
The arguments that should be passed to the tool.

***

## Q5. What happens when `toolChoice="auto"`?

**Answer:**  
Claude decides whether a tool should be used.

***

## Q6. What happens when `toolChoice="any"`?

**Answer:**  
Claude must use a tool but can decide which one.

***

## Q7. Why is complete conversation history important?

**Answer:**  
It preserves context and allows Claude to continue reasoning correctly after tools are executed.

***

## Q8. Why should the chat function return `parts`?

**Answer:**  
Because tool requests are stored in content parts, not just plain text.

***

## Q9. What does `stopReason="tool_use"` mean?

**Answer:**  
Claude is requesting a tool execution and expects the application to provide a tool result.

***

## Q10. Who executes the tool?

**Answer:**  
Your application/server executes the tool, not Claude itself.

***

# Quiz

## 1. Which `toolChoice` option allows Claude to decide whether a tool is needed?

* A. any
* B. specific
* C. auto
* D. manual

✅ **Answer: C. auto**

***

## 2. Which field identifies a specific tool request?

* A. id
* B. toolUseId
* C. requestId
* D. callId

✅ **Answer: B. toolUseId**

***

## 3. What does the `name` field contain?

* A. User name
* B. Model name
* C. Tool name
* D. Session name

✅ **Answer: C. Tool name**

***

## 4. Where are tool arguments stored?

* A. output
* B. schema
* C. name
* D. input

✅ **Answer: D. input**

***

## 5. What indicates Claude wants a tool executed?

* A. stopReason = complete
* B. stopReason = tool\_use
* C. stopReason = stop
* D. stopReason = finish

✅ **Answer: B. stopReason = tool\_use**

***

## 6. What should be sent along with a ToolResult?

* A. Only the result
* B. Only assistant message
* C. Complete conversation history
* D. Nothing else

✅ **Answer: C. Complete conversation history**

***

## 7. Why support multi-part content structures?

* A. Faster execution
* B. Lower cost
* C. Tool and multimodal support
* D. Smaller prompts

✅ **Answer: C. Tool and multimodal support**

***

## 8. Which architecture best describes tool execution?

* A. User → Tool
* B. User → Claude → Tool
* C. User → Claude → Application → Tool → Claude
* D. User → Database

✅ **Answer: C. User → Claude → Application → Tool → Claude**

***

# Exam Tips / Key Takeaways

Remember these interview-worthy concepts:

1. **Tool use is application-mediated** — Claude requests; your app executes.
2. **ToolUse contains three critical fields:**
   * `toolUseId`
   * `name`
   * `input`
3. **Always inspect `stopReason`.**
4. **When `stopReason == "tool_use"`, execute the tool.**
5. **Preserve the entire conversation history.**
6. **Support multi-part messages, not only text.**
7. **Return both text and content parts from helper functions.**
8. **`toolChoice` controls tool invocation behavior.**

# References

* Source page: **Handling tool use responses**
* Course: **Claude with Amazon Bedrock**
* Topic area: **Tool Use / Function Calling / Agent Development**
* Related lessons:
  * Running tool functions
  * Sending tool results
  * Multi-turn conversations with tools
  * Multiple tools
  * MCP Tool Integration

*Content based on the currently open course page “Handling tool use responses”.* [\[Handling t...responses\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276764)
