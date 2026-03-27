# Wave 2: Content Architecture & Internal Linking

> **Part of:** [Topical Authority in SEO — Comprehensive Research Report](../Topical-authority.md)
> **Wave:** 2 of 4 | **Confidence:** Medium-High on architectural topics

---

## 5. Pillar Pages & Topic Clusters — Architecture Deep Dive

The pillar-cluster (hub-and-spoke) model is the dominant architectural framework for building topical authority. This section covers the mechanism of authority passing, optimal cluster sizing, entity relationship mapping, sub-pillar architecture, and planning methodologies.

### 5.1 How Pillar-Cluster Architecture Builds Topical Authority

The mechanism operates through two simultaneous processes: **internal link distribution** and **content depth signaling**.

**Authority Passing Mechanism**

When a pillar page links to cluster pages and vice versa, it creates a tightly interconnected content cluster. **Jaume Ros** (_SEO Silos vs. Topical Clusters_) describes the authority flow:

> _"When you start getting backlinks, the authority from those backlinks will flow throughout the whole Silo and throughout the whole site regardless of where those backlinks come in... based on the internal links, it's going to go down to the vegan pages, to the brunch pages, and to the sushi pages. But because we have a link pointing back to Barcelona, it's also going to go back out to Barcelona and as a result in some way it'll flow over to hotels, to attractions, and it can even flow back to the homepage."_

**Dan McKinnon** (Sierra Interactive, live case study) identifies **four reasons Google rewards hub-and-spoke**:

1. **Google sees depth** — _"One blog says you know about this topic. Six connected blogs say you own it."_
2. **Internal links pass authority** — _"Every time you link from one page to another on your site, you're passing trust. Unlike backlinks to other sites, you control every single one of these."_
3. **Clusters rank faster** — _"When you publish a new spoke page, it doesn't start from zero. It inherits some sort of authority from that hub page."_
4. **LLMs love clusters** — _"ChatGPT, Perplexity, Google, Claude — they all pull from the most comprehensive source on a topic."_

**Content Depth Signaling**

**Matthew Zare** (_Pillar Pages & Topic Clusters_): _"Topical authority signals to Google you are an expert about the topic because you can cover it broadly AND cover all of its aspects deeply and specifically in other articles."_

**Marc Möller** (_Topical Maps L2_): _"What you're trying to do with a topical map is to match what Google has in their Knowledge Graph to your business and talk about all of the important entities and edges that exist for your topic."_

**Confidence: High** — direction of authority flow is consistent across sources. Exact algorithmic weighting of pillar-cluster architecture specifically (vs. generic internal linking) is proprietary.

---

### 5.2 Optimal Cluster Size

**Finding: 8–20 cluster pages per pillar page, with 5–10 topic clusters per site — practitioner consensus, not verified science.**

| Source                                                   | Recommendation                                                         | Basis                                                                  |
| -------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Surfer Academy (survey of ~500 users)                    | 5–10 topic clusters total per site                                     | Survey of Surfer users; 90% agreed topic clusters are "very important" |
| Industry guides (influencers-time.com, tattvammedia.com) | 8–20 cluster pages per pillar                                          | Practitioner compilation, no primary research cited                    |
| Search Engine Land (citing HireGrowth 2025)              | Clusters drive ~30% more organic traffic and hold rankings 2.5x longer | Single vendor analysis; directional only                               |

**Cluster size by page type:**

| Page Type       | Typical Word Count  | Purpose                                                          |
| --------------- | ------------------- | ---------------------------------------------------------------- |
| Pillar page     | 2,000–10,000+ words | Comprehensive A–Z guide; targets short-tail high-volume keywords |
| Sub-pillar page | 1,500–3,000 words   | Mid-level overview for a broad subtopic within the cluster       |
| Cluster page    | 800–2,000 words     | Deep dive on a single subtopic; targets long-tail keywords       |

**Important caveat:** The 30% traffic boost and 2.5x ranking longevity claims (Search Engine Land/HireGrowth) have not been independently replicated. Do not treat these as confirmed benchmarks.

