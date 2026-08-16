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
st.markdown('<div class="hud-sub">REAL-TIME AI OBJECT DETECTION & TELEMETRY SEARCH</div>', unsafe_allow_html=True)

# --- REAL-TIME AI CAMERA ENGINE WITH COCO-SSD ---
spatial_vision_html = """
<!-- TensorFlow.js & COCO-SSD Model CDN -->
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd"></script>

<div style="position: relative; width: 100%; max-width: 480px; margin: 0 auto; background: #0b0f19; border: 1px solid #00f3ff; border-radius: 10px; padding: 10px; box-shadow: 0 0 15px rgba(0,243,255,0.2); font-family: monospace;">
    
    <!-- Status Bar -->
    <div style="display: flex; justify-content: space-between; color: #39ff14; font-size: 0.75rem; margin-bottom: 8px;">
        <span id="aiStatus">AI: LOADING MODEL...</span>
        <span id="targetStatus">STATUS: OFF</span>
    </div>

    <!-- Viewport Container -->
    <div id="viewport" style="position: relative; width: 100%; height: 320px; overflow: hidden; border-radius: 6px; border: 1px solid rgba(0,243,255,0.3); touch-action: none;">
        <video id="webcam" autoplay playsinline muted style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;"></video>
        <canvas id="arCanvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></canvas>
    </div>

    <!-- Controls -->
    <div style="margin-top: 12px; display: flex; gap: 8px; justify-content: center;">
        <button id="startCamBtn" style="background: #05070a; color: #00f3ff; border: 1px solid #00f3ff; padding: 10px 16px; font-weight: bold; font-family: monospace; border-radius: 5px; cursor: pointer;">
            START SCANNER
        </button>
        <button id="resetScanBtn" style="background: #05070a; color: #39ff14; border: 1px solid #39ff14; padding: 10px 16px; font-weight: bold; font-family: monospace; border-radius: 5px; cursor: pointer; display: none;">
            ⚡ SCAN NEW TARGET
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

    // Load Real TensorFlow AI Model
    cocoSsd.load().then(loadedModel => {
        model = loadedModel;
        aiStatus.textContent = "AI: ONLINE (COCO-SSD)";
        aiStatus.style.color = "#00f3ff";
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
                statusText.textContent = "STATUS: SCANNING...";
                detectObjects();
            };
        } catch (err) {
            alert("Camera access denied or unavailable.");
        }
    });

    resetBtn.addEventListener('click', () => {
        lockedDetection = null;
        video.style.transform = "scale(1)";
        statusText.textContent = "STATUS: SCANNING...";
        statusText.style.color = "#39ff14";
    });

    // Touch interaction to manual override target
    canvas.addEventListener('pointerdown', (e) => {
        const rect = canvas.getBoundingClientRect();
        const touchX = e.clientX - rect.left;
        const touchY = e.clientY - rect.top;
        
        lockedDetection = {
            bbox: [touchX - 50, touchY - 50, 100, 100],
            class: "MANUAL SELECTION",
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
                // Pick highest confidence target
                const best = predictions[0];
                if (best.score > 0.5) {
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
        statusText.textContent = "STATUS: TARGET LOCKED";
        statusText.style.color = "#00f3ff";
        
        // Digital Auto-Zoom Effect
        video.style.transformOrigin = `${centerX}px ${centerY}px`;
        video.style.transform = "scale(1.25)";
    }

    function drawLockFrame(det) {
        // Adjust coordinates relative to current canvas size
        const scaleX = canvas.width / video.videoWidth || 1;
        const scaleY = canvas.height / video.videoHeight || 1;
        
        const x = det.bbox[0] * scaleX;
        const y = det.bbox[1] * scaleY;
        const w = det.bbox[2] * scaleX;
        const h = det.bbox[3] * scaleY;

        // 1. Draw Green Stroke Outline Around Object
        ctx.strokeStyle = "#39ff14";
        ctx.lineWidth = 2.5;
        ctx.shadowBlur = 8;
        ctx.shadowColor = "#39ff14";
        ctx.strokeRect(x, y, w, h);

        // 2. HUD Search Window
        const hudX = Math.min(x + w + 10, canvas.width - 150);
        const hudY = Math.max(y, 10);
        
        ctx.fillStyle = "rgba(6, 8, 14, 0.9)";
        ctx.fillRect(hudX, hudY, 140, 75);
        ctx.strokeStyle = "#00f3ff";
        ctx.strokeRect(hudX, hudY, 140, 75);

        ctx.shadowBlur = 0;
        ctx.fillStyle = "#39ff14";
        ctx.font = "bold 9px monospace";
        ctx.fillText("🔍 AI IDENTIFIED:", hudX + 6, hudY + 16);

        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 11px monospace";
        ctx.fillText(det.class.toUpperCase(), hudX + 6, hudY + 34);

        ctx.fillStyle = "#00f3ff";
        ctx.font = "8px monospace";
        ctx.fillText(`CONF: ${(det.score * 100).toFixed(1)}%`, hudX + 6, hudY + 50);
        ctx.fillText("WEB: Indexing Data...", hudX + 6, hudY + 64);
    }
</script>
"""

components.html(spatial_vision_html, height=480)

st.markdown("---")
st.write("📟 SYSTEM ARCHITECTURE: SPATIAL VISION MATRIX v2.0")
