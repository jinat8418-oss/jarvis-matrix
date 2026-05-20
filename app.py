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
    st.subheader("[+] TONY STARK HOLOGRAPHIC MESH GENERATOR")
    st.write("Simulating Jarvis spatial design vectors. Enter structural parameters to process.")
    
    # User Inputs
    component = st.selectbox("Select Target Component Matrix:", ["Aero Spoiler Array", "Supercar Wheel Rim Node", "V10 Engine Block Cylinder"])
    mesh_density = st.slider("Mesh Resolution Density:", 10, 50, 30)
    scale_factor = st.slider("Dimensional Scale Parameter:", 0.5, 2.5, 1.0)
    
    command = st.text_input("Voice/Text Override Command Protocol:", value="Jarvis, initialize rapid prototyping structural sweep.")
    
    if st.button("RUN 3D STRUCTURAL COMPILATION"):
        st.info(f"Processing command: '{command}'... Generating holographic telemetry array.")
        
        if component == "Aero Spoiler Array":
            # Parabolic aerodynamic wing surface profile
            u = np.linspace(0, 2 * np.pi, mesh_density)
            x = scale_factor * np.outer(np.linspace(-3, 3, mesh_density), np.ones(mesh_density))
            y = scale_factor * np.outer(np.linspace(-1, 1, mesh_density), np.ones(mesh_density))**2
            z = scale_factor * 0.2 * np.sin(x)
            
        elif component == "Supercar Wheel Rim Node":
            # 3D structural torus ring
            u = np.linspace(0, 2 * np.pi, mesh_density)
            v = np.linspace(0, 2 * np.pi, mesh_density)
            x = scale_factor * np.outer(3 + np.cos(v), np.cos(u))
            y = scale_factor * np.outer(3 + np.cos(v), np.sin(u))
            z = scale_factor * np.outer(np.sin(v), np.ones(mesh_density))
            
        else:
            # Mechanical V10 Engine Block: 2 banks of 5 rigid cylinders angled at 45 degrees
            x_list, y_list, z_list = [], [], []
            c_u = np.linspace(0, 2 * np.pi, int(mesh_density/2))
            c_v = np.linspace(-1.5, 1.5, int(mesh_density/2))
            
            for bank in [-1, 1]: 
                angle = bank * np.pi / 4 # 45-degree angle shift for V-shape
                for i in range(5): # 5 cylinders per bank
                    z_offset = (i - 2) * 1.5 * scale_factor # Linear spacing down the block length
                    
                    for uc in c_u:
                        for vc in c_v:
                            radius = 0.5 * scale_factor
                            x_cyl = radius * np.cos(uc)
                            y_cyl = vc * scale_factor
                            
                            # Rotate vectors into an aggressive mechanical V alignment
                            x_rot = x_cyl * np.cos(angle) - y_cyl * np.sin(angle)
                            y_rot = x_cyl * np.sin(angle) + y_cyl * np.cos(angle) + (bank * 0.8 * scale_factor)
                            
                            x_list.append(x_rot)
                            y_list.append(y_rot)
                            z_list.append(z_offset)
            
            # Reshape 1D data arrays into structured 2D coordinate spaces for the mesh surface
            total_points = len(x_list)
            rows = int(np.sqrt(total_points))
            while total_points % rows != 0:
                rows -= 1
            cols = int(total_points / rows)
            
            x = np.array(x_list).reshape(rows, cols)
            y = np.array(y_list).reshape(rows, cols)
            z = np.array(z_list).reshape(rows, cols)

        # Build Plotly interactive 3D mesh figure
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
        
        st.plotly_chart(fig, use_container_width=True)
        st.success("MECHANICAL VECTOR PROTOTYPE MOUNTED STABLE.")

# Habit Tracker Section
elif module == "🚨 Habit Tracker Grid":
    st.subheader("[+] DIGITAL HABIT TRACKER MATRIX")
    with st.expander("💾 Sync / Load Previous Progress Data"):
        uploaded_data = st.text_area("Paste your backup code string here to load past history:")
        history = json.loads(uploaded_data) if uploaded_data else {}
        
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
    json_string = json.dumps(history)
    st.code(json_string, language="json")

# Core Sub-Modules
elif module == "Diagnostics":
    st.subheader("[+] SYSTEM DIAGNOSTICS")
    st.text("Core Operational Loop: STABLE\nBandwidth Allocation: MAXIMUM\nAll nodes reporting green.")

elif module == "Content Matrix":
    st.subheader("[+] CREATIVE PIPELINE")
    niche = st.selectbox("Select Target Segment:", ["Cinematic Automotive", "Grooming & Skincare"])
    if st.button("EXECUTE GENERATION"):
        if niche == "Cinematic Automotive":
            hooks = ["Heavy machinery meets a dark aesthetic.", "Chasing shadows in a world full of noise.", "Built for the night shift."]
            bodies = ["[Visual Structure]\n├── Shadow Contrast: 75%\n└── Highlights: Muted Cinematic Green"]
            tags = "#moodandmachine #cinematiccars"
        else:
            hooks = ["Clear skin requires discipline, not random products.", "Stop overwashing your face. Here is the matrix."]
            bodies = ["[Routine Matrix]\n├── AM: Gentle Cleanser + Hydration\n└── PM: Deep Cleanse + Recovery Layer"]
            tags = "#glowup #skincareroutine"
        st.info(f"**Visual Hook:** \"{random.choice(hooks)}\"")
        st.code(random.choice(bodies), language="text")
        st.warning(f"**Aesthetic Tags:** {tags}")

elif module == "F1 Motorsport Vault":
    st.subheader("[+] TELEMETRY ARCHIVE")
    if st.button("PULL RANDOM DATAPOINT"):
        facts = ["F1 cars hit up to 6G deceleration.", "Modern engines operate past 50% thermal efficiency.", "An F1 crew can swap 4 tires in under 1.80 seconds."]
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
                            
