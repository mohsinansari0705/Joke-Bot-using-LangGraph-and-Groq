<div align="center">

# 🤡 Joke Bot using LangGraph & Groq

### An intelligent AI-powered joke generator with Writer-Critic Agent Loop

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.0.40+-00ADD8.svg)](https://www.langchain.com/langgraph)
[![Groq](https://img.shields.io/badge/Groq-Llama_3.1-F55036.svg)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---


## ✨ Features

- � **AI Writer-Critic Loop**: Two AI agents collaborate - one generates jokes, another evaluates them
- 🎯 **15+ Joke Categories**: From "Dad Developer" to "Agentic AI Joker"
- 🌍 **Multi-language Support**: Generate jokes in 5 languages (English, Hindi, Spanish, French, German)
- 🎨 **Customizable Creativity**: Adjust AI temperature for different humor styles
- ⚡ **Powered by Groq**: Lightning-fast inference with Llama 3.1 models
- 🔒 **Built-in API Key Validation**: Secure validation directly in the UI
- 📊 **Session Tracking**: Keep track of jokes generated in your session
- 🎭 **Interactive Web UI**: Beautiful Streamlit interface with real-time feedback


## 🏗️ Architecture

This joke bot uses a sophisticated **agentic workflow** powered by LangGraph:
```
┌─────────────────────────────────────────────┐
│           Streamlit Web Interface           │
│              (chatbot.py)                   │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│            Joke Generation Engine           │
│                (joke_bot.py)                │
│                                             │
│     ┌──────────┐      ┌──────────┐          │
│     │  Writer  │─────▶│  Critic  │          │
│     │  Agent   │      │  Agent   │          │
│     └──────────┘      └──────────┘          │
│       │                   │                 │
│       │     Approved?     │                 │
│       │◀─────────────────┘                  │
│       │                                     │
│       ▼                                     │
│      ✅ Final Joke                          │
└─────────────────────────────────────────────┘
```


**Key Components:**
- **Writer Agent**: Creates original jokes based on category and language
- **Critic Agent**: Evaluates joke quality, appropriateness, and humor
- **State Graph**: LangGraph manages the agent loop and state transitions
- **Retry Logic**: Up to 5 attempts to generate an approved joke

## 🔑 How to Get Free Groq API Key

Groq provides **free API access** to their ultra-fast LLM inference platform:

1. **Visit Groq Console**: Go to [console.groq.com](https://console.groq.com/)
2. **Sign Up**: Create a free account using your email or GitHub
3. **Navigate to API Keys**: Click on "API Keys" in the left sidebar
4. **Create New Key**: Click "Create API Key" button
5. **Copy Your Key**: Copy the key that starts with `gsk_...`
6. **Save It Securely**: You'll need this key to run the joke bot

> 💡 **Note**: Groq's free tier is generous and perfect for this project. No credit card required!

---


## 🚀 Installation

### 1: Clone the Repository

```bash
git clone https://github.com/mohsinansari0705/Joke-Bot-using-LangGraph-and-Groq.git
cd Joke-Bot-using-LangGraph-and-Groq
```

### 2. Create Virtual Environment

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4: Run the Application

```bash
streamlit run chatbot.py
```

The app will automatically open in your browser at `http://localhost:8501` 🎉

---


## 🎮 Usage Guide

### Getting Started

1. **Launch the App**: Run `streamlit run chatbot.py`
2. **Enter API Key**: 
   - Paste your Groq API key in the sidebar
   - Click "🔑 Validate API Key" button
   - Wait for the success message ✅

3. **Configure Settings**: 
   - **Joke Category**: Select from 15+ categories
   - **Language**: Choose from 5 languages
   - **Writer Creativity**: Adjust temperature (0.1-1.0)
   - **Critic Strictness**: Adjust temperature (0.1-1.0)

4. **Start Bot**: Click "🚀 Start Joke Bot"

5. **Generate Jokes**: Click "🎲 Generate New Joke" as many times as you want!

6. **Reset**: Use "🔄 Reset Bot" to start a fresh session

### 🎯 Temperature Settings Explained

| Setting | Low (0.1-0.3) | Medium (0.4-0.7) | High (0.8-1.0) |
|---------|---------------|------------------|----------------|
| **Writer Creativity** | Conservative, safe jokes | Balanced humor | Wild, creative jokes |
| **Critic Strictness** | Very consistent | Moderately flexible | More lenient |

---

## 🎭 Available Joke Categories

<table>
<tr>
<td width="50%">

1. 👨‍💻 **Dad Developer** - Pun-based programming humor
2. 🥋 **Chuck Norris Developer** - Epic coding legends
3. 🧠 **AI Philosopher** - Witty AI consciousness jokes
4. 🐛 **Bug Whisperer** - Debugging nightmares
5. 💾 **Old-School Coder** - Nostalgic tech humor
6. 🎨 **Frontend Philosopher** - CSS and UI/UX pain
7. ⚙️ **Backend Barbarian** - API and database jokes
8. ☁️ **Cloud Comedian** - AWS bills and DevOps chaos
9. 📊 **Data Scientist Monk** - ML and data humor
10. 🔒 **Cybersecurity Cynic** - Security and hacking jokes
11. 🧘‍♂️ **DevOps Therapist** - CI/CD therapy sessions
12. 🤖 **Agentic AI Joker** - AI agents gone wrong
13. 🪶 **Prompt Poet** - Prompt engineering poetry
14. 🧮 **Math & Logic Nerd** - Recursion and logic humor
15. 🎯 **General** - Classic programming jokes

</td>
</tr>
</table>

---


## 🔧 Technical Details

### 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Web Framework** | Streamlit | Interactive UI with session management |
| **Agent Framework** | LangGraph | State machine and agent orchestration |
| **LLM Integration** | LangChain | LLM abstraction and prompt management |
| **LLM Provider** | Groq (Llama 3.1) | Ultra-fast inference engine |
| **Validation** | Pydantic | Data validation and state management |
| **Config Management** | PyYAML | Prompt templates and settings |

### 🔄 Agent Loop Workflow

```python
1. Writer Agent generates joke → 
2. Critic Agent evaluates → 
3. Router checks approval → 
4. If approved: Return joke ✅
5. If rejected & retries < 5: Retry from step 1 🔄
6. If max retries: Return best attempt 🎯
```

### 🧠 Models Used

- **Writer Agent**: `llama-3.1-70b-versatile` (Creative generation)
- **Critic Agent**: `llama-3.1-70b-versatile` (Quality evaluation)
- Both powered by Groq's lightning-fast inference

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

- 🐛 Report bugs and issues
- 💡 Suggest new joke categories
- 🌍 Add support for more languages
- 📝 Improve documentation (README.md)
- ✨ Add new features

### Contribution Steps

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

---


## 🙏 Acknowledgments

Built with ❤️ using amazing open-source technologies:

- 🦜 [LangGraph](https://www.langchain.com/langgraph) - For agent orchestration
- ⚡ [Groq](https://groq.com/) - For lightning-fast LLM inference
- 🎨 [Streamlit](https://streamlit.io/) - For the beautiful web interface
- 🤖 [LangChain](https://www.langchain.com/) - For LLM abstraction

Special thanks to the open-source community! 🌟

---

## 📧 Contact & Support

<div align="center">

**Mohsin Ansari**

[![GitHub](https://img.shields.io/badge/GitHub-mohsinansari0705-181717?logo=github)](https://github.com/mohsinansari0705)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin)](https://linkedin.com/in/mohsinansari0705)

**Live Project Link**: [Joke-Bot-using-LangGraph-and-Groq](https://github.com/mohsinansari0705/Joke-Bot-using-LangGraph-and-Groq)

</div>

---

<div align="center">

### ⭐ Star this repo if you found it helpful!

**Made with 🤖 by AI Agents, for Developers who love to laugh** 😄

</div>
