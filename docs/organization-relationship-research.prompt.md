你是一位跨領域研究員，熟悉社會學、社會心理學、人類學、組織行為、管理學、社會網絡分析、知識圖譜與 LLM 應用。

我要做的不是尋找現成產品，也不是只解釋某幾個工具在幹嘛。我想建立一套「人類中小型群體的人際關係蒸餾 / 組織關係圖譜 / 角色性格推
斷」的方法論概覽，未來可用於從 LINE、email、會議紀錄、訪談、文件、觀察筆記中萃取：

- 群體中的人物角色
- 互動關係
- 權力與影響力
- 信任、衝突、依賴、迴避
- 資訊流與決策流
- 非正式組織
- 情緒勞動與責任轉嫁
- 誰是樞紐、瓶頸、協調者、暗中決策者
- 個體性格、互動風格、工作風格
- 群體中的穩定模式與例外事件

研究主軸請放在「人類中小型群體」而不是只放在公司。公司、團隊、部門、家族企業、社群、學術實驗室、小型組織都可以作為場景。學科比
例請以社會學、社會心理學、人類學、群體研究為主，管理學與組織行為為輔，最後再補充現代資料科學與 LLM 方法。

請產出一份完整研究報告，使用繁體中文。

研究範圍必須包含：

1. 經典理論與上古神書
 - small group research
 - sociometry
 - role theory
 - symbolic interactionism
 - dramaturgical analysis
 - social exchange theory
 - group dynamics
 - informal organization
 - bureaucracy / organization theory
 - power, status, hierarchy, authority
 - social capital, weak ties, structural holes, brokerage
 - trust, conflict, coalition, clique, faction
 - sensemaking, organizational culture, communities of practice

2. 社會網絡與組織網絡分析
 - Social Network Analysis
 - Organizational Network Analysis
 - centrality, brokerage, structural holes, density, reciprocity, clustering
 - knowledge hubs, boundary spanners, bottlenecks
 - formal org chart vs informal network
 - communication network, advice network, trust network, conflict network
 - survey-based ONA, digital trace-based ONA, mixed-method ONA

3. 人格、角色與互動風格推斷
 - personality psychology only where useful; do not reduce everything to MBTI
 - Big Five, interpersonal circumplex, attachment, political skill, emotional labor
 - role behavior vs stable personality
 - how much can be inferred from language, behavior, network position, and repeated incidents
 - limits and ethical risks of inferring personality from text

4. 定性方法
 - ethnography
 - participant observation
 - interview and contextual inquiry
 - grounded theory
 - discourse analysis
 - conversation analysis
 - critical incident technique
 - process tracing
 - event logs and interaction episodes
 - how qualitative evidence captures hidden power, conflict, trust, fear, avoidance, responsibility shifting

5. 知識圖譜、超圖與現代 AI 方法
 - entity-relation extraction
 - event extraction
 - knowledge graph construction
 - social graph construction
 - hypergraph personality / higher-order relations
 - GraphRAG
 - LLM-assisted coding, summarization, relationship extraction, contradiction detection
 - how to combine network metrics with qualitative evidence
 - how to avoid hallucinated relationships

6. 企管與公司場景
 - organizational behavior
 - informal power in companies
 - decision-making networks
 - psychological safety
 - team topology
 - responsibility gaps
 - knowledge management
 - ONA + survey + LLM products such as Teamspective as a modern example, but do not make SaaS products the main focus

請特別回答：

- 如果我要做一套「公司人物與關係圖譜 skill」，它背後其實橫跨哪些學科？
- 每個學科提供的是什麼視角？
- 哪些方法適合從文字紀錄中萃取關係？
- 哪些方法適合從訪談與觀察中萃取關係？
- 哪些方法適合量化網絡？
- 哪些方法適合解讀權力、衝突、信任、情緒、責任？
- 哪些推論是可信的？哪些推論很危險？
- 如果只有 LINE / email / 會議紀錄，能知道什麼？不能知道什麼？
- 如何把「人像」和「人際網絡」分開建模？
- 如何把「事件」作為證據單位，而不是直接下人格判斷？
- 如何把這些方法轉成未來可用的 skill / workflow / artifact？

