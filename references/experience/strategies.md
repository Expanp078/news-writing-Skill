# 独立策略库｜alpha1.2

本文件保存17张综合策略与3张研究吸收策略的稳定ID。字段用于检索和检查，不规定思考顺序、篇幅或创意数量。卡片可组合、反驳、暂不使用；事实与伤害边界不能以创意绕过。

## 读取契约

- `actions/mechanism/checks/failure_signs/failure_recovery/boundary` 是经语义修复的v2.1方法；`operationalization_candidate` 是本次使方法可执行的自主补充，不伪称历史样本已验证。
- `provenance_ids` 仅为历史来源标识，不是文件位置、读取指令或当前新闻证据；运行时不需要历史作品或学习报告。
- `knowledge_nodes` 只使用图谱实际定义的稳定节点；`summary_cards` 只指向现有SC卡。需要细节时读知识库或当前任务材料；历史细节无法验证就不引用。
- 样本条数、获奖身份与旧版confidence不代表统计验证。本版统一以`evidence_scope`表达推断边界。


## SYN2-0001｜问题—主张—受众三角定位

```json
{
  "strategy_id": "SYN2-0001",
  "status": "portable_pattern",
  "trigger": "线索多、价值判断先行或标题想直接定调时",
  "evidence_scope": "全体180件；只迁移定位与审计动作",
  "actions": "把角度写成一条可证主张；列出替代角度和伤害风险；将机构立场单列；为每个主张指定来源和时点",
  "mechanism": "先锁定问题对象，再让证据、结构和受众解释共同约束角度；避免奖项语境替代事实",
  "checks": "主张有主体/时点/范围；推荐语未混入正文；未决因果已标记",
  "failure_signs": "标题承诺口号化；一个人物被当总体；价值词无证据",
  "failure_recovery": "降级主张、缩小范围、回到事实—受众—证据三步；把未决项列入READ_NEXT",
  "boundary": "具体价值判断、政治立场和机构目标保持stance_bound；不能凭单篇升级",
  "operationalization_candidate": {
    "decision_actions": "先写“谁在何时发生何种可核变化，为什么此刻影响谁”；将最有传播力的角度和最有证据的角度并置，说明选用、改写或暂缓原因。读者缺什么知识决定背景位置，不决定事实真伪。",
    "disconfirming_check": "角度是待证问题而非必须兑现的结论；若材料反驳预选角度，应换角度而非挑选有利事实。",
    "boundary_or_alternative": "若受众仅需办事信息，优先讲清条件和行动；人物入口可舍弃，不必强制保留替代角度数量。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0004",
    "SYN2-0006"
  ],
  "knowledge_nodes": [
    "N02",
    "N04",
    "N06",
    "G01"
  ],
  "summary_cards": [
    "SC01",
    "SC02",
    "SC04"
  ],
  "provenance_ids": [
    "AWD-001",
    "AWD-002",
    "AWD-004",
    "AWD-173",
    "AWD-180"
  ],
  "version_relation": "语义修复并操作化原SYN2-0001；不读取历史来源即可执行"
}
```


## SYN2-0002｜证据账本与主张强度闸门

```json
{
  "strategy_id": "SYN2-0002",
  "status": "portable_pattern",
  "trigger": "准备发布、引用数字/引语/政策效果或面临争议来源时",
  "evidence_scope": "跨体裁稳定协议；调查、研究、媒介稿增加专门列",
  "actions": "建立claim ledger；分离事实/解释/价值/预测；根据证据状态调整标题和语气；记录版本与更正入口",
  "mechanism": "账本把“可见细节”转成可审计关系，主张强度随来源独立性、回应质量和更新状态变化",
  "checks": "每条主张有锚点和证据等级；回应/拒答/未取证进入账本；预测与观察分栏",
  "failure_signs": "以权威/奖项/数量替代独立证据；推荐理由伪装正文；固定p01-p10采样被当全文",
  "failure_recovery": "补采独立来源、降级断言、公开未决与更正路径；无法核验则延迟发布",
  "boundary": "不能证明不可见画面/声音/互动效果；不把单一官方结论视为自动充分证据",
  "operationalization_candidate": {
    "decision_actions": "对会改变责任、行动或理解的主张逐项记录：原始材料位置、原话或转述、来源角色、事件时间、发布时间、程序状态、独立性、相反证据和未决项。不同媒体转载同一通稿只算一个来源链。删去不能承担证明责任的绝对词。",
    "disconfirming_check": "账本的目标是解释为何能这样写，不是累积条目。主张覆盖由风险和全文语义决定；没有12条或首10段的上限。来源只能支持其实际知道的范围。",
    "boundary_or_alternative": "材料仅是摘要时不得制造直接引语；高影响缺口未补可转为有归属的状态报道、缩小范围或暂停该结论。"
  },
  "compose_with": [
    "SYN2-0001",
    "SYN2-0008",
    "RES-SYN2-0001"
  ],
  "knowledge_nodes": [
    "N04",
    "G01",
    "G02",
    "G05"
  ],
  "summary_cards": [
    "SC02",
    "SC03",
    "SC09"
  ],
  "provenance_ids": [
    "AWD-006",
    "AWD-012",
    "AWD-019",
    "AWD-039",
    "AWD-180"
  ],
  "version_relation": "语义修复并操作化原SYN2-0002；不读取历史来源即可执行"
}
```


## SYN2-0003｜结构由证明任务决定

