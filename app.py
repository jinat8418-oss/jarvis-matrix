import streamlit as st
import random
import json
from datetime import datetime

# Core Configuration
st.set_page_config(page_title="Jarvis OS", page_icon="📟")

st.title("📟 JARVIS OS : CORE TERMINAL")
st.write("SYSTEM STATUS: ACTIVE // CLOUD NODE CONNECTED")
st.markdown("---")

# Habit Matrix Setup
HABITS = [
    "Study (3-4 Hours)",
    "Workout",
    "No PMO",
    "Asset Building (Pins)",
    "Hydration",
    "Social Momentum",
    "No Junk",
    "Reading 10 Pages",
    "Day/Night Skincare"
]

# Navigation System
st.sidebar.subheader("🕹️ CONTROL PANEL")
module = st.sidebar.radio("CHOOSE SYSTEM MODULE:", [
    "🚨 Habit Tracker Grid",
    "Diagnostics", 
    "Content Matrix", 
    "F1 Motorsport Vault", 
    "Risk Parameters", 
    "Supercar Telemetry"
])

if module == "🚨 Habit Tracker Grid":
    st.subheader("[+] DIGITAL HABIT TRACKER MATRIX")
    st.write("Log your daily execution variables below. Tap to mark your progress.")
    
    with st.expander("💾 Sync / Load Previous Progress Data"):
        uploaded_data = st.text_area("Paste your backup code string here to load past history:")
        if uploaded_data:
            try:
                history = json.loads(uploaded_data)
                st.success("History matrix synced successfully!")
            except:
                st.error("Invalid sync string format.")
                history = {}
        else:
            history = {}

    st.markdown("### 📅 SELECT TRACKING TARGET DATE")
    current_date = datetime.now().strftime("%Y-%m-%d")
    target_date = st.text_input("Logging Date (YYYY-MM-DD):", value=current_date)

    if target_date not in history:
        history[target_date] = {habit: False for habit in HABITS}

    st.markdown("### ❌ HABIT EXECUTION CHECKLIST")
    for habit in HABITS:
        default_val = history[target_date].get(habit, False)
        history[target_date][habit] = st.checkbox(f"Mark ❌ for: {habit}", value=default_val)

    st.markdown("---")
    st.markdown("### 📈 MONTHLY CONSISTENCY METRICS")
    total_days_logged = len(history)
    
    if total_days_logged > 0:
        for habit in HABITS:
            completed_days = sum(1 for date in history if history[date].get(habit, False))
            score_pct = (completed_days / total_days_logged) * 100
            st.write(f"**{habit}**")
            st.progress(int(score_pct))
            st.caption(f"Consistency Rating: {score_pct:.1f}% ({completed_days}/{total_days_logged} Days Execution)")
    else:
        st.info("No tracking logs detected in system memory yet.")

    st.markdown("---")
    st.markdown("### 📤 SAVE PROGRESS DATA")
    st.write("Copy this backup string and save it in a notes app:")
    json_string = json.dumps(history)
    st.code(json_string, language="json")

elif module == "Diagnostics":
    st.subheader("[+] SYSTEM DIAGNOSTICS")
    st.text("Core Operational Loop: STABLE\nBandwidth Allocation: MAXIMUM\nAll nodes reporting green.")

elif module == "Content Matrix":
    st.subheader("[+] CREATIVE PIPELINE")
    niche = st.selectbox("Select Target Segment:", ["Cinematic Automotive", "Grooming & Skincare"])
    
    if st.button("EXECUTE GENERATION"):
        # Expanded multi-option arrays for random generation
        if niche == "Cinematic Automotive":
            hooks = [
                "Heavy machinery meets a dark aesthetic.",
                "Chasing shadows in a world full of noise.",
                "Built for the night shift.",
                "Quiet luxury, loud horsepower.",
                "They look at the shine, we design the silhouette.",
                "Engineered to blend into the darkness."
            ]
            bodies = [
                "[Visual Structure]\n├── Shadow Contrast: 75%\n└── Highlights: Muted Cinematic Green\n└── Framing: Aggressive Low-Angle Grid",
                "[Visual Structure]\n├── Tone Matrix: Midnight Moody Blue\n└── Exposure: -1.2 Ev crushed blacks\n└── Centerpiece: Side-profile lighting split",
                "[Visual Structure]\n├── Grain Filter: 15% Retro Cinematic\n└── Grading: Cyan Shadows / Warm Highlights\n└── Focal Node: Dual-exhaust geometry geometry"
            ]
            tags = "#moodandmachine #cinematiccars #darkaesthetic #automativedesign"
            
        else: # Grooming & Skincare
            hooks = [
                "Clear skin requires discipline, not random products.",
                "Most guys completely ruin their skin with this one mistake.",
                "Fix these 3 bad habits before your skin breaks out.",
                "The ultimate minimal routine for a completely clear complexion.",
                "Stop overwashing your face. Here is the actual matrix.",
                "Skincare is a discipline game. No excuses."
            ]
            bodies = [
                "[Routine Matrix]\n├── AM: Gentle Cleanser + Hydration Lock\n└── PM: Deep Cleanse + Active Recovery Layer",
                "[Routine Matrix]\n├── Shield Phase: Non-comedogenic Sun Protection\n└── Recovery Phase: Cold water wash + Hyaluronic sealing",
                "[Routine Matrix]\n├── Exfoliation Index: 2x per week maximum\n└── Daily Rule: Zero face touching / Sterile microfibers"
            ]
            tags = "#glowup #skincareroutine #mensgrooming #selfimprovement"
            
        st.info(f"**Visual Hook:** \"{random.choice(hooks)}\"")
        st.code(random.choice(bodies), language="text")
        st.warning(f"**Aesthetic Tags:** {tags}")

elif module == "F1 Motorsport Vault":
    st.subheader("[+] TELEMETRY ARCHIVE")
    if st.button("PULL RANDOM DATAPOINT"):
        facts = [
            "F1 cars hit up to 6G deceleration forces during heavy braking zones.",
            "Modern V6 turbo hybrid power units operate past a historic 50% thermal efficiency index.",
            "Past 150 km/h, aerodynamic downforce exceeds the entire net curb weight of an F1 car.",
            "An F1 pit crew can swap 4 tires completely in under 1.80 seconds flat.",
            "F1 tire compounds operate inside an optimal thermal window reaching up to 110°C."
        ]
        st.code(random.choice(facts), language="text")

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
    st.code("├── Powertrain: 5.2L Naturally Aspirated V10\n├── Output: 640 HP @ 8,000 RPM\n└── Performance: 0-100 km/h in 3.1s\n└── Drivetrain: 7-Speed LDF Dual-Clutch / AWD", language="text")

st.markdown("---")
st.write("📟 SECURE CLOUD RUNTIME // END OF LINE.")
