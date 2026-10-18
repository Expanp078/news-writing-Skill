# 00-跨书任务入口图谱

> **最小调用协议**：`任务描述 → 选7类入口之一 → 命中task_route → 读取1个任务节点+3–6张SC卡 → 执行CALL_IF/DO/CHECK → 命中READ_NEXT或风险标签才下钻单书笔记`。图谱是机器路由层；完整卡在 `01-跨书综合知识库.md`，节点与来源索引在 `02-跨书概念索引.yaml`。

## AI调用协议

1. 先识别工况、时效、媒介、受众、风险和交付物；不要按书名检索。
2. 先加载 L0 不变量：事实可追溯、公共意义、责任边界、可理解传播。
3. 证据不稳先走 `SC02`；伦理/制度风险先走 `SC09`；发布/受众问题走 `SC10`；稿件失败走 `SC12`。
4. 基础概念通过节点的 `requires/COMPOSES` 隐式加载；只有 `deep_read_when` 命中才读单书笔记。
5. 任何来源风险、版本风险或精确词句请求都不得用综合推断补齐，必须 `READ_NEXT` 回源并标注 `needs_recheck`。

## 七个入口

|入口ID|入口|首跳|典型触发词|
|---|---|---|---|
|E1|任务与工况|R01–R10|突发、调查、经济、人物、会议、滚动、审校|
|E2|事实与认识|N01–N06|事实、证据、来源、核验、因果、主题|
|E3|报道生产|P01–P07|选题、采访、观察、策划、结构、编辑、发布|
|E4|叙事与表达|X01–X07|导语、倒金字塔、场景、细节、引语、解释、语言|
|E5|传播与受众|M01–M06|受众、媒介、框架、议程、效果、反馈|
|E6|规范与边界|G01–G07|真实性、独立、公平、回应、隐私、伤害、禁慎词|
|E7|诊断与复盘|D01–D06|失实、失焦、失序、失当、误读、纠错|

## 稳定节点块

字段约定：`node_id | label | layer | function | summary_card | requires | drill_down`。

