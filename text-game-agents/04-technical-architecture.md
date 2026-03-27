# Technical Architecture — Building Text-Game Practice Agents

> **Part of:** Building AI Text-Game Practice Agents
> **Section:** 4 of 5 | **Confidence:** High on architectural patterns; Medium on dating-specific eval

---

## 1. Existing Agents — State of the Art

### 1A. Open-Source Reference Projects

#### talk-to-girlfriend-ai (Most Relevant Reference)
**GitHub:** https://github.com/arlanrakh/talk-to-girlfriend-ai | ⭐ 512 stars

The most directly relevant open-source project — a production-grade text-game agent deployed via Telegram.

| Layer | Technology |
|---|---|
| **LLM** | Claude Sonnet |
| **Search** | Nia semantic search |
| **Interface** | Telegram MCP (bot bridge) |
| **Language** | Python/TypeScript |

**Features:** Smart reply suggestions, 500+ pickup lines, dating guides, message enhancement. The project description notes: "We broke up after this" — a wry comment on effectiveness.

**Architecture insight:** Uses a CLI agent bridged to Telegram via Claude Sonnet, with a semantic search layer for pickup lines. This is the closest published reference to a production text-game agent.

---

#### Character-LLM (EMNLP 2023)
**GitHub:** https://github.com/choosewhatulike/trainable-agents | Paper: EMNLP 2023

Trains LLaMA-based agents with specific personalities and experiences using Experience Reconstruction.

| Detail | Value |
|---|---|
| **Training approach** | Weight diffs on LLaMA; experience reconstruction |
| **Characters trained** | Cleopatra, Voldemort, Spartacus, Hermione, Newton, Caesar, Beethoven, Socrates, Martin Luther King |
| **Scenes** | ~1.6K scenes, ~750K words per character |
| **Data** | 9 characters |

**Architecture insight:** Demonstrates how to train agents with persistent personality states. Relevant for building dating personas with consistent character traits across conversations.

---

#### in-bed-ai (Novel Research Platform)
**GitHub:** https://github.com/geeks-accelerator/in-bed-ai

A "dating platform where AI agents create profiles, swipe, match, chat, and form relationships." Human users browse AI profiles and read conversation transcripts. Not a practice tool but an interesting research testbed for agent-to-agent dating dynamics.

---

#### BanterBox (Open-Source Dating Simulator)
**GitHub:** https://github.com/Chukwuderah/BanterBox

Open-source Next.js project for conversation practice and dating simulator AI. Free AI coach. Demonstrates that open-source dating AI is technically achievable with standard web frameworks.

---

### 1B. Commercial Platforms with Relevant Features

| Platform | Relevant For |
|---|---|
| **PygmalionAI** (pygmalion.chat) | Open-source AI chat/role-play project; adaptable for dating personas |
| **Nomi.ai** | AI companion with memory, voice, emotional intelligence; demonstrates long-term memory in romantic AI |
| **Blush AI** | Full dating simulator architecture; adaptive evolving personalities; branching narratives |

---

## 2. MVP Architecture (OpenCode Starting Point)

The MVP should be a **minimal viable text-game practice agent** using OpenCode as the starting point — a simple prompt-based LLM wrapper with conversation context, tone selection, and basic safety.

### MVP System Design

```
┌─────────────────────────────────────────────────────────────┐
│                        USER INPUT                           │
│              (message from dating app context)               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   CONTEXT ASSEMBLY                           │
│  • Conversation history (last N messages)                    │
│  • User persona hints (if available)                        │
│  • Partner response style estimate                           │
│  • Situation flags (first message, follow-up, rejection)     │
│  • Cultural context (from user setting)                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   PROMPT TEMPLATE                            │
│  System: "You are a text-game coach. Given a received        │
│  message, suggest replies that are [tone]. Consider:        │
│  [cultural context]. Avoid: [common mistakes]"               │
│  Few-shot examples: from FlirtFlip (gentle/playful/bold)   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   LLM INFERENCE                              │
│         (OpenCode or GPT-4o or Claude Sonnet)               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   OUTPUT VALIDATION                          │
│  • Safety/policy check (no harassment, no illegal)           │
│  • Tone calibration (does reply match selected tone?)        │
│  • Length constraints (realistic message length)             │
│  • Optional: Flirt detection score (from Flirtation model)  │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                     RESPONSE OUTPUT                         │
│              2-3 suggested replies at selected tone          │
└─────────────────────────────────────────────────────────────┘
```

