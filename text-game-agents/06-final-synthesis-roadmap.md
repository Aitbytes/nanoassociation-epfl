# Building Text-Game Practice Agents — Final Synthesis & Roadmap

> **Part of:** Building AI Text-Game Practice Agents
> **Section:** 6 of 6 | **Confidence:** High on technical/product; Medium on cultural/datasets

---

## 1. What Was Built — Research Summary

This six-part research report covers the full landscape of building AI text-game practice agents:

| Section | Topic | Key Finding |
|---|---|---|
| **1** | Product Landscape | 25+ tools exist; getcomposed.io is a simple GPT wrapper at $9/mo; the field has no dominant leader |
| **2** | Community Signal | The seduction community hasn't adopted these tools; "eager/dead texter" terminology maps to attachment theory; academic research supports response timing, emoji use, and reciprocity |
| **3** | Datasets | 7 relevant datasets found; best for tone training is FlirtFlip (3 intensity levels); no dataset provides conversation pairs with difficulty labels across cultures |
| **4** | Technical Architecture | MVP = prompt-based LLM with tone selector + cultural config; Production = LangChain RAG + multi-agent + persona fine-tuning |
| **5** | Cultural Dimensions | 7 cultural regions documented with actionable norms; Scandinavia and France are hardest for Americans; Germany and Scandinavia are hardest for everyone |
| **6** | This document | Integration roadmap, open questions, and strategic priorities |

---

## 2. The Core Opportunity

### What the Research Reveals

1. **The market is fragmented.** No single tool dominates. Most tools launched 2023–2025. The category is still nascent.

2. **The seduction community is NOT the market.** Reddit communities (r/seduction, r/pickup, r/textgame) show no visible adoption of AI tools. The actual users are presumably more mainstream — people who want help but don't identify with PUA culture.

3. **Cultural tuning is the clearest differentiation opportunity.** Every tool in the market is US-centric. A text-game agent that actually adapts to German directness, Scandinavian reserve, or French charm-first norms would be genuinely novel.

4. **Data is the moat.** The existing datasets are insufficient for training production agents, but the mechanism for acquiring data is clear: track which suggested replies users select, edit, or ignore → build a proprietary conversation-pair dataset → fine-tune on it → improve → collect more data.

5. **Difficulty levels are implementable but unlabeled.** The FlirtFlip 3-level system (gentle/playful/bold) provides the best existing proxy for difficulty. Attachment theory (secure/anxious/avoidant) provides a psychologically grounded taxonomy for persona types.

---

## 3. Recommended Build Roadmap

### Phase 1: MVP (Weeks 1–6)

**Goal:** Ship a working text-game practice agent with tone selection and cultural adaptation.

| Week | Deliverable |
|---|---|
| 1–2 | Set up OpenCode or GPT-4o via Ollama; build basic web chat interface or Telegram bot; implement conversation history context |
| 3–4 | Implement tone picker (Light+Flirty / Bold+Chill / Warm+Grounded); build prompt templates with FlirtFlip few-shot examples |
| 5 | Add 2–3 cultural configs (US baseline, Germany, France); implement basic safety check |
| 6 | User testing with 5–10 beta users; collect feedback on response quality |

**Phase 1 Stack:**
- Python + FastAPI
- OpenCode or GPT-4o via Ollama
- Telegram bot or simple web chat
- FlirtFlip + RODD as prompt context
- SQLite for conversation history

**Success criteria:** Agent generates 2–3 contextually appropriate replies per input; tone selection measurably changes output; cultural config measurably changes output.

---

### Phase 2: Data Flywheel (Months 2–4)

**Goal:** Build proprietary dataset from user interactions; implement evaluation system.

| Month | Deliverable |
|---|---|
| 2 | Track which suggested replies users pick, edit, or ignore; build analytics dashboard; start accumulating conversation pairs |
| 3 | Implement RAG layer with cultural knowledge base; connect vector DB (Chroma); start building cultural knowledge base from Section 5 norms |
| 3–4 | Implement evaluation framework: LLM-as-judge for response quality; safety scoring; cultural appropriateness scoring |
| 4 | Start fine-tuning experiments: fine-tune Llama 3.1 8B on FlirtFlip + synthetic data per persona type |

