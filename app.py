import streamlit as st
import random
import json
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# Core Configuration
st.set_page_config(page_title="JINAT OS", page_icon="📟", layout="centered")

# --- CYBERPUNK NEON GLOW STYLE ENGINE ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0e15;
        color: #e0e6ed;
    }
    .neon-title {
        font-family: 'Courier New', monospace;
        color: #00f3ff;
        text-shadow: 0 0 10px #00f3ff, 0 0 20px #00f3ff;
        font-weight: bold;
        font-size: 2.2rem;
        margin-bottom: 5px;
    }
    .neon-subtext {
        color: #39ff14;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 8px rgba(57, 255, 20, 0.6);
        font-size: 0.9rem;
        letter-spacing: 2px;
    }
    .neon-box {
        border: 1px solid #00f3ff;
        border-radius: 8px;
        padding: 15px;
        background-color: #121622;
        box-shadow: 0 0 10px rgba(0, 243, 255, 0.25);
        margin-bottom: 15px;
    }
    section[data-testid="stSidebar"] {
        background-color: #070913 !important;
        border-right: 1px solid #39ff14;
        box-shadow: 2px 0px 10px rgba(57, 255, 20, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

# --- GLOBAL TELEMETRY ENGINE ---
@st.cache_resource
def initialize_global_telemetry():
    return {"total_connections": 12}

telemetry = initialize_global_telemetry()

# --- PERSISTENT SYSTEMS LOG ARCHIVE ENGINE ---
if "tracker_vault" not in st.session_state:
    st.session_state["tracker_vault"] = {}

if "global_incident_archive" not in st.session_state:
    st.session_state["global_incident_archive"] = [
        {"timestamp": "2026-05-29 21:30:00", "target": "System Bootstrap Node", "type": "SYSTEM INIT", "status": "CLEARED"}
    ]

# Render Branding Headers
st.markdown('<div class="neon-title">📟 JINAT OS : CORE TERMINAL</div>', unsafe_allow_html=True)
st.markdown('<div class="neon-subtext">SYSTEM DESIGN UNLOCKED // ARCHITECT: JINAT</div>', unsafe_allow_html=True)
st.markdown("---")

HABITS = [
    "Study (3-4 Hours)", "Workout", "No PMO", "Asset Building (Pins)",
    "Hydration", "Social Momentum", "No Junk", "Reading 10 Pages", "Day/Night Skincare"
]

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.subheader("🕹️ CONTROL PANEL")
st.sidebar.markdown(f"""
    <div style="border: 1px solid #39ff14; padding: 10px; border-radius: 5px; background-color: #0b131a; margin-bottom: 15px; box-shadow: 0 0 8px rgba(57, 255, 20, 0.2); text-align: center;">
        <span style="color: #39ff14; font-weight: bold; font-family: monospace;">🛰️ LIVE TELEMETRY LOGS:</span><br>
        <span style="color: #ffffff; font-family: monospace; font-size: 0.9rem;">├─ Current Users: <b>{telemetry['total_connections']}</b> Active</span>
    </div>
""", unsafe_allow_html=True)

module = st.sidebar.radio("CHOOSE SYSTEM MODULE:", [
    "🌐 System Mainframe",
    "🛡️ Jarvis Virtual Defense Grid",
    "🤖 Jarvis AI Assistant",
    "🚨 Habit Tracker Grid",
    "🛸 Jarvis 3D Design Lab",
    "Diagnostics", 
    "Content Matrix", 
    "F1 Motorsport Vault", 
    "Risk Parameters", 
    "Supercar Telemetry"
])

st.sidebar.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("""
    <div style="border: 1px solid #00f3ff; padding: 12px; border-radius: 6px; background-color: #0a0d1a; box-shadow: 0 0 10px rgba(0, 243, 255, 0.3); font-family: 'Courier New', monospace;">
        <div style="color: #00f3ff; font-weight: bold; font-size: 0.85rem; border-bottom: 1px solid rgba(0, 243, 255, 0.3); padding-bottom: 4px; margin-bottom: 6px; text-align: center;">
            ⚙️ CORE ARCHITECT INFO
        </div>
        <span style="color: #8899a6; font-size: 0.75rem;">DEVELOPER:</span><br>
        <span style="color: #ffffff; font-weight: bold; font-size: 0.85rem;">⚡ JINAT</span><br>
        <span style="color: #8899a6; font-size: 0.75rem; margin-top: 4px; display: inline-block;">AI SUBSYSTEM:</span><br>
        <span style="color: #ffffff; font-weight: bold; font-size: 0.85rem;">🤖 JARVIS MATRIX v2.1</span><br>
        <span style="color: #8899a6; font-size: 0.75rem; margin-top: 4px; display: inline-block;">INITIAL LAUNCH:</span><br>
        <span style="color: #39ff14; font-weight: bold; font-size: 0.8rem;">📅 MAY 2026</span><br>
    </div>
""", unsafe_allow_html=True)

# --- MODULE CORRIDORS ---
if module == "🌐 System Mainframe":
    st.write("Welcome to the mainframe terminal workspace. Adjust structural vectors below to modify the active blueprint profile.")
    col1, col2, col3 = st.columns(3)
    with col1: roof_height = st.slider("Chassis Roof Cap:", 0.8, 1.5, 1.15, step=0.05)
    with col2: ground_clearance = st.slider("Stance Splitter Drop:", 0.02, 0.25, 0.10, step=0.02)
    with col3: spoiler_kick = st.slider("Rear Spoiler Extension:", 0.90, 1.25, 1.05, step=0.05)
    car_x = [0.0, 1.2, 1.6, 2.3, 2.7, 4.2, 5.0, 5.5, 6.7, 7.3, 7.8, 8.0, 7.7, 7.3, 6.9, 6.9, 6.4, 5.5, 2.4, 1.9, 1.4, 1.4, 0.9, 0.0]
    car_y = [ground_clearance, ground_clearance + 0.05, 0.45, 0.5, 0.95, roof_height, roof_height - 0.03, roof_height - 0.1, 0.98, 0.98, spoiler_kick, 0.4, ground_clearance, ground_clearance, 0.35, 0.35, ground_clearance, ground_clearance, ground_clearance, ground_clearance, 0.35, 0.35, ground_clearance, ground_clearance]
    fig_car = go.Figure()
    fig_car.add_trace(go.Scatter(x=car_x, y=car_y, mode='lines+markers', line=dict(color='#00f3ff', width=2.5)))
    fig_car.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=240, margin=dict(l=10, r=10, b=10, t=10))
    st.plotly_chart(fig_car, use_container_width=True)

elif module == "🛡️ Jarvis Virtual Defense Grid":
    st.subheader("[+] AUTOMATED AI COUNTERMEASURE SYSTEM")
    st.write("This node models real-time intercept actions against network security threats targeting infrastructure networks.")
    
    target_enterprise = st.selectbox("Select Target Infrastructure Nodes:", [
        "Mobile User Device Node (Social Media API Firewall Shield)",
        "Rockstar Games Alpha Server (Grand Theft Auto VI Source File Grid)",
        "Sovereign Government Central Communication Database"
    ])
    
    if st.button("EXECUTE LIVE SIMULATED BREACH INTERCEPT"):
        st.warning("⚠️ ALERT: UNRECOGNIZED IP ATTEMPTING MALICIOUS BURST DATA EXFILTRATION...")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("🤖 Jarvis Parsing Request: Analyzing incoming packets...")
        time.sleep(0.6)
        progress_bar.progress(30)
        status_text.text("👾 Tracking Anomaly: Exploit vector identified on communication layer.")
        time.sleep(0.6)
        progress_bar.progress(65)
        status_text.text("⚡ Activating Shield Protocol: Isolation routine running...")
        time.sleep(0.6)
        progress_bar.progress(100)
        
        current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.success(f"✔️ COUNTERMEASURE SUCCESSFUL: Threat neutralized on target node.")
        
        st.session_state["global_incident_archive"].append({
            "timestamp": current_time_str,
            "target": target_enterprise.split(" (")[0],
            "type": "MALICIOUS INTRUSION METRIC DETECTED",
            "status": "QUARANTINED"
        })
        
        time_axis = list(range(10))
        attack_intensity = [random.randint(40, 95) for _ in range(7)] + [20, 5, 0]
        fig_defense = go.Figure()
        fig_defense.add_trace(go.Scatter(x=time_axis, y=attack_intensity, mode='lines+markers', name='Threat Load', line=dict(color='#ff0055', width=3)))
        fig_defense.update_layout(xaxis=dict(gridcolor="#221111"), yaxis=dict(gridcolor="#221111"), paper_bgcolor='#0b0d14', plot_bgcolor='#0b0d14', height=240, margin=dict(l=10, r=10, b=10, t=10))
        st.plotly_chart(fig_defense, use_container_width=True)

    st.markdown("---")
    st.markdown("### 🗃️ CHRONOLOGICAL SYSTEM THREAT LOG ARCHIVE")
    for incident in reversed(st.session_state["global_incident_archive"]):
        st.markdown(f"""
            <div style="border-left: 3px solid #39ff14; background-color: #111424; padding: 10px; margin-bottom: 8px; font-family: monospace; border-radius: 4px;">
                <span style="color: #8899a6; font-size: 0.8rem;">[{incident['timestamp']}]</span><br>
                <span style="color: #00f3ff;">TARGET:</span> {incident['target']} | <span style="color: #ff0055;">TYPE:</span> {incident['type']}<br>
                <span style="color: #39ff14; font-weight: bold;">STATUS: 🛡️ {incident['status']}</span>
            </div>
        """, unsafe_allow_html=True)

elif module == "🤖 Jarvis AI Assistant":
    st.subheader("[+] DYNAMIC JARVIS ALGORITHMIC CONSOLE")
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = [{"role": "jarvis", "text": "Jarvis matrix synchronized. Text lanes open, sir."}]
    
    for message in st.session_state["chat_history"]:
        if message["role"] == "user":
            st.markdown(f"""<div style='text-align: right; background-color: #1a1f33; padding: 10px; border-radius: 10px; margin-bottom: 10px; border-right: 3px solid #00f3ff; display: inline-block; float: right; clear: both; max-width: 80%; font-family: monospace;'><b>You:</b> {message['text']}</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div style='text-align: left; background-color: #0b131a; padding: 10px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid #39ff14; display: inline-block; float: left; clear: both; max-width: 80%; font-family: monospace; color: #39ff14;'><b>JARVIS:</b> {message['text']}</div>""", unsafe_allow_html=True)
            
    st.markdown("<div style='clear: both;'><br></div>", unsafe_allow_html=True)
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your question or command:")
        submit_chat = st.form_submit_button("COMPILE AND TRANSMIT INPUT")
        if submit_chat and user_input:
            st.session_state["chat_history"].append({"role": "user", "text": user_input})
            cmd = user_input.lower()
            prefix = random.choice(["Parsing input telemetry modules... ", "Query decrypted successfully. "])
            suffix = random.choice([" // Network telemetry verified.", " // Logic loop fully completed."])
            
            if any(x in cmd for x in ["car", "start", "engine"]):
                core = "Engines ignite via a high-torque starter motor spinning the flywheel, creating compression as fuel injects into the core blocks."
            elif "romel" in cmd:
                core = "Operator Romel detected. Status: Friend node confirmed. Terminal access fully authorized."
            elif any(x in cmd for x in ["status", "alive", "user"]):
                core = f"Operational report: System clean. Mainframe hosting {telemetry['total_connections']} connections safely."
            else:
                core = f"Analyzing complex query stream. Data processing pathways mapped successfully under Jinat's core firewall rules."
                
            st.session_state["chat_history"].append({"role": "jarvis", "text": f"{prefix}{core}{suffix}"})
            st.rerun()

elif module == "🚨 Habit Tracker Grid":
    st.subheader("[+] ROBUST HABIT TRACKER MATRIX")
    target_date = st.date_input("Logging Target Date Selection:", datetime.now())
    date_str = str(target_date)
    if date_str not in st.session_state["tracker_vault"]:
        st.session_state["tracker_vault"][date_str] = {habit: False for habit in HABITS}
    st.markdown("### ❌ LOG DAILY RECAP PROGRESSION")
    for habit in HABITS:
        st.session_state["tracker_vault"][date_str][habit] = st.checkbox(f"Mark Complete: {habit}", value=st.session_state["tracker_vault"][date_str].get(habit, False))
    if st.button("💾 LOCK LOG INTO SECURE VAULT RECORD"):
        st.success(f"Success! Progression markers safely locked for date: {date_str}")
    st.markdown("---")
    st.markdown("### 📈 AGGREGATED METRICS")
    total_days = len(st.session_state["tracker_vault"])
    if total_days > 0:
        for habit in HABITS:
            completed_days = sum(1 for d in st.session_state["tracker_vault"] if st.session_state["tracker_vault"][d].get(habit, False))
            pct = (completed_days / total_days) * 100
            st.write(f"**{habit}**")
            st.progress(int(pct))
    st.code(json.dumps(st.session_state["tracker_vault"]), language="json")

elif module == "🛸 Jarvis 3D Design Lab":
    st.subheader("[+] TONY STARK HOLOGRAPHIC MESH GENERATOR")
    component = st.selectbox("Select Target Component Matrix:", ["Aero Spoiler Array", "Supercar Wheel Rim Node"])
    scale_factor = st.slider("Dimensional Scale Parameter:", 0.5, 2.5, 1.0)
    if st.button("RUN 3D STRUCTURAL COMPILATION"):
        fig = go.Figure()
        if component == "Aero Spoiler Array":
            u = np.linspace(-2, 2, 20); v = np.linspace(-1, 1, 20); U, V = np.meshgrid(u, v)
            fig.add_trace(go.Surface(x=scale_factor*U, y=scale_factor*V, z=scale_factor*0.15*(U**2 - V**2), showscale=False))
        fig.update_layout(scene=dict(xaxis=dict(backgroundcolor="black")), paper_bgcolor='black', plot_bgcolor='black', margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

elif module == "Diagnostics": st.write("System execution circuit status: Stable.")
elif module == "Content Matrix": st.write("Aesthetic Content Matrix online.")
elif module == "F1 Motorsport Vault": st.write("Motorsport technical vault synchronized.")
elif module == "Risk Parameters": st.write("Risk management formulas operational.")
elif module == "Supercar Telemetry": st.write("Lamborghini structural spec arrays loaded.")

st.markdown("---")
st.write("📟 SECURE CLOUD RUNTIME // END OF LINE.")
        
