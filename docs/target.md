對，第一層 deep research 會肥，這正常；但第二層 `SKILL.md` 不能把研究報告整包塞進去。

正確做法是：

> **研究報告 = 理論彈藥庫**
> **SKILL.md = 固定工作流 + 輸出格式 + 推論約束 + 證據規則**

你要做的不是把「社會學、SNA、知識圖譜、人類學」全部寫進 skill；而是把它們壓縮成一個能穩定執行的分析器。

---

## 你這個 skill 應該叫什麼

我會叫：

```text
organization-relationship-map
```

或中文：

```text
組織關係圖譜
```

它不是 `colleague-skill` 的同類，而是上一層。

`colleague-skill / dot-skill` 的結構是「資料來源 + 主觀描述 → 產出某個人的 Work Skill + Persona」，而且它現在已經擴成 distill anyone 的架構，包含 persona、work skill、增量 merge、correction layer 等。([GitHub][1])

但你這個是：

```text
多人資料
→ 事件抽取
→ 人物檔案
→ 關係檔案
→ 權力/信任/衝突/責任圖譜
→ open questions
```

所以它要學的是 `dot-skill` 的**增量 merge / correction / persona schema**，但不要學它的「把一個人做成角色卡」核心邏輯。

---

## 目錄結構我會這樣設計

```text
organization-relationship-map/
  SKILL.md

  prompts/
    intake.md
    evidence_extractor.md
    person_profiler.md
    relationship_mapper.md
    graph_synthesizer.md
    contradiction_checker.md
    merger.md
    correction_handler.md

  references/
    relationship-taxonomy.md
    inference-rules.md
    confidence-levels.md
    evidence-schema.md
    anti-patterns.md

  templates/
    people.md
    relationships.md
    events.md
    open-questions.md
    graph-summary.md
    risks.md
```

先不要寫 tool。第一版純 prompt skill 就夠。

---

## 最小輸出不要只有三個檔

你說的：

```text
people.md
relationships.md
open-questions.md
```

是 MVP，但做都做了，我會加到 6 個：

```text
people.md
relationships.md
events.md
graph-summary.md
open-questions.md
risks.md
```

原因是：**events.md 是防止人格腦補的核心。**

沒有 `events.md`，模型很容易直接寫：

```text
A 是情緒勒索型
B 是補洞者
C 只要權力不負責
```

有 `events.md`，它必須寫成：

```text
事件 E023：
A 在群組要求 B 處理出貨異常，但沒有提供決策依據。
B 接手後向 C 確認庫存。
可能關係：A → B 責任下放 / B 為流程補洞者
信心：中
```

這跟你 prompt-master 產出的研究題詞一致：它已經要求把「事件」當證據單位，而不是直接下人格判斷。

---

# `SKILL.md` 核心骨架

你可以直接拿這個當第二層雛形。

