import streamlit as st

# ─── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="K-Friend AI",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Premium Custom CSS ───────────────────────────────────────
st.markdown("""
<style>
/* ── Import Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

/* ── Global Reset ── */
*, *::before, *::after { font-family: 'Plus Jakarta Sans', sans-serif !important; }

/* ── Root Variables ── */
:root {
    --primary: #0D9373;
    --primary-light: #E8F5F0;
    --primary-dark: #065F4A;
    --accent: #FF6B35;
    --bg-main: #F7F9FC;
    --bg-card: #FFFFFF;
    --bg-sidebar: #0B1F1A;
    --text-primary: #1A1D23;
    --text-secondary: #6B7280;
    --text-muted: #9CA3AF;
    --border: #E5E7EB;
    --border-light: #F0F2F5;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
    --shadow-md: 0 4px 16px rgba(0,0,0,0.08);
    --shadow-lg: 0 8px 30px rgba(0,0,0,0.12);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 20px;
}

/* ── Main Background ── */
.stApp, [data-testid="stAppViewContainer"] {
    background: var(--bg-main) !important;
}
.main .block-container {
    max-width: 1100px;
    padding: 1rem 2rem 3rem 2rem;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B1F1A 0%, #0F2E25 50%, #0B1F1A 100%) !important;
}
[data-testid="stSidebar"] * {
    color: #E0E8E5 !important;
}
[data-testid="stSidebar"] .stTextInput label,
[data-testid="stSidebar"] .stTextInput input {
    color: #E0E8E5 !important;
}
[data-testid="stSidebar"] .stTextInput input {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: var(--radius-sm) !important;
}
[data-testid="stSidebar"] .stTextInput input:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 2px rgba(13,147,115,0.25) !important;
}
[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.1) !important;
}

/* ── Tab Styling ── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card);
    border-radius: var(--radius-lg);
    padding: 6px;
    gap: 4px;
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border-light);
}
.stTabs [data-baseweb="tab"] {
    border-radius: var(--radius-md) !important;
    padding: 12px 24px !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    color: var(--text-secondary) !important;
    transition: all 0.2s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
    background: var(--primary-light) !important;
    color: var(--primary-dark) !important;
}
.stTabs [aria-selected="true"] {
    background: var(--primary) !important;
    color: white !important;
}
.stTabs [data-baseweb="tab-highlight"] {
    display: none !important;
}
.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

/* ── Card Style ── */
.card {
    background: var(--bg-card);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border-light);
    margin-bottom: 1rem;
    transition: box-shadow 0.2s ease;
}
.card:hover {
    box-shadow: var(--shadow-md);
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: var(--radius-md) !important;
    padding: 0.7rem 1.5rem !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 2px 8px rgba(13,147,115,0.3) !important;
    letter-spacing: 0.01em !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(13,147,115,0.4) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── Input Fields ── */
.stTextInput input, .stTextArea textarea, .stNumberInput input, .stSelectbox > div > div {
    border-radius: var(--radius-sm) !important;
    border: 1.5px solid var(--border) !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
    font-size: 0.9rem !important;
}
.stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(13,147,115,0.12) !important;
}

/* ── Chat Messages ── */
[data-testid="stChatMessage"] {
    background: var(--bg-card) !important;
    border-radius: var(--radius-lg) !important;
    border: 1px solid var(--border-light) !important;
    box-shadow: var(--shadow-sm) !important;
    padding: 1rem 1.2rem !important;
    margin-bottom: 0.75rem !important;
}

/* ── Chat Input ── */
[data-testid="stChatInput"] {
    border-radius: var(--radius-lg) !important;
}
[data-testid="stChatInput"] textarea {
    border-radius: var(--radius-lg) !important;
    border: 2px solid var(--border) !important;
    padding: 1rem !important;
    font-size: 0.95rem !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(13,147,115,0.12) !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--bg-card) !important;
    border-radius: var(--radius-md) !important;
    border: 1px solid var(--border-light) !important;
    font-weight: 600 !important;
}

/* ── Metrics / Number Input ── */
.stNumberInput > div > div > input {
    text-align: center !important;
    font-weight: 600 !important;
}

/* ── Radio / Checkbox ── */
.stRadio > div, .stCheckbox > label {
    font-weight: 500 !important;
}

/* ── Multiselect pills ── */
[data-baseweb="tag"] {
    background: var(--primary-light) !important;
    color: var(--primary-dark) !important;
    border-radius: 20px !important;
    font-weight: 500 !important;
}

/* ── Success/Error/Warning ── */
.stSuccess { border-radius: var(--radius-md) !important; }
.stError { border-radius: var(--radius-md) !important; }
.stWarning { border-radius: var(--radius-md) !important; }

/* ── Spinner ── */
.stSpinner > div { color: var(--primary) !important; }

/* ── Hero Header ── */
.hero {
    text-align: center;
    padding: 2rem 1rem 1.5rem 1rem;
    margin-bottom: 1rem;
}
.hero-badge {
    display: inline-block;
    background: var(--primary-light);
    color: var(--primary-dark);
    font-size: 0.75rem;
    font-weight: 700;
    padding: 4px 14px;
    border-radius: 20px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}
.hero h1 {
    font-size: 2.4rem;
    font-weight: 800;
    color: var(--text-primary);
    margin: 0.3rem 0;
    line-height: 1.2;
    letter-spacing: -0.02em;
}
.hero h1 .highlight {
    background: linear-gradient(135deg, var(--primary), #14B88E);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero p {
    color: var(--text-secondary);
    font-size: 1.05rem;
    margin-top: 0.5rem;
    font-weight: 400;
    line-height: 1.6;
}

/* ── Quick Action Cards ── */
.quick-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 1rem;
}
.quick-card {
    background: var(--bg-card);
    border: 1.5px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 0.9rem 1rem;
    cursor: pointer;
    transition: all 0.2s ease;
    text-align: left;
}
.quick-card:hover {
    border-color: var(--primary);
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
}
.quick-card .emoji { font-size: 1.3rem; margin-bottom: 0.3rem; }
.quick-card .title { font-size: 0.82rem; font-weight: 600; color: var(--text-primary); line-height: 1.4; }

/* ── Feature Pill ── */
.feature-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 0.78rem;
    font-weight: 500;
    color: var(--text-secondary);
    margin: 3px;
}

/* ── Section Label ── */
.section-label {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    margin-bottom: 0.8rem;
}

/* ── Translator Result Box ── */
.result-box {
    background: linear-gradient(135deg, var(--primary-light) 0%, #F0FBF7 100%);
    border: 1px solid #C6E8DA;
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    margin-top: 1rem;
}

/* ── Phrase Card ── */
.phrase-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.7rem 0;
    border-bottom: 1px solid var(--border-light);
}
.phrase-row:last-child { border-bottom: none; }
.phrase-kr { font-weight: 600; color: var(--text-primary); font-size: 0.9rem; }
.phrase-en { color: var(--text-secondary); font-size: 0.85rem; }

/* ── Stat Card ── */
.stat-row {
    display: flex;
    gap: 12px;
    margin-bottom: 1rem;
}
.stat-card {
    flex: 1;
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 1rem;
    text-align: center;
}
.stat-card .num { font-size: 1.4rem; font-weight: 700; color: var(--primary); }
.stat-card .label { font-size: 0.72rem; color: var(--text-muted); margin-top: 2px; text-transform: uppercase; letter-spacing: 0.05em; }

/* ── Hide Streamlit defaults ── */
#MainMenu { visibility: hidden; }
header { visibility: hidden; }
footer { visibility: hidden; }

/* ── Responsive ── */
@media (max-width: 768px) {
    .hero h1 { font-size: 1.8rem; }
    .quick-grid { grid-template-columns: 1fr; }
    .stat-row { flex-direction: column; }
    .main .block-container { padding: 0.5rem 1rem 2rem 1rem; }
}
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1.5rem 0 0.5rem 0;">
        <div style="font-size: 2.5rem; margin-bottom: 0.3rem;">🇰🇷</div>
        <div style="font-size: 1.4rem; font-weight: 800; letter-spacing: -0.02em;">K-Friend AI</div>
        <div style="font-size: 0.75rem; color: rgba(255,255,255,0.5); margin-top: 4px; letter-spacing: 0.05em; text-transform: uppercase;">Smart Life Assistant</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

    groq_api_key = st.text_input(
        "🔑 Groq API Key",
        type="password",
        help="Get your free key at console.groq.com/keys",
        placeholder="gsk_...",
    )

    if groq_api_key:
        st.success("✓ API key set", icon="✅")
    else:
        st.info("Enter your free Groq API key to start", icon="🔑")

    st.divider()

    st.markdown("""
    <div style="padding: 0 0.2rem;">
        <div style="font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: rgba(255,255,255,0.35); margin-bottom: 12px;">Modules</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; background: rgba(13,147,115,0.15); border-radius: 8px; border: 1px solid rgba(13,147,115,0.2);">
                <span style="font-size: 1.1rem;">💬</span>
                <span style="font-size: 0.85rem; font-weight: 600;">K-Friend Chat</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <span style="font-size: 1.1rem;">🌐</span>
                <span style="font-size: 0.85rem; font-weight: 500;">Translator</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <span style="font-size: 1.1rem;">🛒</span>
                <span style="font-size: 0.85rem; font-weight: 500;">Grocery Planner</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <span style="font-size: 1.1rem;">📸</span>
                <span style="font-size: 0.85rem; font-weight: 500;">Sign Reader</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <span style="font-size: 1.1rem;">💼</span>
                <span style="font-size: 0.85rem; font-weight: 500;">Job Simplifier</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("""
    <div style="text-align: center; padding: 0.5rem 0;">
        <div style="font-size: 0.7rem; color: rgba(255,255,255,0.3);">Built by Shah Zohaib Hassan</div>
        <div style="font-size: 0.65rem; color: rgba(255,255,255,0.2); margin-top: 2px;">KDU Global · AI Department · 2026</div>
    </div>
    """, unsafe_allow_html=True)


# ─── Hero Header ───────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">🇰🇷 AI-Powered Assistant</div>
    <h1>Meet your <span class="highlight">K-Friend</span></h1>
    <p>Navigate life in South Korea with confidence. Chat about visas, translate anything,<br>plan groceries, read Korean signs, and simplify job postings — all in one place.</p>
</div>
""", unsafe_allow_html=True)


# ─── Tabs ──────────────────────────────────────────────────────
tab_chat, tab_translate, tab_grocery, tab_sign, tab_job = st.tabs([
    "💬  K-Friend Chat",
    "🌐  Translator",
    "🛒  Grocery Planner",
    "📸  Sign Reader",
    "💼  Job Simplifier",
])


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 1: K-FRIEND CHATBOT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SYSTEM_PROMPT = """You are K-Friend AI, a warm and knowledgeable assistant designed to help foreigners living in South Korea navigate daily life.

Your expertise covers:
- **Visa & Immigration**: D-2 student visa, E-7 work visa, F-2/F-5 residency, KIIP program, visa renewals, ARC card
- **Daily Life**: Banking (opening accounts, transfers), phone plans, internet setup, utilities, rent (jeonse/wolse)
- **Transportation**: T-money, KTX, intercity buses, subway systems, K-Pass transit card
- **Food & Shopping**: Korean grocery stores, halal food options, Coupang/Baemin/Yogiyo, convenience stores, Daiso
- **Healthcare**: National Health Insurance (NHI), hospital visits, pharmacies, emergency numbers
- **Culture & Language**: Basic Korean phrases, cultural norms, TOPIK exam, Korean classes
- **Work**: Part-time work rules for students (20hrs/week during semester), tax filing, labor rights
- **Education**: Korean university system, GKS scholarship, course registration

Guidelines:
- Always be friendly, supportive, and encouraging — you're their "Korean friend"
- Give specific, actionable answers (phone numbers, websites, exact steps)
- When mentioning Korean terms, include both Korean (한글) and English
- If you're unsure about current regulations, say so and suggest they verify at Hi Korea (hikorea.go.kr) or 1345 immigration hotline
- Use simple English — many users are not native English speakers
- When relevant, mention costs in Korean Won (₩)
- Keep answers concise but complete
"""

with tab_chat:
    st.markdown('<div class="section-label">Ask anything about life in Korea</div>', unsafe_allow_html=True)

    # Initialize chat history
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    # Display chat history
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask me anything — visas, banking, food, transport..."):
        if not groq_api_key:
            st.error("⚠️ Please enter your Groq API key in the sidebar to use the chatbot.")
        else:
            st.session_state.chat_messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        from groq import Groq
                        client = Groq(api_key=groq_api_key)
                        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                        messages += [
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.chat_messages
                        ]
                        response = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=messages,
                            temperature=0.7,
                            max_tokens=1024,
                        )
                        reply = response.choices[0].message.content
                        st.markdown(reply)
                        st.session_state.chat_messages.append(
                            {"role": "assistant", "content": reply}
                        )
                    except Exception as e:
                        st.error(f"Error: {e}")

    # Quick questions — only show when no chat history
    if not st.session_state.chat_messages:
        st.markdown("""
        <div class="quick-grid">
            <div class="quick-card">
                <div class="emoji">🏦</div>
                <div class="title">How do I open a bank account?</div>
            </div>
            <div class="quick-card">
                <div class="emoji">📋</div>
                <div class="title">D-2 visa renewal process?</div>
            </div>
            <div class="quick-card">
                <div class="emoji">🏥</div>
                <div class="title">How does health insurance work?</div>
            </div>
            <div class="quick-card">
                <div class="emoji">🍗</div>
                <div class="title">Halal food options near me?</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Actual clickable buttons (styled to match)
        cols = st.columns(2)
        quick_qs = [
            "How do I open a bank account in Korea?",
            "What's the D-2 visa renewal process?",
            "How does health insurance work for students?",
            "Where can I find halal food in Korea?",
        ]
        for i, q in enumerate(quick_qs):
            with cols[i % 2]:
                if st.button(q, key=f"q_{i}", use_container_width=True):
                    st.session_state.chat_messages.append({"role": "user", "content": q})
                    st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 2: TRANSLATOR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_translate:
    st.markdown('<div class="section-label">English ↔ Korean Translation</div>', unsafe_allow_html=True)

    # Stats row
    st.markdown("""
    <div class="stat-row">
        <div class="stat-card">
            <div class="num">🌐</div>
            <div class="label">Powered by Llama 3.3</div>
        </div>
        <div class="stat-card">
            <div class="num">✨</div>
            <div class="label">Polite Mode (존댓말)</div>
        </div>
        <div class="stat-card">
            <div class="num">📝</div>
            <div class="label">Cultural Notes</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1])

    with col_left:
        direction = st.radio(
            "Direction",
            ["English → Korean", "Korean → English"],
            horizontal=True,
        )

    with col_right:
        polite_mode = st.checkbox(
            "✨ Polite / Formal mode (존댓말)",
            value=True,
            help="Outputs Korean in polite/formal speech level",
        )

    text_input = st.text_area(
        "Enter text to translate",
        height=130,
        placeholder="Type or paste your text here...",
    )

    if st.button("🔄  Translate", type="primary", use_container_width=True, key="translate_btn"):
        if not text_input.strip():
            st.warning("Please enter some text.")
        elif not groq_api_key:
            st.error("⚠️ Please enter your Groq API key in the sidebar.")
        else:
            with st.spinner("Translating..."):
                try:
                    from groq import Groq
                    client = Groq(api_key=groq_api_key)

                    if direction == "English → Korean":
                        translate_prompt = f"""Translate the following English text to Korean.
{"Use polite/formal speech level (존댓말/합쇼체)." if polite_mode else "Use casual speech level (반말)."}

Text: {text_input}

Provide:
1. **Translation**: The Korean translation
2. **Romanization**: The romanized pronunciation
3. **Notes**: Any cultural context or usage tips (1-2 sentences max)"""
                    else:
                        translate_prompt = f"""Translate the following Korean text to English.

Text: {text_input}

Provide:
1. **Translation**: The English translation
2. **Original speech level**: Whether the Korean uses formal (존댓말) or casual (반말) speech
3. **Notes**: Any cultural context or nuance (1-2 sentences max)"""

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": "You are an expert Korean-English translator. Provide accurate, natural translations with helpful cultural context."},
                            {"role": "user", "content": translate_prompt},
                        ],
                        temperature=0.3,
                        max_tokens=512,
                    )
                    result = response.choices[0].message.content
                    st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Translation error: {e}")

    # Essential Phrases
    with st.expander("📚 Essential Korean Phrases for Daily Life"):
        phrases = [
            ("안녕하세요", "annyeonghaseyo", "Hello (formal)"),
            ("감사합니다", "gamsahamnida", "Thank you (formal)"),
            ("이거 얼마예요?", "igeo eolmayeyo?", "How much is this?"),
            ("화장실 어디예요?", "hwajangsil eodiyeyo?", "Where is the bathroom?"),
            ("도와주세요", "dowajuseyo", "Please help me"),
            ("한국어 못해요", "hangugeo mothaeyo", "I can't speak Korean"),
            ("메뉴판 주세요", "menyupan juseyo", "Menu please"),
            ("계산해 주세요", "gyesanhae juseyo", "Bill please"),
            ("여기요!", "yeogiyo!", "Excuse me! (to call staff)"),
            ("매워요?", "maewoyo?", "Is it spicy?"),
        ]
        for kr, roman, en in phrases:
            st.markdown(f"""
            <div class="phrase-row">
                <div>
                    <span class="phrase-kr">{kr}</span>
                    <span style="color: var(--text-muted); font-size: 0.78rem; margin-left: 8px;">({roman})</span>
                </div>
                <span class="phrase-en">{en}</span>
            </div>
            """, unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 3: GROCERY PLANNER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_grocery:
    st.markdown('<div class="section-label">Weekly Grocery Planning</div>', unsafe_allow_html=True)

    # Budget stat cards
    st.markdown("""
    <div class="stat-row">
        <div class="stat-card">
            <div class="num">₩25K</div>
            <div class="label">Avg Student / Week</div>
        </div>
        <div class="stat-card">
            <div class="num">₩40K</div>
            <div class="label">Comfortable / Week</div>
        </div>
        <div class="stat-card">
            <div class="num">🏪</div>
            <div class="label">Korea Store Prices</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        budget = st.number_input(
            "💰 Weekly Budget (₩)",
            min_value=10000,
            max_value=500000,
            value=30000,
            step=5000,
        )
        household_size = st.selectbox(
            "👥 Cooking for",
            ["Just me", "2 people", "3-4 people"],
        )

    with col2:
        dietary = st.multiselect(
            "🍽️ Dietary Requirements",
            ["Halal", "Vegetarian", "Vegan", "No pork", "No seafood", "Gluten-free", "No spicy food"],
            default=[],
        )
        cooking_level = st.select_slider(
            "👨‍🍳 Cooking skill",
            options=["Beginner", "Basic", "Intermediate", "Advanced"],
            value="Basic",
        )

    preferred_stores = st.multiselect(
        "🏪 Where do you usually shop?",
        ["E-Mart / Homeplus", "GS25 / CU / 7-Eleven", "Local market (시장)", "Coupang (online)", "Daiso", "No Preference"],
        default=["No Preference"],
    )

    if st.button("📋  Generate Grocery Plan", type="primary", use_container_width=True, key="grocery_btn"):
        if not groq_api_key:
            st.error("⚠️ Please enter your Groq API key in the sidebar.")
        else:
            with st.spinner("Planning your groceries..."):
                try:
                    from groq import Groq
                    client = Groq(api_key=groq_api_key)

                    dietary_str = ", ".join(dietary) if dietary else "None"
                    stores_str = ", ".join(preferred_stores)

                    grocery_prompt = f"""You are a grocery planning assistant for a foreigner living in South Korea.

Create a weekly grocery plan with these constraints:
- Budget: ₩{budget:,} per week
- Household: {household_size}
- Dietary requirements: {dietary_str}
- Cooking level: {cooking_level}
- Preferred stores: {stores_str}

Provide:

1. **🛒 Shopping List** — organized by category (produce, protein, staples, etc.)
   - Item name in English AND Korean (한글)
   - Estimated price in ₩
   - Where to buy (cheapest store for this item)

2. **🍳 3 Simple Meal Ideas** — using the listed ingredients
   - Quick description + cooking time

3. **💰 Budget Breakdown** — total by category, remaining budget

4. **💡 Money-Saving Tips** — 2-3 Korea-specific tips

Keep prices realistic for South Korea in 2026. Use real store names."""

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": "You are a helpful grocery planning assistant with deep knowledge of South Korean grocery stores, prices, and food culture. You help foreigners shop smart on a budget."},
                            {"role": "user", "content": grocery_prompt},
                        ],
                        temperature=0.7,
                        max_tokens=1500,
                    )
                    result = response.choices[0].message.content
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Error: {e}")

    with st.expander("🏪 Guide to Korean Grocery Stores"):
        st.markdown("""
**Budget-Friendly Options:**
- **Local markets (시장)** — Cheapest for fresh produce, meat, fish
- **E-Mart / Homeplus** — Best for bulk buying rice, oil, staples
- **Coupang Rocket Fresh** — Convenient delivery, good for heavy items
- **No Brand (노브랜드)** — E-Mart's budget line, great value

**Convenience Stores (편의점):**
- GS25, CU, 7-Eleven — Quick meals & snacks
- Triangle kimbap (삼각김밥) ≈ ₩1,200
- Cup ramen + rice ≈ ₩2,500

**Halal / International Food:**
- Itaewon (이태원) — Halal butchers & restaurants
- Ansan Multicultural Food Street
- Coupang search "할랄" (halal) for online options
""")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 4: KOREAN SIGN & MENU PHOTO READER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_sign:
    st.markdown('<div class="section-label">Korean Sign & Menu Photo Reader</div>', unsafe_allow_html=True)

    st.markdown("Upload a photo of any Korean text — a street sign, restaurant menu, product label, notice, or document — and get an instant English translation.")

    st.markdown("")
    sc1, sc2, sc3 = st.columns(3)
    with sc1:
        st.markdown("📸 **Step 1**\n\nUpload a photo")
    with sc2:
        st.markdown("🔍 **Step 2**\n\nOCR extracts text")
    with sc3:
        st.markdown("🌐 **Step 3**\n\nInstant translation")
    st.markdown("---")

    uploaded_image = st.file_uploader(
        "📷 Upload a photo with Korean text",
        type=["jpg", "jpeg", "png", "webp"],
        help="Take a photo of any Korean sign, menu, label, or notice",
    )

    if uploaded_image:
        col_img, col_result = st.columns([1, 1])

        with col_img:
            st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

        with col_result:
            if st.button("🔍  Extract & Translate", type="primary", use_container_width=True, key="ocr_btn"):
                if not groq_api_key:
                    st.error("⚠️ Please enter your Groq API key in the sidebar.")
                else:
                    with st.spinner("Reading Korean text..."):
                        try:
                            import easyocr
                            import numpy as np
                            from PIL import Image
                            import io

                            # Load image
                            image_bytes = uploaded_image.getvalue()
                            image = Image.open(io.BytesIO(image_bytes))
                            image_np = np.array(image)

                            # Run EasyOCR
                            reader = easyocr.Reader(["ko", "en"], gpu=False)
                            results = reader.readtext(image_np)

                            if not results:
                                st.warning("No text detected in the image. Try a clearer photo.")
                            else:
                                # Extract text
                                detected_texts = [text for (_, text, conf) in results]
                                full_text = "\n".join(detected_texts)

                                st.markdown("**📝 Detected Text (Korean):**")
                                st.code(full_text, language=None)

                                # Translate using Groq
                                with st.spinner("Translating..."):
                                    from groq import Groq
                                    client = Groq(api_key=groq_api_key)

                                    translate_prompt = f"""I extracted the following Korean text from a photo (it could be a sign, menu, product label, or notice). Please:

1. **Clean Text**: Fix any OCR errors and show the corrected Korean text
2. **Translation**: Translate everything to English
3. **Context**: Briefly explain what this is (menu item? warning sign? product label?) and any useful context for a foreigner

Extracted text:
{full_text}"""

                                    response = client.chat.completions.create(
                                        model="llama-3.3-70b-versatile",
                                        messages=[
                                            {"role": "system", "content": "You are a Korean-English translator helping foreigners understand Korean text from photos. Fix OCR errors, translate accurately, and provide helpful context."},
                                            {"role": "user", "content": translate_prompt},
                                        ],
                                        temperature=0.3,
                                        max_tokens=800,
                                    )
                                    translation = response.choices[0].message.content
                                    st.markdown("**🌐 Translation & Context:**")
                                    st.markdown(translation)

                        except ImportError:
                            st.error("EasyOCR is not installed. Add `easyocr` to requirements.txt and redeploy.")
                        except Exception as e:
                            st.error(f"Error: {e}")

    else:
        st.markdown("")
        qc1, qc2 = st.columns(2)
        with qc1:
            st.markdown("🍜 **Restaurant menus**")
            st.markdown("📦 **Product labels & ingredients**")
        with qc2:
            st.markdown("🚏 **Street signs & directions**")
            st.markdown("📋 **Notices & documents**")

    with st.expander("💡 Tips for Best Results"):
        st.markdown("""
- **Good lighting** — avoid shadows and glare
- **Straight angle** — hold camera parallel to the text
- **Close up** — make sure text is large and readable in the photo
- **One item at a time** — focus on one sign/menu/label per photo
- Works with: menus, signs, product labels, notices, receipts, subway maps
""")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 5: JOB POSTING SIMPLIFIER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_job:
    st.markdown('<div class="section-label">Job Posting Simplifier</div>', unsafe_allow_html=True)

    st.markdown("Paste a Korean part-time job posting (from Albamon, Saramin, or any site) and get a clear, simple English summary with all the key details extracted.")

    st.markdown("")
    jc1, jc2, jc3 = st.columns(3)
    with jc1:
        st.markdown("💼 **Step 1**\n\nPaste Korean job ad")
    with jc2:
        st.markdown("🔄 **Step 2**\n\nAuto translation")
    with jc3:
        st.markdown("📋 **Step 3**\n\nSimple summary")
    st.markdown("---")

    job_input = st.text_area(
        "📋 Paste Korean job posting here",
        height=180,
        placeholder="알바몬, 사람인, 잡코리아 등에서 복사한 채용공고를 여기에 붙여넣으세요...\n\nPaste the full Korean job posting text here...",
    )

    col_j1, col_j2 = st.columns(2)
    with col_j1:
        check_work_rights = st.checkbox(
            "🎓 Check student work rules",
            value=True,
            help="Adds D-2 visa work hour limits and compliance info",
        )
    with col_j2:
        simple_mode = st.checkbox(
            "📝 Extra simple English",
            value=False,
            help="Uses very basic English for beginner speakers",
        )

    if st.button("📋  Simplify Job Posting", type="primary", use_container_width=True, key="job_btn"):
        if not job_input.strip():
            st.warning("Please paste a Korean job posting first.")
        elif not groq_api_key:
            st.error("⚠️ Please enter your Groq API key in the sidebar.")
        else:
            with st.spinner("Translating and simplifying..."):
                try:
                    from groq import Groq
                    client = Groq(api_key=groq_api_key)

                    language_note = "Use very simple English words (A1-A2 level). Short sentences. No complex vocabulary." if simple_mode else ""
                    work_rights_note = """
Also add a section called "⚠️ Student Work Rules (D-2 Visa)" that checks:
- Does this job seem to exceed 20 hours/week during semester? (D-2 limit)
- Is the hourly pay at or above minimum wage? (2026 Korean minimum wage is ₩10,030/hour)
- Any red flags (no contract mentioned, cash payment, unusually long hours)?
""" if check_work_rights else ""

                    job_prompt = f"""You are a job posting translator and simplifier for foreigners in South Korea.

A foreigner has pasted a Korean job posting. Your job:

1. **📋 Job Summary** — Extract and present clearly:
   - Job title (Korean + English)
   - Company / Location
   - Pay (hourly/monthly, in ₩ and approximate USD)
   - Working hours & days
   - Job duties (simplified)
   - Requirements (Korean level, experience, etc.)
   - How to apply (phone, email, app)

2. **🔑 Key Phrases to Know** — List 3-5 Korean words/phrases from the posting that the applicant should know (with pronunciation and meaning)

3. **⚡ Quick Verdict** — In 1-2 sentences: is this a reasonable job for a foreign student? Any concerns?

{work_rights_note}

{language_note}

Korean job posting:
{job_input}"""

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": "You are an expert at translating and simplifying Korean job postings for foreigners. You know Korean labor law, minimum wage, and D-2 visa work restrictions. Be helpful, accurate, and flag any concerns."},
                            {"role": "user", "content": job_prompt},
                        ],
                        temperature=0.4,
                        max_tokens=1200,
                    )
                    result = response.choices[0].message.content
                    st.markdown(result)

                except Exception as e:
                    st.error(f"Error: {e}")

    # Sample job posting for demo
    with st.expander("📌 Try a Sample Job Posting"):
        sample_job = """[알바몬] 편의점 야간 알바 모집

근무지: 서울특별시 관악구 신림동 CU 편의점
시급: 10,030원 (주휴수당 별도)
근무시간: 22:00 ~ 06:00 (주 5일)
근무기간: 3개월 이상
모집인원: 1명

자격요건:
- 외국인 가능 (의사소통 가능자)
- 성별 무관
- 경험 무관 (초보 가능)

우대사항:
- 편의점 근무 경험자
- 한국어 능통자

지원방법: 전화 문의 010-XXXX-XXXX
담당자: 김OO 점장"""

        st.code(sample_job, language=None)
        if st.button("▶ Use this sample", key="use_sample"):
            st.session_state["job_sample_loaded"] = sample_job
            st.rerun()

    # Load sample if button was pressed
    if "job_sample_loaded" in st.session_state and not job_input:
        st.info("👆 The sample has been loaded. Scroll up and click 'Simplify Job Posting' to try it!")

    with st.expander("🔍 Where to Find Korean Job Postings"):
        st.markdown("""
**Popular Job Sites:**
- **알바몬 (Albamon)** — albamon.com — Largest part-time job site
- **알바천국 (Alba Cheounguk)** — alba.co.kr — "Part-time heaven"
- **사람인 (Saramin)** — saramin.co.kr — Full-time & part-time
- **잡코리아 (JobKorea)** — jobkorea.co.kr — Professional jobs

**For Foreigners Specifically:**
- **Seoul Global Center** — sgc.seoul.go.kr — Job support for foreigners
- **HiKorea** — hikorea.go.kr — Work permit information
- **KDU Career Center** — Check with your university

**Tips:**
- Always check if the job allows foreign workers (외국인 가능)
- D-2 visa: max 20 hours/week during semester, unlimited during breaks
- Minimum wage 2026: ₩10,030/hour — don't accept less
- Always get a written contract (근로계약서)
""")
