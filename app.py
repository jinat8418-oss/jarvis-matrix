import streamlit as st
import random
import json
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# Core Configuration
st.set_page_config(page_title="Jarvis OS", page_icon="📟", layout="centered")

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
    return {"total_connections": 0}

telemetry = initialize_global_telemetry()

if "session_initialized" not in st.session_state:
    st.session_state["session_initialized"] = True
    telemetry["total_connections"] += 1

# Render Neon Branding Headers
st.markdown('<div class="neon-title">📟 JARVIS OS : CORE TERMINAL</div>', unsafe_allow_html=True)
st.markdown('<div class="neon-subtext">SYSTEM STATUS: ACTIVE // CLOUD NODE STREAMING</div>', unsafe_allow_html=True)
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

module = st.sidebar.radio("CHOOSE SYSTEM MODULE:", [
    "🛸 Jarvis 3D Design Lab",
    "🚨 Habit Tracker Grid",
    "Diagnostics", 
    "Content Matrix", 
    "F1 Motorsport Vault", 
    "Risk Parameters", 
    "Supercar Telemetry"
])

# --- 🛠️ PROFESSIONAL DEVELOPER CREDENTIALS PANEL ---
# Using blank lines to push the block naturally down to the bottom of the sidebar
st.sidebar.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("""
    <div style="border: 1px solid #00f3ff; padding: 12px; border-radius: 6px; background-color: #0a0d1a; box-shadow: 0 0 10px rgba(0, 243, 255, 0.3); font-family: 'Courier New', monospace;">
        <div style="color: #00f3ff; font-weight: bold; font-size: 0.85rem; border-bottom: 1px solid rgba(0, 243, 255, 0.3); padding-bottom: 4px; margin-bottom: 6px; text-align: center;">
            ⚙️ CORE ARCHITECT INFO
        </div>
        <span style="color: #8899a6; font-size: 0.75rem;">DEVELOPER:</span><br>
        <span style="color: #ffffff; font-weight: bold; font-size: 0.85rem;">⚡ MR. DREAMY</span><br>
        
        <span style="color: #8899a6; font-size: 0.75rem; margin-top: 4px; display: inline-block;">AI SUBSYSTEM:</span><br>
        <span style="color: #ffffff; font-weight: bold; font-size: 0.85rem;">🤖 JARVIS MATRIX v1.4</span><br>
        
        <span style="color: #8899a6; font-size: 0.75rem; margin-top: 4px; display: inline-block;">INITIAL LAUNCH:</span><br>
        <span style="color: #39ff14; font-weight: bold; font-size: 0.8rem;">📅 MAY 2026</span><br>
        
        <div style="font-size: 0.65rem; color: rgba(0, 243, 255, 0.5); text-align: center; margin-top: 8px; border-top: 1px dotted rgba(0, 243, 255, 0.2); padding-top: 4px;">
            VERIFIED VIA GITHUB DEPLOYMENT
        </div>
    </div>
""", unsafe_allow_html=True)