**Phase 2 Stack:**
- LangChain LCEL for orchestration
- Chroma for vector DB
- LangSmith for tracing and evaluation
- Axolotl for fine-tuning experiments
- Telegram + web chat (both)

**Success criteria:** 500+ conversation pairs collected; fine-tuned model outperforms base model on tone accuracy; evaluation framework operational.

---

### Phase 3: Multi-Agent Production (Months 4–8)

**Goal:** Implement full multi-agent system with specialist agents, long-term memory, and cultural depth.

| Month | Deliverable |
|---|---|
| 4–5 | Implement coordinator agent + specialist agents (response, flirt, escalation); implement memory layer (Zep or LangChain); build cultural config for all 7 regions |
| 5–6 | Implement LlamaGuard for safety; build user feedback loop (rate responses, report outcomes); start A/B testing tone configurations |
| 6–8 | Fine-tune persona-specific models (LoRA adapters for secure/anxious/avoidant personas); implement regional variant agents (DE, FR, SE); conduct user study measuring actual dating outcomes |

**Phase 3 Stack:**
- LangChain multi-agent (coordinator + specialists)
- Pinecone for production vector DB
- Claude Opus 4 or GPT-4o for quality-sensitive calls
- Llama 3.1 405B via VLLM for cost-sensitive calls
- Zep for conversation memory
- Production web + Telegram interface

**Success criteria:** Multi-agent system operational with measurable quality improvement over single-agent; cultural variants measurably outperform US-only agent for non-US users; positive user-reported dating outcomes.

---

## 4. Technical Architecture Summary

### MVP (Phase 1)

```
User message → Context assembly (history, tone, culture) 
  → Prompt template (FlirtFlip examples + cultural config) 
  → LLM (OpenCode/GPT-4o) 
  → Safety check 
  → 2-3 replies
```

### Production (Phase 3)

```
User message → Coordinator agent 
  → Routes to specialist (Response / Flirt / Escalation)
  → RAG retrieval (cultural knowledge base, pickup lines, FlirtFlip examples)
  → LLM (Claude Opus 4 or Llama 3.1 405B)
  → LlamaGuard safety check
  → Synthesis agent
  → Ranked replies + explanation
```

---

## 5. Data Strategy Summary

| Phase | Data Source | Use |
|---|---|---|
| **MVP** | FlirtFlip (tone), RODD (vocabulary), Section 5 cultural norms | Few-shot examples in prompts |
| **Phase 2** | User interaction data (which replies selected/edited/ignored) | Proprietary fine-tuning dataset |
| **Phase 3** | Synthetic data generated per persona type (secure/anxious/avoidant) | Persona fine-tuning |
| **Ongoing** | The Lab-style community sharing (if community forms) | Community flywheel |

**Most important dataset gap:** No conversation-pair dataset with difficulty labels exists publicly. The path to filling this is proprietary data collection through user interactions, not finding a public dataset.

---

## 6. Cultural Implementation Priority

For a global text-game agent, prioritize cultural implementation in this order:

| Priority | Culture | Rationale |
|---|---|---|
| 1 | **US baseline** | Default; establish quality bar here first |
| 2 | **Germany** | Clear, low-context, well-documented; easier to implement than romantic cultures |
| 3 | **France** | High-value market; charm-first requires specific prompt engineering |
| 4 | **Scandinavia** | Hardest for US users to understand; most differentiated content |
| 5 | **UK** | US-adjacent but with meaningful differences; lower lift from US baseline |
| 6 | **Spain/Italy** | High emotional expression familiar to Americans; family dynamics add complexity |
| 7 | **Latin America** | High emotional expression familiar; cultural nuance within region limits dataset scale |

---

