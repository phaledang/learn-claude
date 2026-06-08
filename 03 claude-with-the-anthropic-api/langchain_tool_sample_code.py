### packages
# pip install langchain langchain-anthropic python-dotenv
###
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# ----------------------------
# 1. Define tools
# ----------------------------

@tool
def get_current_time() -> str:
    """Return the current system time."""
    import datetime
    return datetime.datetime.now().isoformat()

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


# ----------------------------
# 2. Define prompt
# ----------------------------

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can use tools."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])


# ----------------------------
# 3. Create model
# ----------------------------

llm = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    temperature=0
)


# ----------------------------
# 4. Create agent (auto tool loop)
# ----------------------------

tools = [get_current_time, add_numbers]

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)


# ----------------------------
# 5. Executor (THIS = loop controller)
# ----------------------------

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True   # show reasoning + tool calls
)


# ----------------------------
# 6. Run (multi-turn auto handling)
# ----------------------------

result = agent_executor.invoke({
    "input": "What time is it and what is 25 + 17?"
})

print(result["output"])