```json
{
  "strategy_id": "SYN2-0003",
  "status": "portable_pattern",
  "trigger": "需要在直接消息、问题链、时间弧、场景或系列之间选结构时",
  "evidence_scope": "跨体裁；结构选项不能脱离证据形状",
  "actions": "选择状态声明、问题链、主题线、场景—机制、栏目契约或系列矩阵之一；为每段标功能；保留反事实检验",
  "mechanism": "结构改变读者如何获得证据，不是装饰；同一动作在消息中确认状态、在直播中管理未知、在研究中呈现方法",
  "checks": "逐项核对下述失败信号是否存在；存在时不得判通过。",
  "failure_signs": "首屏承诺与证据不匹配；段落重复；系列篇章无新增证据；场景脱离公共问题",
  "failure_recovery": "重写主张和材料地图，换发动机；缺乏连续证据则改独立稿；无法完成则明确未完结",
  "boundary": "不得把倒金字塔、场景或问答当无条件模板；长稿固定锚点可能是抽取上限",
  "operationalization_candidate": {
    "decision_actions": "把候选段落标成“读者现在需要知道/相信什么”，试排状态先行、问题链、人物行动弧或机制解释。选择能最少制造误解的一条；叙事线可中途切换，只要转场交代证据关系。",
    "disconfirming_check": "逐段测试移位或删除后的理解损失；重复证明同一点应压缩，新的限制、反证和转折不能因打断故事而丢掉。",
    "boundary_or_alternative": "没有连续现场时可以写解释稿；只有单个可核片段时不拼接出虚构连续场景。结构候选只是工作假设。"
  },
  "compose_with": [
    "SYN2-0005",
    "SYN2-0007",
    "SYN2-0010",
    "SYN2-0011"
  ],
  "knowledge_nodes": [
    "P02",
    "N04",
    "N06",
    "P04"
  ],
  "summary_cards": [
    "SC05",
    "SC06",
    "SC07"
  ],
  "provenance_ids": [
    "AWD-001",
    "AWD-004",
    "AWD-011",
    "AWD-093",
    "AWD-171"
  ],
  "version_relation": "语义修复并操作化原SYN2-0003；不读取历史来源即可执行"
}
```


## SYN2-0004｜立场、伦理与奖项语境分离

```json
{
  "strategy_id": "SYN2-0004",
  "status": "portable_pattern",
  "trigger": "作品带有政策号召、机构自我叙述、强烈情绪或推荐表评价时",
  "evidence_scope": "全体；跨制度迁移只保留边界流程",
  "actions": "标注stance_and_scope；将奖项语境作为解释变量；对未成年人、受害者、匿名、因果和安全信息设置硬闸门；保留反例",
  "mechanism": "把可迁移动作与不可迁移立场拆开，使内容可以吸收而不替组织背书",
  "checks": "逐项核对下述失败信号是否存在；存在时不得判通过。",
  "failure_signs": "推荐语当证据；情绪替代事实；个案直推因果；安全警告被“生动性”删掉",
  "failure_recovery": "退回正文锚点和来源分级；去除不必要细节；缩小结论并记录未决",
  "boundary": "具体政治/组织结论保持source_bound或stance_bound；伦理判断不由奖项等级授权",
  "operationalization_candidate": {
    "decision_actions": "将素材中的观察事实、作者判断、组织目标、推荐评价分开。每个强价值词问：是来源的判断，还是记者可独立证明的结果？涉及脆弱主体时按报道目的选择最小必要识别。",
    "disconfirming_check": "明确立场可以进入评论，但不能改变事实门槛。赞誉或奖项只说明评奖语境，不证明传播成效、伦理正确或因果成立。",
    "boundary_or_alternative": "无法同时实现戏剧性和伤害控制时，重构叙述视角或删细节；不把伦理审查简化为统一匿名。"
  },
  "compose_with": [
    "SYN2-0001",
    "SYN2-0002",
    "RES-SYN2-0002"
  ],
  "knowledge_nodes": [
    "G01",
    "G02",
    "G03",
    "M01"
  ],
  "summary_cards": [
    "SC02",
    "SC04",
    "SC09"
  ],
  "provenance_ids": [
    "AWD-026",
    "AWD-063",
    "AWD-168",
    "AWD-175",
    "AWD-180"
  ],
  "version_relation": "语义修复并操作化原SYN2-0004；不读取历史来源即可执行"
}
```


## SYN2-0005｜消息先报状态转换，再分配首屏承诺

```json
{
  "strategy_id": "SYN2-0005",
  "status": "conditional_pattern",
  "trigger": "突发、制度决定、科学完成、公共服务结果或象征入口需要快速交代时",
  "evidence_scope": "HARD_NEWS 17件；跨文化消息须联动SYN2-0009",
  "actions": "先判状态类型和生效时点；核验主体、程序和影响范围；人物或场景入口不得延迟关键状态；位置由证据与读者需要决定",
  "mechanism": "首屏是可验证的状态声明（动作/状态+主体/时间+影响/下一步）；结构选择随状态类型变化",
  "checks": "时间线与程序身份核对；标题与首段一致；政策目标与已生效结果分开",
  "failure_signs": "标题口号化；英雄化吞掉程序；“首次/世界级”无来源；人物入口迟迟未回事实",
  "failure_recovery": "回退为核验状态句；降级绝对词；补下一步和限制",
  "boundary": "个人见证和机构叙事不能替代制度状态；AWD-112/156正文短，需数据质量标记",
  "operationalization_candidate": {
    "decision_actions": "先辨宣布、拟议、提交、通过、签署、实施、完成，分别标主体和时间。首屏写已确认变化及影响范围；背景、个人见证和下一步按读者决策需要加入，不设导语句式。",
    "disconfirming_check": "将标题与证据逐词对照，尤其是“已”“首次”“全面”“将”；预计与完成不可互换。截止时间约束全文时态。",
    "boundary_or_alternative": "场景入口只在不延迟关键状态、且确有核实细节时采用；缺日期不凭“今天”补写。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0003",
    "SYN2-0009"
  ],
  "knowledge_nodes": [
    "N01",
    "N04",
    "P02",
    "G05"
  ],
  "summary_cards": [
    "SC02",
    "SC05",
    "SC08",
    "SC10"
  ],
  "provenance_ids": [
    "AWD-001",
    "AWD-019",
    "AWD-055",
    "AWD-087",
    "AWD-112",
    "AWD-161",
    "AWD-162"
  ],
  "version_relation": "语义修复并操作化原SYN2-0005；不读取历史来源即可执行"
}
```


