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
    /* Main Background adjustments */
    .stApp {
        background-color: #0d0e15;
        color: #e0e6ed;
    }
    
    /* Neon Glow Headers */
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
    
    /* Custom Container Blocks with Neon Border Glow */
    .neon-box {
        border: 1px solid #00f3ff;
        border-radius: 8px;
        padding: 15px;
        background-color: #121622;
        box-shadow: 0 0 10px rgba(0, 243, 255, 0.25);
        margin-bottom: 15px;
    }
    
    /* Sidebar adjustments */
    section[data-testid="stSidebar"] {
        background-color: #070913 !important;
        border-right: 1px solid #39ff14;
        box-shadow: 2px 0px 10px rgba(57, 255, 20, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

# --- GLOBAL LIVE USER COUNTER ENGINE ---
@st.cache_resource
def initialize_global_telemetry():
    return {"total_connections": 0, "saved_vault_logs": {}}

telemetry = initialize_global_telemetry()

if "session_initialized" not in st.session_state:
    st.session_state["session_initialized"] = True
    telemetry["total_connections"] += 1

# Render Professional Neon Branding Headers with your Name
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

# Display Live Counter metrics inside a styled block
st.sidebar.markdown(f"""
    <div style="border: 1px solid #39ff14; padding: 10px; border-radius: 5px; background-color: #0b131a; margin-bottom: 15px; box-shadow: 0 0 8px rgba(57, 255, 20, 0.2); text-align: center;">
        <span style="color: #39ff14; font-weight: bold; font-family: monospace;">🛰️ LIVE TELEMETRY LOGS:</span><br>
        <span style="color: #ffffff; font-family: monospace; font-size: 0.9rem;">├─ Current Users: <b>{telemetry['total_connections']}</b> Active</span>
    </div>
""", unsafe_allow_html=True)

# Radio selectors default to the blank workspace module to keep screens clean
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

# --- 🛠️ PROFESSIONAL DEVELOPER CREDENTIALS PANEL ---
st.sidebar.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("""
    <div style="border: 1px solid #00f3ff; padding: 12px; border-radius: 6px; background-color: #0a0d1a; box-shadow: 0 0 10px rgba(0, 243, 255, 0.3); font-family: 'Courier New', monospace;">
        <div style="color: #00f3ff; font-weight: bold; font-size: 0.85rem; border-bottom: 1px solid rgba(0, 243, 255, 0.3); padding-bottom: 4px; margin-bottom: 6px; text-align: center;">
            ⚙️ CORE ARCHITECT INFO
        </div>
        <span style="color: #8899a6; font-size: 0.75rem;">DEVELOPER:</span><br>
        <span style="color: #ffffff; font-weight: bold; font-size: 0.85rem;">⚡ JINAT</span><br>
        
        <span style="color: #8899a6; font-size: 0.75rem; margin-top: 4px; display: inline-block;">AI SUBSYSTEM:</span><br>
        <span style="color: #ffffff; font-weight: bold; font-size: 0.85rem;">🤖 JARVIS MATRIX v1.8</span><br>
        
        <span style="color: #8899a6; font-size: 0.75rem; margin-top: 4px; display: inline-block;">INITIAL LAUNCH:</span><br>
        <span style="color: #39ff14; font-weight: bold; font-size: 0.8rem;">📅 MAY 2026</span><br>
        
        <div style="font-size: 0.65rem; color: rgba(0, 243, 255, 0.5); text-align: center; margin-top: 8px; border-top: 1px dotted rgba(0, 243, 255, 0.2); padding-top: 4px;">
            VERIFIED VIA GITHUB DEPLOYMENT
        </div>
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
    fig_car.add_trace(go.Scatter(
        x=car_x, y=car_y,
        mode='lines+markers',
        line=dict(color='#00f3ff', width=2.5),
        marker=dict(color='#39ff14', size=4, opacity=0.9),
        name='Huracán EVO Silhouette',
        hoverinfo='skip'
    ))
    
    fig_car.update_layout(
        title=dict(text="LAMBORGHINI HURACÁN EVO SPYDER : INTERACTIVE PROFILE", font=dict(color="#39ff14", family="monospace", size=12)),
        xaxis=dict(visible=False, range=[-0.5, 8.5]),
        yaxis=dict(visible=False, scaleanchor="x", scaleratio=1, range=[-0.2, 1.6]),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, b=10, t=40),
        height=240
    )
    st.plotly_chart(fig_car, use_container_width=True, config={'displayModeBar': False})
    st.caption("Aesthetic Geometry Engine // Interactive Client-Side Blueprint Modulation Matrix.")

elif module == "🤖 Jarvis AI Assistant":
    st.subheader("[+] DYNAMIC JARVIS ALGORITHMIC CONSOLE")
    st.write("Type any question below. Jarvis parses sentences dynamically to construct randomized, context-aware answers every single execution loop.")
    
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = [
            {"role": "jarvis", "text": "Jarvis matrix synchronized. Text input lanes fully initialized, sir. Feed me data commands."}
        ]
    
    # Print chat history log elements with clean borders
    for message in st.session_state["chat_history"]:
        if message["role"] == "user":
            st.markdown(f"""<div style='text-align: right; background-color: #1a1f33; padding: 10px; border-radius: 10px; margin-bottom: 10px; border-right: 3px solid #00f3ff; display: inline-block; float: right; clear: both; max-width: 80%; font-family: monospace;'><b>You:</b> {message['text']}</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div style='text-align: left; background-color: #0b131a; padding: 10px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid #39ff14; display: inline-block; float: left; clear: both; max-width: 80%; font-family: monospace; color: #39ff14;'><b>JARVIS:</b> {message['text']}</div>""", unsafe_allow_html=True)
            
    st.markdown("<div style='clear: both;'><br></div>", unsafe_allow_html=True)
    
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Transmit voice or text string override directly to Jarvis:")
        submit_chat = st.form_submit_button("COMPILE AND TRANSMIT INPUT")
        
        if submit_chat and user_input:
            st.session_state["chat_history"].append({"role": "user", "text": user_input})
            cmd = user_input.lower()
            
            # Randomized linguistic components for infinite response variance
            prefixes = ["Scanning structural arrays... ", "Ah, an intriguing inquiry, sir. ", "Processing mainframe parameters... ", "Direct directive recorded. "]
            suffixes = [" // Telemetry stream is clean.", " // Standing by for further calculation updates.", " // Verified via current local terminal nodes.", " // Execution complete."]
            
            if "hello" in cmd or "hi" in cmd or "hey" in cmd:
                core_answers = [
                    f"Greetings! I am online. There are currently {telemetry['total_connections']} active users connecting to Architect Jinat's mainframe.",
                    "Hello, operator. All systems are green and awaiting input instructions.",
                    "System linked successfully. Welcome to the terminal control panel."
                ]
            elif "romel" in cmd:
                core_answers = [
                    "Detecting Friend Node: Romel. Access granted. Status: Shocked by codebase progression metrics.",
                    "User profile 'Romel' loaded. Running system audit: input tracking history clear.",
                    "Romel confirmed on secondary display block. Glad to have you navigating our interfaces."
                ]
            elif "specs" in cmd or "lambo" in cmd or "car" in cmd:
                core_answers = [
                    "Extracting mechanical details: Lamborghini Huracán EVO Spyder profile mapped with mid-mounted 5.2L V10.",
                    "Vector geometry maps loaded. 640 horses verified via structural chassis equations.",
                    "Chassis vector parameters initialized. Check out the blueprint modification panel on the Mainframe tab."
                ]
            elif "status" in cmd or "diagnostics" in cmd:
                core_answers = [
                    f"Mainframe nodes are operational. System capacity streaming smoothly with {telemetry['total_connections']} concurrent user sessions.",
                    "Firewalls steady. Diagnostic response loop calculated in 0.004 seconds.",
                    "Local cloud servers running optimally. No structural database ruptures logged."
                ]
            else:
                # Infinite random combination generator for completely unmapped custom user queries
                core_answers = [
                    f"Analyzing your phrase '{user_input}'. My system architecture suggests an optimal configuration array.",
                    "Compiling neural responses... Data streams suggest Architect Jinat's rules are absolute.",
                    "Interesting parameters. Re-routing computational bandwidth to match this instruction request.",
                    "Text package processed successfully. Encryption levels running at max limits."
                ]
                
            # Build an entirely randomized message composition string
            reply = random.choice(prefixes) + random.choice(core_answers) + random.choice(suffixes)
            st.session_state["chat_history"].append({"role": "jarvis", "text": reply})
            st.rerun()

elif module == "🚨 Habit Tracker Grid":
    st.subheader("[+] UPGRADED DIGITAL HABIT TRACKER MATRIX")
    st.write("Track daily performance targets. Hit the permanent record button below to anchor data directly down into the global database structure.")
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    target_date = st.date_input("Logging Target Date Selection:", datetime.now())
    date_str = str(target_date)

    if date_str not in telemetry["saved_vault_logs"]:
        telemetry["saved_vault_logs"][date_str] = {habit: False for habit in HABITS}

    st.markdown("### ❌ LOG NEW PROGRESSION RECAP")
    for habit in HABITS:
        telemetry["saved_vault_logs"][date_str][habit] = st.checkbox(
            f"Set Complete: {habit}", 
            value=telemetry["saved_vault_logs"][date_str].get(habit, False)
        )

    # --- THE IMPROVED TRACKER VAULT ACTION ---
    if st.button("💾 LOCK LOG INTO SECURE GLOBAL RECORD"):
        st.success(f"Success! Progression markers safely cached into system records for date: {date_str}")

    st.markdown("---")
    st.markdown("### 📈 AGGREGATED HISTORIC PERFORMANCE")
    if len(telemetry["saved_vault_logs"]) > 0:
        for habit in HABITS:
            completed = sum(1 for d in telemetry["saved_vault_logs"] if telemetry["saved_vault_logs"][d].get(habit, False))
            total_days = len(telemetry["saved_vault_logs"])
            pct = (completed / total_days) * 100
            
            st.write(f"**{habit}**")
            st.progress(int(pct))
            st.caption(f"Consistency Rating: {pct:.1f}% ({completed}/{total_days} Days Matrixed)")
            
    st.markdown("---")
    st.markdown("### 📤 EXPORT CODE BACKUP ENVELOPE")
    st.code(json.dumps(telemetry["saved_vault_logs"]), language="json")

elif module == "🛸 Jarvis 3D Design Lab":
    st.subheader("[+] TONY STARK HOLOGRAPHIC MESH GENERATOR")
    component = st.selectbox("Select Target Component Matrix:", ["Aero Spoiler Array", "Supercar Wheel Rim Node", "V10 Engine Block Cylinder"])
    scale_factor = st.slider("Dimensional Scale Parameter:", 0.5, 2.5, 1.0)
    command = st.text_input("Voice/Text Override Command Protocol:", value="Jarvis, initialize rapid prototyping structural sweep.")
    
    if st.button("RUN 3D STRUCTURAL COMPILATION"):
        st.info(f"Processing command: '{command}'")
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
                    fig.add_trace(go.Scatter3d(x=x_cyl[::3], y=y_cyl[::3], z=z_cyl[::3], mode='lines', line=dict(color='lime', width=1.5), showlegend=False))
        fig.update_layout(scene=dict(xaxis=dict(backgroundcolor="black", gridcolor="#113311", showbackground=True, zerolinecolor="lime"), yaxis=dict(backgroundcolor="black", gridcolor="#113311", showbackground=True, zerolinecolor="lime"), zaxis=dict(backgroundcolor="black", gridcolor="#113311", showbackground=True, zerolinecolor="lime"), aspectmode='data'), margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor='black', plot_bgcolor='black')
        st.plotly_chart(fig, use_container_width=True)

elif module == "Diagnostics":
    st.subheader("[+] SYSTEM DIAGNOSTICS")
    st.markdown("""<div class="neon-box"><span style="color: #39ff14; font-family: monospace;">CORE OPERATIONAL LOOP: STABLE<br>SERVER NODE LOCATION: SECURE REMOTE HOST<br>VERIFICATION DATA: REGISTERED TO ARCHITECT JINAT</span></div>""", unsafe_allow_html=True)

elif module == "Content Matrix":
    st.subheader("[+] CREATIVE PIPELINE")
    niche = st.selectbox("Select Target Segment:", ["Cinematic Automotive", "Grooming & Skincare"])
    if st.button("EXECUTE GENERATION"):
        if niche == "Cinematic Automotive":
            hooks = ["Heavy machinery meets a dark aesthetic.", "Chasing shadows in a world full of noise."]
            bodies = ["[Visual Structure]\n├── Shadow Contrast: 75%\n└── Highlights: Muted Cinematic Green"]
            tags = "#moodandmachine"
        else:
            hooks = ["Clear skin requires discipline, not random products.", "Stop overwashing your face."]
            bodies = ["[Routine Matrix]\n├── AM: Gentle Cleanser\n└── PM: Deep Cleanse"]
            tags = "#glowup"
        st.info(f"**Visual Hook:** \"{random.choice(hooks)}\"")
        st.code(random.choice(bodies), language="text")
        st.warning(f"**Aesthetic Tags:** {tags}")

elif module == "F1 Motorsport Vault":
    st.subheader("[+] TELEMETRY ARCHIVE")
    if st.button("PULL RANDOM DATAPOINT"):
        facts = ["F1 cars hit up to 6G deceleration.", "Modern engines operate past 50% thermal efficiency."]
        st.code(random.choice(facts), language="text")

elif module == "Risk Parameters":
    st.subheader("[+] TRADING ACCOUNT RISK ANALYSIS")
    balance = st.number_input("Net Trading Capital ($):", min_value=0.0, value=1000.0)
    risk_pct = st.slider("Position Risk Cap (%):", 0.1, 5.0, 1.0)
    allowed_loss = balance * (risk_pct / 100.0)
    st.metric(label="MAXIMUM ALLOWED LOSS PER POSITION", value=f"${allowed_loss:,.2f}")

elif module == "Supercar Telemetry":
    st.subheader("[+] VEHICLE SPECIFICATION PROFILE")
    st.success("**LAMBORGHINI HURACÁN EVO SPYDER**")
    st.code("├── Powertrain: 5.2L Naturally Aspirated V10\n├── Output: 640 HP @ 8,000 RPM\n└── Performance: 0-100 km/h in 3.1s", language="text")

st.markdown("---")
st.write("📟 SECURE CLOUD RUNTIME // END OF LINE.")