# --- MODULE CORRIDORS ---
if module == "🛸 Jarvis 3D Design Lab":
    st.subheader("[+] TONY STARK HOLOGRAPHIC MESH GENERATOR")
    st.write("Enter structural parameters to calculate visual vector fields.")
    
    component = st.selectbox("Select Target Component Matrix:", ["Aero Spoiler Array", "Supercar Wheel Rim Node", "V10 Engine Block Cylinder"])
    scale_factor = st.slider("Dimensional Scale Parameter:", 0.5, 2.5, 1.0)
    command = st.text_input("Voice/Text Override Command Protocol:", value="Jarvis, initialize rapid prototyping structural sweep.")
    
    if st.button("RUN 3D STRUCTURAL COMPILATION"):
        st.info(f"Processing command: '{command}'")
        fig = go.Figure()
        
        if component == "Aero Spoiler Array":
            u = np.linspace(-2, 2, 20)
            v = np.linspace(-1, 1, 20)
            U, V = np.meshgrid(u, v)
            X, Y = scale_factor * U, scale_factor * V
            Z = scale_factor * 0.15 * (U**2 - V**2)
            fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', showscale=False))
            
        elif component == "Supercar Wheel Rim Node":
            u = np.linspace(0, 2*np.pi, 24)
            v = np.linspace(0, 2*np.pi, 24)
            U, V = np.meshgrid(u, v)
            R, r = 2.0 * scale_factor, 0.6 * scale_factor
            X = (R + r * np.cos(V)) * np.cos(U)
            Y = (R + r * np.cos(V)) * np.sin(U)
            Z = r * np.sin(V)
            fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Cividis', showscale=False))
            
        else:
            colors = ['#00FFCC', '#0099FF']
            for b_idx, bank in enumerate([-1, 1]): 
                angle = bank * np.pi / 5  
                for i in range(5): 
                    z_offset = (i - 2) * 1.6 * scale_factor 
                    x_center = bank * 1.0 * scale_factor
                    u, h = np.linspace(0, 2*np.pi, 16), np.linspace(-1.2, 1.2, 10)
                    x_cyl, y_cyl, z_cyl = [], [], []
                    for h_val in h:
                        for angle_val in u:
                            rx = (0.45 * scale_factor) * np.cos(angle_val) * np.cos(angle) - h_val * np.sin(angle) + x_center
                            ry = (0.45 * scale_factor) * np.cos(angle_val) * np.sin(angle) + h_val * np.cos(angle)
                            x_cyl.append(rx); y_cyl.append(ry); z_cyl.append(h_val + z_offset)
                    
                    fig.add_trace(go.Mesh3d(x=x_cyl, y=y_cyl, z=z_cyl, alphahull=0, color=colors[b_idx], opacity=0.45, showlegend=False))
                    fig.add_trace(go.Scatter3d(x=x_cyl[::3], y=y_cyl[::3], z=z_cyl[::3], mode='lines', line=dict(color='lime', width=1.5), showlegend=False))

        fig.update_layout(
            scene=dict(
                xaxis=dict(backgroundcolor="black", gridcolor="#113311", showbackground=True, zerolinecolor="lime"),
                yaxis=dict(backgroundcolor="black", gridcolor="#113311", showbackground=True, zerolinecolor="lime"),
                zaxis=dict(backgroundcolor="black", gridcolor="#113311", showbackground=True, zerolinecolor="lime"),
                aspectmode='data'
            ),
            margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor='black', plot_bgcolor='black'
        )
        st.plotly_chart(fig, use_container_width=True)

elif module == "🚨 Habit Tracker Grid":
    st.subheader("[+] DIGITAL HABIT TRACKER MATRIX")
    with st.expander("💾 Sync / Load Previous Progress Data"):
        uploaded_data = st.text_area("Paste your backup code string here:")
        history = json.loads(uploaded_data) if uploaded_data else {}
        
    current_date = datetime.now().strftime("%Y-%m-%d")
    target_date = st.text_input("Logging Date (YYYY-MM-DD):", value=current_date)

    if target_date not in history:
        history[target_date] = {habit: False for habit in HABITS}

    st.markdown("### ❌ HABIT EXECUTION CHECKLIST")
    for habit in HABITS:
        history[target_date][habit] = st.checkbox(f"Mark ❌ for: {habit}", value=history[target_date].get(habit, False))

    st.markdown("---")
    st.markdown("### 📈 MONTHLY CONSISTENCY METRICS")
    if len(history) > 0:
        for habit in HABITS:
            completed = sum(1 for d in history if history[d].get(habit, False))
            pct = (completed / len(history)) * 100
            st.write(f"**{habit}**")
            st.progress(int(pct))
            st.caption(f"Consistency Rating: {pct:.1f}% ({completed}/{len(history)} Days)")
    
    st.markdown("---")
    st.markdown("### 📤 SAVE PROGRESS DATA")
    st.code(json.dumps(history), language="json")

elif module == "Diagnostics":
    st.subheader("[+] SYSTEM DIAGNOSTICS")
    st.markdown("""
        <div class="neon-box">
            <span style="color: #39ff14; font-family: monospace;">
                CORE OPERATIONAL LOOP: STABLE<br>
                BANDWIDTH ALLOCATION: MAXIMUM<br>
                SERVER NODE LOCATION: SECURE REMOTE HOST<br>
                VERIFICATION DATA: REGISTERED TO ARCHITECT
            </span>
        </div>
    """, unsafe_allow_html=True)

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
            
