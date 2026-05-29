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
        
