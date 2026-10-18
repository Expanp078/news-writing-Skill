# alpha1.1 项目产物、状态与质量门槛

## 1. 推荐项目目录

每次用户任务建立独立项目目录。目录名由 `task_id` 和简短主题组成，不覆盖既有项目：

```text
news-project/
├── 00-input-manifest.yaml
├── 01-analysis-report.md
├── 02-prewriting-plan.md
├── drafts/
│   ├── draft-v1.md
│   ├── draft-v2.md
│   └── ...
├── reviews/
│   ├── review-r1.md
│   ├── review-r2.md
│   └── ...
├── revisions/
│   ├── revision-log-r1.md
│   └── ...
├── state/
│   ├── progress.yaml
│   ├── resource-load-log.yaml
│   └── input-hashes.yaml
└── final/
    └── final.md
```

## 2. 状态字段

```yaml
task_id: NW-YYYYMMDD-###
skill_version: alpha1.1
state: intake|source_mapped|knowledge_analysis_done|prewriting_done|draft_vN_done|review_rN_done|converged|blocked|final
current_draft: drafts/draft-vN.md
current_review: reviews/review-rN.md
rounds_completed: 0
minimum_rounds: 3
convergence: pending|continue|no_material_change|blocked
unresolved: []
resource_snapshot: {}
writer_context_id: <主写作者标识>
reviewer_context_ids: []
last_update: <ISO-8601>
```

## 3. 写入原则

- 任何主产物先写临时文件、检查必填元数据和哈希，再原子改名；
- 不覆盖分析报告、准备文档、旧稿、旧审阅或修订记录；
- 状态推进必须在对应产物存在且可回读后进行；
- 当前稿、上一稿和所有资源哈希写入状态，避免源材料中途变化导致错误比较；
- 检查者只写自己的 review 文件，不直接修改稿件；
- 用户要求简短交付时，也保留内部 AI 可用产物，除非用户明确要求不留中间文件。

## 4. 终验清单

### 知识和事实

- [ ] 首轮分析确实读取图谱、L0 不变量和相关综合卡；
- [ ] 分析报告有材料地图、claim ledger、来源状态、受众和风险；
- [ ] 经验库在分析报告完成后调用，并标出触发条件和边界；
- [ ] 精确规则、低置信锚点、高风险主张已回源或降级；
- [ ] 稿件没有把经验案例、奖项评价或机构立场冒充事件事实；
- [ ] 未知、冲突和未回应保持可见。
- [ ] 输入清单和分析报告记录材料截点、事件时间、来源发布时间、产品状态和更新触发；
- [ ] 每条高影响 claim 标记来源访问层级和引语模式；未加载原文时没有直接引语；
- [ ] 会议/政策/成果文件标记程序状态、正式题名状态和审批主体。

### 写作和创意

- [ ] 写作前准备不是分析报告的复制，而是可执行的角度/结构/材料选择；
- [ ] 角度和结构至少经过真实比较，或记录了无需比较的理由；
- [ ] 每个关键段落、场景或模块有功能和证据责任；
- [ ] 结构、开头和结尾服从当前材料与受众，不机械套用获奖文本；
- [ ] 允许出现新洞见、反例、冲突或未决，不强行归入既有策略。

### 独立审阅和迭代

- [ ] 每轮检查者使用新上下文并记录加载清单；
- [ ] 检查者盲读时没有看到主写作者准备和上一轮意见；
- [ ] 至少三轮 review—revision 已完成；
- [ ] 每条 P0/P1 有处理记录；
- [ ] 检查意见含位置、依据、后果和修复方向；
- [ ] 第三轮以后才使用 `no_material_change`；
- [ ] 最新检查文档明确写出 `unresolved_p0_p1: 0` 或列出未关闭的 finding ID；
- [ ] 收敛不是由字符相似度单独决定。

### 交付

- [ ] `final/final.md` 可独立阅读；
- [ ] 内部流程痕迹已从终稿清除，但必要的来源和不确定性保留；
- [ ] 所有中间产物和版本可回溯；
- [ ] 若被 `blocked`，交付中明确写出可写范围和阻断原因，不伪造完成。

## 5. 版本升级触发器

以下变化不应直接修改 alpha1.1 的 references：

- 图谱、综合知识库或经验库的主版本发生变化；
- 资源哈希变化；
- 新增体裁或新的外部工具依赖；
- 前向测试发现主流程缺少阶段门槛；
- 检查者独立性、收敛规则或高风险边界发生实质调整。

这些情况应建立新版本或显式重建记录，并保留 alpha1.1 快照以便回退。