輸出格式：

# 研究報告標題

## 1. Executive Summary
用 8-12 點濃縮整個領域的核心結論。

## 2. 這個領域其實叫什麼
說明它不是單一學科，而是哪些領域的交會。請給出一張「領域地圖」。

## 3. 核心理論脈絡
按學科整理，每個理論請包含：
- 核心問題
- 代表人物 / 代表書或論文
- 對「人際關係蒸餾」有什麼用
- 盲點或誤用風險

## 4. 方法論總覽
分成：
- 定性方法
- 定量網絡方法
- 混合方法
- AI / LLM / knowledge graph 方法

每一類請說明：
- 適合回答什麼問題
- 需要什麼資料
- 產出什麼 artifact
- 可信度如何評估
- 常見錯誤

## 5. 關係類型分類法
建立一個 taxonomy，至少包含：
- 權力關係
- 信任關係
- 衝突關係
- 依賴關係
- 資訊流
- 決策流
- 情緒支持 / 情緒消耗
- 責任轉嫁
- 協作關係
- 非正式聯盟
- 迴避 / 繞路 / bypass
- mentorship / sponsorship
- gatekeeping / brokerage

每一種關係請提供：
- 定義
- 可觀察證據
- 可能的錯誤推論
- 適合的資料來源

## 6. 人物建模與角色建模
請區分：
- persona / personality
- social role
- organizational role
- network position
- behavioral pattern
- reputation
- inferred motive

說明為什麼不能直接把「某次行為」當成「人格」，以及如何用多事件證據建立較可靠的人物 profile。

## 7. 從資料到圖譜的工作流
設計一套高層工作流，不要寫程式碼，但要足夠具體：
- 原始資料類型
- 清洗與匿名化
- 人物識別
- 事件抽取
- 關係抽取
- 證據綁定
- 信心分級
- 衝突證據處理
- network metrics
- qualitative memo
- 最終 artifact

## 8. 公司場景應用
說明這套方法如何應用在公司、部門、家族企業、小型團隊。請包含：
- formal org chart vs informal org chart
- 老闆真正聽誰的
- 誰掌握資訊
- 誰是瓶頸
- 誰在補洞
- 誰常常繞過誰
- 誰只要權力不負責
- 誰是情緒中心或衝突來源
- 哪些判斷需要更多證據，不能武斷下結論

## 9. 現代 AI 系統如何做
請概覽：
- LLM relationship extraction
- knowledge graph construction
- social graph extraction
- hypergraph / higher-order interaction
- GraphRAG
- ONA + survey + LLM
- limitations: hallucination, privacy, defamation, confirmation bias, false precision

## 10. Canonical Reading List
請按類別列出經典書籍、論文、研究方向。不要只列新文章。每個來源請附 1-2 句「為什麼值得讀」。

## 11. 給 skill 設計的啟發
最後請把研究轉成未來設計「organization relationship map skill」的啟發：
- 最小可行輸入
- 最小可行輸出
- 應該避免的輸出
- 人物檔案 schema
- 關係檔案 schema
- 事件證據 schema
- open questions schema
- confidence levels
- ethical guardrails

## 12. 一頁式總結
用一頁整理：
- 這個領域的全貌
- 最重要的 10 個概念
- 最值得讀的 10 個來源
- 未來做 skill 時最該採用的 10 條原則

引用要求：
- 盡量引用學術書籍、經典論文、權威綜述、學術出版社、可靠商業案例。
- 每個重要理論、方法、人物、書籍或產品都要附來源。
- 不要捏造來源、DOI、頁碼或不存在的書名。
- 如果某個來源不確定，標註「不確定」。
- 不要只引用近年的 AI 文章；必須包含經典社會學、社會心理學、組織理論與管理學來源。

寫作風格：
- 不要寫成工具介紹。
- 不要寫成產品競品分析。
- 不要只寫摘要，要建立概念地圖。
- 保持研究報告口吻，但要實用，讓我看完能知道這個領域有哪些方法可以被轉成 skill。
