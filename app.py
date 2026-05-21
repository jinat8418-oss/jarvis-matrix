import streamlit as st
import random
import json
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

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

# --- GLOBAL LIVE TELEMETRY MATRIX ---
@st.cache_resource
def initialize_global_telemetry():
    return {"total_connections": 0}

telemetry = initialize_global_telemetry()

if "session_initialized" not in st.session_state:
    st.session_state["session_initialized"] = True
    telemetry["total_connections"] += 1

# --- PERSISTENT TRACKER VAULT STORAGE ---
if "tracker_vault" not in st.session_state:
    st.session_state["tracker_vault"] = {}

# Render Professional Neon Branding Headers
st.markdown('<div class="neon-title">📟 JINAT OS : CORE TERMINAL</div>', unsafe_allow_html=True)
st.markdown('<div class="neon-subtext">SYSTEM DESIGN UNLOCKED // ARCHITECT: JINAT</div>', unsafe_allow_html=True)
st.markdown("---")

# Habit Matrix Setup
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
        <span style="color: #ffffff; font-weight: bold; font-size: 0.85rem;">🤖 JARVIS MATRIX v1.9</span><br>
        <span style="color: #8899a6; font-size: 0.75rem; margin-top: 4px; display: inline-block;">INITIAL LAUNCH:</span><br>
        <span style="color: #39ff14; font-weight: bold; font-size: 0.8rem;">📅 MAY 2026</span><br>
    </div>