**Confidence: Medium** — consistent practitioner range, no rigorous controlled experiments.

---

### 5.3 Mapping Entity Relationships for Topic Clusters

The most detailed frameworks come from **Koray GÜBÜR** and **Marc Möller**, who ground their approaches in how Google's Knowledge Graph structures knowledge.

**Marc Möller's Wikipedia/Knowledge Graph Approach**

1. Take your core topic → look at connected Wikipedia articles via `blindpete.github.io/wiki-graph/` or `xefer.com/wikipedia`
2. Visualize the graph — topics close to the core are essential; very distant topics are optional
3. Topics that appear as dedicated Wikipedia articles = candidate for dedicated page; topics that only appear as sections = candidate for paragraph treatment

Example: From "drinking water," "luxury water" is close (needs modest coverage), but "fecal coliform bacteria" is far (may not belong in your topical map).

**Rank Math's Entity Mapping Workflow**

1. Identify core **entities** (nouns) for a topic — e.g., for BBQ: brisket, smoker, wood, temperature, rub, smoke ring
2. Define **attributes** for each entity — e.g., brisket attributes: cut, grade, fat content; smoker attributes: type, fuel source
3. Map **entity relationships** — e.g., "brisket is cooked using smoker," "smoker uses wood," "wood imparts flavor to brisket"
4. Check content against the map to fill gaps

**Koray GÜBÜR's Entity-Attribute-Value (EAV) Framework**

Koray argues most SEOs over-index on entities when **attributes are more important**:

> _"One of the mistakes that all SEOs do is we all focus on entities. I can tell you that this entity focus is a little bit too much. In fact, we should be focusing on mostly and mainly on attributes, because attributes are way much more important than the entities."_

The EAV model structures content as triples: **Subject-Predicate-Object** (e.g., "brisket" + "has" + "fat content"), mirroring how Google's Knowledge Graph stores relationships.

Koray's additional semantic dimensions:

- **Contextual flow**: The sequence of context from start to finish should be logical and focused (not zigzag between unrelated concepts)
- **Contextual vector**: The overall directional focus of the content should stay on-topic
- **Contextual coverage**: How much space/text you dedicate to each subtopic signals its importance to Google — paragraph = minor; dedicated page = major

**Matthew Zare's AI-Driven Workflow**

Zare reverses the traditional keyword-first approach:

1. Define brand persona → identify semantic themes
2. Map **pain points → standardized keywords** (AI converts user pain points to search-optimized parent keywords)
3. Cluster keywords into subcategories (subclusters)
4. Assign H1s that address pain points; article body targets standardized keywords
5. Specify internal link strategy for each cluster before writing

**Confidence: Medium-High** — entity mapping methodology is well-described; optimal density thresholds are not quantified.

---

### 5.4 Sub-Pillars vs. Cluster Pages — When to Use Each

A sub-pillar (mid-level page) is warranted when:

| Condition                                                             | Implication                                            |
| --------------------------------------------------------------------- | ------------------------------------------------------ |
| A cluster topic is broad enough to warrant its own mid-level overview | Create a sub-pillar, then cluster subtopics beneath it |
| Multiple cluster pages share a common sub-theme                       | Extract the sub-theme into a sub-pillar                |
| The sub-theme has enough search demand for its own pillar keyword     | Treat as a second-tier pillar, interlinked upward      |

**Jaume Ros on silos vs. clusters:**

> _"With silos, you can't link to your cousins — if you link from attractions in Barcelona to restaurants in Sevilla, that would break your Silo. With topical clusters, there are no rules about internal linking between clusters."_

He also notes silos and topic clusters can coexist: an e-commerce site can maintain strict category silos for product pages while running a blog with topic clusters.

**The hierarchical depth possible (Ros):**

```
Theme
  └── Topic
        └── Subtopic
              └── Sub-subtopic
```

**Confidence: Medium** — sub-pillar criteria are logically sound but lack documented case studies with measurable ranking impact.

---

