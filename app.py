
import streamlit as st
import streamlit.components.v1 as components

# --- FULLSCREEN CONFIGURATION ---
st.set_page_config(page_title="JINAT VISION MATRIX", page_icon="⚡", layout="wide")

# --- PREMIUM WHITE & CYAN HUD STYLING ---
st.markdown("""
    <style>
    .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 100% !important;
    }
    header, footer, #MainMenu {visibility: hidden;}
    
    body, .stApp {
        background-color: #F1F5F9 !important;
        color: #0F172A;
        font-family: 'Consolas', 'Courier New', monospace;
    }

    .hud-title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        margin-bottom: 2px;
    }
    .hud-title {
        color: #0F172A;
        font-size: 1.3rem;
        font-weight: 900;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    .blue-glow {
        color: #2563EB;
        text-shadow: 0 0 10px rgba(37, 99, 235, 0.3);
    }
    .hud-subtitle {
        text-align: center;
        color: #64748B;
        font-size: 0.7rem;
        letter-spacing: 2px;
        margin-bottom: 10px;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER WITH USER BRANDING ---
st.markdown("""
    <div class="hud-title-container">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="3"></circle>
            <path d="M3 7V5a2 2 0 0 1 2-2h2"></path>
            <path d="M17 3h2a2 2 0 0 1 2 2v2"></path>
            <path d="M21 17v2a2 2 0 0 1-2 2h-2"></path>
            <path d="M7 21H5a2 2 0 0 1-2-2v-2"></path>
        </svg>
        <span class="hud-title">JARVIS <span class="blue-glow">VISION MATRIX</span></span>
    </div>
    <div class="hud-subtitle">OPERATOR: JINAT // DYNAMIC SPATIAL TELEMETRY</div>
""", unsafe_allow_html=True)

# --- FULL VIEWPORT TENSORFLOW ENGINE ---
spatial_vision_html = """
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd"></script>

<div style="position: relative; width: 100%; max-width: 600px; margin: 0 auto; background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 14px; padding: 12px; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08); font-family: monospace;">
    
    <!-- Top Operator Telemetry Bar -->
    <div style="display: flex; justify-content: space-between; color: #475569; font-size: 0.7rem; letter-spacing: 1px; margin-bottom: 8px; font-weight: bold;">
        <span id="aiStatus" style="color: #2563EB;">SYS: JINAT_CORE_READY</span>
        <span id="targetStatus" style="color: #64748B;">STATUS: STANDBY</span>
    </div>

    <!-- Viewport Container with Dynamic Zoom Frame -->
    <div id="viewport" style="position: relative; width: 100%; height: 58vh; max-height: 460px; min-height: 320px; overflow: hidden; border-radius: 10px; border: 1px solid #E2E8F0; background: #000; touch-action: none;">
        <div id="zoomContainer" style="width: 100%; height: 100%; transform-origin: center; transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
            <video id="webcam" autoplay playsinline muted style="width: 100%; height: 100%; object-fit: cover;"></video>
            <canvas id="arCanvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></canvas>
        </div>
    </div>

    <!-- Control Buttons -->
    <div style="margin-top: 12px; display: flex; gap: 10px; justify-content: center;">
        <button id="startCamBtn" style="background: #2563EB; color: #FFFFFF; border: none; padding: 12px 24px; font-weight: 800; font-family: monospace; border-radius: 8px; cursor: pointer; letter-spacing: 1.5px; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);">
            INITIALIZE SCANNER
        </button>
        <button id="resetScanBtn" style="background: #F8FAFC; color: #2563EB; border: 1.5px solid #2563EB; padding: 12px 20px; font-weight: 700; font-family: monospace; border-radius: 8px; cursor: pointer; display: none; letter-spacing: 1px;">
            ⚡ RESET / SCAN NEW
        </button>
    </div>
</div>

<script>
    const video = document.getElementById('webcam');
    const canvas = document.getElementById('arCanvas');
    const ctx = canvas.getContext('2d');
    const zoomContainer = document.getElementById('zoomContainer');
    const startBtn = document.getElementById('startCamBtn');
    const resetBtn = document.getElementById('resetScanBtn');
    const aiStatus = document.getElementById('aiStatus');
    const statusText = document.getElementById('targetStatus');
    const viewport = document.getElementById('viewport');

    let model = null;
    let isScanning = false;
    let lockedDetection = null;

    // Class Color Mapping Engine
    function getColorForClass(className) {
        const cls = className.toLowerCase();
        if (cls.includes('book') || cls.includes('paper')) return '#10B981'; // Emerald Green
        if (cls.includes('laptop') || cls.includes('tv') || cls.includes('cell phone') || cls.includes('calculator')) return '#00D8FF'; // Cyber Cyan
        if (cls.includes('bag') || cls.includes('backpack') || cls.includes('suitcase')) return '#8B5CF6'; // Violet
        if (cls.includes('manual')) return '#F59E0B'; // Amber
        return '#2563EB'; // Royal Blue Default
    }

    cocoSsd.load().then(loadedModel => {
        model = loadedModel;
        aiStatus.textContent = "SYS: JINAT_AI_ONLINE";
        aiStatus.style.color = "#2563EB";
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
                statusText.style.color = "#2563EB";
                detectObjects();
            };
        } catch (err) {
            alert("Camera Access Denied.");
        }
    });

    resetBtn.addEventListener('click', () => {
        lockedDetection = null;
        zoomContainer.style.transform = "scale(1)";
        zoomContainer.style.transformOrigin = "center";
        statusText.textContent = "STATUS: SEARCHING...";
        statusText.style.color = "#2563EB";
    });

    // Tap to Focus & Manual Target Search
    canvas.addEventListener('pointerdown', (e) => {
        const rect = canvas.getBoundingClientRect();
        const touchX = e.clientX - rect.left;
        const touchY = e.clientY - rect.top;
        
        lockedDetection = {
            bbox: [touchX - 50, touchY - 50, 100, 100],
            class: "MANUAL TARGET",
            score: 0.98,
            isManual: true
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
                if (best.score > 0.40) {
                    lockedDetection = best;
                    const [bx, by, bw, bh] = best.bbox;
                    
                    // Remap misclassifications on desktop/paper items
                    if (best.class === 'laptop' && bw < 180) {
                        lockedDetection.class = 'CALCULATOR / DEVICE';
                    }
                    
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
        statusText.textContent = "STATUS: TARGET LOCKED";
        statusText.style.color = "#10B981";
        
        // Physical Canvas Zoom directly onto coordinates
        const originX = (centerX / canvas.width) * 100;
        const originY = (centerY / canvas.height) * 100;
        zoomContainer.style.transformOrigin = `${originX}% ${originY}%`;
        zoomContainer.style.transform = "scale(1.25)";
    }

    function drawLockFrame(det) {
        const scaleX = canvas.width / video.videoWidth || 1;
        const scaleY = canvas.height / video.videoHeight || 1;
        
        const x = det.bbox[0] * scaleX;
        const y = det.bbox[1] * scaleY;
        const w = det.bbox[2] * scaleX;
        const h = det.bbox[3] * scaleY;

        const dynamicColor = getColorForClass(det.class);

        // Dynamic Color Bounding Brackets
        const corner = 16;
        ctx.strokeStyle = dynamicColor;
        ctx.lineWidth = 3;
        ctx.shadowBlur = 10;
        ctx.shadowColor = dynamicColor;

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

        // HUD Info Panel
        const hudX = Math.min(x + w + 10, canvas.width - 150);
        const hudY = Math.max(y, 10);
        const hudW = 140;
        const hudH = 75;

        ctx.fillStyle = "rgba(15, 23, 42, 0.92)";
        ctx.fillRect(hudX, hudY, hudW, hudH);
        ctx.strokeStyle = dynamicColor;
        ctx.lineWidth = 1.5;
        ctx.strokeRect(hudX, hudY, hudW, hudH);

        ctx.shadowBlur = 0;
        ctx.fillStyle = "#94A3B8";
        ctx.font = "bold 9px 'Consolas', monospace";
        ctx.fillText("TARGET ACQUIRED:", hudX + 8, hudY + 18);

        ctx.fillStyle = "#FFFFFF";
        ctx.font = "bold 11px 'Consolas', monospace";
        ctx.fillText(det.class.toUpperCase(), hudX + 8, hudY + 36);

        ctx.fillStyle = dynamicColor;
        ctx.font = "9px 'Consolas', monospace";
        ctx.fillText(`CONF: ${(det.score * 100).toFixed(1)}%`, hudX + 8, hudY + 52);
        
        ctx.fillStyle = "#38BDF8";
        ctx.fillText(det.isManual ? "MODE: TAP SEARCH" : "NET: SEARCH COMPLETE", hudX + 8, hudY + 66);
    }
</script>
"""

components.html(spatial_vision_html, height=540)

        
        
        
        
        