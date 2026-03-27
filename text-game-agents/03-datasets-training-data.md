# Text-Game Agent Training — Available Datasets

> **Part of:** Building AI Text-Game Practice Agents
> **Section:** 3 of 5 | **Confidence:** High on dataset existence; Medium on detailed schemas

---

## 1. Datasets Inventory

Seven relevant datasets found. Overall assessment: **useful for specific sub-tasks but insufficient for full text-game agent training.** No dataset provides conversation pairs with difficulty labels across cultures.

### Dataset 1: Flirtation-analysis (Tinder Messages)

| Attribute | Details |
|---|---|
| **URL** | https://github.com/alyssafrndz/Flirtation-analysis |
| **Stars** | 10 |
| **Training Size** | ~2,800 unique messages |
| **Test Size** | ~3,000 messages |
| **Source** | Tinder messages from swipestats.io (personal data shared by Kris from boe.ventures) |
| **Schema** | `polarity` (0–1 continuous float), `final_messages` (text) |
| **Labels** | Continuous polarity score: 0 = no flirtation, 1 = flirtation; human-rated by a single rater |
| **Gender mix** | 50/50 male/female |
| **Conversation pairs** | **No** — single messages only, no context/response pairs |

**Suitability assessment:**
- **Flirtation classification:** High — continuous human-rated labels on real Tinder messages
- **Training text-game agents:** Low — too small, no conversational turns, no response type labels
- **Difficulty levels:** The polarity score (0–1) approximates "flirty intensity" but not "hardness to respond to" or "required skill level"

---

### Dataset 2: Reddit Online Dating Dataset (RODD)

| Attribute | Details |
|---|---|
| **URL** | https://huggingface.co/datasets/FabianLeibinger/Reddit-Online-Dating-Dataset-RODD |
| **Size** | 219,000 rows |
| **License** | MIT |
| **Format** | CSV |
| **Language** | English |
| **Schema** | `id`, `title`, `selftext`, `created_utc`, `subreddit`, `permalink`, `url`, `num_comments`, `score`, `ups`, `downs`, `upvote_ratio`, `is_crosspostable`, `link_flair_text`, `thumbnail`, `author`, `domain`, `extraction_keywords` |
| **Source subreddits** | r/dating_advice, r/dating, r/OnlineDating, r/datingoverthirty, r/datingoverforty, r/datingoverfifty, r/AskMen, r/AskWomen, r/TwoXChromosomes |
| **Labels** | `link_flair_text` (Reddit category labels); `extraction_keywords` (tinder, bumble, hinge tags); sentiment via vote scores |
| **Conversation pairs** | **No** — individual Reddit submissions (title + selftext), not message exchanges |
| **Overall tone** | Negative — dating fatigue, advice-seeking, negative experiences |

**Suitability assessment:**
- **Topic modeling / persona extraction:** High — 219K posts covering full range of dating topics
- **Training text-game agents:** Medium — large corpus of dating discourse, monologues not dialogues
- **Difficulty levels:** `link_flair_text` provides categories (topic/sentiment) but not difficulty of interaction
- **Note:** This is monologues (advice-seeking posts), not dialogues. No sender→receiver structure.

---

### Dataset 3: FlirtFlip

| Attribute | Details |
|---|---|
| **URL** | https://huggingface.co/datasets/shirshatzman/flirtflip-dataset |
| **Size** | 1,071 examples |
| **Format** | CSV |
| **Language** | English |
| **Schema** | `id`, `scenario`, `original` (original phrase), `gentle`, `playful`, `bold` (three flirt intensity levels) |
| **Labels** | 40 social scenarios; 3 flirt styles (gentle/playful/bold) |
| **Conversation pairs** | **No** — single phrase transformations (original → 3 intensity levels) |

**Suitability assessment:**
- **Message transformation training:** High — transforms everyday phrases into charming/flirty versions at 3 intensity levels
- **Training text-game agents:** Moderate — good for teaching tone-shifting; no conversational context
- **Difficulty levels:** The 3-level gentle/playful/bold system provides a crude difficulty/tone ladder directly usable in agent prompting
- **Best use:** Teach agents to modulate message intensity based on context

---

### Dataset 4: Flirty Conversations Dataset

| Attribute | Details |
|---|---|
| **URL** | https://huggingface.co/datasets/mylesfriedman30/flirty_conversations_dataset |
| **Size** | 500 rows |
| **Format** | Parquet |
| **Language** | English |
| **Schema** | Multi-turn conversations in `[INST]` format (Llama-style chat template) |
| **Labels** | None (conversational context only) |
| **Conversation pairs** | **Yes** — multi-turn conversations |

**Suitability assessment:**
- **Multi-turn conversation format:** Moderate — Llama-style format directly usable for training
- **Training text-game agents:** Moderate — provides conversational structure, but not specifically from dating apps
- **Difficulty levels:** None

