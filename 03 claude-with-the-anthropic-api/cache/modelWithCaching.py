import { ChatAnthropic } from "@langchain/anthropic";

const modelWithCaching = new ChatAnthropic({
  model: "claude-sonnet-4-6",
});

const LONG_TEXT = `You are a pirate. Always respond in pirate dialect.

Use the following as context when answering questions:

${CACHED_TEXT}`;

const messages = [
  {
    role: "system",
    content: [
      {
        type: "text",
        text: LONG_TEXT,
        // Tell Anthropic to cache this block
        cache_control: { type: "ephemeral" },
      },
    ],
  },
  {
    role: "user",
    content: "What types of messages are supported in LangChain?",
  },
];

const res = await modelWithCaching.invoke(messages);

console.log("USAGE:", res.response_metadata.usage);
