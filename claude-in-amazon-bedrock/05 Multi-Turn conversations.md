# Multi-Turn conversations

**Source:** Multi-Turn Conversations (Claude with Amazon Bedrock)  
Source page: Multi-Turn conversations [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

# Key Concepts

## 1. Multi-Turn Conversations

A multi-turn conversation means maintaining context across multiple interactions between a user and Claude.

Example:

**Turn 1**

* User: "What's 1+1?"
* Claude: "2"

**Turn 2**

* User: "And 3 more?"

Expected answer:

* Claude: "5"

This only works if the earlier conversation history is provided again in the next API request. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## 2. No Message Storage

A critical concept when using Claude through Amazon Bedrock:

* Bedrock does **not store messages**
* Claude does **not remember previous API calls**
* Every API request is completely independent
* Context is not automatically retained between calls [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

### Implication

If you send:

```text
And 3 more?
```

without previous messages, Claude has no idea what "3 more" refers to. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## 3. Maintaining Conversation Context

To enable multi-turn conversations:

### Step 1: Store messages yourself

Maintain a message list in your application.

```python
messages = []
```

### Step 2: Add every user message

```python
add_user_message(messages, "What's 1+1?")
```

### Step 3: Store Claude's response

```python
add_assistant_message(messages, "2")
```

### Step 4: Send the entire conversation each time

```python
client.converse(
    modelId=model_id,
    messages=messages
)
```

Send all previous messages with each request. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## 4. Message Structure

User messages:

```python
{
    "role": "user",
    "content": [
        {"text": text}
    ]
}
```

Assistant messages:

```python
{
    "role": "assistant",
    "content": [
        {"text": text}
    ]
}
```

Both are stored in the same conversation list. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## 5. Helper Functions

The course recommends helper functions for managing messages.

### Add User Message

```python
def add_user_message(messages, text):
    user_message = {
        "role": "user",
        "content": [{"text": text}]
    }
    messages.append(user_message)
```

### Add Assistant Message

```python
def add_assistant_message(messages, text):
    assistant_message = {
        "role": "assistant",
        "content": [{"text": text}]
    }
    messages.append(assistant_message)
```

### Chat Function

```python
def chat(messages):
    response = client.converse(
        modelId=model_id,
        messages=messages
    )

    return response["output"]["message"]["content"][0]["text"]
```

These helper functions simplify conversation management. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## 6. Conversation Workflow

Typical process:

```text
1. Create message list
2. Add user message
3. Call Claude
4. Save Claude response
5. Add follow-up user message
6. Send complete history again
7. Receive contextual response
```

This pattern enables stateful conversations on top of a stateless API. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## 7. Message Role Alternation

Claude requires roles to alternate properly.

Valid pattern:

```text
user
assistant
user
assistant
user
assistant
```

Invalid patterns:

```text
user
user
assistant
```

or

```text
assistant
assistant
user
```

Always alternate roles to match natural conversation flow and API requirements. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

# Architecture Summary

```text
User
  ↓
Application
  ↓
Store messages locally
  ↓
Build complete history
  ↓
Bedrock Converse API
  ↓
Claude Response
  ↓
Store response locally
  ↓
Next Request Includes Entire History
```

***

# Q\&A

### Q1. Does Claude automatically remember previous API calls?

**Answer:** No. Claude does not store or remember previous messages. Every API call is independent. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

### Q2. Why might Claude misunderstand a follow-up question?

**Answer:** Because the previous conversation context was not included in the request. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

### Q3. Who is responsible for maintaining conversation history?

**Answer:** The application developer must maintain and resend the message history. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

### Q4. What must be sent with every follow-up request?

**Answer:** The complete conversation history (user and assistant messages). [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

### Q5. Why use helper functions?

**Answer:** To simplify creation and management of user and assistant messages. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

### Q6. What message role sequence is required?

**Answer:**

```text
user → assistant → user → assistant
```

Roles should alternate properly. [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

# Quiz

## Question 1

Where does Claude store previous messages?

A. In Bedrock  
B. In Claude Memory  
C. In a Database Automatically  
D. Nowhere

✅ **Answer: D. Nowhere** [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## Question 2

To maintain context across requests, what must developers do?

A. Enable memory mode  
B. Re-send conversation history  
C. Use system prompts only  
D. Enable caching

✅ **Answer: B. Re-send conversation history** [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## Question 3

What happens if only "And 3 more?" is sent?

A. Claude always answers 5  
B. Claude remembers automatically  
C. Claude lacks context and may respond incorrectly  
D. The request fails

✅ **Answer: C. Claude lacks context and may respond incorrectly** [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## Question 4

Which role sequence is valid?

A.

```text
user
user
assistant
```

B.

```text
assistant
assistant
user
```

C.

```text
user
assistant
user
assistant
```

D.

```text
user
user
user
```

✅ **Answer: C** [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## Question 5

What is the main purpose of the `messages` list?

A. Store model weights

B. Store API keys

C. Store conversation history

D. Store embeddings

✅ **Answer: C. Store conversation history** [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

## Question 6

Which API call is used in the examples?

A. `client.chat()`

B. `client.generate()`

C. `client.converse()`

D. `client.run()`

✅ **Answer: C. `client.converse()`** [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

***

# References

* Anthropic Partners Training – Claude in Amazon Bedrock
* Module: **Working with the API**
* Lesson: **Multi-Turn Conversations** [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)

# Key Takeaway

**Claude on Bedrock is stateless. To build conversational applications, your application must store and resend the complete conversation history for every request while maintaining proper role alternation (user ↔ assistant).** [\[Multi-Turn...versations\]](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock/276722)