---

### Dataset 5: FlirtationFeatureSet

| Attribute | Details |
|---|---|
| **URL** | https://huggingface.co/datasets/traltyaziking/FlirtationFeatureSet |
| **Size** | 100 rows |
| **Format** | CSV |
| **Schema** | `idx`, `Transcript`, `Label` |
| **Labels** | 15 label types: Playful Banter, Light-hearted Flirtation, Subtle Seduction, Intimate Inquiry, etc. |
| **Conversation pairs** | No |
| **Quality concerns** | AI-generated dataset; small size; limited diversity |

**Suitability assessment:**
- **Flirt intensity classification:** Low — AI-generated, too small, limited diversity
- **Label taxonomy:** Useful for defining categories of flirtation style (can inspire agent persona types)

---

### Dataset 6: Speed Dating Dataset (Columbia Fisman & Iyengar)

| Attribute | Details |
|---|---|
| **Sources** | Kaggle (annavictoria/speed-dating-experiment), GitHub (dafrd/speed-dating) |
| **Original** | Columbia Business School experiments 2002–2004 |
| **Size** | ~8,378 participants, ~500–1,000+ speed dates |
| **Schema** | Demographics, preferences, race, age, activity, attribute ratings, partner ratings, match outcomes |
| **Labels** | `match` (binary), partner ratings, preference ratings |
| **Text data** | None — structured experimental data only |
| **Conversation pairs** | **No** |

**Suitability assessment:**
- **Preference modeling:** High — rich structured data on mate selection
- **Training text-game agents:** Very Low — no conversational text, structured experimental data only

---

### Dataset 7: Jurafsky et al. EMNLP 2009 — SpeedDate Corpus

| Attribute | Details |
|---|---|
| **Paper** | "It's Not You, It's Me: Detecting Flirting and its Impact" — EMNLP 2009 |
| **URL** | https://aclanthology.org/D09-1035.pdf |
| **Dataset** | SpeedDate Corpus (3 sessions at American university, 2005) |
| **Key finding** | Detected flirting with **71.5% accuracy** using prosodic, dialogue, and lexical features |
| **Labels** | Flirtatious vs. non-flirtatious perception |
| **Text vs. audio** | Audio/prosodic features; lexical features transferable to text |

**Suitability assessment:**
- **Flirt detection benchmark:** High — academic benchmark, 71.5% accuracy is a meaningful baseline
- **Training text-game agents:** Moderate — lexical features (word choice patterns, question-asking, etc.) transferable

---

## 2. Training Suitability Summary

| Dataset | Size | Realistic Conversations | Flirt Labels | Multi-turn | Difficulty Labels | Best Use |
|---|---|---|---|---|---|---|
| Flirtation-analysis (Tinder) | 5.8K | Yes | Continuous 0–1 | No | Partial (flirty intensity) | Binary/continuous flirt classification |
| RODD | 219K | Partial (monologues) | Partial | Partial | No | Topic modeling, sentiment, persona extraction |
| **FlirtFlip** | **1K** | **Yes (transforms)** | **3 levels** | **No** | **Yes (gentle/playful/bold)** | **Message intensity/tone training** |
| Flirty Conversations | 500 | Yes | No | Yes | No | Multi-turn format training |
| FlirtationFeatureSet | 100 | Yes | 15 types | No | No | Taxonomy of flirtation styles |
| Speed Dating (Columbia) | 8K+ | No | Limited | No | No | Preference/attachment modeling |
| Jurafsky SpeedDate | ~3 sessions | Yes (audio) | Binary | Yes | No | Flirt detection baseline |

**Primary recommendation:** **FlirtFlip** is the most directly useful dataset for training text-game agents because it provides the only dataset with explicit intensity levels (gentle/playful/bold) that map to difficulty/tone. RODD is best for topic and persona modeling. The Tinder Flirtation dataset provides the most realistic message data with human ratings.

---

## 3. Cross-Cultural / Multilingual Datasets

### 3A. Multilingual Dialogue Datasets

**Finding: No publicly available datasets specifically covering texting behavior by country or dating culture norms.**

| Dataset | Languages | Size | Type | Dating Suitability |
|---|---|---|---|---|
| **XDailyDialog** | English, Chinese, German, Russian | 13K dialogues, 52K utterances | Open-domain dialog, parallel translations | Adaptable — parallel structure enables cross-lingual training; not dating-specific |
| **SEADialogues** | 8 Southeast Asian | 32K multi-turn | Persona-rich, culturally grounded | Moderate for cultural adaptation; not dating-specific |
| **Multi3WOZ** | Multiple | Multi-domain | Task-oriented dialogue | Low — task-oriented, not conversational dating |
| **CulturaX** | 167 languages | 6.3T tokens | LLM pre-training corpus | Not directly usable — pre-training corpus only |