## SYN2-0006｜评论先锁论证对象，再选语气

```json
{
  "strategy_id": "SYN2-0006",
  "status": "conditional_pattern",
  "trigger": "需要反驳、解释政策/经济、判断伤害、纪念、自省或表达外交立场时",
  "evidence_scope": "COMMENTARY 28件；评论可联动INTERNATIONAL与理论研究",
  "actions": "写出对方最强命题与自身主张；建立事实前提—因果/解释—价值—行动链；列出反例",
  "mechanism": "说服力来自可见推理接缝；语气服从论证任务，而非反过来制造证据",
  "checks": "事实前提有来源；政策愿景不写成效果；结尾行动建议能回到证据；机构立场显式",
  "failure_signs": "情绪/权威压过证据；“双方都有道理”回避差异；一例跳到普遍结论",
  "failure_recovery": "删修辞、补前提、降级因果；把争议和未知写入结尾",
  "boundary": "评论允许明确立场，但不跳过事实账本；纪念性和外交性不可外推为普遍判断",
  "operationalization_candidate": {
    "decision_actions": "先复原被评论对象最强而非最弱的论点；分开事实前提、推断、价值选择和行动建议。选反驳、解释、纪念或倡议的语气，使读者能看见不同意发生在哪一步。",
    "disconfirming_check": "用最强反例挑战自己；若只推翻某一理由，不宣称整个立场被推翻。规范建议写清实施主体和代价。",
    "boundary_or_alternative": "锋利或克制均可，不能借假对称回避证据差异；外交、纪念语境的语气不自动迁移到客观消息。"
  },
  "compose_with": [
    "SYN2-0001",
    "SYN2-0002",
    "SYN2-0004"
  ],
  "knowledge_nodes": [
    "N06",
    "M01",
    "G02",
    "P05"
  ],
  "summary_cards": [
    "SC02",
    "SC04",
    "SC08",
    "SC09"
  ],
  "provenance_ids": [
    "AWD-002",
    "AWD-021",
    "AWD-057",
    "AWD-091",
    "AWD-139",
    "AWD-166"
  ],
  "version_relation": "语义修复并操作化原SYN2-0006；不读取历史来源即可执行"
}
```


## SYN2-0007｜叙事发动机与重大主题分叉

```json
{
  "strategy_id": "SYN2-0007",
  "status": "conditional_pattern",
  "trigger": "需要把人物、机制、系统暴露、历史档案或宏阔主题组织成长稿时",
  "evidence_scope": "NARRATIVE_FEATURE 57件；重大主题与调查性叙事按证据形状分流",
  "actions": "写中心公共问题；判断有无连续现场、档案、多案例或责任链；系列建立总问题—单篇贡献矩阵",
  "mechanism": "场景承担时间、行动或决策证据；主题线把个案接回公共问题；重大主题的机构立场单列",
  "checks": "区分场景是事实证据、机制说明还是氛围；删去作为证据的场景会失去什么，替代材料能否承担同一证明责任；人物不被当总体；每篇新增证据；主题号召有来源与边界",
  "failure_signs": "文学化心理臆测；人物包装；系列重复；宏阔结尾遮蔽证据或立场",
  "failure_recovery": "改为解释稿/个案稿；补档案和多方材料；拆出stance_bound段；停止无证据续篇",
  "boundary": "重大主题不自动等于调查；调查结论需独立证据和回应权；场景细节不是传播效果证明",
  "operationalization_candidate": {
    "decision_actions": "从连续行动、时间跨度、制度机制、档案冲突中找真正推动阅读的动力；给人物一个可证问题，而非预先安排英雄弧。宏观主题通过行动后果、对照和机制获得意义。",
    "disconfirming_check": "观察、当事人回忆、文件记载、作者解释应可区分；必要时交代场景重建来源。不能用结尾拔高补足缺失的因果链。",
    "boundary_or_alternative": "“删场景仍可证”不应机械理解：场景本身可为重要证据。删除测试要问损失的是证据、理解、风险提示还是纯装饰。"
  },
  "compose_with": [
    "SYN2-0003",
    "SYN2-0004",
    "SYN2-0008",
    "SYN2-0015"
  ],
  "knowledge_nodes": [
    "N06",
    "P02",
    "P04",
    "G03"
  ],
  "summary_cards": [
    "SC04",
    "SC05",
    "SC06",
    "SC09"
  ],
  "provenance_ids": [
    "AWD-004",
    "AWD-026",
    "AWD-093",
    "AWD-129",
    "AWD-142",
    "AWD-171",
    "AWD-175"
  ],
  "version_relation": "语义修复并操作化原SYN2-0007；不读取历史来源即可执行"
}
```


## SYN2-0008｜调查/监督：回应改变主张权重

