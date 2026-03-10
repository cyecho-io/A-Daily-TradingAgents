# A-Daily-TradingAgents: 构建你的私人轻量级 AI 交易智囊团

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Strategy-Prompt_as_a_Strategy-orange.svg" alt="Strategy">
  <img src="https://img.shields.io/badge/AI-Multi_Agent_Debate-purple.svg" alt="AI">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</div>

<div align="center">
  <h3>简单高效 · 个人专属 · 开箱即用 · 策略即提示词</h3>
</div>

---

## 📖 项目定位：为什么我们需要一个新的 AI 交易系统？

目前市面上的量化交易或金融 AI 开源项目，往往存在两极分化的问题，让普通个人投资者望而却步：

*   **传统量化框架（如 VN.py, Qlib 等）：** 属于“重型武器”。需要复杂的环境配置（各种数据库、消息队列）、陡峭的代码学习曲线，对仅仅想用 AI 辅助看盘的个人投资者来说，门槛太高。
*   **通用 Agent 框架（如 AutoGen, CrewAI 等）：** 它们很轻量，但需要用户自己编写大量代码来接入金融行情数据、对接交易接口，毫无“金融属性”。

**A-Daily-TradingAgents** 正是为了填补这一空白而生。它的独特定位是：**“一个你能在笔记本上轻松跑起来的、由多个 AI 专家组成的私人交易智囊团”**。

## ✨ 核心亮点：降维打击的极简体验

*   **🪶 极致轻量，零门槛部署**：抛弃繁重的 MySQL、Redis、Kafka 等企业级重度依赖。默认使用 SQLite，真正做到 `git clone` 就能跑。
*   **🧠 Prompt as a Strategy (提示词即策略)**：你不需要懂复杂的 Python 量化代码！通过修改简单的配置文件（Prompt），你就能定制一个具备特殊交易风格的 AI 专家（例如：“打板情绪大师”、“均线回归交易员”、“宏观防守主理人”）。
*   **🗣️ 多专家圆桌会诊 (Multi-Agent Debate)**：就像组建你的游戏战队一样组合你的 Agents。技术面分析师看 K 线，基本面研究员看财报，风控官做最终安全确认。多维博弈，产出极高质量的分析建议。
*   **👁️ 直观可视的“白盒化”输出**：拒绝传统量化冷冰冰的“买/卖”信号。系统会以流式 Markdown 的形式，将多个专家探讨、争论的思考全过程展现给你，为你提供极高的情绪价值和学习参考。
*   **🔋 数据工厂统一上下文**：内置强大的数据工厂，一次性准备所有上下文数据（Tushare/AKShare 行情、资金流向、甚至舆情），一次性喂给大模型，确保其具备“上帝视角”。

## 📸 运行截图

### ✨ 掌控全局：现代化选股 Web 看板
![9e530036ccab133369490d203480ea3d](https://github.com/user-attachments/assets/004ebe2d-2b22-4252-b817-db964d2d92b5)

### 🗣️ 专家圆桌：多 Agent 思考逻辑流式白盒展现
<img width="3344" height="1982" alt="cfa7cf1694be9004b9d6f835c257687f" src="https://github.com/user-attachments/assets/0884b10b-f8d5-4bd4-96a8-e2b5bbbae968" />

### 🧠 捏造你的专家：全 UI 定制专属 Agent Prompt
<img width="3372" height="2476" alt="b19350e229b2e18d3af3a34d173bfd0b" src="https://github.com/user-attachments/assets/1d42a17c-51f7-4b29-accf-ce1a10e10a37" />


## 🚀 极简三步快速开始 

本项目已实现**零配置/零中间件**的极简启动！

### 1. 克隆代码

```bash
git clone https://github.com/cyecho-io/A-Daily-TradingAgents.git
cd A-Daily-TradingAgents
```

### 2. 准备依赖与配置

如果你只打算体验使用，推荐使用虚拟环境：

```bash
# 1. 创建并激活虚拟环境
python -m venv .venv
source .venv/bin/activate  # Windows 下请使用 .venv\Scripts\activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 准备配置文件
cp config.json.example config.json
```

*(温馨提示：请使用你最顺手的编辑器打开 `config.json`，填入你的大模型 `api_key` 和数据源 `tushare_token`，若无 tushare 会自动降级使用免费的行情源。本项目完美支持 DeepSeek 等平价且聪明的模型！)*

### 3. 一键启动 (自动构建并运行)

一切就绪后，直接运行启动脚本！它会自动检查环境、初始化 SQLite 数据库，并拉起后端服务：

```bash
python start.py
```

🎉 **开启你的智囊团**：
启动完毕后，在浏览器中打开 **`http://127.0.0.1:8100`** 即可进入 Web 看板！

*(对于开发者：如果想要二次开发前端界面，可以在 `frontend/` 目录下运行 `npm install` 和 `npm run dev` 启用热更新模式)*


## 📂 优雅简单的代码架构 (遵循 KISS 原则)

| 核心组件 | 说明 |
| :--- | :--- |
| `start.py` / `main.py` | 极简启动入口，一键拉起桌面级服务 |
| `agents.yaml` *(规划中)* | **策略即提示词的核心！**在这里编辑人设，立即生效新专家 |
| `agent_analyst.py` | 🧠 Multi-Agent 多专家辩论调度引擎 |
| `llm_analyst.py` | 大模型通信底层（深度适配 DeepSeek/OpenAI/Gemini） |
| `strategy_data_factory.py` | 统一数据工厂，抓取并对齐所有量化和行情上下文 |
| `database.py` | 傻瓜式 SQLite 适配层，无需任何外部数据库安装 |
| `frontend/` | Vue3 + Vite 打造的现代化丝滑交互界面 |


## ⚠️ 免责声明

本项目仅供技术研究与学习交流使用。**市场有风险，投资需谨慎**。项目中的任何策略或分析结果均不构成投资建议。请勿将本项目的任何自动化信号直接用于真实资金的实盘交易环节。

---
*Powered by Cyecho*
