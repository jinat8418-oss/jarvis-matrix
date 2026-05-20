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
    
    # 1. Data Backup / Restore Portal
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

    # 2. Select Date to Log
    st.markdown("### 📅 SELECT TRACKING TARGET DATE")
    current_date = datetime.now().strftime("%Y-%m-%d")
    target_date = st.text_input("Logging Date (YYYY-MM-DD):", value=current_date)

    if target_date not in history:
        history[target_date] = {habit: False for habit in HABITS}

    # 3. Interactive Habit Grid Checklist
    st.markdown("### ❌ HABIT EXECUTION CHECKLIST")
    for habit in HABITS:
        # Load state if it exists
        default_val = history[target_date].get(habit, False)
        history[target_date][habit] = st.checkbox(f"Mark ❌ for: {habit}", value=default_val)

    st.markdown("---")
    
    # 4. Generate Monthly Insights & Analytics
    st.markdown("### 📈 MONTHLY CONSISTENCY METRICS")
    total_days_logged = len(history)
    
    if total_days_logged > 0:
        for habit in HABITS:
            completed_days = sum(1 for date in history if history[date].get(habit, False))
            score_pct = (completed_days / total_days_logged) * 100
            
            # Show a progress score for consistency
            st.write(f"**{habit}**")
            st.progress(int(score_pct))
            st.caption(f"Consistency Rating: {score_pct:.1f}% ({completed_days}/{total_days_logged} Days Execution)")
    else:
        st.info("No tracking logs detected in system memory yet.")

    st.markdown("---")
    
    # 5. Data Export Node
    st.markdown("### 📤 SAVE PROGRESS DATA")
    st.write("To keep your data safe across browser refreshes, copy this backup string and save it in a notes app, or paste it back in above next time!")
    json_string = json.dumps(history)
    st.code(json_string, language="json")

# Keep old modules working perfectly below
elif module == "Diagnostics":
    st.subheader("[+] SYSTEM DIAGNOSTICS")
    st.text("Core Operational Loop: STABLE\nBandwidth Allocation: MAXIMUM\nAll nodes reporting green.")

elif module == "Content Matrix":
    st.subheader("[+] CREATIVE PIPELINE")
    niche = st.selectbox("Select Target Segment:", ["Cinematic Automotive", "Grooming & Skincare"])
    if st.button("EXECUTE GENERATION"):
        captions = {
            "Cinematic Automotive": {"hook": "Heavy machinery meets a dark aesthetic.", "body": "[Visual Structure]\n├── Shadow: 70%\n└── Highlights: Muted Green", "tags": "#moodandmachine"},
            "Grooming & Skincare": {"hook": "Clear skin requires discipline.", "body": "[Routine Matrix]\n├── AM: Cleanse\n└── PM: Recovery Layer", "tags": "#glowup"}
        }
        data = captions[niche]
        st.info(f"**Visual Hook:** \"{data['hook']}\"")
        st.code(data['body'], language="text")
        st.warning(f"**Aesthetic Tags:** {data['tags']}")

elif module == "F1 Motorsport Vault":
    st.subheader("[+] TELEMETRY ARCHIVE")
    if st.button("PULL RANDOM DATAPOINT"):
        facts = ["F1 cars hit up to 6G deceleration forces.", "Modern engines operate past 50% thermal efficiency.", "Past 150 km/h, downforce exceeds curb weight."]
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
    st.success("**%s**" % "LAMBORGHINI HURACÁN EVO SPYDER")
    st.code("├── Powertrain: 5.2L Naturally Aspirated V10\n├── Output: 640 HP @ 8,000 RPM\n└── Performance: 0-100 km/h in 3.1s", language="text")

st.markdown("---")
st.write("📟 SECURE CLOUD RUNTIME // END OF LINE.")
            
