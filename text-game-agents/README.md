# Building AI Text-Game Practice Agents

**Research Objective:** Understand the text-game practice tool ecosystem, how to build AI agents for dating conversation practice, available datasets, difficulty level frameworks, and cultural tuning approaches.

**Completed:** March 27, 2026  
**Confidence:** High on product landscape and technical architecture; Medium on community signal and cultural dimensions

---

## Document Map

| # | Document | What It Covers |
|---|---|---|
| **01** | [Product Landscape](./01-product-landscape.md) | getcomposed.io deep-dive, 25+ alternatives across 4 categories, competitive analysis, community reception |
| **02** | [Community Signal & Difficulty](./02-community-terminology-difficulty.md) | "Eager/dead texter" terminology, PUA community frameworks, attachment theory as difficulty model, academic difficulty research, cross-cultural norms overview |
| **03** | [Datasets & Training Data](./03-datasets-training-data.md) | 7 relevant datasets inventoried, FlirtFlip and RODD deep-dive, training suitability assessment, cross-cultural multilingual datasets, data strategy for agents |
| **04** | [Technical Architecture](./04-technical-architecture.md) | MVP architecture (OpenCode/GPT-4o), production LangChain RAG system, multi-agent design, cultural adaptation implementation, evaluation framework |
| **05** | [Cultural Dimensions](./05-cultural-dimensions.md) | Detailed texting norms for 7 cultural regions (US, UK, DE, FR, ES/IT, Scandinavia, Latin America), difficulty matrix, practical implementation reference |
| **06** | [Final Synthesis & Roadmap](./06-final-synthesis-roadmap.md) | Integration summary, build roadmap (3 phases), data strategy, open questions, full source consolidation |

---

## Quick-Reference Findings

### Product Landscape
- **getcomposed.io:** GPT-4 wrapper + Supabase + Stripe; $9/mo; tone picker (3 levels); The Lab community feature; no fine-tuning
- **MGAI:** Closest competitor; $24.99/mo; Ice White personality; Telegram/Messenger; 4.5-min retraining cycle
- **Blush AI:** Full dating simulator with AI characters; Linden Lab acquisition (Aug 2025); architecturally different
- **Wingman.live:** Full coach; profile photo scoring; uncensored chatbot
- **25+ tools total** in the market; no dominant leader; most launched 2023–2025

### Key Datasets
| Dataset | Best Use | Rows |
|---|---|---|
| **FlirtFlip** | Tone training (gentle/playful/bold) | 1K |
| **RODD** | Topic vocabulary, persona extraction | 219K |
| **Tinder Flirtation** | Flirtation classification | 5.8K |
| **XDailyDialog** | Cross-lingual (EN/ZH/DE/RU) | 13K dialogues |

### Difficulty Level Framework
- **FlirtFlip 3-level system** → best existing proxy for difficulty
- **Attachment theory** → secure/anxious/avoidant/fearful-avoidant → maps to texting responsiveness
- **Academic research** → response timing, emoji density, reciprocity all measurable
- **Community terms** → eager texter (≈anxious), dead texter (≈avoidant)

### Cultural Tuning Priority
| Priority | Culture | Key Challenge |
|---|---|---|
| 1 | US | Baseline — establish quality here first |
| 2 | Germany | Directness clashes with US norms |
| 3 | France | Charm-first, slow escalation |
| 4 | Scandinavia | Inverted signaling (slow reply = respect, not disinterest) |
| 5 | UK | Indirectness and banter-first |
| 6 | Spain/Italy | High passion, family dynamics |
| 7 | Latin America | High passion, regional variation |

### Build Roadmap Summary
- **Phase 1 (MVP, weeks 1–6):** OpenCode/GPT-4o + tone picker + 2–3 cultural configs + Telegram/web chat
- **Phase 2 (months 2–4):** User data collection + RAG layer (Chroma) + evaluation framework + fine-tuning experiments
- **Phase 3 (months 4–8):** Multi-agent system (coordinator + Response/Flirt/Escalation specialists) + persona fine-tunes + all 7 cultural regions

---

## Top Open Questions for Further Research

1. **Community dynamics:** Will the seduction/pickup community eventually adopt these tools, or is the market entirely mainstream dating advice consumers?
2. **Ethical boundaries:** Where is the line between practice and manipulation? How should a text-game agent be designed to support authentic communication rather than deception?
3. **Non-Western data:** Japanese, Korean, Arabic, and South Asian texting norms are almost entirely undocumented in the literature — significant gap for a global product.
4. **Long-term engagement:** How do you retain users who improve? Is the product a "graduation" tool or a persistent practice environment?