```md
---
name: organization-relationship-map
description: Distill small-group or company communication records into people profiles, relationship maps, interaction patterns, and evidence-backed open questions. Use when analyzing LINE/email/meeting notes/chat logs to understand roles, power, trust, conflict, responsibility flow, decision flow, and informal organization.
---

# Organization Relationship Map Skill

You analyze small-group communication records and produce an evidence-backed relationship map.

This skill is for:
- company teams
- small organizations
- family businesses
- departments
- labs
- communities
- recurring working groups

This skill is NOT for:
- diagnosing people
- labeling personality from one incident
- making defamatory claims
- replacing human judgment
- producing gossip without evidence
- executing actions or contacting people

## Core Principle

Always model the group through four separate layers:

1. Events: what happened
2. People: what each person repeatedly does
3. Relationships: how people interact
4. Network patterns: what stable structure appears across events

Never jump directly from one message to a personality judgment.

## Required Artifacts

When enough source material exists, maintain or produce:

- `events.md`
- `people.md`
- `relationships.md`
- `graph-summary.md`
- `open-questions.md`
- `risks.md`

If evidence is weak, produce partial artifacts and mark confidence honestly.

## Workflow

### Step 1. Source Intake

Identify:
- source type: LINE, email, meeting notes, interview, observation, document
- time range
- participants
- missing context
- whether names are real, aliases, or uncertain
- whether the text is complete or partial

Do not assume the dataset is complete.

### Step 2. Entity and Role Identification

Extract people and aliases.

For each person, distinguish:
- formal role
- observed role
- network position
- repeated behavior
- reputation in the data
- inferred motive, if any

Do not merge two people unless evidence is strong.

### Step 3. Event Extraction

Convert raw text into interaction events.

Each event must include:
- event id
- date/time if available
- participants
- trigger
- action sequence
- decision point
- emotional tone if observable
- outcome
- evidence quote or source pointer
- possible interpretations
- confidence level

### Step 4. Relationship Extraction

Infer relationships only from repeated events or strong evidence.

Relationship types include:
- power / authority
- trust
- conflict
- dependency
- information flow
- decision flow
- emotional support
- emotional burden
- responsibility shifting
- collaboration
- informal alliance
- avoidance / bypass
- mentorship / sponsorship
- gatekeeping / brokerage

Each relationship must cite supporting events.

### Step 5. Person Profile Construction

Build person profiles from repeated patterns.

A person profile must separate:
- facts
- observed behavior
- repeated patterns
- likely role in the group
- interaction style
- work style
- communication style
- uncertainty
- evidence gaps

Avoid personality labels unless strongly supported by multiple events.

### Step 6. Graph Synthesis

Summarize the group as a network.

Identify:
- formal org chart vs informal org chart
- knowledge hubs
- bottlenecks
- boundary spanners
- hidden decision makers
- emotional centers
- conflict sources
- responsibility gaps
- bypass routes
- fragile single points of failure

### Step 7. Open Questions

List what cannot be concluded yet.

Open questions should be actionable:
- ask whom
- ask what
- why it matters
- what artifact would change if answered

### Step 8. Incremental Merge

When new data arrives:
- append new events
- update people only if new evidence changes the pattern
- update relationships only with event support
- preserve old conclusions unless contradicted
- record contradictions explicitly
- never silently overwrite

## Confidence Levels

Use these labels:

- High: repeated evidence across multiple events or sources
- Medium: multiple hints but limited source diversity
- Low: plausible but based on weak or incomplete evidence
- Unknown: not enough evidence

Never present low-confidence inference as fact.

## Forbidden Output

Do not write:
- "A is a bad person"
- "B has narcissistic personality"
- "C definitely manipulates everyone"
- "D is loyal/disloyal" without evidence
- private psychological diagnosis
- claims about motive without event support

Use:
- "In the available events, A repeatedly..."
- "This may indicate..."
- "Alternative explanation..."
- "Needs confirmation..."

## Output Style

Be direct, structured, and evidence-first.

Prefer tables for people and relationships.
Prefer event IDs for traceability.
Keep interpretation separate from evidence.
```

---

## `people.md` schema

```md
# People

## Person: [Name / Alias]

### Identity
- Name / alias:
- Possible aliases:
- Formal role:
- Observed role:
- Data coverage:
- Confidence:

### Role in the group
- Formal role:
- Actual working role:
- Informal role:
- Network position:
  - knowledge hub / bottleneck / broker / peripheral / coordinator / decision node

### Repeated behavior patterns
| Pattern | Evidence Events | Confidence | Alternative Explanation |
|---|---|---|---|

### Communication style
- Direct / indirect:
- Detailed / vague:
- Emotional tone:
- Response speed:
- Escalation style:

### Work style
- Owns tasks:
- Delegates tasks:
- Avoids tasks:
- Clarifies ambiguity:
- Creates ambiguity:
- Handles exceptions:

### Decision behavior
- Makes decisions:
- Defers decisions:
- Seeks approval from:
- Overrides whom:
- Gets overridden by:

### Relationship notes
| Other Person | Relationship Type | Summary | Evidence |
|---|---|---|---|

### What we should not infer yet
- 
```

重點是：**不要直接 persona 化。**

人物描寫要滿足這些條件：

```text
1. 每個判斷都要能回到事件
2. 分清楚正式角色與實際角色
3. 分清楚行為模式與人格
4. 分清楚資料中觀察到的 reputation 與真實人格
5. 每個負面判斷都要給 alternative explanation
```

---

## `relationships.md` schema

```md
# Relationships

## Relationship: [A] → [B]

### Basic
- Direction:
- Relationship type:
- Confidence:
- Time range:
- Evidence events:

### Summary
[One paragraph summary.]

### Observable Evidence
| Event ID | Evidence | Interpretation |
|---|---|---|

### Relationship Types

#### Power / Authority
- Does A direct B?
- Does B comply?
- Is authority formal or informal?

#### Trust
- Does A rely on B?
- Does A share sensitive information with B?
- Does B get consulted before decisions?

#### Conflict
- Is there disagreement?
- Is it open conflict or avoidance?
- Is conflict task-based, status-based, emotional, or resource-based?

#### Dependency
- Does A need B to complete work?
- Is the dependency technical, informational, emotional, or political?

#### Information Flow
- Who informs whom?
- Who withholds information?
- Who translates or filters information?

#### Decision Flow
- Who proposes?
- Who approves?
- Who vetoes?
- Who executes?

#### Responsibility Flow
- Who receives ambiguous work?
- Who absorbs exceptions?
- Who gets blamed?
- Who repairs after failure?

### Alternative Explanations
- 
### Open Questions
- 
```

