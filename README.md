# 🇰🇷 K-Friend AI

**Smart Life Assistant for Foreigners Living in South Korea**

A Streamlit web application that helps foreigners navigate daily life in Korea through AI-powered tools.

## Features

| Module | Description | AI Backend |
|--------|-------------|------------|
| 💬 K-Friend Chat | Conversational assistant for Korea life questions | Llama 3.3 70B (Groq) |
| 🌐 Translator | EN ↔ KO translation with polite mode (존댓말) | Llama 3.3 70B (Groq) |
| 🛒 Grocery Planner | Budget-based weekly grocery plans with Korean store prices | Llama 3.3 70B (Groq) |

## Quick Start

### 1. Get a Free Groq API Key
1. Go to [console.groq.com](https://console.groq.com/keys)
2. Sign up (free)
3. Create an API key

### 2. Install & Run Locally
```bash
# Clone or download this folder
cd kfriend-ai

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### 3. Deploy to Streamlit Cloud (Free)
1. Push this folder to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo → select `app.py`
4. Deploy!

Users enter their own Groq API key in the sidebar — no secrets needed in deployment.

## Tech Stack

- **Frontend**: Streamlit
- **LLM**: Llama 3.3 70B via Groq API (free tier)
- **Language**: Python 3.10+

## Project Info

- **Author**: Shah Zohaib Hassan (2517011)
- **Course**: Project-Based Machine Learning
- **University**: Kyungdong University Global (KDU Global)
- **Year**: 2025–2026
