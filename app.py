.import streamlit as st

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
*, *::before, *::after { font-family: 'Plus Jakarta Sans', sans-serif !important; }
[data-testid="stIconMaterial"], .material-symbols-rounded, .material-icons {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
    font-weight: normal !important;
    font-style: normal !important;
    line-height: 1 !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
    -webkit-font-feature-settings: 'liga' !important;
    -webkit-font-smoothing: antialiased !important;
}
span:has(> [data-testid="stIconMaterial"]) {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
    line-height: 1 !important;
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