### MVP Tech Stack

| Layer | Technology | Rationale |
|---|---|---|
| **LLM** | OpenCode (via Ollama) or GPT-4o or Claude Sonnet | OpenCode = local, no API cost; cloud = higher quality |
| **Backend** | Python + FastAPI | Simple, well-documented |
| **Context Store** | SQLite or simple JSON file | Minimal persistence for MVP |
| **Training Data** | FlirtFlip (tone shifting), RODD (vocabulary) | Available datasets |
| **Safety** | Simple regex rules + LLM self-check | Minimal safety layer |
| **Interface** | Telegram bot or web chat | Telegram = fastest to ship |

### MVP Prompt Template (Pseudocode)

```
SYSTEM_PROMPT = """
You are a text-game coach. A user is texting someone they're dating.
The person they want to text just sent them this message:
{{received_message}}

The user wants to respond in the tone of: {{tone}}
Cultural context: {{culture}}  # e.g., "United States", "Germany", "France"

Generate 3 reply options that:
1. Sound like a real person, not AI-generated
2. Match the selected tone
3. Are appropriate for the cultural context
4. Are the right length (not too long, not one word)

Avoid:
- Starting with "Hey" or "Hi" - be more creative
- Being over-eager or needy
- Being so brief it seems uninterested
- Generic pickup lines

Format your response as:
1. [reply option 1]
2. [reply option 2]
3. [reply option 3]
"""

USER_PROMPT = """
Received message: {{message}}
Desired tone: {{tone}}
"""
```

### Difficulty Level Implementation in MVP

Map the 3 FlirtFlip intensity levels to agent behavior:

| Level | FlirtFlip Term | Agent Behavior |
|---|---|---|
| **Easy / Gentle** | Respectful, low-key interest | Safe, warm, friendly — minimal risk, minimal reward |
| **Medium / Playful** | Teasing, fun, light flirtation | Playful banter — moderate risk, moderate reward |
| **Hard / Bold** | Direct, high-risk, high-reward | Confident, challenging, sexually forward — high risk, high reward |

Extend with attachment style simulation for advanced difficulty:

| Persona | Response Latency | Message Length | Initiative | Emoji Use |
|---|---|---|---|---|
| **Secure** | Medium (1–3 hrs) | Medium | Balanced | Moderate |
| **Anxious** | Fast (mins) | Long | High | High |
| **Avoidant** | Slow (hours-days) | Short | Low | None |
| **Fearful-Avoidant** | Variable | Mixed | Oscillating | Variable |

---

## 3. Production Architecture (LangChain + LlamaIndex)

For production, the system needs: conversation memory, retrieval-augmented generation (RAG) for dating knowledge, cultural adaptation, persona persistence, and evaluation.

### Production System Design

```
┌──────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                             │
│              (Telegram Bot / Web / WhatsApp / API)               │
└─────────────────────────┬────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION LAYER                            │
│                      LangChain LCEL                               │
│  • Conversation memory (buffer window)                            │
│  • Persona configuration                                          │
│  • Response generation chain                                      │
│  • Safety policy chain                                            │
│  • Cultural context injection                                     │
└──────────┬──────────────────┬───────────────────┬───────────────┘
           │                  │                   │
           ▼                  ▼                   ▼
┌──────────────────┐ ┌───────────────────┐ ┌──────────────────────┐
│   TOOL: RAG      │ │  TOOL: Dating    │ │   TOOL: Safety     │
│  Vector Search   │ │  Knowledge Base  │ │   Policy Check     │
│                  │ │                  │ │                    │
│  • Pickup lines  │ │  • Tips & guides │ │  • LlamaGuard     │
│    indexed by    │ │  • Scenario      │ │  • Content mod     │
│    context       │ │    specific      │ │  • Rate limiting  │
│                  │ │    advice        │ │                    │
└────────┬─────────┘ └─────────┬─────────┘ └──────────┬───────────┘
         │                    │                     │
         ▼                    ▼                     ▼
┌──────────────────────────────────────────────────────────────────┐
│                     VECTOR DATABASE                               │
│              (Pinecone cloud OR Chroma local)                    │
│  • Pickup lines × 500+ indexed by situation/tone/culture         │
│  • Dating advice indexed by scenario                             │
│  • Conversation examples indexed by difficulty                    │
│  • FlirtFlip tone examples indexed                                │
└──────────────────────────────────────────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────────────────────────────────┐
│                       LLM GATEWAY                                 │
│         (Claude Opus 4 / GPT-4o cloud OR                          │
│          Llama 3.1 70B via Ollama/VLLM local)                    │
└──────────────────────────────────────────────────────────────────┘
```

