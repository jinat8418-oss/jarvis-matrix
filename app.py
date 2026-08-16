import streamlit as st
import streamlit.components.v1 as components

# --- CORE PAGE CONFIGURATION ---
st.set_page_config(page_title="JARVIS SPATIAL VISION", page_icon="👁️", layout="centered")

# --- CYBERPUNK AR INTERFACE STYLING ---
st.markdown("""
    <style>
    .stApp {
        background-color: #06080e;
        color: #00f3ff;
        font-family: 'Courier New', monospace;
    }
    .hud-header {
        text-align: center;
        color: #00f3ff;
        text-shadow: 0 0 12px #00f3ff;
        font-weight: bold;
        font-size: 1.8rem;
        margin-bottom: 2px;
    }
    .hud-sub {
        text-align: center;
        color: #39ff14;
        text-shadow: 0 0 8px rgba(57, 255, 20, 0.5);
        font-size: 0.8rem;
        letter-spacing: 2px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="hud-header">👁️ JARVIS SPATIAL SEARCH GRID</div>', unsafe_allow_html=True)
st.markdown('<div class="hud-sub">REAL-TIME OBJECT DETECTION & TELEMETRY SEARCH</div>', unsafe_allow_html=True)

# --- REAL-TIME CAMERA + CANVAS ANALYSIS ENGINE ---
spatial_vision_html = """
<div style="position: relative; width: 100%; max-width: 480px; margin: 0 auto; background: #0b0f19; border: 1px solid #00f3ff; border-radius: 10px; padding: 10px; box-shadow: 0 0 15px rgba(0,243,255,0.2); font-family: monospace;">
    
    <!-- Status Bar -->
    <div style="display: flex; justify-content: space-between; color: #39ff14; font-size: 0.75rem; margin-bottom: 8px;">
        <span>SYS: ONLINE</span>
        <span id="targetStatus">STATUS: SEARCHING FOR TARGET</span>
    </div>

    <!-- Viewport Container -->
    <div style="position: relative; width: 100%; height: 320px; overflow: hidden; border-radius: 6px; border: 1px solid rgba(0,243,255,0.3);">
        <video id="webcam" autoplay playsinline muted style="width: 100%; height: 100%; object-fit: cover;"></video>
        <canvas id="arCanvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;"></canvas>
    </div>

    <!-- Controls -->
    <div style="margin-top: 12px; text-align: center;">
        <button id="startCamBtn" style="background: #05070a; color: #00f3ff; border: 1px solid #00f3ff; padding: 10px 20px; font-weight: bold; font-family: monospace; border-radius: 5px; cursor: pointer; box-shadow: 0 0 8px rgba(0,243,255,0.3);">
            INITIALIZE OPTICAL SCANNER
        </button>
    </div>
</div>

<script>
    const video = document.getElementById('webcam');
    const canvas = document.getElementById('arCanvas');
    const ctx = canvas.getContext('2d');
    const startBtn = document.getElementById('startCamBtn');
    const statusText = document.getElementById('targetStatus');

    let isScanning = false;
    let scanProgress = 0;
    let targetFound = false;
    let zoomLevel = 1.0;

    // Adjust canvas dimensions internal resolution
    function syncCanvasSize() {
        canvas.width = video.clientWidth || 340;
        canvas.height = video.clientHeight || 320;
    }

    startBtn.addEventListener('click', async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({
                video: { facingMode: 'environment' }
            });
            video.srcObject = stream;
            video.onloadedmetadata = () => {
                syncCanvasSize();
                isScanning = true;
                startBtn.style.display = 'none';
                statusText.textContent = "STATUS: LOCKING TARGET...";
                requestAnimationFrame(renderARLoop);
            };
        } catch (err) {
            alert("Camera Access Required: Please allow camera permissions to initialize optical scanner.");
        }
    });

    // Simulated Knowledge Base for Search Telemetry
    const mockDb = [
        { name: "HIGH-PERFORMANCE CORE", category: "ELECTRONICS / HARDWARE", confidence: "98.4%", query: "Indexing Architecture Metrics..." },
        { name: "OPTICAL SENSOR ASSEMBLY", category: "HARDWARE / CAMERA", confidence: "96.1%", query: "Searching Global Telemetry..." },
        { name: "SMART AGENT INTERFACE", category: "AI / EMBEDDED SYSTEM", confidence: "99.2%", query: "Retrieving Web Search Logs..." }
    ];
    
    let activeData = mockDb[0];

    function renderARLoop() {
        if (!isScanning) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        const cx = canvas.width / 2;
        const cy = canvas.height / 2;
        const boxWidth = 140 * zoomLevel;
        const boxHeight = 140 * zoomLevel;
        const x = cx - (boxWidth / 2);
        const y = cy - (boxHeight / 2);

        // Dynamic targeting effect (Pulse / Zoom)
        if (scanProgress < 100) {
            scanProgress += 0.8;
            if (scanProgress > 50 && zoomLevel < 1.15) {
                zoomLevel += 0.003; // Smooth digital auto-zoom feel
            }
        } else {
            targetFound = true;
            statusText.textContent = "STATUS: TARGET LOCKED";
            statusText.style.color = "#00f3ff";
        }

        // 1. Draw Bounding Stroke Outline
        ctx.strokeStyle = targetFound ? "#39ff14" : "#00f3ff";
        ctx.lineWidth = 2;
        ctx.shadowBlur = 10;
        ctx.shadowColor = targetFound ? "#39ff14" : "#00f3ff";

        // Draw Corner Reticles
        const cornerLen = 18;
        // Top-Left
        ctx.beginPath(); ctx.moveTo(x, y + cornerLen); ctx.lineTo(x, y); ctx.lineTo(x + cornerLen, y); ctx.stroke();
        // Top-Right
        ctx.beginPath(); ctx.moveTo(x + boxWidth - cornerLen, y); ctx.lineTo(x + boxWidth, y); ctx.lineTo(x + boxWidth, y + cornerLen); ctx.stroke();
        // Bottom-Left
        ctx.beginPath(); ctx.moveTo(x, y + boxHeight - cornerLen); ctx.lineTo(x, y + boxHeight); ctx.lineTo(x + cornerLen, y + boxHeight); ctx.stroke();
        // Bottom-Right
        ctx.beginPath(); ctx.moveTo(x + boxWidth - cornerLen, y + boxHeight); ctx.lineTo(x + boxWidth, y + boxHeight); ctx.lineTo(x + boxWidth, y + boxHeight - cornerLen); ctx.stroke();

        // 2. Draw Sci-Fi HUD Search Box (Positioned to the right of target)
        if (targetFound) {
            const hudX = x + boxWidth + 12;
            const hudY = y - 10;
            const hudW = 150;
            const hudH = 110;

            // Connector Line from Box to Search Panel
            ctx.beginPath();
            ctx.moveTo(x + boxWidth, cy);
            ctx.lineTo(hudX, cy);
            ctx.strokeStyle = "#00f3ff";
            ctx.stroke();

            // Background Panel
            ctx.fillStyle = "rgba(10, 15, 25, 0.85)";
            ctx.fillRect(hudX, hudY, hudW, hudH);
            ctx.strokeRect(hudX, hudY, hudW, hudH);

            // Telemetry Text
            ctx.shadowBlur = 0;
            ctx.fillStyle = "#39ff14";
            ctx.font = "bold 9px monospace";
            ctx.fillText("🔍 SEARCH RESULTS:", hudX + 8, hudY + 18);

            ctx.fillStyle = "#ffffff";
            ctx.font = "bold 10px monospace";
            ctx.fillText(activeData.name, hudX + 8, hudY + 36);

            ctx.fillStyle = "#00f3ff";
            ctx.font = "8px monospace";
            ctx.fillText(`CLASS: ${activeData.category}`, hudX + 8, hudY + 54);
            ctx.fillText(`CONF: ${activeData.confidence}`, hudX + 8, hudY + 68);

            ctx.fillStyle = "#8899a6";
            ctx.fillText("WEB: Query Complete", hudX + 8, hudY + 88);
            ctx.fillText("STATUS: Indexing...", hudX + 8, hudY + 98);
        } else {
            // Scanning Line Animation
            const scanLineY = y + ((scanProgress / 100) * boxHeight);
            ctx.beginPath();
            ctx.moveTo(x, scanLineY);
            ctx.lineTo(x + boxWidth, scanLineY);
            ctx.strokeStyle = "rgba(57, 255, 20, 0.8)";
            ctx.stroke();
        }

        requestAnimationFrame(renderARLoop);
    }
</script>
"""

components.html(spatial_vision_html, height=460)

st.markdown("---")
st.write("📟 SYSTEM ARCHITECTURE: SPATIAL VISION MATRIX v1.0")
