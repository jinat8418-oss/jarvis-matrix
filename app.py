import streamlit as st
import random

# Page & Retro Terminal Styling
st.set_page_config(page_title="Jarvis OS", page_icon="📟", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #050508; color: #33ff33; font-family: 'Courier New', monospace; }
    h1, h2, h3, label { color: #00ffcc !important; font-family: 'Courier New', monospace !important; }
    div, p, span { color: #e0e0e0; font-family: 'Courier New', monospace !important; }
    .stButton>button { 
        background-color: #0a0f1d; color: #00ffcc; border: 1px dashed #00ffcc; 
        border-radius: 0px; font-family: 'Courier New', monospace; width: 100%;
    }
    .stButton>button:hover { background-color: #00ffcc; color: #050508; box-shadow: 0px 0px 10px #00ffcc; }
    .stCodeBlock, stAlert { background-color: #0a0a0f !important; border: 1px solid #33ff33 !important; }
    </style>
    """, unsafe_style_allowed=True)

st.title("📟 JARVIS_OS : CORE")
st.write("SYSTEM: ONLINE // ENGINE: CLOUD_MATRIX")
st.markdown("=========================================================")

# Data Pools
captions = {
    "Cinematic Automotive": {
        "hook": "Heavy machinery meets dark aesthetic.",
        "body": "[Layout: Split Grid]\n├── Left: Deep shadows\n└── Right: Sharp specs",
        "tags": "#moodandmachine #cinematiccars"
    },
    "Grooming & Skincare": {
        "hook": "Fix these habits for clear skin.",
        "body": "[Layout: Split Carousel]\n├── Clean: Wash face (2x max)\n└── Dirty: Overwashing face",
        "tags": "#glowup #skincareroutine"
    }
}

f1_facts = [
    "F1 cars decelerate from 100 to 0 km/h in under 15 meters (6G forces).",
    "Modern V6 turbo hybrids break past 50% thermal efficiency.",
    "At 150 km/h, F1 downforce exceeds the weight of the car itself."
]

# Sidebar Menu
st.sidebar.markdown("### 🕹️ MENU")
module = st.sidebar.radio("SELECT VECTOR", ["> STATUS", "> CONTENT", "> F1_VAULT", "> RISK_CALC", "> LAMBO_SPECS"])

if module == "> STATUS":
    st.subheader("[+] DIAGNOSTICS")
    st.text_area("Output", "Jarvis Core Operating Loop: NOMINAL\nAll systems fully green.", height=100)

elif module == "> CONTENT":
    st.subheader("[+] CREATIVE PIPELINE")
    niche = st.selectbox("Select Segment", ["Cinematic Automotive", "Grooming & Skincare"])
    if st.button("GENERATE STRATEGY"):
        data = captions[niche]
        st.markdown(f"**[HOOK]**\n```text\n-> {data['hook']}\n```")
        st.markdown("**[BLUEPRINT]**")
        st.code(data['body'], language="text")
        st.markdown(f"**[TAGS]**\n`{data['tags']}`")

elif module == "> F1_VAULT":
    st.subheader("[+] RACING INTEL")
    if st.button("FETCH RANDOM TELEMETRY"):
        st.code(random.choice(f1_facts), language="text")

elif module == "> RISK_CALC":
    st.subheader("[+] RISK PARAMETERS")
    balance = st.number_input("Capital ($)", min_value=0.0, value=1000.0)
    risk_pct = st.slider("Risk Boundary (%)", 0.1, 5.0, 1.0)
    allowed_loss = balance * (risk_pct / 100.0)
    st.markdown(f"### MAX LOSS ALLOWED: `${allowed_loss:,.2f}`")
    st.markdown("`Set hard stop-loss based on this matrix.`")

elif module == "> LAMBO_SPECS":
    st.subheader("[+] HURACÁN EVO SPYDER SPECS")
    st.code("├── Engine: 5.2L V10\n├── Power: 640 HP @ 8,000 RPM\n├── Acceleration: 0-100 km/h in 3.1s\n└── Drive: 7-Speed Dual-Clutch / AWD", language="text")

st.markdown("=========================================================")
st.write("📟 OPERATION SECURE // END OF LINE.")
