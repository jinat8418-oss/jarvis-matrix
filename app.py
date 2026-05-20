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
    scale_factor = st.slider("Dimensional Scale Parameter:", 0.5, 2.5, 1.0)
    command = st.text_input("Voice/Text Override Command Protocol:", value="Jarvis, initialize rapid prototyping structural sweep.")
    
    if st.button("RUN 3D STRUCTURAL COMPILATION"):
        st.info(f"Processing command: '{command}'... Generating holographic telemetry array.")
        
        fig = go.Figure()
        
        if component == "Aero Spoiler Array":
            # Parabolic wing profile
            u = np.linspace(-2, 2, 20)
            v = np.linspace(-1, 1, 20)
            U, V = np.meshgrid(u, v)
            X = scale_factor * U
            Y = scale_factor * V
            Z = scale_factor * 0.15 * (U**2 - V**2)
            fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', showscale=False))
            
        elif component == "Supercar Wheel Rim Node":
            # Clean structural torus ring
            u = np.linspace(0, 2*np.pi, 24)
            v = np.linspace(0, 2*np.pi, 24)
            U, V = np.meshgrid(u, v)
            R, r = 2.0 * scale_factor, 0.6 * scale_factor
            X = (R + r * np.cos(V)) * np.cos(U)
            Y = (R + r * np.cos(V)) * np.sin(U)
            Z = r * np.sin(V)
            fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Cividis', showscale=False))
            
        else:
            # TRUE V10 ENGINE BLOCK MECHANICS: 10 individual, non-connected physical cylinders
            colors = ['#00FFCC', '#0099FF']
            
            for b_idx, bank in enumerate([-1, 1]): 
                angle = bank * np.pi / 5  # Sharp V-angle displacement (~36 degrees)
                
                for i in range(5): # 5 cylinders on each side
                    z_offset = (i - 2) * 1.6 * scale_factor # Linear spacing along block length
                    x_center = bank * 1.0 * scale_factor
                    
                    # Generate standalone cylinder geometry coordinates
                    u = np.linspace(0, 2*np.pi, 16)
                    h = np.linspace(-1.2, 1.2, 10)
                    
                    x_cyl, y_cyl, z_cyl = [], [], []
                    
                    for r_val in [0.45 * scale_factor]: # Cylinder radius
                        for h_val in h:
                            for angle_val in u:
                                # Apply rotation parameters to tilt the cylinders into a solid V-shape
                                nx = r_val * np.cos(angle_val)
                                ny = h_val
                                
                                rx = nx * np.cos(angle) - ny * np.sin(angle) + x_center
                                ry = nx * np.sin(angle) + ny * np.cos(angle)
                                
                                x_cyl.append(rx)
                                y_cyl.append(ry)
                                z_cyl.append(h_val + z_offset)
                    
                    # Mount each cylinder as its own individual 3D solid mesh trace
                    fig.add_trace(go.Mesh3d(
                        x=x_cyl, y=y_cyl, z=z_cyl,
                        alphahull=0,
                        color=colors[b_idx],
                        opacity=0.45,
                        name=f"Cylinder {i+1} [Bank {'A' if bank==-1 else 'B'}]",
                        showlegend=False
                    ))
                    
                    # Add bright neon wireframe borders over each cylinder profile
                    fig.add_trace(go.Scatter3d(
                        x=x_cyl[::3], y=y_cyl[::3], z=z_cyl[::3],
                        mode='lines',
                        line=dict(color='lime', width=1.5),
                        showlegend=False
                    ))

        # Core Dark Terminal Styling Layout
        fig.update_layout(
            scene=dict(
                xaxis=dict(backgroundcolor="black", gridcolor="#113311", showbackground=True, zerolinecolor="lime", title="X-VECTOR"),
                yaxis=dict(backgroundcolor="black", gridcolor="#113311", showbackground=True, zerolinecolor="lime", title="Y-VECTOR"),
                zaxis=dict(backgroundcolor="black", gridcolor="#113311", showbackground=True, zerolinecolor="lime", title="Z-BLOCK"),
                aspectmode='data'
            ),
            margin=dict(l=0, r=0, b=0, t=0),
            paper_bgcolor='black',
            plot_bgcolor='black'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.success("🤖 MATRIX PATCH COMPLETE. V10 BLOCK TELEMETRY STABLE.")

# Keep all other sub-modules running perfectly below
elif module == "🚨 Habit Tracker Grid":
    st.subheader("[+] DIGITAL HABIT TRACKER MATRIX")
    with st.expander("💾 Sync / Load Previous Progress Data"):
        uploaded_data = st.text_area("Paste your backup code string here to load past history:")
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
    st.text("Core Operational Loop: STABLE\nBandwidth Allocation: MAXIMUM\nAll nodes reporting green.")

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
