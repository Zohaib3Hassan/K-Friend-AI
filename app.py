No, you do **not** need to change anything in Streamlit Secrets if the secret name is exactly:

```toml
GROQ_API_KEY = "your_groq_key_here"
```

The code below automatically reads that secret. Replace your whole `app.py` with this:

```python
import streamlit as st

# ─── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="K-Friend AI",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ───────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body,
.stApp,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] strong,
[data-testid="stMarkdownContainer"] em,
[data-testid="stMarkdownContainer"] a,
h1, h2, h3, h4, h5, h6,
label,
input:not([class*="stIconMaterial"]):not([class*="material-symbols-rounded"]):not([class*="material-icons"]),
textarea,
button:not([class*="stIconMaterial"]):not([class*="material-symbols-rounded"]):not([class*="material-icons"]),
.stTabs [data-baseweb="tab"] p,
.sidebar-logo,
.sidebar-title,
.sidebar-subtitle,
.module-chip,
.hero,
.hero-badge,
.hero h1,
.hero p,
.hero-panel,
.quick-card,
.trust-pill,
.sec-label,
.module-head,
.module-head h2,
.module-head p {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

[data-testid="stIconMaterial"],
.stIconMaterial,
.material-symbols-rounded,
.material-icons {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
    font-weight: normal !important;
    font-style: normal !important;
    line-height: 1 !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
    font-feature-settings: 'liga' !important;
    -webkit-font-feature-settings: 'liga' !important;
    -webkit-font-smoothing: antialiased !important;
}

:root {
    --primary: #0D9373;
    --primary-2: #15B58D;
    --primary-soft: #E8F7F2;
    --primary-dark: #064A3A;
    --ink: #111827;
    --text-primary: #1A1D23;
    --text-secondary: #5E6675;
    --text-muted: #8A94A6;
    --bg-main: #F4F7F6;
    --bg-card: #FFFFFF;
    --bg-soft: #F9FBFA;
    --border: #DEE6E2;
    --border-light: #EDF2F0;
    --warning: #B7791F;
    --warning-soft: #FFF7E6;
    --blue: #2563EB;
    --blue-soft: #EAF1FF;
    --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.06);
    --shadow-md: 0 12px 28px rgba(15, 23, 42, 0.08);
    --shadow-lg: 0 20px 48px rgba(6, 74, 58, 0.16);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
}

.stApp, [data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at top left, rgba(13,147,115,0.14), transparent 30rem),
        linear-gradient(180deg, #FBFDFC 0%, var(--bg-main) 100%) !important;
}
[data-testid="stMainBlockContainer"], .main .block-container {
    max-width: 1180px;
    padding: 1.15rem 2rem 3rem 2rem;
}

div[data-testid="stVerticalBlock"] { gap: 1rem; }
div[data-testid="stHorizontalBlock"] { gap: 1rem; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B1F1A 0%, #0F2E25 50%, #0B1F1A 100%) !important;
}
[data-testid="stSidebar"] * { color: #E0E8E5 !important; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    line-height: 1.45;
}
[data-testid="stSidebar"] .stTextInput input {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 8px !important;
    color: #E0E8E5 !important;
}
[data-testid="stSidebar"] .stTextInput input:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 2px rgba(13,147,115,0.25) !important;
}
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.1) !important; }
.sidebar-logo {
    text-align:center;
    padding: 1.25rem 0 0.35rem 0;
}
.sidebar-mark {
    width: 58px;
    height: 58px;
    margin: 0 auto 0.7rem auto;
    display: grid;
    place-items: center;
    border-radius: 18px;
    background: linear-gradient(145deg, rgba(255,255,255,0.16), rgba(255,255,255,0.06));
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow: 0 18px 40px rgba(0,0,0,0.22);
    color: #F4FFFB !important;
    font-size: 1.05rem;
    font-weight: 900;
    letter-spacing: 0;
}
.sidebar-title { font-size: 1.35rem; font-weight: 800; }
.sidebar-subtitle {
    font-size: 0.72rem;
    color: rgba(255,255,255,0.56) !important;
    margin-top: 4px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}
.module-list {
    display: grid;
    gap: 0.45rem;
    margin-top: 0.55rem;
}
.module-chip {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    padding: 0.62rem 0.72rem;
    border-radius: var(--radius-sm);
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    font-size: 0.86rem;
    font-weight: 650;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card);
    border-radius: var(--radius-lg);
    padding: 6px;
    gap: 4px;
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border-light);
    overflow-x: auto;
    scrollbar-width: none;
}
.stTabs [data-baseweb="tab-list"]::-webkit-scrollbar { display: none; }
.stTabs [data-baseweb="tab"] {
    border-radius: var(--radius-md) !important;
    padding: 10px 18px !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    color: var(--text-secondary) !important;
    transition: all 0.2s ease !important;
    min-width: max-content;
}
.stTabs [data-baseweb="tab"]:hover {
    background: var(--primary-soft) !important;
    color: var(--primary-dark) !important;
}
.stTabs [aria-selected="true"] {
    background: var(--primary) !important;
    color: white !important;
}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* Buttons */
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
    min-height: 2.75rem !important;
    white-space: normal !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(13,147,115,0.4) !important;
}
.stButton > button:focus {
    box-shadow: 0 0 0 3px rgba(13,147,115,0.18), 0 4px 16px rgba(13,147,115,0.28) !important;
}

/* Inputs */
.stTextInput input, .stTextArea textarea, .stNumberInput input, .stSelectbox [data-baseweb="select"],
.stMultiSelect [data-baseweb="select"] {
    border-radius: var(--radius-sm) !important;
    border: 1.5px solid var(--border) !important;
    font-size: 0.9rem !important;
    background: #FFFFFF !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(13,147,115,0.12) !important;
}
label, .stRadio, .stCheckbox, .stSelectbox, .stMultiSelect, .stNumberInput {
    color: var(--text-primary) !important;
}

/* Chat */
[data-testid="stChatMessage"] {
    background: var(--bg-card) !important;
    border-radius: var(--radius-lg) !important;
    border: 1px solid var(--border-light) !important;
    box-shadow: var(--shadow-sm) !important;
    padding: 1rem 1.2rem !important;
    margin-bottom: 0.75rem !important;
}
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-user"] {
    background: var(--primary) !important;
}
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-assistant"] {
    background: var(--blue) !important;
}

/* Multiselect pills */
[data-baseweb="tag"] {
    background: var(--primary-light) !important;
    color: var(--primary-dark) !important;
    border-radius: 20px !important;
    font-weight: 500 !important;
}

/* Info cards */
.info-card {
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 1.2rem;
    text-align: center;
    box-shadow: var(--shadow-sm);
}
.info-card .ic-emoji { font-size: 1.5rem; margin-bottom: 0.4rem; }
.info-card .ic-title { font-size: 0.85rem; font-weight: 700; color: var(--text-primary); }
.info-card .ic-sub { font-size: 0.72rem; color: var(--text-muted); margin-top: 2px; }

/* Hero */
.hero {
    position: relative;
    overflow: hidden;
    display: grid;
    grid-template-columns: minmax(0, 1.25fr) minmax(280px, 0.75fr);
    gap: 1.4rem;
    align-items: stretch;
    padding: 1.35rem;
    margin: 0.25rem 0 1.1rem 0;
    border: 1px solid rgba(13,147,115,0.16);
    border-radius: var(--radius-lg);
    background:
        linear-gradient(135deg, rgba(255,255,255,0.96), rgba(232,247,242,0.92)),
        radial-gradient(circle at 85% 15%, rgba(21,181,141,0.22), transparent 18rem);
    box-shadow: var(--shadow-lg);
}
.hero-copy {
    display: flex;
    min-width: 0;
    flex-direction: column;
    justify-content: center;
    padding: 0.4rem 0.25rem;
}
.hero-badge {
    display: inline-block;
    width: fit-content;
    background: var(--primary-soft);
    color: var(--primary-dark);
    font-size: 0.72rem; font-weight: 700;
    padding: 4px 14px; border-radius: 20px;
    letter-spacing: 0.04em; text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.hero h1 {
    font-size: clamp(2rem, 4vw, 3.35rem);
    font-weight: 800;
    color: var(--text-primary);
    margin: 0.1rem 0;
    line-height: 1.05;
    letter-spacing: 0;
}
.hero h1 .hl {
    background: linear-gradient(135deg, var(--primary), var(--primary-2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero p {
    color: var(--text-secondary);
    font-size: 1rem;
    max-width: 660px;
    margin: 0.75rem 0 0 0;
    line-height: 1.65;
}
.hero-panel {
    min-width: 0;
    border-radius: var(--radius-md);
    background: rgba(255,255,255,0.72);
    border: 1px solid rgba(13,147,115,0.14);
    padding: 1rem;
    display: grid;
    align-content: center;
    gap: 0.7rem;
}
.hero-panel-title {
    font-size: 0.78rem;
    font-weight: 800;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
.quick-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.65rem;
}
.quick-card {
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    padding: 0.8rem;
    min-height: 82px;
    box-shadow: var(--shadow-sm);
}
.quick-card strong {
    display: block;
    color: var(--ink);
    font-size: 0.92rem;
    margin-bottom: 0.2rem;
}
.quick-card span {
    display: block;
    color: var(--text-muted);
    font-size: 0.75rem;
    line-height: 1.35;
}
.trust-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.9rem;
}
.trust-pill {
    border: 1px solid rgba(13,147,115,0.18);
    background: rgba(255,255,255,0.74);
    border-radius: 999px;
    color: var(--primary-dark);
    font-weight: 700;
    font-size: 0.78rem;
    padding: 0.38rem 0.72rem;
}

/* Section label */
.sec-label {
    font-size: 0.7rem; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 0.6rem;
}
.module-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    margin: 0.35rem 0 0.9rem 0;
}
.module-head h2 {
    color: var(--text-primary);
    font-size: 1.35rem;
    line-height: 1.2;
    margin: 0;
}
.module-head p {
    color: var(--text-secondary);
    margin: 0.35rem 0 0 0;
    line-height: 1.55;
    max-width: 720px;
}
.module-icon {
    width: 46px;
    height: 46px;
    flex: 0 0 auto;
    display: grid;
    place-items: center;
    border-radius: var(--radius-md);
    background: var(--primary-soft);
    border: 1px solid rgba(13,147,115,0.16);
    font-size: 1.35rem;
}
.surface {
    background: rgba(255,255,255,0.7);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-lg);
    padding: 1rem;
    box-shadow: var(--shadow-sm);
}
.stAlert {
    border-radius: var(--radius-md) !important;
}
.streamlit-expanderHeader {
    font-weight: 700 !important;
}
.stFileUploader [data-testid="stFileUploaderDropzone"] {
    background: rgba(255,255,255,0.72) !important;
    border: 1.5px dashed var(--border) !important;
    border-radius: var(--radius-md) !important;
    padding: 1rem !important;
}
.stFileUploader [data-testid="stFileUploaderDropzone"] button {
    border-radius: var(--radius-sm) !important;
    min-height: 2.5rem !important;
}
.stTextArea textarea {
    min-height: 150px !important;
    line-height: 1.55 !important;
}

/* Hide defaults */
#MainMenu, header, footer, [data-testid="stHeader"] { display: none !important; }

@media (max-width: 768px) {
    [data-testid="stMainBlockContainer"], .main .block-container { padding: 0.75rem 0.85rem 2rem 0.85rem; }
    .hero {
        grid-template-columns: 1fr;
        padding: 1rem;
        gap: 1rem;
        margin-top: 0;
    }
    .hero-panel { padding: 0.8rem; }
    .quick-grid { grid-template-columns: 1fr 1fr; gap: 0.5rem; }
    .quick-card { padding: 0.68rem; min-height: 74px; }
    .hero p { font-size: 0.94rem; line-height: 1.55; }
    .module-head { align-items: flex-start; }
    .module-head h2 { font-size: 1.15rem; }
    .module-icon { width: 40px; height: 40px; font-size: 1.15rem; }
    .stTabs [data-baseweb="tab"] { padding: 9px 12px !important; font-size: 0.8rem !important; }
}
@media (max-width: 480px) {
    .quick-grid { grid-template-columns: 1fr; }
    .hero h1 { font-size: 1.85rem; }
    .trust-pill { width: 100%; text-align: center; }
}
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-mark">KR</div>
        <div class="sidebar-title">K-Friend AI</div>
        <div class="sidebar-subtitle">Smart Life Assistant</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

    groq_api_key = st.secrets.get("GROQ_API_KEY", "")

    st.divider()
    st.markdown("**Modules**")
    st.markdown("""
    <div class="module-list">
        <div class="module-chip">💬 <span>K-Friend Chat</span></div>
        <div class="module-chip">🌐 <span>Translator</span></div>
        <div class="module-chip">🛒 <span>Grocery Planner</span></div>
        <div class="module-chip">📸 <span>Sign Reader</span></div>
        <div class="module-chip">💼 <span>Job Simplifier</span></div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.caption("Built by Shah Zohaib Hassan")
    st.caption("KDU Global · AI Department · 2026")


# ─── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-copy">
        <div class="hero-badge">Korea-ready AI life assistant</div>
        <h1>Meet your <span class="hl">K-Friend</span> in Korea</h1>
        <p>One calm place for the daily questions foreigners actually face: visas, banking, Korean phrases, groceries, signs, and student jobs.</p>
        <div class="trust-row">
            <div class="trust-pill">Built for students</div>
            <div class="trust-pill">Korean + English</div>
            <div class="trust-pill">Fast practical answers</div>
        </div>
    </div>
    <div class="hero-panel">
        <div class="hero-panel-title">Ready for daily life</div>
        <div class="quick-grid">
            <div class="quick-card"><strong>Visa help</strong><span>D-2 rules, ARC, renewal, 1345 guidance</span></div>
            <div class="quick-card"><strong>Translate</strong><span>Formal Korean, romanization, cultural notes</span></div>
            <div class="quick-card"><strong>Food plans</strong><span>Budget, halal needs, Korean store tips</span></div>
            <div class="quick-card"><strong>Photo OCR</strong><span>Menus, signs, labels, notices</span></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Tabs ──────────────────────────────────────────────────────
tab_chat, tab_translate, tab_grocery, tab_sign, tab_job = st.tabs([
    "💬  Chat", "🌐  Translator", "🛒  Grocery", "📸  Sign Reader", "💼  Jobs",
])


def module_header(icon, title, subtitle):
    st.markdown(f"""
    <div class="module-head">
        <div>
            <div class="sec-label">{title}</div>
            <h2>{title}</h2>
            <p>{subtitle}</p>
        </div>
        <div class="module-icon">{icon}</div>
    </div>
    """, unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 1: CHATBOT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SYSTEM_PROMPT = """You are K-Friend AI, a warm and knowledgeable assistant for foreigners in South Korea.

Your expertise: Visa & Immigration (D-2, E-7, F-2/F-5, KIIP, ARC), Daily Life (banking, phone, utilities, rent jeonse/wolse), Transportation (T-money, KTX, buses, K-Pass), Food & Shopping (grocery stores, halal food, Coupang/Baemin, Daiso), Healthcare (NHI, hospitals, pharmacies, 119), Culture & Language (Korean phrases, TOPIK, cultural norms), Work (student 20hr/week limit, tax, labor rights), Education (GKS, course registration).

Rules: Be friendly and supportive. Give specific actionable answers. Include Korean (한글) + English for Korean terms. Mention costs in ₩. If unsure, suggest hikorea.go.kr or 1345 hotline. Use simple English."""

with tab_chat:
    module_header(
        "💬",
        "K-Friend Chat",
        "Ask practical questions about visas, banking, transport, food, healthcare, culture, and student life in South Korea.",
    )

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything — visas, banking, food, transport..."):
        if not groq_api_key:
            st.error("⚠️ Please enter your Groq API key in the sidebar.")
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
                        messages += [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_messages]
                        response = client.chat.completions.create(
                            model="llama-3.3-70b-versatile", messages=messages,
                            temperature=0.7, max_tokens=1024,
                        )
                        reply = response.choices[0].message.content
                        st.markdown(reply)
                        st.session_state.chat_messages.append({"role": "assistant", "content": reply})
                    except Exception as e:
                        st.error(f"Error: {e}")

    if not st.session_state.chat_messages:
        st.divider()
        st.markdown("**💡 Try asking:**")
        c1, c2 = st.columns(2)
        for i, q in enumerate([
            "How do I open a bank account in Korea?",
            "What's the D-2 visa renewal process?",
            "How does health insurance work for students?",
            "Where can I find halal food in Korea?",
        ]):
            with [c1, c2][i % 2]:
                if st.button(q, key=f"q_{i}", use_container_width=True):
                    st.session_state.chat_messages.append({"role": "user", "content": q})
                    st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 2: TRANSLATOR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_translate:
    module_header(
        "🌐",
        "Translator",
        "Translate between English and Korean with natural wording, romanization, speech level, and quick cultural context.",
    )

    col_l, col_r = st.columns([1, 1])
    with col_l:
        direction = st.radio("Direction", ["English → Korean", "Korean → English"], horizontal=True)
    with col_r:
        polite_mode = st.checkbox("✨ Polite / Formal mode (존댓말)", value=True)

    text_input = st.text_area("Enter text to translate", height=130,
        placeholder="Type or paste your text here...")

    if st.button("🔄  Translate", type="primary", use_container_width=True, key="tr_btn"):
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
                        tp = f"""Translate to Korean. {"Use polite/formal speech (존댓말)." if polite_mode else "Use casual speech (반말)."}
Text: {text_input}
Provide: 1. **Translation** 2. **Romanization** 3. **Notes** (cultural context, 1-2 sentences)"""
                    else:
                        tp = f"""Translate to English.
Text: {text_input}
Provide: 1. **Translation** 2. **Speech level** (formal 존댓말 or casual 반말) 3. **Notes** (cultural context, 1-2 sentences)"""

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": "You are an expert Korean-English translator. Accurate, natural translations with cultural context."},
                            {"role": "user", "content": tp},
                        ],
                        temperature=0.3, max_tokens=512,
                    )
                    st.success("✅ Translation complete!")
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")

    with st.expander("📚 Essential Korean Phrases"):
        for kr, roman, en in [
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
        ]:
            st.markdown(f"**{kr}** ({roman}) — {en}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 3: GROCERY PLANNER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_grocery:
    module_header(
        "🛒",
        "Grocery Planner",
        "Build a realistic weekly shopping plan using your budget, cooking skill, dietary needs, and preferred Korean stores.",
    )

    c1, c2 = st.columns(2)
    with c1:
        budget = st.number_input("💰 Weekly Budget (₩)", min_value=10000, max_value=500000, value=30000, step=5000)
        household_size = st.selectbox("👥 Cooking for", ["Just me", "2 people", "3-4 people"])
    with c2:
        dietary = st.multiselect("🍽️ Dietary Requirements",
            ["Halal", "Vegetarian", "Vegan", "No pork", "No seafood", "Gluten-free", "No spicy food"])
        cooking_level = st.select_slider("👨‍🍳 Cooking skill",
            options=["Beginner", "Basic", "Intermediate", "Advanced"], value="Basic")

    preferred_stores = st.multiselect("🏪 Where do you usually shop?",
        ["E-Mart / Homeplus", "GS25 / CU / 7-Eleven", "Local market (시장)", "Coupang (online)", "Daiso", "No Preference"],
        default=["No Preference"])

    if st.button("📋  Generate Grocery Plan", type="primary", use_container_width=True, key="gr_btn"):
        if not groq_api_key:
            st.error("⚠️ Please enter your Groq API key in the sidebar.")
        else:
            with st.spinner("Planning your groceries..."):
                try:
                    from groq import Groq
                    client = Groq(api_key=groq_api_key)
                    dietary_str = ", ".join(dietary) if dietary else "None"
                    stores_str = ", ".join(preferred_stores)
                    gp = f"""Create a weekly grocery plan for a foreigner in South Korea.
Budget: ₩{budget:,}/week | Household: {household_size} | Dietary: {dietary_str} | Cooking: {cooking_level} | Stores: {stores_str}

Provide:
1. **🛒 Shopping List** by category — item in English AND Korean (한글), price in ₩, best store
2. **🍳 3 Simple Meal Ideas** using listed ingredients with cooking time
3. **💰 Budget Breakdown** by category with remaining budget
4. **💡 Money-Saving Tips** — 2-3 Korea-specific tips

Use realistic 2026 South Korea prices and real store names."""

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": "You are a grocery planning assistant for foreigners in South Korea. Deep knowledge of Korean stores, prices, and food culture."},
                            {"role": "user", "content": gp},
                        ],
                        temperature=0.7, max_tokens=1500,
                    )
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")

    with st.expander("🏪 Guide to Korean Grocery Stores"):
        st.markdown("""
**Budget-Friendly:** Local markets (시장) for fresh produce · E-Mart/Homeplus for bulk · Coupang Rocket Fresh for delivery · No Brand (노브랜드) for budget items

**Convenience Stores (편의점):** GS25, CU, 7-Eleven — Triangle kimbap ≈ ₩1,200 · Cup ramen + rice ≈ ₩2,500

**Halal / International:** Itaewon (이태원) halal butchers · Ansan Multicultural Food Street · Coupang search "할랄"
""")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 4: SIGN READER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_sign:
    module_header(
        "📸",
        "Sign Reader",
        "Upload a Korean menu, sign, label, or notice. K-Friend extracts the text and explains what it means in English.",
    )

    uploaded_image = st.file_uploader("📷 Upload a photo with Korean text",
        type=["jpg", "jpeg", "png", "webp"],
        help="Take a photo of any Korean sign, menu, label, or notice")

    if uploaded_image:
        col_img, col_res = st.columns([1, 1])
        with col_img:
            st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
        with col_res:
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

                            image_bytes = uploaded_image.getvalue()
                            image = Image.open(io.BytesIO(image_bytes))
                            image_np = np.array(image)

                            reader = easyocr.Reader(["ko", "en"], gpu=False)
                            results = reader.readtext(image_np)

                            if not results:
                                st.warning("No text detected. Try a clearer photo.")
                            else:
                                detected_texts = [text for (_, text, conf) in results]
                                full_text = "\n".join(detected_texts)

                                st.markdown("**📝 Detected Korean Text:**")
                                st.code(full_text, language=None)

                                with st.spinner("Translating..."):
                                    from groq import Groq
                                    client = Groq(api_key=groq_api_key)
                                    response = client.chat.completions.create(
                                        model="llama-3.3-70b-versatile",
                                        messages=[
                                            {"role": "system", "content": "You are a Korean-English translator helping foreigners understand Korean text from photos. Fix OCR errors, translate accurately, and provide helpful context."},
                                            {"role": "user", "content": f"""I extracted this Korean text from a photo. Please:
1. **Clean Text**: Fix any OCR errors, show corrected Korean
2. **Translation**: Full English translation
3. **Context**: What is this? (menu item? warning sign? label?) Any useful info for a foreigner.

Extracted text:
{full_text}"""},
                                        ],
                                        temperature=0.3, max_tokens=800,
                                    )
                                    st.markdown("**🌐 Translation:**")
                                    st.markdown(response.choices[0].message.content)
                        except ImportError:
                            st.error("EasyOCR not installed. Add `easyocr` to requirements.txt and redeploy.")
                        except Exception as e:
                            st.error(f"Error: {e}")
    else:
        st.info("📸 Upload a photo of a Korean menu, sign, product label, or notice to get started.")

    with st.expander("💡 Tips for Best Results"):
        st.markdown("""
- **Good lighting** — avoid shadows and glare
- **Straight angle** — hold camera parallel to the text
- **Close up** — make sure text is large and readable
- **One item at a time** — focus on one sign/menu/label per photo
""")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 5: JOB SIMPLIFIER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_job:
    module_header(
        "💼",
        "Job Simplifier",
        "Paste a Korean part-time job post and get a simple English summary with pay, hours, red flags, and student visa checks.",
    )

    job_input = st.text_area("📋 Paste Korean job posting here", height=180,
        placeholder="알바몬, 사람인, 잡코리아 등에서 복사한 채용공고를 여기에 붙여넣으세요...\n\nPaste the full Korean job posting text here...")

    c1, c2 = st.columns(2)
    with c1:
        check_work_rights = st.checkbox("🎓 Check student work rules (D-2 visa)", value=True)
    with c2:
        simple_mode = st.checkbox("📝 Extra simple English", value=False,
            help="Uses very basic English for beginner speakers")

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

                    lang_note = "Use very simple English (A1-A2 level). Short sentences." if simple_mode else ""
                    visa_note = """
Also add "⚠️ Student Work Rules (D-2 Visa)":
- Does this exceed 20 hours/week during semester?
- Is pay at/above minimum wage? (2026: ₩10,030/hour)
- Any red flags (no contract, cash payment, long hours)?""" if check_work_rights else ""

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": "You are an expert at translating Korean job postings for foreigners. You know Korean labor law, minimum wage, and D-2 visa work restrictions."},
                            {"role": "user", "content": f"""Translate and simplify this Korean job posting:

1. **📋 Job Summary**: Job title (Korean + English), company/location, pay (₩ + ~USD), hours & days, duties, requirements, how to apply
2. **🔑 Key Korean Phrases**: 3-5 words from the posting the applicant should know (with pronunciation + meaning)
3. **⚡ Quick Verdict**: Is this reasonable for a foreign student? Any concerns?
{visa_note}
{lang_note}

Job posting:
{job_input}"""},
                        ],
                        temperature=0.4, max_tokens=1200,
                    )
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")

    with st.expander("📌 Try a Sample Job Posting"):
        sample = """[알바몬] 편의점 야간 알바 모집

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
        st.code(sample, language=None)
        st.caption("Copy and paste the above into the text area, then click 'Simplify Job Posting'")

    with st.expander("🔍 Where to Find Korean Job Postings"):
        st.markdown("""
**Job Sites:** 알바몬 albamon.com · 알바천국 alba.co.kr · 사람인 saramin.co.kr · 잡코리아 jobkorea.co.kr

**For Foreigners:** Seoul Global Center sgc.seoul.go.kr · HiKorea hikorea.go.kr · Your university career center

**Tips:** Check for 외국인 가능 (foreigners OK) · D-2 visa: max 20hrs/week during semester · Minimum wage 2026: ₩10,030/hr · Always get a written contract (근로계약서)
""")
```
