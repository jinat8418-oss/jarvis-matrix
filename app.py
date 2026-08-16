import streamlit as st
import streamlit.components.v1 as components

# --- FULLSCREEN SCI-FI CONFIGURATION ---
st.set_page_config(page_title="JARVIS OPTICAL HUD", page_icon="🌐", layout="wide")

# --- PREMIUM CINEMATIC UI STYLING ---
st.markdown("""
    <style>
    /* Remove Default Streamlit Padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 100% !important;
    }
    header, footer, #MainMenu {visibility: hidden;}
    
    body, .stApp {
        background-color: #030712 !important;
        color: #F8FAFC;
        font-family: 'Consolas', 'Courier New', monospace;
    }

    /* Sci-Fi Glow Utility Classes */
    .cyan-glow {
        color: #00D8FF;
        text-shadow: 0 0 10px rgba(0, 216, 255, 0.75), 0 0 20px rgba(0, 216, 255, 0.4);
    }
    .hud-title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        margin-bottom: 2px;
    }
    .hud-title {
        color: #F8FAFC;
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: 3px;
        text-transform: uppercase;
    }
    .hud-subtitle {
        text-align: center;
        color: #64748B;
        font-size: 0.7rem;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER WITH VECTOR OPTIC EYE ---
st.markdown("""
    <div class="hud-title-container">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#00D8FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0px 0px 6px #00D8FF);">
            <circle cx="12" cy="12" r="3"></circle>
            <path d="M3 7V5a2 2 0 0 1 2-2h2"></path>
            <path d="M17 3h2a2 2 0 0 1 2 2v2"></path>
            <path d="M21 17v2a2 2 0 0 1-2 2h-2"></path>
            <path d="M7 21H5a2 2 0 0 1-2-2v-2"></path>
        </svg>
        <span class="hud-title">JARVIS <span class="cyan-glow">VISION MATRIX</span></span>
    </div>
    <div class="hud-subtitle">SPATIAL QUANTUM SCANNER // REAL-TIME HUD TELEMETRY</div>
""", unsafe_allow_html=True)

# --- FULL VIEWPORT TENSORFLOW ENGINE ---
spatial_vision_html = """
<!-- TensorFlow.js & COCO-SSD Model CDN -->
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd"></script>

<div style="position: relative; width: 100%; max-width: 600px; margin: 0 auto; background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(0, 216, 255, 0.3); border-radius: 12px; padding: 12px; box-shadow: 0 0 25px rgba(0, 216, 255, 0.15); backdrop-filter: blur(8px);">
    
    <!-- Top System Telemetry Bar -->
    <div style="display: flex; justify-content: space-between; color: #94A3B8; font-size: 0.7rem; letter-spacing: 1px; margin-bottom: 8px; font-weight: bold;">
        <span id="aiStatus" style="color: #00D8FF;">CORE: LOADING MODEL...</span>
        <span id="targetStatus" style="color: #64748B;">STATUS: STANDBY</span>
    </div>

    <!-- Full Aspect Viewport -->
    <div id="viewport" style="position: relative; width: 100%; height: 60vh; max-height: 480px; min-height: 340px; overflow: hidden; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.1); background: #000; touch-action: none;">
        <video id="webcam" autoplay playsinline muted style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease-out;"></video>
        <canvas id="arCanvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></canvas>
    </div>

    <!-- Action Bar -->
    <div style="margin-top: 12px; display: flex; gap: 10px; justify-content: center;">
        <button id="startCamBtn" style="background: linear-gradient(135deg, #0072FF 0%, #00D8FF 100%); color: #030712; border: none; padding: 12px 24px; font-weight: 800; font-family: monospace; border-radius: 6px; cursor: pointer; letter-spacing: 1.5px; box-shadow: 0 0 15px rgba(0, 216, 255, 0.4);">
            INITIALIZE MATRIX SCAN
        </button>
        <button id="resetScanBtn" style="background: rgba(15, 23, 42, 0.8); color: #00D8FF; border: 1px solid #00D8FF; padding: 12px 20px; font-weight: 700; font-family: monospace; border-radius: 6px; cursor: pointer; display: none; letter-spacing: 1px; box-shadow: 0 0 10px rgba(0, 216, 255, 0.2);">
            ⚡ TARGET NEW OBJECT
        </button>
    </div>
</div>

<script>
    const video = document.getElementById('webcam');
    const canvas = document.getElementById('arCanvas');
    const ctx = canvas.getContext('2d');
    const startBtn = document.getElementById('startCamBtn');
    const resetBtn = document.getElementById('resetScanBtn');
    const aiStatus = document.getElementById('aiStatus');
    const statusText = document.getElementById('targetStatus');
    const viewport = document.getElementById('viewport');

    let model = null;
    let isScanning = false;
    let lockedDetection = null;

    cocoSsd.load().then(loadedModel => {
        model = loadedModel;
        aiStatus.textContent = "CORE: NEURAL ENGINE ACTIVE";
        aiStatus.style.color = "#00D8FF";
    });

    function syncCanvas() {
        canvas.width = viewport.clientWidth;
        canvas.height = viewport.clientHeight;
    }

    startBtn.addEventListener('click', async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } });
            video.srcObject = stream;
            video.onloadedmetadata = () => {
                syncCanvas();
                isScanning = true;
                startBtn.style.display = 'none';
                resetBtn.style.display = 'inline-block';
                statusText.textContent = "STATUS: SEARCHING...";
                statusText.style.color = "#00D8FF";
                detectObjects();
            };
        } catch (err) {
            alert("Camera Access Denied: Enable camera permissions to project HUD.");
        }
    });

    resetBtn.addEventListener('click', () => {
        lockedDetection = null;
        video.style.transform = "scale(1)";
        statusText.textContent = "STATUS: SEARCHING...";
        statusText.style.color = "#00D8FF";
    });

    canvas.addEventListener('pointerdown', (e) => {
        const rect = canvas.getBoundingClientRect();
        const touchX = e.clientX - rect.left;
        const touchY = e.clientY - rect.top;
        
        lockedDetection = {
            bbox: [touchX - 60, touchY - 60, 120, 120],
            class: "MANUAL TARGET",
            score: 0.99
        };
        triggerZoomAndSearch(touchX, touchY);
    });

    async function detectObjects() {
        if (!isScanning) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        if (model && !lockedDetection) {
            const predictions = await model.detect(video);
            if (predictions.length > 0) {
                const best = predictions[0];
                if (best.score > 0.45) {
                    lockedDetection = best;
                    const [bx, by, bw, bh] = best.bbox;
                    triggerZoomAndSearch(bx + bw / 2, by + bh / 2);
                }
            }
        }

        if (lockedDetection) {
            drawLockFrame(lockedDetection);
        }

        requestAnimationFrame(detectObjects);
    }

    function triggerZoomAndSearch(centerX, centerY) {
        statusText.textContent = "STATUS: LOCK ENGAGED";
        statusText.style.color = "#38BDF8";
        
        video.style.transformOrigin = `${centerX}px ${centerY}px`;
        video.style.transform = "scale(1.2)";
    }

    function drawLockFrame(det) {
        const scaleX = canvas.width / video.videoWidth || 1;
        const scaleY = canvas.height / video.videoHeight || 1;
        
        const x = det.bbox[0] * scaleX;
        const y = det.bbox[1] * scaleY;
        const w = det.bbox[2] * scaleX;
        const h = det.bbox[3] * scaleY;

        // 1. Futuristic Bounding Stroke Corner Reticles
        const corner = 18;
        ctx.strokeStyle = "#00D8FF";
        ctx.lineWidth = 3;
        ctx.shadowBlur = 12;
        ctx.shadowColor = "#00D8FF";

        // Draw HUD Bracket Corners
        ctx.beginPath();
        // Top Left
        ctx.moveTo(x, y + corner); ctx.lineTo(x, y); ctx.lineTo(x + corner, y);
        // Top Right
        ctx.moveTo(x + w - corner, y); ctx.lineTo(x + w, y); ctx.lineTo(x + w, y + corner);
        // Bottom Left
        ctx.moveTo(x, y + h - corner); ctx.lineTo(x, y + h); ctx.lineTo(x + corner, y + h);
        // Bottom Right
        ctx.moveTo(x + w - corner, y + h); ctx.lineTo(x + w, y + h); ctx.lineTo(x + w, y + h - corner);
        ctx.stroke();

        // Crosshairs in Center
        const cx = x + w/2;
        const cy = y + h/2;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(cx - 8, cy); ctx.lineTo(cx + 8, cy);
        ctx.moveTo(cx, cy - 8); ctx.lineTo(cx, cy + 8);
        ctx.stroke();

        // 2. Futuristic Arc HUD Telemetry Box
        const hudX = Math.min(x + w + 12, canvas.width - 160);
        const hudY = Math.max(y, 10);
        const hudW = 150;
        const hudH = 80;

        // Connector Line
        ctx.beginPath();
        ctx.moveTo(x + w, cy);
        ctx.lineTo(hudX, cy);
        ctx.strokeStyle = "rgba(0, 216, 255, 0.6)";
        ctx.stroke();

        // Glassmorphism HUD Panel Background
        ctx.fillStyle = "rgba(3, 7, 18, 0.88)";
        ctx.fillRect(hudX, hudY, hudW, hudH);
        ctx.strokeStyle = "#00D8FF";
        ctx.lineWidth = 1;
        ctx.strokeRect(hudX, hudY, hudW, hudH);

        // Telemetry Data Text
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#94A3B8";
        ctx.font = "bold 9px 'Consolas', monospace";
        ctx.fillText("TARGET IDENTIFIED:", hudX + 8, hudY + 18);

        ctx.fillStyle = "#F8FAFC";
        ctx.font = "bold 12px 'Consolas', monospace";
        ctx.fillText(det.class.toUpperCase(), hudX + 8, hudY + 36);

        ctx.fillStyle = "#00D8FF";
        ctx.font = "9px 'Consolas', monospace";
        ctx.fillText(`ACCURACY: ${(det.score * 100).toFixed(1)}%`, hudX + 8, hudY + 52);
        
        ctx.fillStyle = "#38BDF8";
        ctx.fillText("NET: Indexing Logs...", hudX + 8, hudY + 68);
    }
</script>
"""

components.html(spatial_vision_html, height=560)