```json
{
  "strategy_id": "SYN2-0008",
  "status": "conditional_pattern",
  "trigger": "指控可能影响个人/机构责任、政策执行或公共安全时",
  "evidence_scope": "AWD-039、AWD-180直接验证；AWD-026/093/119/142为相邻样本，保持条件级",
  "actions": "把指控拆成可核查范围；建立独立证据矩阵；提出可回答问题并记录回应/拒答；将责任强度与程序状态分开；保留整改追踪",
  "mechanism": "回应不是形式平衡，而是证据节点：承认、否认、补件、拒答和矛盾都会改变claim权重",
  "checks": "回应时间与内容可回溯；来源独立；匿名/未成年人风险；后续整改与版本记录",
  "failure_signs": "未回应被写成有罪；个案外推普遍；处分结果代替前置核验；“两边各一半”掩盖权力差",
  "failure_recovery": "补采或缩小范围；降级责任词；公开未取证和未回应；设更新责任",
  "boundary": "直接调查样本不足以形成普遍规范；服务行动介入需另用SYN2-0014",
  "operationalization_candidate": {
    "decision_actions": "将指控拆成事实行为、程序违规、因果责任、动机四个不同强度；发送具体可回答问题，留合理回应机会。回应逐项进入证据矩阵，核对它新增、否认或未回答了什么。",
    "disconfirming_check": "拒答只证明截至某时没有取得回应；处分是程序事实，不能倒推所有指控均成立。双方话语篇幅不等于证据权重。",
    "boundary_or_alternative": "两个直接历史样本只支持条件经验；具体责任和发布判断依赖当前证据。无法安全完成时可发表已证事实及明确未决问题。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0004",
    "SYN2-0010"
  ],
  "knowledge_nodes": [
    "N04",
    "N05",
    "G02",
    "G03",
    "G05"
  ],
  "summary_cards": [
    "SC02",
    "SC03",
    "SC09",
    "SC12"
  ],
  "provenance_ids": [
    "AWD-039",
    "AWD-026",
    "AWD-093",
    "AWD-142",
    "AWD-180"
  ],
  "version_relation": "语义修复并操作化原SYN2-0008；不读取历史来源即可执行"
}
```


## SYN2-0009｜国际传播：语境预算与感官桥边界

```json
{
  "strategy_id": "SYN2-0009",
  "status": "conditional_pattern",
  "trigger": "面向跨文化受众，主体、制度或争点缺少共享背景时",
  "evidence_scope": "INTERNATIONAL 25件；消息/评论/系列可叠加",
  "actions": "列出受众未知项；核对称谓、译名、单位、制度和历史；用当地见证/感官细节降低进入成本；记录误读与反馈",
  "mechanism": "传播摩擦主要来自共享背景差；感官桥改善可理解性，但不等于传播成效或国家态度",
  "checks": "语境包覆盖背景—争点—证据—影响—限制；原话与机构叙事分层；反馈与效果不臆测",
  "failure_signs": "直译歧义；只讲我方结论；外国受访者装饰化；感官细节替代冲突解释",
  "failure_recovery": "补背景和来源；拆事实稿/解释稿；保留原称谓并给可读译名；删除效果断言",
  "boundary": "外交接入、独家专访和机构立场source_bound；受众效果需独立反馈",
  "operationalization_candidate": {
    "decision_actions": "先列目标受众缺少的制度、历史、单位和称谓背景，只补影响理解判断的语境。用当地可核行动或具体经验作为入口，再连接争点、证据、影响与限制。",
    "disconfirming_check": "让不了解本地话语的读者复述要点或列潜在误读；这只是理解测试，不能据此声称国家态度或大范围传播效果。",
    "boundary_or_alternative": "人物见证不能代表其国家；直译与本地化均应保护事实强度、归属和不确定性，涉及争议称谓按任务范围核对。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0005",
    "SYN2-0006",
    "SYN2-0010"
  ],
  "knowledge_nodes": [
    "N03",
    "M01",
    "M02",
    "G02"
  ],
  "summary_cards": [
    "SC04",
    "SC07",
    "SC10"
  ],
  "provenance_ids": [
    "AWD-017",
    "AWD-034",
    "AWD-051",
    "AWD-053",
    "AWD-158",
    "AWD-161",
    "AWD-179"
  ],
  "version_relation": "语义修复并操作化原SYN2-0009；不读取历史来源即可执行"
}
```


## SYN2-0010｜连续产品分叉：栏目契约与有限系列

```json
{
  "strategy_id": "SYN2-0010",
  "status": "conditional_pattern",
  "trigger": "连续发布、追踪报道或多篇项目需要管理承诺时",
  "evidence_scope": "COLUMN 21件；系列报道及国际/通讯系列作为交叉形态",
  "actions": "先判长期栏目还是有限项目；栏目定义读者契约、线索入口和追踪节点；系列定义总问题、终点和每篇不可替代证据；维护版本表",
  "mechanism": "栏目靠稳定期待积累信任；系列靠递进证据完成项目；两者均需独立可读与更新责任",
  "checks": "每期/每篇新增事实；线索筛选偏差可见；回应时限和追踪兑现；跨渠道版本一致",
  "failure_signs": "栏目口号化；系列换案例不增证据；追踪承诺未兑现；离开前文无法理解",
  "failure_recovery": "改独立稿；补总问题/单篇贡献矩阵；公开未完成承诺和更新日期",
  "boundary": "栏目资源、热线、机构品牌和调查法律风险source_bound；连续性不自动证明质量",
  "operationalization_candidate": {
    "decision_actions": "先问项目是否有可完成的总问题：有则设计有限系列，逐篇记录新增证据与终点；长期栏目则明确稳定服务、线索入口、回应和追踪责任。每篇提供最低必要上下文。",
    "disconfirming_check": "每次更新回答新发生了什么、旧判断是否改变、承诺是否兑现；没有新贡献时合并或停更，不为保持节奏复制结构。",
    "boundary_or_alternative": "稳定栏目不是永不结束的系列；资源不足就缩减承诺。公开跟进安排不等于保证事件一定获得解决。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0008",
    "SYN2-0009"
  ],
  "knowledge_nodes": [
    "P01",
    "P02",
    "G05",
    "M02"
  ],
  "summary_cards": [
    "SC05",
    "SC10",
    "SC11"
  ],
  "provenance_ids": [
    "AWD-006",
    "AWD-014",
    "AWD-046",
    "AWD-063",
    "AWD-067",
    "AWD-171",
    "AWD-180"
  ],
  "version_relation": "语义修复并操作化原SYN2-0010；不读取历史来源即可执行"
}
```