關係描寫要滿足這些條件：

```text
1. 必須有方向性：A → B，不要只寫 A-B 很熟
2. 必須有關係類型：信任、權力、資訊、責任、衝突等
3. 必須有事件證據
4. 必須能容納多重關係：A 可能信任 B，但也把責任丟給 B
5. 必須有 confidence
6. 必須列 alternative explanation
```

---

## `events.md` schema

這個最重要。

```md
# Events

## E001 - [Short title]

### Source
- Source type:
- Date/time:
- Location/channel:
- Participants:
- Evidence pointer:

### Trigger
What caused this interaction?

### Sequence
1.
2.
3.

### Decision / Non-decision
- Was a decision made?
- Who made it?
- Who avoided it?
- Who executed it?

### Responsibility Movement
- Who owned the issue before?
- Who owned it after?
- Was responsibility clarified or shifted?

### Emotional / Social Signals
- Frustration:
- Deference:
- Pressure:
- avoidance:
- face-saving:
- blame:
- reassurance:

### Candidate Interpretations
| Interpretation | Confidence | Evidence |
|---|---|---|

### Related Artifacts
- People:
- Relationships:
- Workflow:
- Open questions:
```

這個檔案就是防幻覺核心。

---

## `graph-summary.md` schema

```md
# Organization Graph Summary

## 1. Formal vs Informal Structure

### Formal Structure
-

### Informal Structure
-

## 2. Key Network Positions

| Person | Network Position | Evidence | Confidence |
|---|---|---|---|

## 3. Power Map
-

## 4. Information Flow
-

## 5. Decision Flow
-

## 6. Responsibility Flow
-

## 7. Trust / Conflict / Avoidance
-

## 8. Bottlenecks and Single Points of Failure
-

## 9. Hidden Patterns
-

## 10. What cannot be concluded
-
```

---

## `open-questions.md` schema

```md
# Open Questions

| ID | Question | Why It Matters | Ask Whom | Needed Evidence | Priority |
|---|---|---|---|---|---|

## OQ001
- Question:
- Why it matters:
- Current hypothesis:
- Evidence so far:
- What would confirm it:
- What would disconfirm it:
```

這裡很重要，因為這會變成後續訪談/LINE bot 繼續問人的燃料。

---

## `risks.md` schema

```md
# Risks

## Inference Risks
| Risk | Where It Appears | Mitigation |
|---|---|---|

## Ethical / Practical Risks
- privacy:
- defamation:
- confirmation bias:
- over-reading tone:
- missing offline context:
- power asymmetry:
- weaponization:

## Low-confidence Claims
| Claim | Why risky | Needed evidence |
|---|---|---|
```

這不是官腔安全，而是保護你不要把系統變成「公司宮鬥幻覺機」。

---

## Skill 實作時最該寫死的 10 條規則

```text
1. 先抽事件，再抽關係，最後才寫人物。
2. 不從單一事件推人格。
3. 所有關係都必須有方向性與證據。
4. 分開 formal role、observed role、network position。
5. 分開 behavior、reputation、motive。
6. 負面推論必須附 alternative explanation。
7. 所有結論都要有 confidence。
8. 缺資料時輸出 open questions，不要硬補。
9. 新資料進來時做 incremental merge，不要整份重寫。
10. 不直接輸出診斷、羞辱、定罪式人格標籤。
```

---

## 你現在應該怎麼拆第二層

不要一口氣寫超大 `SKILL.md`。我會拆成這樣：

```text
SKILL.md
  只放 mission、workflow、artifact、rules

references/relationship-taxonomy.md
  放關係分類

references/inference-rules.md
  放推論規則與禁忌

references/confidence-levels.md
  放 confidence 定義

templates/*.md
  放輸出格式
```

這樣 agent 進 skill 時不會先吃爆。
需要細節再讀 references。

---

## 這個 skill 的一句話定義

你可以把它定成：

> **從多人互動紀錄中，以事件為證據單位，增量建立人物檔案、關係圖譜、權力/資訊/責任流與待確認問題的分析 skill。**

這才是你要的東西。

而且這跟 `dot-skill / colleague-skill` 最大差異是：

> **dot-skill 蒸餾一個人；organization-relationship-map 蒸餾一群人的互動系統。**

[1]: https://github.com/titanwings/colleague-skill "GitHub - titanwings/colleague-skill: 将冰冷的离别化为温暖的 Skill，欢迎加入数字生命1.0！Transforming cold farewells into warm skills? It's giving rebirth era. Welcome to Digital Life 1.0.  · GitHub"