### 5.5 Topic-First vs. Keyword-First Planning

**Consensus: Topic-first dominates, but keyword data informs prioritization.**

| Approach          | Description                                                                    | Sources                                           |
| ----------------- | ------------------------------------------------------------------------------ | ------------------------------------------------- |
| **Topic-first**   | Start with the topics you want to own; find keywords that support those topics | Marketing Explained, Surfer Academy, Matthew Zare |
| **Keyword-first** | Start with keyword research; group keywords into topics                        | Traditional SEO (largely superseded)              |
| **Hybrid**        | Topic-first for strategy; keyword data (volume, difficulty) for prioritization | Semrush, most modern practitioners                |

> _"In the past, creating content for inbound marketing used to be based solely around keywords. But if you're looking to bring in more traffic to your website and increase conversions, creating content for keywords won't be enough... when users make a search in Google, they're not searching with keywords. They're just trying to solve problems or questions they have. Google wants to answer those problems."_ — **Marketing Explained**, YouTube

**Cluster-first vs. pillar-first:** Moz (Chima Mmeje) recommends publishing **subtopics first** to build momentum before the pillar goes live. This evidence-based cluster-first approach appears more widely supported in current practice.

**Confidence: High** — topic-first is the dominant practitioner recommendation; keyword-first is largely considered outdated.

---

### 5.6 Multi-Pillar Sites and Nested Clusters

**Multi-pillar sites** have multiple independent topic clusters, each with its own pillar page — the natural evolution for sites covering multiple distinct topic areas.

**Nested clusters** apply the same hub-and-spoke logic at multiple levels:

```
Main Pillar: "Content Marketing"
  ├── Sub-Pillar: "Content Writing"
  │     ├── Cluster: "Headlines that convert"
  │     ├── Cluster: "Copywriting formulas"
  │     └── Cluster: "Product descriptions"
  ├── Sub-Pillar: "Content Distribution"
  │     ├── Cluster: "Email newsletter strategy"
  │     └── Cluster: "Social media distribution"
  └── Sub-Pillar: "Content Measurement"
        ├── Cluster: "Content KPIs"
        └── Cluster: "Analytics setup"
```

**Confidence: Medium** — the hierarchical extension is logically consistent but specific case studies demonstrating measurable lifts from nested clusters are rare.

---

## 6. Internal Linking Strategies

Internal linking is the connective tissue of topical authority — it redistributes PageRank, signals topical relationships, and enables Google to crawl and understand site structure.

### 6.1 The PageRank Redistribution Mechanism

Google's Gary Illyes confirmed in 2017 that PageRank is still an active ranking signal. Internal links redistribute PageRank throughout a site, following a pyramid structure.

**Ahrefs confirms the mechanism:**

> _"Every link on a page dilutes value passed through others — a page with 100 links passes roughly 1/100th equity through each."_

**The pyramid architecture (Moz):**

> _"This structure has the minimum amount of links possible between the homepage and any given page... allows link equity to flow throughout entire site."_

**Key principle from Search Engine Journal:** _"If the URL internal links from the same family are around 75% or higher, that suggests internal links are helping solidify topical authority."_

**Confidence: High** — PageRank is confirmed active by Google; the redistribution mechanism is well-understood.

---

### 6.2 Link Types and Authority-Passing Value

| Link Type                                         | Authority Value | Notes                                                                         |
| ------------------------------------------------- | --------------- | ----------------------------------------------------------------------------- |
| **Contextual links** (in-body content, editorial) | **HIGHEST**     | Within main content body; highest editorial weight                            |
| **Navigational links** (primary menu)             | **MEDIUM**      | Template links; essential for structure but discounted                        |
| **Breadcrumb links**                              | **MEDIUM**      | Google treats as normal links in PageRank computation (Gary Illyes confirmed) |
| **Related content modules**                       | **MEDIUM**      | Good for surfacing older content; horizontal authority distribution           |
| **Sidebar links**                                 | **LOW**         | Typically template-based; less editorial weight                               |
| **Footer links**                                  | **LOW**         | Users ignore; algorithms discount                                             |