## SYN2-0011｜融合/直播：把未完结知识显式化

```json
{
  "strategy_id": "SYN2-0011",
  "status": "productive_tension",
  "trigger": "直播、现场节目、VCR/同期编排或互动问答的文字材料需要复盘时",
  "evidence_scope": "MULTIMEDIA_TEXTUAL 4件；AWD-011/101为持续更新样本，AWD-010为访谈cue样本",
  "actions": "维护known/unknown/updated三栏与时间戳；把观众问题列入待核队列；记录主持/记者/专家交接和脚本cue；区分文本证据与效果",
  "mechanism": "直播的产品不是“更生动成稿”，而是持续更新的知识过程；开放未知比假闭环更诚实",
  "checks": "暂定判断标时点；更新责任人可见；cue/画面/声音/互动分栏；无播放数据不推收视/传播",
  "failure_signs": "强行闭环；脚本顺序被当受众效果；观众问题被当悬念填充；未更新却使用已完成时态",
  "failure_recovery": "发布“截至时点”版本；补后续更新或明确未核；将不可见媒介效果降为待核",
  "boundary": "文字稿不能证明视听效果；现场安全和法定发布规则优先于叙事完整",
  "operationalization_candidate": {
    "decision_actions": "现场按已知、未知、新更正管理知识；为每条信息标来源与时间，为待核问题指定接手角色。交接可从主持到记者到专家，但角色只能解释其权限内证据。",
    "disconfirming_check": "不把节目结束当事件闭环。脚本、镜头说明、实际画面、观众行为是不同材料；仅有文字时只评价可见文字组织。",
    "boundary_or_alternative": "突发安全信息先发布有来源的行动提示；无核验结论保持开放。不能用流畅串词填满事实空白。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0003",
    "SYN2-0010"
  ],
  "knowledge_nodes": [
    "M02",
    "G05",
    "N04",
    "P05"
  ],
  "summary_cards": [
    "SC02",
    "SC08",
    "SC10"
  ],
  "provenance_ids": [
    "AWD-010",
    "AWD-011",
    "AWD-101"
  ],
  "version_relation": "语义修复并操作化原SYN2-0011；不读取历史来源即可执行"
}
```


## SYN2-0012｜科学新闻双时钟：研究有效性与发布窗口

```json
{
  "strategy_id": "SYN2-0012",
  "status": "conditional_pattern",
  "trigger": "科学结果处于论文、发布会、embargo或分类解释可能变动的阶段时",
  "evidence_scope": "AWD-019为直接样本；科学/工程消息可局部组合",
  "actions": "分别记录embargo、论文/同行评审、发布会和采访时间；区分已观察结果、分类解释和记者推断；标题随状态调整",
  "mechanism": "同一事实同时受研究有效性和发布窗口约束；快讯时点不提高分类结论稳定度",
  "checks": "术语可追溯；标题强度与审查状态匹配；“首次/重大”有来源；不确定性显式",
  "failure_signs": "将发布会宣传当论文结论；把分类重划写成定论；宏转录组等术语被过度通俗化",
  "failure_recovery": "改写为“发现/提示/可能”；补论文和方法限制；延迟不可核断言",
  "boundary": "研究对象、样本和外部事实须回源；不可用新闻时效绕过科学审查",
  "operationalization_candidate": {
    "decision_actions": "并列记录研究阶段和发布时钟：预印本/同行评审/重复验证，与禁发期/发布会/新闻截止。把结果、机制解释、分类命名、应用前景拆开；每一层采用各自证据强度。",
    "disconfirming_check": "同行评审不等于最后真理，新闻发布不等于研究已经成熟；检查样本、测量口径、适用范围及替代解释。",
    "boundary_or_alternative": "“提示”“可能”不能挽救根本无证据的说法；保留真正可证结果，删除空泛突破叙事，不机械降低所有语气。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0005",
    "RES-SYN2-0001"
  ],
  "knowledge_nodes": [
    "N04",
    "P03",
    "G01",
    "G05"
  ],
  "summary_cards": [
    "SC02",
    "SC07",
    "SC10"
  ],
  "provenance_ids": [
    "AWD-019"
  ],
  "version_relation": "语义修复并操作化原SYN2-0012；不读取历史来源即可执行"
}
```


## SYN2-0013｜独家/权威来源的接入—独立性拆分