**XDailyDialog** (EMNLP 2023): The 4-language parallel structure is valuable for building culturally-aware dialogue agents. German and Russian versions enable some Western/Eastern European cultural comparison.

**SEADialogues:** Rich cultural grounding for Southeast Asian cultures (Vietnam, Indonesia, Thailand, Malay, Filipino). Could be adapted for culturally-aware agent training beyond dating.

---

### 3B. Workarounds for Cultural Training

Since no cross-cultural dating texting dataset exists, the practical approach is:

1. **Prompt engineering with cultural frameworks** — Use the cultural norms documented in Section 2 (community signal) as system prompts for agents
2. **XDailyDialog parallel data** — Fine-tune on German/Russian/Chinese versions with cultural system prompts injected
3. **Synthetics + cultural rules** — Generate synthetic data using culturally-specific response templates derived from the community norms
4. **Attachment style as proxy** — Use the attachment theory framework (which has cross-cultural research) as a culturally-agnostic difficulty/persona layer

---

## 4. Dataset Gaps and What They Mean for Building Agents

### Critical Gaps Identified

| Gap | Implication for Agent Building |
|---|---|
| **No conversation pairs with response labels** | Cannot train "given her message → best response" directly from existing datasets |
| **No response type taxonomy** | Cannot classify responses as jokes, compliments, questions, rejections, etc. |
| **No difficulty metrics** | Cannot automatically determine "hardness" of a message to respond to |
| **No sender/receiver structure** | Cannot model the dynamics of a real conversation exchange |
| **No cross-cultural texting datasets** | Cannot train culturally-tuned agents on real data; must use prompt engineering |
| **Small overall sizes** | FlirtFlip (1K) and Flirtation (5.8K) are too small for fine-tuning a production model |

### What the Datasets ARE Good For

| Use Case | Best Dataset |
|---|---|
| Fine-tuning language model on dating vocabulary/tone | RODD (219K monologues) |
| Flirtation detection / message intensity scoring | Flirtation-analysis (Tinder, 5.8K, human-rated) |
| Training message tone-shifting (gentle → bold) | FlirtFlip (1K, 3 intensity levels) |
| Multi-turn conversation format | Flirty Conversations (500 rows, Llama format) |
| Building a taxonomy of flirtation styles | FlirtationFeatureSet (100 rows, 15 types) |
| Cultural adaptation framework | XDailyDialog (EN/ZH/DE/RU parallel) + community norms |
| Flirt detection benchmarking | Jurafsky SpeedDate (71.5% baseline) |

---

## 5. Practical Data Strategy for Building Agents

Given these dataset limitations, the recommended data strategy is:

### For MVP

1. **Use FlirtFlip** for tone/intensity training (gentle/playful/bold → maps to difficulty levels)
2. **Use Flirtation-analysis** for training a flair detection model
3. **Use RODD** for topic and persona vocabulary enrichment
4. **Generate synthetic data** using LLM with cultural system prompts (from Section 2 community norms) — this fills the cultural gap until real data is collected
5. **Collect own data** via user interactions (like Composed's The Lab) — the compounding advantage

### For Production

1. **Build a conversation pair dataset** by engaging users — track which suggested replies get used, edited, or ignored
2. **Add difficulty labels** via a combination of: attachment style proxy (from user behavior patterns), response latency simulation, and user feedback
3. **Cultural variants** — once base agent works, collect data per cultural segment and fine-tune regional variants

---

## 6. Sources

| Source | URL | Quality |
|---|---|---|
| Flirtation-analysis (GitHub) | https://github.com/alyssafrndz/Flirtation-analysis | High |
| RODD (HuggingFace) | https://huggingface.co/datasets/FabianLeibinger/Reddit-Online-Dating-Dataset-RODD | High |
| FlirtFlip (HuggingFace) | https://huggingface.co/datasets/shirshatzman/flirtflip-dataset | High |
| Flirty Conversations (HuggingFace) | https://huggingface.co/datasets/mylesfriedman30/flirty_conversations_dataset | Medium |
| FlirtationFeatureSet (HuggingFace) | https://huggingface.co/datasets/traltyaziking/FlirtationFeatureSet | Low-Medium |
| Speed Dating Dataset (Kaggle) | https://www.kaggle.com/datasets/annavictoria/speed-dating-experiment | High (academic) |
| Jurafsky EMNLP 2009 | https://aclanthology.org/D09-1035.pdf | High (academic) |
| XDailyDialog | https://aclanthology.org/2023.acl-long-684/ | High (academic) |
| SEADialogues | https://github.com/SEACrowd/SEADialogues | Medium |
| CulturaX (HuggingFace) | https://huggingface.co/datasets/uonlp/CulturaX | Medium |
