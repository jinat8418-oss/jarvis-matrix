import streamlit as st
import streamlit.components.v1 as components

# Core Configuration
st.set_page_config(page_title="JINAT OS", page_icon="📟", layout="centered")

# --- CYBERPUNK NEON GLOW STYLE ENGINE ---
st.markdown("""
    <style>
    .stApp { background-color: #0d0e15; color: #e0e6ed; }
    .neon-title {
        font-family: 'Courier New', monospace;
        color: #00f3ff;
        text-shadow: 0 0 10px #00f3ff;
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
    section[data-testid="stSidebar"] { background-color: #070913 !important; border-right: 1px solid #39ff14; }
    </style>
""", unsafe_allow_html=True)

# Render Branding Headers
st.markdown('<div class="neon-title">📟 JINAT OS : CORE TERMINAL</div>', unsafe_allow_html=True)
st.markdown('<div class="neon-subtext">SYSTEM DESIGN UNLOCKED // ARCHITECT: JINAT</div>', unsafe_allow_html=True)
st.markdown("---")

module = st.sidebar.radio("CHOOSE SYSTEM MODULE:", [
    "🌐 System Mainframe",
    "🔦 Hardware Pulse Override"
])

if module == "🌐 System Mainframe":
    st.write("Welcome to the main terminal workspace. Use the sidebar menu to launch the hardware testing suite.")

elif module == "🔦 Hardware Pulse Override":
    st.subheader("📡 HARDWARE APERTURE TELEMETRY")
    st.write("This module utilizes the HTML5 Media Capture interface to send manual override pulses to the device's physical flashlight.")
    st.info("💡 Note: Open this module on a phone, tap the button below, and allow camera access to toggle the hardware lighting array.")
    
    # Embedded HTML5 Canvas with Native Hardware Torch JavaScript Engine
    hardware_js_component = """
    <div style="background-color: #121622; border: 1px solid #00f3ff; border-radius: 8px; padding: 20px; text-align: center; font-family: monospace;">
        <h4 style="color: #00f3ff; margin-top: 0;">⚡ HARDWARE OVERRIDE TRIGGER</h4>
        <p style="color: #8899a6; font-size: 0.85rem;">Status: Waiting for initialization signal...</p>
        
        <button id="torchBtn" style="background-color: #05070a; color: #39ff14; border: 1px solid #39ff14; padding: 12px 24px; font-weight: bold; font-family: monospace; border-radius: 4px; cursor: pointer; box-shadow: 0 0 10px rgba(57, 255, 20, 0.2);">
            TRIGGER PHYSICAL TORCH PULSE
        </button>
        
        <p id="errLog" style="color: #ff0055; font-size: 0.8rem; margin-top: 10px;"></p>
    </div>

    <script>
        let streamTrack = null;
        let isLightOn = false;
        const btn = document.getElementById('torchBtn');
        const errLog = document.getElementById('errLog');

        btn.addEventListener('click', async () => {
            try {
                if (!streamTrack) {
                    const constraints = { video: { facingMode: 'environment' } };
                    const stream = await navigator.mediaDevices.getUserMedia(constraints);
                    streamTrack = stream.getVideoTracks()[0];
                }

                if (streamTrack && 'applyConstraints' in streamTrack) {
                    isLightOn = !isLightOn;
                    await streamTrack.applyConstraints({
                        advanced: [{ torch: isLightOn }]
                    });
                    
                    btn.textContent = isLightOn ? "TERMINATE TORCH PULSE" : "TRIGGER PHYSICAL TORCH PULSE";
                    btn.style.color = isLightOn ? "#ff0055" : "#39ff14";
                    btn.style.borderColor = isLightOn ? "#ff0055" : "#39ff14";
                } else {
                    errLog.textContent = "Error: Torch control constraint not supported on this browser version.";
                }
            } catch (err) {
                errLog.textContent = "Hardware Link Interrupted: Ensure permission is allowed.";
                console.error(err);
            }
        });
    </script>
    """
    
    components.html(hardware_js_component, height=200)
    
