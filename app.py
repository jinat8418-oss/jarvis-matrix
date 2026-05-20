import streamlit as st
import random

# Core Configuration
st.set_page_config(page_title="Jarvis OS", page_icon="📟")

st.title("📟 JARVIS OS : CORE TERMINAL")
st.write("SYSTEM STATUS: ACTIVE // CLOUD NODE CONNECTED")
st.markdown("---")

# Data Stores
captions = {
    "Cinematic Automotive": {
        "hook": "Heavy machinery meets a dark aesthetic.",
        "body": "[Visual Structure]\n├── Shadow Contrast: 70%\n└── Highlights: Muted Cinematic Green",
        "tags": "#moodandmachine #cinematiccars"
    },
    "Grooming & Skincare": {
        "hook": "Clear skin requires discipline, not random products.",
        "body": "[Routine Matrix]\n├── AM: Gentle Cleanser + Hydration\n└── PM: Deep Cleanse + Recovery Layer",
        "tags": "#glowup #skincareroutine"
    }
}

f1_facts = [
    "F1 cars decelerate from 100 to 0 km/h in under 15 meters, hitting up to 6G forces.",
    "Modern V6 turbo hybrid power units operate past a historic 50% thermal efficiency index.",
    "Past 150 km/h, aerodynamic downforce exceeds the entire net curb weight of an F1 car."
]

# Navigation System
st.sidebar.subheader("🕹️ CONTROL PANEL")
module = st.sidebar.radio("CHOOSE SYSTEM MODULE:", ["Diagnostics", "Content Matrix", "F1 Motorsport Vault", "Risk Parameters", "Supercar Telemetry"])

if module == "Diagnostics":
    st.subheader("[+] SYSTEM DIAGNOSTICS")
    st.text("Core Operational Loop: STABLE\nBandwidth Allocation: MAXIMUM\nAll nodes reporting green.")

elif module == "Content Matrix":
    st.subheader("[+] CREATIVE PIPELINE")
    niche = st.selectbox("Select Target Segment:", ["Cinematic Automotive", "Grooming & Skincare"])
    if st.button("EXECUTE GENERATION"):
        data = captions[niche]
        st.info(f"**Visual Hook:** \"{data['hook']}\"")
        st.code(data['body'], language="text")
        st.warning(f"**Aesthetic Tags:** {data['tags']}")

elif module == "F1 Motorsport Vault":
    st.subheader("[+] TELEMETRY ARCHIVE")
    if st.button("PULL RANDOM DATAPOINT"):
        st.code(random.choice(f1_facts), language="text")

elif module == "Risk Parameters":
    st.subheader("[+] TRADING ACCOUNT RISK ANALYSIS")
    balance = st.number_input("Net Trading Capital ($):", min_value=0.0, value=1000.0)
    risk_pct = st.slider("Position Risk Cap (%):", 0.1, 5.0, 1.0)
    allowed_loss = balance * (risk_pct / 100.0)
    st.metric(label="MAXIMUM ALLOWED LOSS PER POSITION", value=f"${allowed_loss:,.2f}")
    st.error("CRITICAL: Set hard stop-loss brackets exactly at this limit.")

elif module == "Supercar Telemetry":
    st.subheader("[+] VEHICLE SPECIFICATION PROFILE")
    st.success("**LAMBORGHINI HURACÁN EVO SPYDER**")
    st.code("├── Powertrain: 5.2L Naturally Aspirated V10\n├── Output: 640 HP @ 8,000 RPM\n├── Performance: 0-100 km/h in 3.1 Seconds\n└── Drive Vector: All-Wheel Drive // 7-Speed LDF Dual-Clutch", language="text")

st.markdown("---")
st.write("📟 SECURE CLOUD RUNTIME // END OF LINE.")