## 7. Open Questions

1. **Community adoption:** Will the target users come from the seduction community, mainstream dating advice consumers, or somewhere else? This affects content tone, feature prioritization, and marketing.

2. **Monetization beyond subscription:** Composed charges $9/mo. MGAI charges $24.99/mo with a book bundle. What's the right model for an agent that also collects data and improves over time?

3. **Privacy and trust:** The 2024 FlirtAI data breach (160K chat screenshots exposed) is a category-wide risk. How should a new entrant build trust before users share real conversations?

4. **Ethical considerations:** At what point does a text-game agent enable manipulation rather than authentic communication? Where is the line between helpful practice and deceptive behavior?

5. **Language coverage:** The research focused on English and European languages. What about Arabic, Japanese, Korean, and Hindi markets — both in terms of cultural norms and available training data?

6. **Long-term engagement:** How does the product keep users practicing once they improve? Is the product a "graduation" tool (users outgrow it) or a persistent practice environment?

---

## 8. Consolidated Source List

### Products Researched

| Product | URL | Confidence |
|---|---|---|
| getcomposed.io | https://getcomposed.io/ | High |
| MGAI | https://www.gameglobal.net/products/mgai/ | High |
| Blush AI | https://blushai.app/landing | High |
| Wingman.live | https://wingman.live/ | High |
| Wit Dating AI | https://witdating.com/ | High |
| Rizzagic AI | https://www.rizzagic.ai/ | High |
| YouRizzAI | https://yourizzai.com/ | High |
| BanterBox | https://bntrbox.com/ | High |

### Datasets

| Dataset | URL | Best Use |
|---|---|---|
| FlirtFlip | https://huggingface.co/datasets/shirshatzman/flirtflip-dataset | Tone/intensity training |
| RODD | https://huggingface.co/datasets/FabianLeibinger/Reddit-Online-Dating-Dataset-RODD | Topic/vocabulary enrichment |
| Tinder Flirtation | https://github.com/alyssafrndz/Flirtation-analysis | Flirtation classification |
| Flirty Conversations | https://huggingface.co/datasets/mylesfriedman30/flirty_conversations_dataset | Multi-turn format |
| XDailyDialog | https://aclanthology.org/2023.acl-long-684/ | Cross-lingual dialogue |

### Existing Agents

| Project | URL | Relevance |
|---|---|---|
| talk-to-girlfriend-ai | https://github.com/arlanrakh/talk-to-girlfriend-ai | Most relevant reference |
| Character-LLM | https://github.com/choosewhatulike/trainable-agents | Persona training methodology |
| in-bed-ai | https://github.com/geeks-accelerator/in-bed-ai | Research platform |

### Academic Research

| Study | URL | Quality |
|---|---|---|
| Teichmann et al. (2026) JSPR — texting timing | https://doi.org/10.1177/02654075251377184 | High (peer-reviewed) |
| Huh (2025) PLOS ONE — emoji responsiveness | https://doi.org/10.1371/journal.pone.0326189 | High (peer-reviewed) |
| Jurafsky EMNLP 2009 — flirt detection | https://aclanthology.org/D09-1035.pdf | High (peer-reviewed) |
| PMC LDR texting (2021) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8669216/ | High (peer-reviewed) |
| Microsoft agent eval framework | https://devblogs.microsoft.com/ise/intuitive-evaluation-framework-for-agentic-chatbots/ | High |

---

## 9. Research Provenance

| Metric | Value |
|---|---|
| **Products analyzed** | 25+ across 4 categories |
| **Datasets inventoried** | 7 relevant datasets |
| **Countries covered** | 7 cultural regions (US, UK, DE, FR, ES/IT, Scandinavia, Latin America) |
| **Academic sources** | 5 peer-reviewed studies |
| **Open-source projects** | 4 reference implementations |
| **Total sources** | 40+ primary and secondary sources |
| **Waves of research** | 3 full waves + 3 experiments |
| **Documents produced** | 6 sections |
