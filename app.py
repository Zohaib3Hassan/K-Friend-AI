import streamlit as st

# ─── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="K-Friend AI",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    /* Main header styling */
    .main-header {
        text-align: center;
        padding: 1rem 0 0.5rem 0;
    }
    .main-header h1 {
        color: #0F6E56;
        font-size: 2.2rem;
        margin-bottom: 0.2rem;
    }
    .main-header p {
        color: #666;
        font-size: 1rem;
    }
    /* Chat message styling */
    .stChatMessage {
        border-radius: 12px;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #f8fffe;
    }
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        border-radius: 8px 8px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/color/96/south-korea.png", width=60)
    st.title("K-Friend AI")
    st.caption("Smart Life Assistant for Foreigners in South Korea")
    st.divider()

    # API Key input
    groq_api_key = st.text_input(
        "🔑 Groq API Key",
        type="password",
        help="Get your free key at https://console.groq.com/keys",
    )

    st.divider()
    st.markdown("**Modules**")
    st.markdown("1. 💬 K-Friend Chat")
    st.markdown("2. 🌐 Translator")
    st.markdown("3. 🛒 Grocery Planner")
    st.divider()
    st.caption("Built by Shah Zohaib Hassan · KDU Global · 2026")

# ─── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>🇰🇷 K-Friend AI</h1>
    <p>Your Smart Life Assistant for Living in South Korea</p>