```yaml
nodes:
  - {node_id: N00, label: 任务不变量, layer: L0, function: 事实/公共意义/责任/理解四闸门, summary_card: SC02+SC09+SC10, requires: [], drill_down: B03/B04/B05}
  - {node_id: N01, label: 新闻本源与事实变动, layer: L1, function: 确认报道对象是可验证的新近事实, summary_card: SC01+SC02, requires: [], drill_down: B03}
  - {node_id: N02, label: 新闻价值与公共利益, layer: L2, function: 排序影响/时新/受众需要并控制猎奇, summary_card: SC01, requires: [N01], drill_down: B03/B04/B02}
  - {node_id: N03, label: 传播系统与受众, layer: L1, function: 识别编码/媒介/受众/反馈/噪音, summary_card: SC10, requires: [], drill_down: B08/B03}
  - {node_id: N04, label: 来源分级与claim ledger, layer: L2, function: 将事实/引语/因果拆解并逐项核验, summary_card: SC02, requires: [N01], drill_down: B04/B01/B05/B06}
  - {node_id: N05, label: 采访问题树与现场记录, layer: L2→L3, function: 生成事实、反证、可核细节, summary_card: SC03, requires: [N04], drill_down: B06/B01/B07}
  - {node_id: N06, label: 主题角度框架, layer: L2→L3, function: 从材料关系提炼可证中心问题并审计责任归因, summary_card: SC04, requires: [N04], drill_down: B05/B02/B08}
  - {node_id: P01, label: 生产闭环, layer: L3, function: 线索→策划→采访→核验→结构→发布→反馈, summary_card: SC11, requires: [N02,N04,N06], drill_down: B01/B02/B05/B06}
  - {node_id: P02, label: 结构选择器, layer: L3→L4, function: 按时效/体裁/受众选倒金字塔或叙事结构, summary_card: SC05, requires: [N06], drill_down: B01/B02/B07/B10}
  - {node_id: P03, label: 专业解释闭环, layer: L4, function: 现象→机制→证据→影响→限制→公共意义, summary_card: SC07, requires: [N04,N06], drill_down: B07/B10/B09}
  - {node_id: P04, label: 事实化叙事, layer: L4, function: 用可核场景/细节/引语降低抽象度而不虚构, summary_card: SC06, requires: [N04,N05], drill_down: B07/B10/B04}
  - {node_id: P05, label: 语言与编辑闸门, layer: L4→L5, function: 准确→清楚→简洁→通俗→规范三轮审校, summary_card: SC08, requires: [P01,P02], drill_down: B09/B11/B01}
  - {node_id: M01, label: 议程与框架, layer: L2, function: 区分让什么可见与如何解释, summary_card: SC04+SC10, requires: [N03,N04], drill_down: B08}
  - {node_id: M02, label: 受众媒介适配, layer: L3→L5, function: 改变呈现不改变事实/不确定性, summary_card: SC10, requires: [N03], drill_down: B08/B03/B02}
  - {node_id: G01, label: 真实性与持续核验, layer: L0, function: 来源审查/交叉验证/透明纠错, summary_card: SC02, requires: [N04], drill_down: B04/B01/B05}
  - {node_id: G02, label: 独立公平回应权, layer: L5, function: 证据加权而非机械两边平衡, summary_card: SC09, requires: [G01], drill_down: B04/B03}
  - {node_id: G03, label: 隐私创伤与伤害控制, layer: L5, function: 最小必要识别与比例性公共利益, summary_card: SC09, requires: [G01], drill_down: B04/B06/B07}
  - {node_id: G04, label: B11机构语言规范, layer: L5, function: 2019-07新华社禁慎词范围化审校, summary_card: SC08+SC09, requires: [G01], drill_down: B11}
  - {node_id: G05, label: 版本/更正责任, layer: L5→L6, function: 发布后反馈、修订和可追踪版本, summary_card: SC10, requires: [G01], drill_down: B04/B08/B02}
  - {node_id: D01, label: 失实诊断, layer: L7, function: 补证/降级/延迟/更正, summary_card: SC12, requires: [G01], drill_down: B01/B05/B06}
  - {node_id: D02, label: 失焦诊断, layer: L7, function: 重选主题角度与典型事实, summary_card: SC12, requires: [N06], drill_down: B05/B07/B10}
  - {node_id: D03, label: 失序诊断, layer: L7, function: 重排信息层级、转场和背景, summary_card: SC12, requires: [P02], drill_down: B01/B02/B07}
  - {node_id: D04, label: 失当诊断, layer: L7, function: 语言/伦理/媒介风险修复, summary_card: SC12, requires: [P05,G02], drill_down: B09/B11/B07}
```

## 语义边表

|from|edge|to|条件/意义|
|---|---|---|---|
|N01|requires|N00|事实对象先过不变量|
|N01|supports|N04|事实变动触发核验|
|N02|requires|N01|价值不能脱离事实|
|N04|supports|N06|证据池先于主题|
|N05|supports|N04|采访生成并测试证据|
|N06|tensions_with|M01|角度/主题与框架需分层|
|N04|constrains|P02|结构不得隐藏关键事实|
|P02|refines|P04|叙事是条件分支|
|P03|refines|P04|机制解释回接场景|
|P05|constrains|P04|生动服从事实和规范|
|M01|supports|M02|框架影响受众适配|
|G01|supports|G02|公平建立在可核事实|
|G02|constrains|G03|公共利益不能无限侵扰|
|G04|constrains|P05|机构术语仅在适用范围|
|G05|supports|G01|更正反馈闭环真实性|
|D01|drill_down|N04|失实回证据链|
|D02|drill_down|N06|失焦回主题角度|
|D03|drill_down|P02|失序回结构选择|
|D04|drill_down|P05|失当回语言/伦理|
|P01|composes|N02+N04+N05+N06|生产闭环组合基础节点|
|SC11|applies_to|P01|模板编排任务|
|SC12|applies_to|D01+D02+D03+D04|统一诊断|

## 10 个 task routes

