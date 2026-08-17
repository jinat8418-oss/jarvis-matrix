import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="JINAT VISION MATRIX", page_icon="⚡", layout="wide")

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

spatial_vision_html = """
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.10.0/dist/tf.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd@2.2.3/dist/coco-ssd.min.js"></script>

<div style="position: relative; width: 100%; max-width: 600px; margin: 0 auto; background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 14px; padding: 12px; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08); font-family: monospace;">
    
    <div style="display: flex; justify-content: space-between; align-items: center; color: #475569; font-size: 0.7rem; letter-spacing: 1px; margin-bottom: 8px; font-weight: bold;">
        <span id="aiStatus" style="color: #2563EB;">SYS: JINAT_CORE_READY</span>
        
        <div style="background: rgba(15, 23, 42, 0.95); border: 1.5px solid #00D8FF; border-radius: 6px; padding: 4px 8px; box-shadow: 0 0 8px rgba(0, 216, 255, 0.4); display: flex; align-items: center; gap: 8px;">
            <span style="color: #00D8FF; font-size: 0.65rem;">SESSION_NODES: <span id="userCount" style="color: #FFFFFF; font-weight: 900;">1</span></span>
            <span style="color: #CBD5E1;">|</span>
            <span style="color: #00D8FF; font-size: 0.65rem;">LAST: <span id="badgeLastTarget" style="color: #10B981; font-weight: 800;">NONE</span></span>
        </div>
    </div>

    <div id="viewport" style="position: relative; width: 100%; height: 50vh; max-height: 420px; min-height: 300px; overflow: hidden; border-radius: 10px; border: 1px solid #E2E8F0; background: #000; touch-action: none;">
        <div id="zoomContainer" style="width: 100%; height: 100%; transform-origin: center; transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
            <video id="webcam" autoplay playsinline muted style="width: 100%; height: 100%; object-fit: cover;"></video>
            <canvas id="arCanvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></canvas>
        </div>

        <div id="hudCard" style="display: none; position: absolute; bottom: 12px; left: 12px; right: 12px; background: rgba(15, 23, 42, 0.92); border: 1.5px solid #2563EB; border-radius: 8px; padding: 10px 14px; color: #FFFFFF; box-shadow: 0 4px 15px rgba(0,0,0,0.3); backdrop-filter: blur(4px); pointer-events: none; z-index: 10;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                <span style="font-size: 0.65rem; color: #94A3B8; font-weight: bold; letter-spacing: 1px;">TARGET ACQUIRED</span>
                <span id="hudConf" style="font-size: 0.7rem; color: #2563EB; font-weight: bold;">CONF: 0.0%</span>
            </div>
            <div id="hudClass" style="font-size: 1.1rem; font-weight: 900; letter-spacing: 1px; color: #FFFFFF;">UNKNOWN</div>
            <div id="hudMode" style="font-size: 0.65rem; color: #38BDF8; margin-top: 2px;">NET: SEARCH COMPLETE</div>
        </div>
    </div>

    <div style="margin-top: 10px; display: flex; gap: 10px; justify-content: center;">
        <button id="startCamBtn" style="background: #2563EB; color: #FFFFFF; border: none; padding: 10px 20px; font-weight: 800; font-family: monospace; border-radius: 8px; cursor: pointer; letter-spacing: 1.5px; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);">
            INITIALIZE SCANNER
        </button>
        <button id="resetScanBtn" style="background: #F8FAFC; color: #2563EB; border: 1.5px solid #2563EB; padding: 10px 18px; font-weight: 700; font-family: monospace; border-radius: 8px; cursor: pointer; display: none; letter-spacing: 1px;">
            ⚡ RESET / SCAN NEW
        </button>
    </div>

    <div style="margin-top: 14px; border-top: 1px dashed #CBD5E1; padding-top: 10px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-size: 0.65rem; color: #00D8FF; font-weight: bold; letter-spacing: 1px; background: #0F172A; padding: 2px 6px; border-radius: 4px;">SYSTEM LOG // TELEMETRY REPOSITORY</span>
            <span id="logCount" style="font-size: 0.65rem; color: #64748B;">ENTRIES: 0</span>
        </div>
        
        <div id="historyTableContainer" style="max-height: 120px; overflow-y: auto; border: 1px solid #E2E8F0; border-radius: 6px; background: #F8FAFC;">
            <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.65rem; color: #334155;">
                <thead>
                    <tr style="background: #0F172A; color: #00D8FF; border-bottom: 1px solid #334155;">
                        <th style="padding: 6px;">TIME</th>
                        <th style="padding: 6px;">OBJECT CLASS</th>
                        <th style="padding: 6px;">ACCURACY</th>
                        <th style="padding: 6px;">MODE</th>
                    </tr>
                </thead>
                <tbody id="historyTableBody">
                    <tr id="emptyRow">
                        <td colspan="4" style="padding: 10px; text-align: center; color: #94A3B8;">AWAITING FIRST TARGET LOCK...</td>
                    </tr>
                </tbody>
            </table>
        </div>
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
    const viewport = document.getElementById('viewport');
    
    const hudCard = document.getElementById('hudCard');
    const hudClass = document.getElementById('hudClass');
    const hudConf = document.getElementById('hudConf');
    const hudMode = document.getElementById('hudMode');
    
    const badgeLastTarget = document.getElementById('badgeLastTarget');
    const historyTableBody = document.getElementById('historyTableBody');
    const emptyRow = document.getElementById('emptyRow');
    const logCount = document.getElementById('logCount');

    let model = null;
    let isScanning = false;
    let lockedDetection = null;
    let scanHistory = [];

    function getColorForClass(className) {
        const cls = className.toLowerCase();
        if (cls.includes('book') || cls.includes('paper')) return '#10B981'; 
        if (cls.includes('laptop') || cls.includes('tv') || cls.includes('cell phone') || cls.includes('calculator')) return '#00D8FF'; 
        if (cls.includes('bag') || cls.includes('backpack') || cls.includes('suitcase')) return '#8B5CF6'; 
        if (cls.includes('manual')) return '#F59E0B'; 
        return '#2563EB'; 
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
        hudCard.style.display = "none";
    });

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
        triggerZoomAndSearch(touchX, touchY, lockedDetection);
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
                    
                    if (best.class === 'laptop' && bw < 180) {
                        lockedDetection.class = 'CALCULATOR / DEVICE';
                    }
                    
                    triggerZoomAndSearch(bx + bw / 2, by + bh / 2, lockedDetection);
                }
            }
        }

        if (lockedDetection) {
            drawLockFrame(lockedDetection);
        }

        requestAnimationFrame(detectObjects);
    }

    function triggerZoomAndSearch(centerX, centerY, det) {
        const originX = Math.min(Math.max((centerX / canvas.width) * 100, 20), 80);
        const originY = Math.min(Math.max((centerY / canvas.height) * 100, 20), 80);
        zoomContainer.style.transformOrigin = `${originX}% ${originY}%`;
        zoomContainer.style.transform = "scale(1.15)";

        addScanToHistory(det);
    }

    function addScanToHistory(det) {
        const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        const className = det.class.toUpperCase();
        const scoreStr = `${(det.score * 100).toFixed(1)}%`;
        const modeStr = det.isManual ? "MANUAL" : "AUTO";

        badgeLastTarget.textContent = className.length > 10 ? className.substring(0, 10) + ".." : className;

        if (emptyRow) emptyRow.style.display = "none";

        const newRow = document.createElement('tr');
        newRow.style.borderBottom = "1px solid #E2E8F0";
        newRow.innerHTML = `
            <td style="padding: 6px; font-weight: bold; color: #64748B;">${timeStr}</td>
            <td style="padding: 6px; font-weight: 800; color: ${getColorForClass(det.class)};">${className}</td>
            <td style="padding: 6px;">${scoreStr}</td>
            <td style="padding: 6px; color: #2563EB; font-weight: bold;">${modeStr}</td>
        `;
        historyTableBody.insertBefore(newRow, historyTableBody.firstChild);

        scanHistory.push(det);
        logCount.textContent = `ENTRIES: ${scanHistory.length}`;
    }

    function drawLockFrame(det) {
        const scaleX = canvas.width / video.videoWidth || 1;
        const scaleY = canvas.height / video.videoHeight || 1;
        
        const x = det.bbox[0] * scaleX;
        const y = det.bbox[1] * scaleY;
        const w = det.bbox[2] * scaleX;
        const h = det.bbox[3] * scaleY;

        const dynamicColor = getColorForClass(det.class);

        const corner = 16;
        ctx.strokeStyle = dynamicColor;
        ctx.lineWidth = 3;
        ctx.shadowBlur = 10;
        ctx.shadowColor = dynamicColor;

        ctx.beginPath();
        ctx.moveTo(x, y + corner); ctx.lineTo(x, y); ctx.lineTo(x + corner, y);
        ctx.moveTo(x + w - corner, y); ctx.lineTo(x + w, y); ctx.lineTo(x + w, y + corner);
        ctx.moveTo(x, y + h - corner); ctx.lineTo(x, y + h); ctx.lineTo(x + corner, y + h);
        ctx.moveTo(x + w - corner, y + h); ctx.lineTo(x + w, y + h); ctx.lineTo(x + w, y + h - corner);
        ctx.stroke();

        hudCard.style.display = "block";
        hudCard.style.borderColor = dynamicColor;
        hudClass.textContent = det.class.toUpperCase();
        hudConf.textContent = `CONF: ${(det.score * 100).toFixed(1)}%`;
        hudConf.style.color = dynamicColor;
        hudMode.textContent = det.isManual ? "MODE: TAP SEARCH" : "NET: SEARCH COMPLETE";
    }
</script>
"""

components.html(spatial_vision_html, height=720)