</div>
""", unsafe_allow_html=True)

# ─── Tabs ──────────────────────────────────────────────────────
tab_chat, tab_translate, tab_grocery = st.tabs([
    "💬 K-Friend Chat",
    "🌐 Translator",
    "🛒 Grocery Planner",
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
    st.markdown("##### Ask me anything about life in Korea! 🇰🇷")

    # Initialize chat history
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    # Display chat history
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("e.g. How do I open a bank account in Korea?"):
        if not groq_api_key:
            st.error("⚠️ Please enter your Groq API key in the sidebar to use the chatbot.")
        else:
            # Add user message
            st.session_state.chat_messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate response
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

    # Quick question buttons
    if not st.session_state.chat_messages:
        st.markdown("---")
        st.markdown("**Try asking:**")
        cols = st.columns(2)
        quick_questions = [
            "How do I open a bank account?",
            "What's the D-2 visa renewal process?",
            "How does the health insurance work?",
            "Best halal restaurants near universities?",
        ]
        for i, q in enumerate(quick_questions):
            with cols[i % 2]:
                if st.button(f"💡 {q}", key=f"quick_{i}", use_container_width=True):
                    st.session_state.chat_messages.append({"role": "user", "content": q})
                    st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 2: EN ↔ KO TRANSLATOR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_translate:
    st.markdown("##### Translate between English and Korean 🌐")

    col_left, col_right = st.columns(2)

    with col_left:
        direction = st.radio(
            "Translation Direction",
            ["English → Korean", "Korean → English"],
            horizontal=True,
        )

    with col_right:
        polite_mode = st.checkbox(
            "✨ Polite/Formal mode (존댓말)",
            value=True,
            help="Rewrites Korean output in polite/formal speech level",
        )

    text_input = st.text_area(
        "Enter text to translate:",
        height=120,
        placeholder="Type or paste your text here...",
    )

    if st.button("🔄 Translate", type="primary", use_container_width=True):
        if not text_input.strip():
            st.warning("Please enter some text to translate.")
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
3. **Notes**: Any cultural context or usage tips (1-2 sentences max)

Format your response clearly with these three sections."""
                    else:
                        translate_prompt = f"""Translate the following Korean text to English.

Text: {text_input}

Provide:
1. **Translation**: The English translation
2. **Original speech level**: Whether the Korean uses formal (존댓말) or casual (반말) speech
3. **Notes**: Any cultural context or nuance that doesn't directly translate (1-2 sentences max)

Format your response clearly with these three sections."""

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": "You are an expert Korean-English translator. Provide accurate, natural translations with helpful cultural context.",
                            },
                            {"role": "user", "content": translate_prompt},
                        ],
                        temperature=0.3,
                        max_tokens=512,
                    )
                    result = response.choices[0].message.content
                    st.success("Translation complete!")
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Translation error: {e}")

    # Common phrases section
    with st.expander("📚 Essential Korean Phrases for Daily Life"):
        phrases = {
            "안녕하세요 (annyeonghaseyo)": "Hello (formal)",
            "감사합니다 (gamsahamnida)": "Thank you (formal)",
            "이거 얼마예요? (igeo eolmayeyo?)": "How much is this?",
            "화장실 어디예요? (hwajangsil eodiyeyo?)": "Where is the bathroom?",
            "도와주세요 (dowajuseyo)": "Please help me",
            "한국어 못해요 (hangugeo mothaeyo)": "I can't speak Korean",
            "메뉴판 주세요 (menyupan juseyo)": "Please give me the menu",
            "계산해 주세요 (gyesanhae juseyo)": "Bill/check please",
            "여기요! (yeogiyo!)": "Excuse me! (to call staff)",
            "매워요? (maewoyo?)": "Is it spicy?",
        }
        for kr, en in phrases.items():
            st.markdown(f"**{kr}** — {en}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE 3: SMART GROCERY PLANNER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_grocery:
    st.markdown("##### Plan your weekly groceries on a budget 🛒")

    col1, col2 = st.columns(2)

    with col1:
        budget = st.number_input(
            "💰 Weekly Budget (₩)",
            min_value=10000,
            max_value=500000,
            value=30000,
            step=5000,
            help="Average student spends ₩25,000–40,000/week on groceries",
        )

        household_size = st.selectbox(
            "👥 Cooking for",
            ["Just me", "2 people", "3-4 people"],
        )

    with col2:
        dietary = st.multiselect(
            "🍽️ Dietary Requirements",
            [
                "Halal",
                "Vegetarian",
                "Vegan",
                "No pork",
                "No seafood",
                "Gluten-free",
                "No spicy food",
            ],
            default=[],
        )

        cooking_level = st.select_slider(
            "👨‍🍳 Cooking skill",
            options=["Beginner", "Basic", "Intermediate", "Advanced"],
            value="Basic",
        )

    preferred_stores = st.multiselect(
        "🏪 Where do you usually shop?",
        [
            "E-Mart / Homeplus",
            "GS25 / CU / 7-Eleven",
            "Local market (시장)",
            "Coupang (online)",
            "Daiso",
            "No Preference",
        ],
        default=["No Preference"],
    )

    if st.button("📋 Generate Grocery Plan", type="primary", use_container_width=True):
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

1. **Shopping List** — organized by category (produce, protein, staples, etc.)
   - Item name in English AND Korean (한글)
   - Estimated price in ₩
   - Where to buy (which store type is cheapest for this item)

2. **3 Simple Meal Ideas** — using the ingredients from the list
   - Quick description
   - Approximate cooking time

3. **Budget Breakdown** — total by category, remaining budget

4. **Money-Saving Tips** — 2-3 Korea-specific tips (e.g. "Buy rice in bulk at E-Mart", "Check Coupang Rocket Fresh for deals", "Local 시장 is cheapest for vegetables")

Keep prices realistic for South Korea in 2026. Use real store names and real product availability.
Format clearly with headers and bullet points."""

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a helpful grocery planning assistant with deep knowledge of South Korean grocery stores, prices, and food culture. You help foreigners shop smart on a budget.",
                            },
                            {"role": "user", "content": grocery_prompt},
                        ],
                        temperature=0.7,
                        max_tokens=1500,
                    )
                    result = response.choices[0].message.content
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Error generating plan: {e}")

    # Helpful info
    with st.expander("🏪 Guide to Korean Grocery Stores"):
        st.markdown("""
**Budget-Friendly Options:**
- **Local markets (시장)** — Cheapest for fresh produce, meat, and fish
- **E-Mart / Homeplus** — Best for bulk buying rice, cooking oil, staples
- **Coupang Rocket Fresh** — Convenient delivery, good for heavy items
- **No Brand (노브랜드)** — E-Mart's budget line, great value

**Convenience Stores (편의점):**
- GS25, CU, 7-Eleven — Good for quick meals, snacks
- Triangle kimbap (삼각김밥) = ~₩1,200, full meal
- Cup ramen + rice = ~₩2,500

**For Halal/International Food:**
- Itaewon (이태원) — Halal butchers and restaurants
- Ansan Multicultural Food Street — international ingredients
- Coupang search "할랄" (halal) — some options available online
""")
