# woodstuck 进化记忆

这个目录用于让 `woodstuck` 在每次真实协作后，留下可复用的经验，而不是每次从零判断。

它不是模型底层“自动永久学习”，而是 skill 内部的可维护进化层。

现在它分成两条学习链：

- `本地蒸馏`
  - 从你和我的真实协作里，沉淀稳定偏好、过稿规律、业务判断方式
- `联网蒸馏`
  - 从最新交互、科技、视觉、版式、产品案例里，吸收外部增量信号

## 结构

- `PROFILE.md`
  - 当前已经稳定成立的用户偏好、过稿规律、输出习惯
- `EVOLUTION_RULES.md`
  - 如何把一次对话沉淀成长期可复用规则
- `ONLINE_LEARNING_PROTOCOL.md`
  - 什么时候需要联网，以及联网后该怎么蒸馏
- `TREND_LOG.md`
  - 联网学习后的高价值趋势记录
- `SESSION_LOG.md`
  - 每次重要协作后的简短沉淀记录
- `SESSION_TEMPLATE.md`
  - 标准化沉淀模板
- `../scripts/append_session_log.py`
  - 一键追加单条学习记录的辅助脚本

## 使用方式

每次命中 `woodstuck` 时，不再默认把学习层全读一遍。

推荐顺序：

1. 先读 `PROFILE.md`
2. 只有在要做沉淀/进化动作时，再读 `EVOLUTION_RULES.md`
3. 如果任务偏当前趋势或方向判断，再读 `ONLINE_LEARNING_PROTOCOL.md`
4. 只有任务明显命中近期重复模式时，才查看 `SESSION_LOG.md` 最近几条
5. 如果需要最新外部输入，先联网，再把高价值信号写入 `TREND_LOG.md`
6. 完成任务后，把这次对话的有效信号写入 `SESSION_LOG.md`
7. 如果同类信号重复出现 3 次以上，再升级写入 `PROFILE.md`

如果需要更稳定地追加记录，可优先使用：

```bash
python scripts/append_session_log.py \
  --task "任务内容" \
  --reaction "用户反应" \
  --effective "有效做法" \
  --ineffective "无效做法" \
  --rule "可复用规则" \
  --promote "否"
```

## 目标

让 skill 的进化更像：

- 越来越懂这个用户怎么收稿
- 越来越懂哪些表达更容易过
- 越来越懂哪些风格和路径不要再重复踩坑
- 越来越懂外面最新什么值得学，什么只是热闹
- 越来越能把单页判断升级成产品、增长和创业判断

而不是只做一次性的临场发挥。
