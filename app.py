import streamlit as st
import random

# Page setup for retro terminal styling
st.set_page_config(page_title="Jarvis Terminal OS", page_icon="📟", layout="centered")

# Hardcore Neon Hacker UI Custom Overrides
st.markdown("""
    <style>
    /* Dark Terminal Background */
    .main { background-color: #050508; color: #33ff33; font-family: 'Courier New', Courier, monospace; }
    
    /* Neon Cyan Terminal Titles */
    h1, h2, h3, label { font-family: 'Courier New', Courier, monospace !important; color: #00ffcc !important; letter-spacing: 2px; }
    
    /* Global Monospace Text */
    div, p, span { font-family: 'Courier New', Courier, monospace !important; color: #e0e0e0; }
    
    /* Custom Dashed Cyber Buttons */
    .stButton>button { 
        background-color: #0a0f1d; 
        color: #00ffcc; 
        border: 1px dashed #00ffcc; 
        border-radius: 0px; 
        font-family: 'Courier New', Courier, monospace;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover { 
        background-color: #00ffcc; 
        color: #050508; 
        border: 1px solid #00ffcc;
        box-shadow: 0px 0px 10px #00ffcc;
    }
    
    /* Code block container borders */
    .stCodeBlock, stAlert { background-color: #0a0a0f !important; border: 1px solid #33ff33 !important; }
    </style>
    """, unsafe_style_allowed=True)

st.title("📟 JARVIS_OS : CORE_WEB_INTERFACE")
st.write("SYSTEM STATUS: ONLINE // SECURITY PROTOCOLS: ACTIVE // ENGINE: CLOUD_MATRIX")
st.markdown("=========================================================================")

# Shared Content Datapools
captions_pool = {
    "Cinematic Automotive": {
        "title": "Aesthetic Velocity Strategy",
        "hooks": ["Heavy machinery meets dark aesthetic.", "Chasing shadows in a world full of noise.", "Built for the night shift."],
        "bodies": ["[Layout: Split Contrast Grid]\n├── Left Panel : Deep shadows / Car silhouette\n└── Right Panel: Sharp typography / Mechanical specs"],
        "tags": "#moodandmachine #cinematiccars #darkaesthetic"
    },
    "Grooming & Skincare": {
        "title": "Glow-Up Core Matrix",
        "hooks": ["Fix these habits for clear skin.", "Most guys ignore these basic rules.", "Instantly do this: No excuses."],
        "bodies": ["[Layout: Clean vs Dirty Split Carousel]\n├── Clean: Wash face gently (2x max) | Non-comedogenic layers\n└── Dirty: Overwashing your skin | Using random harsh chemicals"],
        "tags": "#glowup #mensgrooming #skincareroutine"
    }
}

f1_facts = [
    {"topic": "Braking G-Force Parameters", "fact": "Deceleration from 100 to 0 km/h occurs in under 15 meters. Drivers sustain brief deceleration loads crossing 5G to 6G benchmarks under heavy threshold braking zones."},
    {"topic": "V6 Hybrid Thermal Efficiency", "fact": "Modern F1 1.6L V6 turbo hybrid power units cross a historic 50% thermal efficiency index, making them the most efficient combustion engines created."},
    {"topic": "Downforce Aero Dynamics", "fact": "At speeds scaling past 150 km/h, negative lift dynamics exceed the net structural curb mass of the vehicle, meaning it could aerodynamically track upside down."}
]

# Sidebar Selection Matrix
st.sidebar.markdown("### 🕹️ SYSTEM_MENU")
module = st.sidebar.radio("SELECT MODE VECTOR", [
    "> STATUS_CHECK", 
    "> CONTENT_GENERATOR", 
    "> F1_MOTORSPORT_VAULT", 
    "> RISK_CALCULATOR", 
    "> SUPERCAR_TELEMETRY"
])

if module == "> STATUS_CHECK":
    st.subheader("[+] SYSTEM DIAGNOSTICS")
    st.text_area("Terminal Output", "Jarvis Core Operating Loop: NOMINAL\nCloud Instance Allocation: STABLE\nData Storage Arrays: MOUNTED\nReady for input parsing...", height=120)

elif module == "> CONTENT_GENERATOR":
    st.subheader("[+] CREATIVE PIPELINE INJECTION")
    niche = st.selectbox("Select Target Segment", ["Cinematic Automotive", "Grooming & Skincare"])
    
    if st.button("EXECUTE GENERATION PROTOCOL"):
        data = captions_pool[niche]
        hook = random.choice(data["hooks"])
        body = random.choice(data["bodies"])
        
        st.markdown(f"**[VISUAL_HOOK_OVERLAY]**\n```text\n-> \" {hook.upper()} \"\n```")
        st.markdown("**[STRATEGY_BLUEPRINT_BODY]**")
        st.code(body, language="text")
        st.markdown(f"**[AEST_TAG_BUNDLE]**\n```text\n{data['tags']}\n```")

elif module == "> F1_MOTORSPORT_VAULT":
    st.subheader("[+] RACING TELEMETRY INTEL")
    if st.button("FETCH RANDOM TELEMETRY LOG"):
        item = random.choice(f1_facts)
        st.markdown(f"**DATA VECTOR: {item['topic'].upper()}**")
        st.code(item["fact"], language="text")

elif module == "> RISK_CALCULATOR":
    st.subheader("[+] ACCOUNT POSITION RISK PARAMETERS")
    balance = st.number_input("Input Net Trading Capital ($)", min_value=0.0, value=1000.0, step=100.0)
    risk_pct = st.slider("Position Risk Boundary (%)", 0.1, 5.0, 1.0, step=0.1)
    
    allowed_loss = balance * (risk_pct / 100.0)
    st.markdown(f"### MAXIMUM LOSS ALLOWED: `${allowed_loss:,.2f}`")
    st.markdown("
  http://googleusercontent.com/immersive_entry_chip/0

---

