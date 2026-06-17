# Playbooks

这个目录放 `woodstuck` 的模式化打法。

主 Skill 负责：

- 触发
- 路由
- 最小加载
- 全局硬规则

这里负责：

- 某一类任务该怎么审
- 先看什么
- 输出怎么收
- 哪些误判最常见

## 当前 playbooks

- `visual-review.md`
- `interaction-review.md`
- `business-expansion.md`
- `img2-iteration.md`
- `startup-judgment.md`
- `membership-review.md`
- `concept-edition-review.md`

## 维护规则

- 新增玩法时，优先往对应 playbook 补，不要先把主 Skill 写胖
- 只有跨模式都成立的规则，才回写 `SKILL.md`
- 如果一个模式开始包含大量业务细分，再继续往下拆子文件，而不是把例外塞回主 Skill
