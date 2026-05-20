import streamlit as st
import random
import json
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# Core Configuration
st.set_page_config(page_title="Jarvis OS", page_icon="📟")

st.title("📟 JARVIS OS : CORE TERMINAL")
st.write("SYSTEM STATUS: ACTIVE // CLOUD NODE CONNECTED")
st.markdown("---")

# Habit Matrix Setup
HABITS = [
    "Study (3-4 Hours)", "Workout", "No PMO", "Asset Building (Pins)",
    "Hydration", "Social Momentum", "No Junk", "Reading 10 Pages", "Day/Night Skincare"
]

# Navigation System
st.sidebar.subheader("🕹️ CONTROL PANEL")
module = st.sidebar.radio("CHOOSE SYSTEM MODULE:", [
    "🛸 Jarvis 3D Design Lab",
    "🚨 Habit Tracker Grid",
    "Diagnostics", 
    "Content Matrix", 
    "F1 Motorsport Vault", 
    "Risk Parameters", 
    "Supercar Telemetry"
])

if module == "🛸 Jarvis 3D Design Lab":
    st.subheader("[+] TONY STARK HOLOGRAPHIC HOLOGRAPHIC MESH GENERATOR")
    st.write("Simulating Jarvis spatial design vectors. Enter structural parameters to process.")
    
    # User Inputs
    component = st.selectbox("Select Target Component Matrix:", ["Aero Spoiler Array", "Supercar Wheel Rim Node", "V10 Engine Block Cylinder"])
    mesh_density = st.slider("Mesh Resolution Density (Polygons):", 10, 50, 30)
    scale_factor = st.slider("Dimensional Scale Parameter:", 0.5, 2.5, 1.0)
    
    command = st.text_input("Voice/Text Override Command Protocol:", value="Jarvis, initialize rapid prototyping structural sweep.")
    
    if st.button("RUN 3D STRUCTURAL COMPILATION"):
        st.info(f"Processing command: '{command}'... Generating holographic telemetry array.")
        
        # Math engine to construct real interactive 3D coordinates based on selection
        u = np.linspace(0, 2 * np.pi, mesh_density)
        v = np.linspace(0, np.pi, mesh_density)
        
        if component == "Aero Spoiler Array":
            # Generate a parabolic aerodynamic wing surface profile
            x = scale_factor * np.outer(np.linspace(-3, 3, mesh_density), np.ones(mesh_density))
            y = scale_factor * np.outer(np.linspace(-1, 1, mesh_density), np.ones(mesh_density))**2
            z = scale_factor * 0.2 * np.sin(x)
        elif component == "Supercar Wheel Rim Node":
            # Generate a highly complex 3D structural torus ring
            x = scale_factor * np.outer(3 + np.cos(v), np.cos(u))
            y = scale_factor * np.outer(3 + np.cos(v), np.sin(u))
            z = scale_factor * np.outer(np.sin(v), np.ones(mesh_density))
        else:
            # Generate a complex interlocking hyper-cylinder block matrix
            x = scale_factor * np.outer(np.sin(v), np.cos(u)) * (1 + 0.3 * np.sin(4*u))
            y = scale_factor * np.outer(np.sin(v), np.sin(u)) * (1 + 0.3 * np.sin(4*u))
            z = scale_factor * np.outer(np.cos(v), np.ones(mesh_density))

        # Build the dynamic Plotly interactive 3D mesh figure
        fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis', showscale=False)])
        
        fig.update_layout(
            title=f"Jarvis Rendering: {component}",
            scene=dict(
                xaxis=dict(backgroundcolor="black", gridcolor="lime", showbackground=True, zerolinecolor="lime"),
                yaxis=dict(backgroundcolor="black", gridcolor="lime", showbackground=True, zerolinecolor="lime"),
                zaxis=dict(backgroundcolor="black", gridcolor="lime", showbackground=True, zerolinecolor="lime"),
            ),
            margin=dict(l=0, r=0, b=0, t=40),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        # Inject the live 3D rendering canvas right onto the phone interface
        st.plotly_chart(fig, use_container_width=True)
        st.success("HOLOGRAPHIC PROTOTYPE MOUNTED STABLE. ROTATION CHANNELS UNLOCKED.")

# Keeping all your previous modules running perfectly below
elif module == "🚨 Habit Tracker Grid":
    st.subheader("[+] DIGITAL HABIT TRACKER MATRIX")
    with st.expander("💾 Sync / Load Previous Progress Data"):
        uploaded_data = st.text_area("Paste your backup code string here:")
        history = json.loads(uploaded_data) if uploaded_data else {}
    current_date = datetime.now().strftime("%Y-%m-%d")
    target_date = st.text_input("Logging Date (YYYY-MM-DD):", value=current_date)
    if target_date not in history: history[target_date] = {habit: False for habit in HABITS}
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
    st.code(json.dumps(history), language="json")

elif module == "Diagnostics":
    st.subheader("[+] SYSTEM DIAGNOSTICS")
    st.text("Core Operational Loop: STABLE\nBandwidth Allocation: MAXIMUM")

elif module == "Content Matrix":
    st.subheader("[+] CREATIVE PIPELINE")
    niche = st.selectbox("Select Target Segment:", ["Cinematic Automotive", "Grooming & Skincare"])
    if st.button("EXECUTE GENERATION"):
        if niche == "Cinematic Automotive":
            hooks = ["Heavy machinery meets a dark aesthetic.", "Chasing shadows in a world full of noise.", "Built for the night shift."]
            bodies = ["[Visual Structure]\n├── Shadow Contrast: 75%\n└── Highlights: Muted Cinematic Green"]
            tags = "#moodandmachine #cinematiccars"
        else:
            hooks = ["Clear skin requires discipline, not random products.", "Most guys ignore basic rules."]
            bodies = ["[Routine Matrix]\n├── AM: Gentle Cleanser\n└── PM: Deep Cleanse"]
            tags = "#glowup #skincareroutine"
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
            