""", unsafe_allow_html=True)

# --- MODULE CORRIDORS ---
if module == "🌐 System Mainframe":
    st.write("Welcome to the mainframe terminal workspace. Adjust structural vectors below to modify the active blueprint profile.")
    
    st.markdown("### 🛠️ ACTIVE BLUEPRINT SHAPING TUNNEL")
    col1, col2, col3 = st.columns(3)
    with col1:
        roof_height = st.slider("Chassis Roof Cap:", 0.8, 1.5, 1.15, step=0.05)
    with col2:
        ground_clearance = st.slider("Stance Splitter Drop:", 0.02, 0.25, 0.10, step=0.02)
    with col3:
        spoiler_kick = st.slider("Rear Spoiler Extension:", 0.90, 1.25, 1.05, step=0.05)
        
    car_x = [0.0, 1.2, 1.6, 2.3, 2.7, 4.2, 5.0, 5.5, 6.7, 7.3, 7.8, 8.0, 7.7, 7.3, 6.9, 6.9, 6.4, 5.5, 2.4, 1.9, 1.4, 1.4, 0.9, 0.0]
    car_y = [ground_clearance, ground_clearance + 0.05, 0.45, 0.5, 0.95, roof_height, roof_height - 0.03, roof_height - 0.1, 0.98, 0.98, spoiler_kick, 0.4, ground_clearance, ground_clearance, 0.35, 0.35, ground_clearance, ground_clearance, ground_clearance, ground_clearance, 0.35, 0.35, ground_clearance, ground_clearance]
    
    fig_car = go.Figure()
    fig_car.add_trace(go.Scatter(x=car_x, y=car_y, mode='lines+markers', line=dict(color='#00f3ff', width=2.5), name='Profile'))
    fig_car.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=240, margin=dict(l=10, r=10, b=10, t=10))
    st.plotly_chart(fig_car, use_container_width=True)

elif module == "🤖 Jarvis AI Assistant":
    st.subheader("[+] PARSING MATRIX: INFINITE QUESTION AI")
    st.write("Ask Jarvis absolute anything. The parsing core separates concepts to build customized, non-repeating answers.")
    
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = [{"role": "jarvis", "text": "Jarvis online. Awaiting complex logical strings, sir."}]
    
    for message in st.session_state["chat_history"]:
        if message["role"] == "user":
            st.markdown(f"""<div style='text-align: right; background-color: #1a1f33; padding: 10px; border-radius: 10px; margin-bottom: 10px; border-right: 3px solid #00f3ff; display: inline-block; float: right; clear: both; max-width: 80%; font-family: monospace;'><b>You:</b> {message['text']}</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div style='text-align: left; background-color: #0b131a; padding: 10px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid #39ff14; display: inline-block; float: left; clear: both; max-width: 80%; font-family: monospace; color: #39ff14;'><b>JARVIS:</b> {message['text']}</div>""", unsafe_allow_html=True)
            
    st.markdown("<div style='clear: both;'><br></div>", unsafe_allow_html=True)
    
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your question or command:")
        submit_chat = st.form_submit_button("TRANSMIT TO PARSING CORES")
        
        if submit_chat and user_input:
            st.session_state["chat_history"].append({"role": "user", "text": user_input})
            cmd = user_input.lower()
            
            # Context Identifiers
            is_car = any(x in cmd for x in ["car", "start", "engine", "drive", "lambo", "speed", "v10"])
            is_romel = "romel" in cmd
            is_status = any(x in cmd for x in ["status", "alive", "user", "system", "diagnostic"])
            is_greeting = any(x in cmd for x in ["hello", "hi", "hey", "sup", "bro"])
            
            # Framework Construction Components
            prefix = random.choice([
                "Manoeuvring computational grids... ", 
                "Parsing input telemetry modules... ", 
                "Query decrypted successfully. ", 
                "Initializing thematic response parameters... "
            ])
            suffix = random.choice([
                " // Network telemetry verified.", 
                " // Core matrix streaming stable.", 
                " // Awaiting next mainframe input line.", 
                " // Logic loop fully completed."
            ])
            
            # --- PROCEDURAL MULTI-TRACK ANSWER ENGINE ---
            if is_car:
                if "start" in cmd or "how" in cmd:
                    core = random.choice([
                        "Engines ignite via a high-torque starter motor spinning the flywheel, creating compression as fuel injects into the core blocks.",
                        "To fire up high-performance nodes, electric ignition switches trigger immediate spark generation within the internal cylinder layout.",
                        "Initial mechanical crank vectors send electric power lines rushing down the powertrain to prompt autonomous valve orchestration."
                    ])
                else:
                    core = random.choice([
                        "Chassis profile vectors indicate optimal drag parameters for our current mid-engine concept setup.",
                        "Vehicular statistics logged: A naturally aspirated multi-valve assembly is active inside our simulation.",
                        "Supercar data channels confirm power distribution matrices are completely clear."
                    ])
            elif is_romel:
                core = random.choice([
                    "Operator Romel detected. System status: Friend node confirmed. Terminal access fully authorized.",
                    "Romel data log read verified. Currently monitoring code metrics alongside Architect Jinat.",
                    "Alert: Romel signature found. Running secondary validation protocol... Access cleared."
                ])
            elif is_status:
                core = random.choice([
                    f"Operational report: System clean. Mainframe hosting {telemetry['total_connections']} connections safely.",
                    "Telemetry systems stable. Memory load optimal. Firewalls protecting local scripts are humming.",
                    "System check complete. No corrupted blocks found. Everything running perfectly."
                ])
            elif is_greeting:
                core = random.choice([
                    "Greetings, user. Ready to accept command blocks and layout modifications.",
                    "Hello! Central communication feeds are humming. Give me your directives.",
                    "Core terminal activated. I am listening closely, sir."
                ])
            else:
                # Infinite variation array for completely arbitrary or unmapped text fields
                core = random.choice([
                    f"Analyzing your complex query: '{user_input}'. Data processing fields recommend staying sharp and focused.",
                    f"The logical structure of '{user_input}' has been mapped. Jinat's operational mainframe permits this testing track.",
                    "Linguistic pathways processed. Calculations indicate high synchronization with our current network framework.",
                    "Phrase parsed. Compiling data files... System parameters suggest maximum execution efficiency."
                ])
                
            reply = f"{prefix}{core}{suffix}"
            st.session_state["chat_history"].append({"role": "jarvis", "text": reply})
            st.rerun()

elif module == "🚨 Habit Tracker Grid":
    st.subheader("[+] ROBUST HABIT TRACKER MATRIX")
    st.write("Track daily performance targets with persistent runtime tracking logic.")
    
    target_date = st.date_input("Logging Target Date Selection:", datetime.now())
    date_str = str(target_date)

    # Automatically provision space if this date is brand new
    if date_str not in st.session_state["tracker_vault"]:
        st.session_state["tracker_vault"][date_str] = {habit: False for habit in HABITS}

    st.markdown("### ❌ LOG DAILY RECAP PROGRESSION")
    
    # Render checkboxes reading from and writing to session_state memory directly
    for habit in HABITS:
        st.session_state["tracker_vault"][date_str][habit] = st.checkbox(
            f"Mark Complete: {habit}", 
            value=st.session_state["tracker_vault"][date_str].get(habit, False)
        )

    # Physical Save / Action confirmation button
    if st.button("💾 LOCK LOG INTO SECURE VAULT RECORD"):
        st.success(f"Success! Progression markers safely locked into system records for date: {date_str}")

    st.markdown("---")
    st.markdown("### 📈 AGGREGATED METRICS & CONSISTENCY RATING")
    
    total_days = len(st.session_state["tracker_vault"])
    if total_days > 0:
        for habit in HABITS:
            completed_days = sum(1 for d in st.session_state["tracker_vault"] if st.session_state["tracker_vault"][d].get(habit, False))
            pct = (completed_days / total_days) * 100
            
            st.write(f"**{habit}**")
            st.progress(int(pct))
            st.caption(f"Consistency Rating: {pct:.1f}% ({completed_days}/{total_days} Days Matrixed)")
    else:
        st.info("No active historic logs found. Check items above to generate telemetry data fields.")
            
    st.markdown("---")
    st.markdown("### 📤 EXPORT CODE BACKUP ENVELOPE")
    st.code(json.dumps(st.session_state["tracker_vault"]), language="json")

elif module == "🛸 Jarvis 3D Design Lab":
    st.subheader("[+] TONY STARK HOLOGRAPHIC MESH GENERATOR")
    component = st.selectbox("Select Target Component Matrix:", ["Aero Spoiler Array", "Supercar Wheel Rim Node", "V10 Engine Block Cylinder"])
    scale_factor = st.slider("Dimensional Scale Parameter:", 0.5, 2.5, 1.0)
    
    if st.button("RUN 3D STRUCTURAL COMPILATION"):
        fig = go.Figure()
        if component == "Aero Spoiler Array":
            u = np.linspace(-2, 2, 20); v = np.linspace(-1, 1, 20); U, V = np.meshgrid(u, v)
            X, Y = scale_factor * U, scale_factor * V
            Z = scale_factor * 0.15 * (U**2 - V**2)
            fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', showscale=False))
        elif component == "Supercar Wheel Rim Node":
            u = np.linspace(0, 2*np.pi, 24); v = np.linspace(0, 2*np.pi, 24); U, V = np.meshgrid(u, v)
            R, r = 2.0 * scale_factor, 0.6 * scale_factor
            X = (R + r * np.cos(V)) * np.cos(U); Y = (R + r * np.cos(V)) * np.sin(U); Z = r * np.sin(V)
            fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Cividis', showscale=False))
        else:
            colors = ['#00FFCC', '#0099FF']
            for b_idx, bank in enumerate([-1, 1]): 
                angle = bank * np.pi / 5  
                for i in range(5): 
                    z_offset = (i - 2) * 1.6 * scale_factor; x_center = bank * 1.0 * scale_factor
                    u, h = np.linspace(0, 2*np.pi, 16), np.linspace(-1.2, 1.2, 10)
                    x_cyl, y_cyl, z_cyl = [], [], []
                    for h_val in h:
                        for angle_val in u:
                            rx = (0.45 * scale_factor) * np.cos(angle_val) * np.cos(angle) - h_val * np.sin(angle) + x_center
                            ry = (0.45 * scale_factor) * np.cos(angle_val) * np.sin(angle) + h_val * np.cos(angle)
                            x_cyl.append(rx); y_cyl.append(ry); z_cyl.append(h_val + z_offset)
                    fig.add_trace(go.Mesh3d(x=x_cyl, y=y_cyl, z=z_cyl, alphahull=0, color=colors[b_idx], opacity=0.45, showlegend=False))
        fig.update_layout(scene=dict(xaxis=dict(backgroundcolor="black"), yaxis=dict(backgroundcolor="black"), zaxis=dict(backgroundcolor="black")), paper_bgcolor='black', plot_bgcolor='black', margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

elif module == "Diagnostics":
    st.subheader("[+] SYSTEM DIAGNOSTICS")
    st.markdown("""<div class="neon-box"><span style="color: #39ff14; font-family: monospace;">CORE OPERATIONAL LOOP: STABLE<br>SERVER NODE LOCATION: SECURE REMOTE HOST<br>VERIFICATION DATA: REGISTERED TO ARCHITECT JINAT</span></div>""", unsafe_allow_html=True)

elif module == "Content Matrix":
    st.subheader("[+] CREATIVE PIPELINE")
    niche = st.selectbox("Select Target Segment:", ["Cinematic Automotive", "Grooming & Skincare"])
    if st.button("EXECUTE GENERATION"):
        if niche == "Cinematic Automotive":
            hook = "Heavy machinery meets a dark aesthetic."
            body = "[Visual Structure]\n├── Shadow Contrast: 75%\n└── Highlights: Muted Cinematic Green"
            tags = "#moodandmachine"
        else:
            hook = "Clear skin requires discipline, not random products."
            body = "[Routine Matrix]\n├── AM: Gentle Cleanser\n└── PM: Deep Cleanse"
            tags = "#glowup"
        st.info(f"**Visual Hook:** \"{hook}\"")
        st.code(body, language="text")
        st.warning(f"**Aesthetic Tags:** {tags}")

elif module == "F1 Motorsport Vault":
    st.subheader("[+] TELEMETRY ARCHIVE")
    if st.button("PULL RANDOM DATAPOINT"):
        st.code("Modern F1 power units exceed 50% thermal efficiency metrics.", language="text")

elif module == "Risk Parameters":
    st.subheader("[+] TRADING ACCOUNT RISK ANALYSIS")
    balance = st.number_input("Net Trading Capital ($):", min_value=0.0, value=1000.0)
    risk_pct = st.slider("Position Risk Cap (%):", 0.1, 5.0, 1.0)
    allowed_loss = balance * (risk_pct / 100.0)
    st.metric(label="MAXIMUM ALLOWED LOSS PER POSITION", value=f"${allowed_loss:,.2f}")

elif module == "Supercar Telemetry":
    st.subheader("[+] VEHICLE SPECIFICATION PROFILE")
    st.success("**%s**" % "LAMBORGHINI HURACÁN EVO SPYDER")
    st.code("├── Powertrain: 5.2L Naturally Aspirated V10\n├── Output: 640 HP @ 8,000 RPM\n└── Performance: 0-100 km/h in 3.1s", language="text")

st.markdown("---")
st.write("📟 SECURE CLOUD RUNTIME // END OF LINE.")
