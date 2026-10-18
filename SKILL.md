---
name: news-writing-alpha1
description: "用跨书知识库与获奖经验库完成新闻稿分析、写作和多轮审阅。"
metadata:
  version: "alpha1.0"
  short-description: "基于跨书知识库和获奖经验库的新闻稿分析、起草与多轮独立审阅"
---

# 新闻稿写作 alpha1.0

本 Skill 用于新闻消息、通讯、深度、调查/舆论监督、评论、政策/经济解释、国际传播、专栏/系列单篇和文字化融合稿的分析、起草、修订与交付。它把跨书知识库作为分析入口，把历届新闻奖经验库作为条件化写作经验层。

## 核心工作方式

收到材料后，先完成材料预检和知识库分析报告，再形成写作前准备文档，然后起草第一版。第一版交给独立的、全新上下文的检查智能体审阅；主写作者根据意见修订。至少完成三轮检查—修订，直到检查智能体判断最新稿与上一稿没有实质变化，且没有未处理的高严重度问题，才交付终稿。

流程有门槛，但不是固定写作模板。主写作者可以改变任务路由、提出新的角度或结构、保留替代方案和未决张力；经验卡用于改变判断，不用于复制获奖作品的句式。检查智能体可以挑战知识库中的策略，并提出新的结构性解法。

## 必须遵守的边界

- 事实、来源观点、记者推断、机构立场和奖项语境分层；材料不能证明的事实不得补写。
- 未加载原文时禁止直接引语；会议/政策/成果文件的预告、草案、提交、通过和生效必须分开记录。
- 先加载图谱和相关综合知识，再按 `READ_NEXT` 下钻单书笔记；不要默认把全部书籍笔记或案例报告塞入上下文。
- 在分析报告完成后才调用经验库选择策略、条件分支和反例。
- 每一版稿件和每一份检查意见都保留，不能覆盖历史版本。
- 检查智能体在盲读前不得读取主写作者的写作前准备、上一轮检查意见或隐藏决策记录。

## 按需读取的参考资料

- 任务路由、加载顺序和资源边界：[references/routing.md](references/routing.md)
- 分析报告和写作前准备协议：[references/analysis-and-prewrite.md](references/analysis-and-prewrite.md)
- 独立检查、修订和收敛协议：[references/review-and-convergence.md](references/review-and-convergence.md)
- 主写作者与检查智能体交接提示词：[references/agent-prompts.md](references/agent-prompts.md)
- 项目产物字段、版本状态和验收：[references/artifacts-and-quality.md](references/artifacts-and-quality.md)
- 当前资源快照与来源哈希：[references/source-manifest.yaml](references/source-manifest.yaml)

如果这些 references 尚未随 Skill 安装，先完成资源构建，不要跳过分析报告或独立审阅阶段。