```json
{
  "strategy_id": "SYN2-0013",
  "status": "source_bound",
  "trigger": "稿件依赖独家监管层消息、高层专访或单一权威入口时",
  "evidence_scope": "AWD-012、AWD-034直接样本；不升级普遍模板",
  "actions": "记录来源角色、授权范围、议程与时点；把事实/预测/意图拆分；寻找可独立核验文件和反方材料；核对译文/引语",
  "mechanism": "接入价值解决“拿到什么”，独立性决定“能证明什么”；独家本身是待核变量",
  "checks": "授权和引语边界可回溯；独立来源状态标记；机构动机与未回应可见",
  "failure_signs": "头衔/独家替代证据；来源数量代替独立性；预测被写成事实",
  "failure_recovery": "降级为据称/计划/意向；补文件或延迟；把独家作为报道条件而非质量结论",
  "boundary": "强机构接入、外交时点和发布规则source_bound",
  "operationalization_candidate": {
    "decision_actions": "标来源接近什么决策、有什么利益和授权边界；把“能采访到”与“能独立验证”分栏。优先寻找同期文件、实际执行、受影响方和相反材料。",
    "disconfirming_check": "多个官员若依赖同一内部说法仍可能不独立；来源头衔只影响其知识范围判断，不直接为因果与预测背书。",
    "boundary_or_alternative": "材料确实只能支持某人表态时，可以报道表态及身份，不把计划写成必然结果，也不把所有权威来源一概降为不可靠。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0004",
    "SYN2-0009"
  ],
  "knowledge_nodes": [
    "N04",
    "G01",
    "G02"
  ],
  "summary_cards": [
    "SC02",
    "SC09"
  ],
  "provenance_ids": [
    "AWD-012",
    "AWD-034"
  ],
  "version_relation": "语义修复并操作化原SYN2-0013；不读取历史来源即可执行"
}
```


## SYN2-0014｜介入式求药：服务行动生成制度线索

```json
{
  "strategy_id": "SYN2-0014",
  "status": "novel_insight",
  "trigger": "记者介入帮助受影响者解决紧急问题，同时希望解释制度缺口时",
  "evidence_scope": "AWD-006直接样本；不能当普遍调查规范",
  "actions": "单列service_action；记录介入前后状态、行动触发来源、利益冲突和替代服务渠道；将“获药结果”与“药品为何退出”分为两条claim",
  "mechanism": "介入会改变事件路径，也会生成新证据；救助成功不等于制度因果成立",
  "checks": "披露行动和样本变化；独立核验药品退出；回应与替代解释；对被助者隐私和依赖保持边界",
  "failure_signs": "记者行动诱导结果；把帮助对象当代表样本；救助结果替代制度证据；不披露利益冲突",
  "failure_recovery": "先救急再记账；补独立来源；把制度结论降为假设或待核；必要时转交专业服务",
  "boundary": "source_bound/novel_insight；救助义务、资源和诱导风险随机构而变",
  "operationalization_candidate": {
    "decision_actions": "把记者做过什么、何时介入、如何影响样本和结果单列；将帮助的实际结果与制度失灵解释拆成独立证据链。对救助对象避免以采访或曝光作为帮助条件。",
    "disconfirming_check": "记者行动既能发现线索，也改变被观察事件；解释机制需额外证据，不能把被解决的个案当作未介入状态的自然样本。",
    "boundary_or_alternative": "危急时以专业服务与当事人安全为先；介入边界随机构、情境与利益关系变化。此卡不授权记者承担医疗或执法职责。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0008",
    "SYN2-0004"
  ],
  "knowledge_nodes": [
    "N04",
    "N05",
    "G02",
    "G03"
  ],
  "summary_cards": [
    "SC02",
    "SC03",
    "SC09"
  ],
  "provenance_ids": [
    "AWD-006"
  ],
  "version_relation": "语义修复并操作化原SYN2-0014；不读取历史来源即可执行"
}
```


## SYN2-0015｜场景的决策功能：风险沟通而非装饰

```json
{
  "strategy_id": "SYN2-0015",
  "status": "conditional_pattern",
  "trigger": "现场细节同时承担警告、转移、求助、确认或责任选择时",
  "evidence_scope": "AWD-168直接样本；灾害/安全通讯可局部复用",
  "actions": "标注decision_function；把警告句与时间线、隐患图、现场观察相连；先保留安全信息再回接主题",
  "mechanism": "场景改变读者的行动判断，具有证据和安全功能；删景可能删掉关键风险提示",
  "checks": "警告对应可观察事实；情绪未替代风险；场景后补总体机制；隐私和安全信息不过曝",
  "failure_signs": "为追求生动删掉警告；干部情绪被当因果证据；场景与总体风险脱节",
  "failure_recovery": "恢复决定性句；补时间、地点和可验证风险；把情绪降为人物感受",
  "boundary": "安全场景需遵守专业和伦理规则；不由单篇升级为灾害传播效果",
  "operationalization_candidate": {
    "decision_actions": "识别场景中谁根据什么信号作出什么决定，其行动后果如何；把警告、转移、求助、确认与时间地点相连。决定保留细节前先问它是否改变风险理解。",
    "disconfirming_check": "人物情绪可以解释体验，不能代替危险程度证据；决定性警告需要留出理解空间，而不是只保留最戏剧性的画面。",
    "boundary_or_alternative": "历史场景不是当前避险指令；实际安全建议只能来自当前合格来源，且不得泄露会增加伤害的敏感位置。"
  },
  "compose_with": [
    "SYN2-0003",
    "SYN2-0004",
    "SYN2-0005"
  ],
  "knowledge_nodes": [
    "P04",
    "N04",
    "G03",
    "P02"
  ],
  "summary_cards": [
    "SC02",
    "SC05",
    "SC06",
    "SC09"
  ],
  "provenance_ids": [
    "AWD-168"
  ],
  "version_relation": "语义修复并操作化原SYN2-0015；不读取历史来源即可执行"
}
```