**A note on link position (Mueller vs. Ahrefs):**

| Source           | Position          | View                                                                                                         |
| ---------------- | ----------------- | ------------------------------------------------------------------------------------------------------------ |
| **Ahrefs**       | Main content body | "Highest value: Links in your main content body"                                                             |
| **John Mueller** | Any position      | "I don't think there is anything quantifiably different about internal links in different parts of the page" |

**Resolution:** These address different concepts — Ahrefs discusses topical signal value (contextual links carry semantic meaning); Mueller discusses PageRank flow by location. Both can be simultaneously true.

---

### 6.3 The Middleman Method

**Definition:** Using high-authority pages (those with existing external backlinks) as intermediaries to pass PageRank to weaker target pages ("money pages").

**Three required ingredients (per Adogy):**

1. **Backlinks to the linking page** — Without external backlinks, the middleman has no extra PageRank to pass
2. **Matching searcher intent** — The target page must satisfy what users searching for that query want
3. **Competing against appropriate pages** — Don't try to boost a new page to compete with established authority pages

**Steve Toth (SEO Notebook)** demonstrates verticalization — prioritizing which cluster pages get the most prominent internal links based on business value:

> _"I want to make engineers the first link in the content. Since mechanical engineers is my second most important page, I'm going to make it the first link in that page."_

**Confidence: Medium-High** — the principle is well-established; specific results depend on the existing backlink profile of the middleman page.

---

### 6.4 Orphan Page Elimination

Orphan pages have no internal links pointing to them and cannot be discovered by Googlebot through normal crawling.

**Discovery methods:**

| Method                | Tool               | How                                                   |
| --------------------- | ------------------ | ----------------------------------------------------- |
| Screaming Frog        | Orphan Page filter | Links tab → filter "Orphan Pages"                     |
| Google Search Console | Links report       | Manual review of pages with few/no internal links     |
| Ahrefs Site Audit     | Best by Links      | Sort by "Unique Inlinks" column, find low-count pages |

**Fixes:**

| Strategy                | Method                                                        |
| ----------------------- | ------------------------------------------------------------- |
| Contextual linking      | Add links from relevant high-authority content                |
| Related content modules | Surface orphan pages in "related articles" sections           |
| XML sitemap             | Ensure orphan pages are in sitemap as fallback discovery path |
| Breadcrumb inclusion    | Add breadcrumbs to connect orphan pages to site hierarchy     |

> _"Poorly linked new page may take longer to be discovered"_ — **Screaming Frog**

**Confidence: High** — orphan page problem and solutions are well-documented.

---

### 6.5 Crawl Budget Management

Googlebot has a finite crawl budget per site. Internal linking architecture directly affects how efficiently that budget is used.

| Factor                                  | Impact                                              |
| --------------------------------------- | --------------------------------------------------- |
| Large sites (10k+ pages)                | Need deliberate crawl budget optimization           |
| Pages with more internal/external links | Prioritized for crawling                            |
| Slow pages                              | Less crawling (Google cites page speed as a factor) |

**Best practices:**

| Practice                                  | Impact                                                                                    |
| ----------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Flat architecture**                     | Keep important pages within 1–3 clicks of homepage                                        |
| **Link to important pages from homepage** | Direct crawl path to priority content                                                     |
| **Improve site speed**                    | "Making a site faster improves user experience while also increasing crawl rate" — Google |
| **Fix redirect chains**                   | Unnecessary redirects eat crawl budget                                                    |
| **Update XML sitemaps**                   | Help bots discover new/changed pages                                                      |

> _"The fewer clicks it takes to reach a page from homepage, the more likely it is to be crawled, indexed and ranked well"_ — **Gabriela Troxler, Screaming Frog**

**Confidence: High** — crawl budget management is confirmed by Google's documentation.

---

### 6.6 Anchor Text Best Practices for Topical Authority

**Do:**