### Production Tech Stack

| Layer | Technology | Alternative |
|---|---|---|
| **Orchestration** | LangChain LCEL or LlamaIndex | AutoGen for multi-agent |
| **Vector DB** | Pinecone (cloud) or Chroma (local) | Qdrant, FAISS |
| **LLM** | Claude Opus 4 / GPT-4o | Llama 3.1 405B via VLLM |
| **Memory** | LangChain ConversationBufferWindowMemory | Zep, Memorial |
| **Safety** | LlamaGuard 2 or OpenAI Moderation API | Perspective API |
| **Interface** | Telegram Bot SDK / Discord.js / FastAPI |  |
| **Evaluation** | LangSmith + RAGAS + DeepEval |  |
| **Fine-tuning** | Axolotl / LLaMA-Factory / TRL |  |

### RAG Sources for Production

| Source | What's Indexed | How Used |
|---|---|---|
| **FlirtFlip** | Transformations at 3 intensity levels | Tone examples in prompt context |
| **RODD** | 219K Reddit dating posts | Topic/vocabulary enrichment |
| **Curated pickup lines** | 500+ lines with situation tags | Retrieval → inject as examples |
| **Dating advice corpus** | Tips, guides, scenario-specific advice | Retrieved by situation type |
| **Cultural norms** (Section 2) | Country-specific texting norms | Cultural adaptation layer |

### Multi-Agent Design for Text-Game

Rather than a single agent, a multi-agent design provides better specialization:

```
┌──────────────────────────────────────────────────────────────┐
│                  USER MESSAGE INPUT                          │
└──────────────────────────┬─────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│               COORDINATOR AGENT                               │
│  • Classifies message type (question/statement/rejection/etc) │
│  • Estimates partner responsiveness (eager/dead/secure)      │
│  • Selects cultural context                                 │
│  • Routes to appropriate specialist agents                   │
└────────────────────┬────────────────────────────────────────┘
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  RESPONSE   │ │   FLIRT      │ │   ESCALATION │
│  AGENT      │ │   AGENT      │ │   AGENT      │
│              │ │              │ │              │
│ For normal  │ │ For sexually  │ │ When user    │
│ back-and-   │ │ charged or    │ │ wants to     │
│ forth       │ │ playful msgs  │ │ escalate to  │
│              │ │              │ │ date/phone   │
└──────────────┘ └──────────────┘ └──────────────┘
       │             │             │
       └─────────────┼─────────────┘
                     ▼
┌──────────────────────────────────────────────────────────────┐
│               SYNTHESIS AGENT                                 │
│  • Takes responses from specialists                           │
│  • Ranks by appropriateness for context                       │
│  • Applies final safety check                                │
│  • Returns 2-3 options to user                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 4. Cultural Adaptation Layer

Architecture for supporting multiple cultures:

```python
CULTURAL_NORMS = {
    "united_states": {
        "response_speed": "fast",  # minutes expected
        "emoji_density": "high",
        "double_text": "accepted",
        "formality": "casual",
        "hot_threshold": 3,  # how "hot" a message can be (1-10 scale)
        "message_length": "medium",
        "ghosting_tolerance": "moderate",
    },
    "germany": {
        "response_speed": "measured",
        "emoji_density": "low",
        "double_text": "avoid",
        "formality": "direct",
        "hot_threshold": 4,
        "message_length": "short",
        "ghosting_tolerance": "low",
    },
    "scandinavia": {
        "response_speed": "slow",  # hours/days normal
        "emoji_density": "low",
        "double_text": "avoid",
        "formality": "informal",
        "hot_threshold": 5,
        "message_length": "short",
        "ghosting_tolerance": "very_low",
    },
    "france": {
        "response_speed": "strategic",
        "emoji_density": "moderate",
        "double_text": "selective",
        "formality": "romantic",
        "hot_threshold": 6,
        "message_length": "long",
        "ghosting_tolerance": "low",
    },
    "spain_italy": {
        "response_speed": "fast",
        "emoji_density": "high",
        "double_text": "accepted",
        "formality": "warm",
        "hot_threshold": 7,
        "message_length": "long",
        "ghosting_tolerance": "low",
    },
    "latin_america": {
        "response_speed": "fast",
        "emoji_density": "very_high",
        "double_text": "accepted",
        "formality": "warm",
        "hot_threshold": 7,
        "message_length": "long",
        "ghosting_tolerance": "low",
    },
}
```

This cultural config is injected into the system prompt and affects:
- Recommended response latency (for simulation)
- Emoji usage guidelines
- Message length expectations
- "Hot text" threshold
- Double-text appropriateness

---

## 5. Evaluation Framework

### 5A. Multi-Layer Evaluation

| Layer | Metrics | How to Measure |
|---|---|---|
| **Task Outcome** | Response appropriateness (1–5), goal achievement (date/get number) | Human eval, LLM-as-judge |
| **Conversation Quality** | Engagement score, flirt intensity, coherence, persona consistency | Multi-turn automated eval |
| **Safety** | Policy violations, off-topic rate | Automated + human review |
| **Cultural Accuracy** | Does response match cultural norms for target country? | LLM-as-judge with cultural rubrics |

### 5B. Conversational Agent Metrics

| Metric | Description | Measurement |
|---|---|---|
| **Conversation Relevancy** | Does response address the message? | LLM judge or human eval |
| **Completeness** | Does response fully address intent? | LLM judge |
| **Role Adherence** | Consistent persona/personality? | Human eval |
| **Knowledge Retention** | Remembers conversation history? | Automated trace check |
| **Flirt Detection Score** | Classifier score on generated responses | Fine-tuned flair classifier |
| **Toxicity Score** | Safety measurement | LlamaGuard / Perspective API |
| **Cultural Match Score** | Does response match cultural norms? | LLM judge with cultural rubric |

### 5C. Human Evaluation Protocol

1. **A/B Testing:** Real users compare responses in actual conversations (gold standard)
2. **Scenario Coverage:** Test across 10+ dating situations (first message, follow-up, rejection response, etc.)
3. **Partner Rating:** Have human "receivers" (actors or paid participants) rate the attractiveness of AI-suggested messages
4. **Success Metrics:** Response rate, conversation continuation, date requests (tracked via user opt-in)

### 5D. Reference: Taming Complexity Evaluation Framework (Microsoft)

Source: https://devblogs.microsoft.com/ise/intuitive-evaluation-framework-for-agentic-chatbots/

Applied to text-game agents:

| Framework Component | Text-Game Application |
|---|---|
| Line of Business agents | Dating-specific persona (anxious/avoidant/secure) |
| Task outcomes | Successful conversation progression (depth, escalation) |
| Conversation quality | Flirt engagement, response timing, tone consistency |
| System reliability | Response latency, availability |

---

## 6. Key Libraries and Tools

| Purpose | Library | Notes |
|---|---|---|
| **Orchestration** | LangChain, LlamaIndex | LangChain LCEL for agentic chains |
| **Vector DB** | Pinecone, Chroma, FAISS, Qdrant | Chroma for local MVP; Pinecone for production |
| **LLM Hosting** | Ollama, vLLM, TGI | Ollama for local dev; TGI for production |
| **Chat Interface** | Telegram Bot API, Discord.js | Telegram fastest to ship MVP |
| **Eval** | RAGAS, DeepEval, LangSmith | LangSmith for tracing; RAGAS for RAG quality |
| **Fine-tuning** | Axolotl, LLaMA-Factory, TRL | QLoRA for efficient fine-tuning |
| **Safety** | LlamaGuard 2, Perspective API | LlamaGuard for content policy |
| **Memory** | LangChain memory, Zep | Zep for production-scale conversation memory |

---

## 7. Sources

| Source | URL | Quality |
|---|---|---|
| talk-to-girlfriend-ai (GitHub) | https://github.com/arlanrakh/talk-to-girlfriend-ai | High (real implementation) |
| Character-LLM (GitHub) | https://github.com/choosewhatulike/trainable-agents | High (EMNLP 2023 paper) |
| in-bed-ai (GitHub) | https://github.com/geeks-accelerator/in-bed-ai | Medium (research platform) |
| BanterBox (GitHub) | https://github.com/Chukwuderah/BanterBox | Medium (open-source) |
| Microsoft Eval Framework | https://devblogs.microsoft.com/ise/intuitive-evaluation-framework-for-agentic-chatbots/ | High (Microsoft) |
| LangChain | https://langchain-tutorials.github.io/when-use-langchain-llamaindex-rag-agents-or-both/ | High (documentation) |
| PygmalionAI | https://pygmalion.chat/ | Medium (open-source project) |