## SYN2-0016｜低金额高权力：公共重要性看程序伤害

```json
{
  "strategy_id": "SYN2-0016",
  "status": "novel_insight",
  "trigger": "线索金额小、受众规模小但存在权力不对称、程序异常或弱者被迫参与时",
  "evidence_scope": "AWD-026直接样本；调查/监督选题条件分支",
  "actions": "先标权力关系、受影响者、程序异常和后果；再看金额、热度和官方处分；保护未成年人/贫困身份",
  "mechanism": "公共重要性由权力与程序伤害构成，不由金额阈值决定；处分是后续证据而非前置核验替代",
  "checks": "受助者是否被迫；记者事实与处分分离；回应权和隐私；责任归因有范围",
  "failure_signs": "以金额或热度筛选公共利益；处分结果代替事实；暴露弱者身份换取冲击",
  "failure_recovery": "缩小人物识别；补程序证据；从个案转机制假设并标未决",
  "boundary": "source_bound/novel_insight；当地法规和处分程序需重新核对",
  "operationalization_candidate": {
    "decision_actions": "金额小的线索先画权力与程序关系：谁能拒绝、谁承担后果、规则如何执行、有没有可重复机制；再决定调查价值与保护措施。",
    "disconfirming_check": "寻找可核的程序事实与权力后果，避免以悲情和低金额反差直接制造道德结论。后续处分与前置事实分别陈述。",
    "boundary_or_alternative": "小事件并非天然有重大公共性；证据只能支持个案时就写个案，不能为升格选题夸大普遍性。"
  },
  "compose_with": [
    "SYN2-0004",
    "SYN2-0008",
    "SYN2-0001"
  ],
  "knowledge_nodes": [
    "N02",
    "N04",
    "G02",
    "G03"
  ],
  "summary_cards": [
    "SC01",
    "SC02",
    "SC09"
  ],
  "provenance_ids": [
    "AWD-026"
  ],
  "version_relation": "语义修复并操作化原SYN2-0016；不读取历史来源即可执行"
}
```


## SYN2-0017｜长期追踪：时间跨度是证据，预测必须条件化

```json
{
  "strategy_id": "SYN2-0017",
  "status": "conditional_pattern",
  "trigger": "报道跨多年重复访问、历史序列与政策趋势并置时",
  "evidence_scope": "AWD-093、AWD-142直接样本；环境/土地/治理主题可组合",
  "actions": "建立基线、测量口径、访问时点和缺失记录；把观察趋势、机制解释、情景预测分栏；列替代政策路径",
  "mechanism": "重复访问增加时间证据，但不自动提供总体代表性；线性外推必须写条件",
  "checks": "每次访问新增证据；口径一致；预测有触发条件和不确定性；政策/替代解释可见",
  "failure_signs": "把长期追踪当代表性证明；把趋势当确定未来；忽略口径和政策变化",
  "failure_recovery": "改“若…则可能”；补样本和口径；把预测移入情景段；安排后续复核",
  "boundary": "source_bound/conditional；预测不能替代调查结果",
  "operationalization_candidate": {
    "decision_actions": "建立可比时间序列：每次访问的对象、指标定义、缺失、政策与环境变化。将观测变化、解释机制、条件预测分栏，标哪些跨时比较成立。",
    "disconfirming_check": "重复访问增加纵向证据，不增加样本代表性；幸存者偏差、对象流失、口径更改都可能伪造趋势。",
    "boundary_or_alternative": "预测须带条件和失效信号；若条件未知，只写观察及解释候选，不必强写未来段。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0007",
    "SYN2-0008"
  ],
  "knowledge_nodes": [
    "N04",
    "P03",
    "G05"
  ],
  "summary_cards": [
    "SC02",
    "SC03",
    "SC07",
    "SC10"
  ],
  "provenance_ids": [
    "AWD-093",
    "AWD-142"
  ],
  "version_relation": "语义修复并操作化原SYN2-0017；不读取历史来源即可执行"
}
```


## RES-SYN2-0001｜研究吸收：过程可审计、外部效度与资源依赖

```json
{
  "strategy_id": "RES-SYN2-0001",
  "status": "research_candidate",
  "trigger": "阅读新闻业务研究、媒体转型或产品研究，需要转译为可试点机制时",
  "evidence_scope": "RESEARCH_ABSORB 6件；以AWD-127、AWD-128、AWD-150、AWD-151、AWD-173、AWD-174为样本",
  "actions": "写研究问题—对象—方法—证据—论证链；分离过程、内容质量与传播指标；记录样本框、回收率、非响应、资源依赖和外部效度；转译为小规模试点和反例",
  "mechanism": "研究价值在可审计过程和条件机制，不在“爆款公式”或单一机构结果；迁移前重新取样",
  "checks": "指标分母可查；样本与方法透明；过程变量可复现；组织资源依赖和外部效度有标记",
  "failure_signs": "5.6亿阅读被当成功因果；单机构能力被当普遍；政策建议被当规范",
  "failure_recovery": "降级为research_candidate/source_bound；设计跨机构对照或后续试点；保留不确定性",
  "boundary": "不替代事实核验、法律伦理和组织决策；不能把论文立场直接当写作规则",
  "operationalization_candidate": {
    "decision_actions": "把研究结果拆成问题、对象、方法、过程变量、结果指标、资源依赖；问同样动作在另一机构是否还能发生。设计小范围可逆试点，用内容质量和可达性指标与传播量并行观察。",
    "disconfirming_check": "大阅读量不能证明某项写法造成成功；需要基线、分母、比较对象和替代解释。资源不可得时试的是适配后的机制，不能宣称复现原结果。",
    "boundary_or_alternative": "试点方案属于research_candidate；没有对照时保留探索性结论，伦理与新闻真实性不作为可牺牲的试验变量。"
  },
  "compose_with": [
    "SYN2-0002",
    "SYN2-0004",
    "RES-SYN2-0002"
  ],
  "knowledge_nodes": [
    "N04",
    "N06",
    "P01",
    "P03"
  ],
  "summary_cards": [
    "SC02",
    "SC04",
    "SC07",
    "SC11"
  ],
  "provenance_ids": [
    "AWD-127",
    "AWD-128",
    "AWD-150",
    "AWD-151",
    "AWD-173",
    "AWD-174"
  ],
  "version_relation": "语义修复并操作化原RES-SYN2-0001；不读取历史来源即可执行"
}
```