| Practice                | Example                                               |
| ----------------------- | ----------------------------------------------------- |
| Descriptive anchor text | "email segmentation guide" instead of "click here"    |
| Varied anchor text      | Mix exact match, partial match, branded anchors       |
| Topical keywords        | Include target keywords naturally within anchor text  |
| Relevant to destination | Anchor text should describe the linked page's content |

**Don't:**

| Practice                             | Why                                          |
| ------------------------------------ | -------------------------------------------- |
| Exact match repetitive               | Looks manipulative; dilutes value            |
| Generic "click here"                 | Wastes anchor text opportunity               |
| Same anchor text for different pages | Confuses Google and users                    |
| Over-optimization                    | Google may discount if obviously manipulated |

**Recommended ratio:** Aim for ~75%+ of internal links to a page from **topically similar** pages. Diverse anchor text profile across the site.

> _"Anchor text helps inform search engines of the nature of the page being linked to"_ — **Search Engine Journal**

---

### 6.7 Tools for Internal Link Audits

| Tool                          | Key Features                                                                  | Use Case                     |
| ----------------------------- | ----------------------------------------------------------------------------- | ---------------------------- |
| **Google Search Console**     | Links report, internal links per page                                         | Free, limited to sample data |
| **Screaming Frog SEO Spider** | Crawl depth, unique inlinks, orphan page filter, custom n-gram search         | Comprehensive site audit     |
| **Ahrefs Site Audit**         | Site Explorer, Best by Links, URL Rating (PageRank proxy), link opportunities | Backlink-aware audit         |
| **LinkWhisper** (WordPress)   | Automated internal linking suggestions within WordPress                       | Quick win identification     |

**Screaming Frog audit workflow:**

1. Crawl site → Inlinks tab → sort by "Unique Inlinks" ascending → find pages with few internal links
2. Use "Orphan Pages" filter to find undiscoverable pages
3. Custom n-gram search to find unlinked keyword mentions sitewide
4. Export crawl depth data → target pages buried >4 clicks from homepage

**Confidence: High** — tools are well-established and widely used by practitioners.

---

## Sources — Wave 2

### YouTube

| Source                            | URL ID                                      | Tier   |
| --------------------------------- | ------------------------------------------- | ------ |
| Jaume Ros                         | `BXaXmDsZqZo`                               | Tier 1 |
| Dan McKinnon / Sierra Interactive | `fvoX5xiIc34`                               | Tier 1 |
| Steve Toth / SEO Notebook         | `8OXdvz2HRis`                               | Tier 1 |
| Surfside PPC                      | `T9FDrrm3BF8`                               | Tier 1 |
| Marketing Explained               | `AzTutClzfs4`                               | Tier 1 |
| Surfer Academy                    | `oXPP2Tt1mHM`                               | Tier 1 |
| Matthew Zare                      | `xzNO5s41HOg`                               | Tier 1 |
| Koray GÜBÜR                       | `fb5nXF6eu5U`, `_U0UQsah3Pc`, `-scFvl1NeIE` | Tier 1 |
| Marc Möller                       | `dH6FXL_O-qo`, `p-7I6Hsqwcs`                | Tier 1 |
| Kasra Dash                        | `SCb52wXdMFQ`                               | Tier 1 |
| Rank Math SEO                     | `l-vy9bNn7nI`                               | Tier 1 |
| Webfor                            | `FuFPKQluDJk`                               | Tier 2 |

### Web

| Source                                                         |
| -------------------------------------------------------------- |
| Ahrefs — Internal Links for SEO: A Complete Guide              |
| Moz — Internal Links SEO Best Practices                        |
| Backlinko — Internal Linking for SEO: The Complete Guide       |
| Search Engine Journal — Internal Linking for Topical Authority |
| Search Engine Land — Topic Clusters & Pillar Pages Guide       |
| Screaming Frog Blog — Internal Linking and Crawl Budget        |
| Semrush — Topic Clusters Guide                                 |
| NeuronWriter — Semantic Density vs Content Length              |
| TopicalHQ — Entity Coverage Tools Guide                        |