|route_id|触发|顺序|主要卡|升级|
|---|---|---|---|---|
|R01|突发/热搜|事实变动→价值→高影响核验→倒金字塔→发布|SC01→SC02→SC05→SC08|SC10/SC12|
|R02|调查/监督|公共后果→多方采访→证据/回应→框架→伦理|SC01→SC03→SC02→SC04→SC09|SC10/SC12|
|R03|经济/政策解释|影响→数据/原件→机制→个案→通俗化|SC01→SC02→SC04→SC07→SC08|SC09|
|R04|人物/特稿|公共意义→观察采访→核验→中心问题→场景叙事|SC01→SC03→SC02→SC04→SC05→SC06|SC09|
|R05|争议/解释|拆claim→框架审计→回应→机制解释→受众测试|SC02→SC04→SC09→SC07→SC10|SC12|
|R06|会议/政策发布|原文核对→公共影响→直接导语→背景/术语|SC02→SC04→SC05→SC07→SC08|SC10|
|R07|网络/滚动|逐次claim+时间戳→首屏事实→压缩→版本反馈|SC02→SC05→SC08→SC10|SC12|
|R08|高风险称谓/审校|事实身份→伦理→句法→B11范围→版本|SC02→SC09→SC08→SC10|B11原笔记|
|R09|稿件退修/误读|根因分类→回中间物→闸门复测|SC12→SC02/04/05/08/09|SC10|
|R10|跨书复杂/代理协作|统一ledger→分工→证据闸门→整合→发布|SC11→SC02→SC04→SC05→SC09→SC10|SC12|

## risk_router

```yaml
risk_router:
  source_uncertainty: SC02 -> downgrade_exact_claim -> READ_NEXT[source_note]
  legal_ethics: SC09 -> SC02/SC03 -> editor_or_legal_review
  terminology_version: SC09 -> B11_scope_check -> B11_note
  audience_misread: SC10 -> SC04/SC07/SC08 -> SC12_if_persistent
  published_error: SC10 -> versioned_correction -> SC12_process_review
  conflict_unresolved: preserve_conditions -> delay_or_qualify -> source_check
```

## artifact_router

```yaml
artifact_router:
  idea: {artifact: 线索卡, next: SC01}
  claim: {artifact: claim_ledger, next: SC02}
  interview: {artifact: 问题树+现场记录, next: SC03}
  angle: {artifact: 主题/角度卡, next: SC04}
  structure: {artifact: 结构草图, next: SC05}
  draft: {artifact: 稿件+三轮审校表, next: SC08}
  publish: {artifact: 版本日志+更正记录, next: SC10}
  failure: {artifact: 诊断单, next: SC12}
```

## source_router

- 事实/价值/新闻制度：B03、B04；报道生产/采访/结构：B01、B02、B05、B06。
- 叙事/专业解释/编辑：B07、B09、B10；传播/受众/框架/效果：B08。
- 机构语言：B11（仅2019年7月新华社规范，`needs_recheck`）。
- 精确数字/人名/表格/页码：B01、B03 OCR风险先回原PDF；B06 EPUB结构锚点先回逻辑章节；B08图表缺失不得补数值；B10结构重建片段先回原文。

## 冲突/优先级矩阵

|冲突|条件化裁决|
|---|---|
|倒金字塔 vs 叙事|硬新闻/时效/首屏选倒金字塔；过程/人物/机制解释选场景或主题线，均须证据锚点|
|客观性 vs 框架|客观性=证据透明、回应和可纠错；允许主题但不得把选择伪装自然事实|
|简洁 vs 背景|删冗余保留影响判断所需最小充分背景；缺背景导致误读则补背景|
|生动 vs 核验|只用可核场景、行动、原话；不可证细节改概括或删除|
|速度 vs 核验|高影响claim提高门槛；可发布则显式标未知，否则延迟|
|全面 vs 平衡|按证据、影响、权力不对称配置；不制造假对称|
|点击 vs 公共价值|点击仅反馈信号，不替代公共意义、理解和长期效果|

## deep_read_when

- `exact_word_or_rule`：下钻B11；先验证2019版当前是否仍适用。
- `low_confidence_anchor`：下钻对应B01/B03 OCR、B06 EPUB、B08图表、B10结构笔记。
- `high_risk_claim`：下钻B04/B01/B05/B06证据、回应、伦理条目。
- `case_or_example_needed`：下钻B07/B10场景、引语、结构案例。
- `legal_or_privacy_boundary`：下钻SC09指向的单书笔记并咨询现行规则。