## RES-SYN2-0002｜业务研究与理论论文边界：保留论证层级

```json
{
  "strategy_id": "RES-SYN2-0002",
  "status": "conditional_pattern",
  "trigger": "需要吸收新闻论文或理论文本，却担心把规范主张当业务事实时",
  "evidence_scope": "JOURNALISM_THEORY 11件与RESEARCH_ABSORB 6件分开；理论卡保持stance_bound",
  "actions": "理论文本先抽概念、前提、推理和规范范围；业务研究再抽样本、方法、机制和试点条件；两者都列反例与制度语境",
  "mechanism": "论证层级决定可迁移范围：理论提供问题和概念边界，业务研究提供条件机制；均不能越过证据形状直接变成写作模板",
  "checks": "概念定义稳定；样本/方法/引用可查；规范与观察分层；迁移对象明确",
  "failure_signs": "把论文“应当”写成经验规律；把业务指标写成因果；忽略制度/资源边界",
  "failure_recovery": "分栏重写为“理论命题/经验证据/可试点动作”；标stance_bound或research_candidate；要求新样本",
  "boundary": "跨制度迁移和事实结论均需重采；不授予普遍规范地位",
  "operationalization_candidate": {
    "decision_actions": "按论证性质分栏，而非仅按作品类别：描述性发现需要材料，因果解释需要识别条件，规范主张需要价值前提，业务建议需要资源与试点条件。混合文本可同时进入多栏。",
    "disconfirming_check": "同一论文的合理规范目标和薄弱经验证据可以并存；保留分歧，不因立场认同而放宽方法，也不因方法有限否认全部概念价值。",
    "boundary_or_alternative": "当前写作只能借用经检验适合的问题意识和方法；论文的组织制度目标不能自动成为所有稿件规则。"
  },
  "compose_with": [
    "RES-SYN2-0001",
    "SYN2-0001",
    "SYN2-0004"
  ],
  "knowledge_nodes": [
    "N04",
    "N06",
    "G02",
    "P01"
  ],
  "summary_cards": [
    "SC02",
    "SC04",
    "SC09",
    "SC11"
  ],
  "provenance_ids": [
    "AWD-127",
    "AWD-128",
    "AWD-150",
    "AWD-151",
    "AWD-173",
    "AWD-174"
  ],
  "version_relation": "语义修复并操作化原RES-SYN2-0002；不读取历史来源即可执行"
}
```


## RES-SYN2-0003｜新闻论文的概念—证据—规范链

```json
{
  "strategy_id": "RES-SYN2-0003",
  "status": "candidate/source_conflict",
  "trigger": "处理新闻理论/论文作品，需要复盘其推理而非模仿文风时",
  "evidence_scope": "理论概念与论证审计候选；原类别与引用冲突，不能声称11件历史验证。",
  "actions": "定位研究问题和概念定义；检视论证前提、引用证据、反例和适用制度；将规范建议与描述性发现分开",
  "mechanism": "理论论文的可吸收部分是问题意识和论证审计；其价值判断和制度目标保持立场绑定",
  "checks": "概念无偷换；引用与结论强度一致；反例处理；规范和事实分栏",
  "failure_signs": "论文权威被当现场证据；“应当”变成事实报道规则；忽略相反案例",
  "failure_recovery": "降级为stance_bound；仅吸收概念/检查问题；交由业务研究或新数据验证",
  "boundary": "不能直接指导具体稿件事实、采访或法律判断",
  "operationalization_candidate": {
    "decision_actions": "提取核心概念及其排除范围，复原前提到结论的推理；将“是什么”“为什么”“应当怎样”分开。把理论转成当前材料可回答的检查问题，而不直接替当前事实作答。",
    "disconfirming_check": "此处是论证审计候选，非已由11篇论文证明的普遍方法。若概念无法操作化，可保留为启发，不能声称完成经验验证。",
    "boundary_or_alternative": "原卡引用的4篇属于新闻业务研究，无法支持新闻论文样本声明；本版撤回该证据归属与11件支持数，保留低置信的概念审计用途。"
  },
  "compose_with": [
    "RES-SYN2-0002",
    "SYN2-0001",
    "SYN2-0004"
  ],
  "knowledge_nodes": [
    "N06",
    "N04",
    "G02"
  ],
  "summary_cards": [
    "SC02",
    "SC04",
    "SC09"
  ],
  "provenance_ids": [],
  "version_relation": "语义修复并操作化原RES-SYN2-0003；不读取历史来源即可执行"
}
```
