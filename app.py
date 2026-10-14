import streamlit as st
import streamlit.components.v1 as components

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Phòng Thí Nghiệm Hình Học Ảo AI - Lớp 5/2",
    page_icon="📐",
    layout="wide"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 1rem;
    }
    .top-banner {
        background: linear-gradient(135deg, #0b7285 0%, #1971c2 60%, #3b5bdb 100%);
        color: white;
        padding: 18px 24px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 6px 18px rgba(25, 113, 194, 0.25);
        margin-bottom: 12px;
    }
    .top-banner h1 {
        font-size: 1.75rem;
        margin: 0;
        color: white;
        font-weight: 800;
    }
    .top-banner p {
        font-size: 1rem;
        margin: 5px 0 0 0;
        color: #e3fafc;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="top-banner">
    <h1>📐 PHÒNG THÍ NGHIỆM HÌNH HỌC ẢO AI - LỚP 5/2</h1>
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn • Kéo thả Thước Đo Độ, Thước Thẳng & Ê-ke trực quan</p>
</div>
""", unsafe_allow_html=True)

# ==================== ỨNG DỤNG TƯƠNG TÁC HTML5 CANVAS + AI SENSOR ====================
geometry_app_html = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
    * { box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; user-select: none; }
    body { margin: 0; padding: 0; background: #f8f9fa; color: #212529; }
    .app-wrapper {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        max-width: 1200px;
        margin: 0 auto;
    }
    .canvas-panel {
        flex: 2;
        min-width: 340px;
        background: white;
        border-radius: 16px;
        padding: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border: 2px solid #dee2e6;
    }
    .control-panel {
        flex: 1;
        min-width: 300px;
        background: white;
        border-radius: 16px;
        padding: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border: 2px solid #dee2e6;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }
    .toolbar {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 10px;
        justify-content: center;
    }
    .btn {
        padding: 9px 14px;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        font-size: 0.92rem;
        cursor: pointer;
        transition: all 0.15s;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    .btn:hover { transform: translateY(-2px); filter: brightness(1.05); }
    .btn-tool { background: #e7f5ff; color: #1864ab; border: 2px solid #74c0fc; }
    .btn-tool.active { background: #1971c2; color: white; border-color: #1864ab; }
    .btn-magic { background: #fff3bf; color: #d9480f; border: 2px solid #fcc419; }
    .btn-new { background: #ebfbee; color: #2b8a3e; border: 2px solid #69db7c; }
    .btn-submit { background: linear-gradient(135deg, #f76707, #e8590c); color: white; width: 100%; justify-content: center; font-size: 1.05rem; padding: 12px; }

    canvas {
        width: 100%;
        height: auto;
        background: #ffffff;
        border: 2px solid #ced4da;
        border-radius: 12px;
        cursor: grab;
        touch-action: none;
    }
    canvas:active { cursor: grabbing; }

    .ai-sensor-bar {
        margin-top: 8px;
        padding: 11px 14px;
        border-radius: 10px;
        font-size: 0.95rem;
        font-weight: 600;
        background: #e3fafc;
        border-left: 5px solid #15aabf;
        color: #0b7285;
    }
    .ai-sensor-bar.aligned {
        background: #d3f9d8;
        border-left-color: #2b8a3e;
        color: #1b4332;
    }
    .score-card {
        background: linear-gradient(135deg, #fff9db, #ffec99);
        border: 2px solid #fcc419;
        border-radius: 12px;
        padding: 10px 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: bold;
        color: #d9480f;
    }
    .mission-box {
        background: #f1f3f5;
        border-radius: 12px;
        padding: 12px;
        border-left: 5px solid #1971c2;
    }
    .input-group {
        display: flex;
        gap: 8px;
        align-items: center;
        margin-top: 6px;
    }
    input[type="number"], select, input[type="text"] {
        width: 100%;
        padding: 9px 12px;
        border: 2px solid #adb5bd;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: bold;
    }
    .slider-row {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.9rem;
        font-weight: 600;
        background: #f8f9fa;
        padding: 6px 10px;
        border-radius: 8px;
    }
    .tt27-box {
        background: #f8f9fa;
        border: 1px dashed #868e96;
        border-radius: 10px;
        padding: 10px;
        font-size: 0.86rem;
        color: #495057;
    }
</style>
</head>
<body>

<div class="app-wrapper">
    <!-- CỘT TRÁI: BẢNG VẼ & THƯỚC ẢO TƯƠNG TÁC -->
    <div class="canvas-panel">
        <div class="toolbar">
            <button id="btnProtractor" class="btn btn-tool active" onclick="toggleTool('protractor')">📐 Thước Đo Độ (180°)</button>
            <button id="btnRuler" class="btn btn-tool" onclick="toggleTool('ruler')">📏 Thước Thẳng (cm)</button>
            <button id="btnEke" class="btn btn-tool" onclick="toggleTool('eke')">🔺 Thước Ê-ke Vuông</button>
            <button class="btn btn-magic" onclick="autoAlignTool()">🧲 AI Đặt Thước Mẫu</button>
            <button class="btn btn-new" onclick="generateNewProblem()">🎲 Đổi Hình Mới</button>
        </div>

        <canvas id="geoCanvas" width="760" height="460"></canvas>

        <!-- Thanh xoay thước mượt mà cho điện thoại & máy tính -->
        <div class="slider-row">
            <span>🔄 Xoay thước đang chọn:</span>
            <input type="range" id="angleSlider" min="-180" max="180" value="0" style="flex:1;" oninput="rotateActiveTool(this.value)">
            <span id="angleLabel" style="min-width:45px; text-align:right;">0°</span>
            <button class="btn" style="padding:4px 10px; background:#e9ecef;" onclick="rotateActiveTool(0); document.getElementById('angleSlider').value=0;">Đặt ngang 0°</button>
        </div>

        <div id="aiSensor" class="ai-sensor-bar">
            🤖 <b>Trợ lý AI:</b> Hãy dùng chuột hoặc ngón tay <b>kéo Tâm thước (chấm đỏ)</b> đặt trùng vào <b>Đỉnh O</b> của góc nhé!
        </div>
    </div>

    <!-- CỘT PHẢI: NHIỆM VỤ, KIỂM TRA ĐÁP ÁN & ĐÁNH GIÁ TT27 -->
    <div class="control-panel">
        <div class="score-card">
            <div>👤 <span id="stNameDisplay">Học sinh 5/2</span></div>
            <div>⭐ <span id="starCount">50</span> Sao</div>
            <div>🏆 Đúng: <span id="correctCount">0</span> bài</div>
        </div>

        <div style="display:flex; gap:6px;">
            <input type="text" id="studentName" placeholder="Nhập tên học sinh..." value="Minh Khôi (Tổ 1)" oninput="updateStudentName()">
        </div>

        <div>
            <label style="font-weight:bold; font-size:0.9rem;">🎯 Chọn Chuyên đề Thực hành Hình học 5:</label>
            <select id="modeSelect" onchange="changeMode()" style="margin-top:4px;">
                <option value="angle">1. Thực hành Đo Góc (Góc nhọn, vuông, tù)</option>
                <option value="segment">2. Thực hành Đo Độ Dài Đoạn Thẳng (cm)</option>
                <option value="triangle">3. Đo Đáy & Đường Cao Tam Giác -> Tính Diện Tích</option>
            </select>
        </div>

        <div class="mission-box">
            <div style="font-weight:800; color:#1864ab; margin-bottom:4px;" id="missionTitle">📋 NHIỆM VỤ ĐO GÓC:</div>
            <div id="missionDesc" style="font-size:0.95rem; line-height:1.4;">
                Hãy dùng <b>Thước Đo Độ</b> để đo số đo của <b>góc AOB</b> trên hình vẽ và cho biết đó là loại góc gì.
            </div>

            <!-- Khu vực nhập kết quả Đo Góc -->
            <div id="inputAngleBox" style="margin-top:10px;">
                <label style="font-size:0.9rem; font-weight:bold;">Số đo góc em đo được (Độ °):</label>
                <div class="input-group">
                    <input type="number" id="ansAngle" placeholder="Ví dụ: 60" step="5">
                    <select id="ansAngleType">
                        <option value="nhon">Góc nhọn (&lt; 90°)</option>
                        <option value="vuong">Góc vuông (= 90°)</option>
                        <option value="tu">Góc tù (&gt; 90°)</option>
                    </select>
                </div>
            </div>

            <!-- Khu vực nhập kết quả Đo Đoạn Thẳng -->
            <div id="inputSegmentBox" style="margin-top:10px; display:none;">
                <label style="font-size:0.9rem; font-weight:bold;">Độ dài đoạn thẳng AB em đo được (cm):</label>
                <div class="input-group">
                    <input type="number" id="ansSegment" placeholder="Ví dụ: 6.5" step="0.5">
                    <span style="font-weight:bold;">cm</span>
                </div>
            </div>

            <!-- Khu vực nhập kết quả Diện tích Tam giác -->
            <div id="inputTriangleBox" style="margin-top:10px; display:none;">
                <label style="font-size:0.88rem; font-weight:bold;">Nhập số đo Đáy (a), Chiều cao (h) và Diện tích (S):</label>
                <div class="input-group">
                    <input type="number" id="ansBase" placeholder="Đáy a (cm)" step="1">
                    <input type="number" id="ansHeight" placeholder="Cao h (cm)" step="1">
                </div>
                <div class="input-group">
                    <input type="number" id="ansArea" placeholder="Diện tích S = (a × h) : 2 (cm²)" step="0.5">
                </div>
            </div>
        </div>

        <button class="btn btn-submit" onclick="checkAnswer()">✅ NỘP KẾT QUẢ ĐO & KIỂM TRA</button>

        <div id="feedbackMsg" style="font-weight:bold; font-size:0.95rem; min-height:24px;"></div>

        <div class="tt27-box">
            <b>📋 Nhận xét Kĩ năng Hình học (Thông tư 27):</b>
            <div id="tt27Text" style="margin-top:4px;">
                Học sinh biết sử dụng thước đo góc và thước thẳng có chia vạch cm để đo đại lượng hình học; rèn luyện tính cẩn thận, chính xác.
            </div>
        </div>
    </div>
</div>

<script>
const canvas = document.getElementById('geoCanvas');
const ctx = canvas.getContext('2d');
const PX_PER_CM = 40; // 1 cm = 40 pixels trên bảng vẽ

// Trạng thái công cụ
let tools = {
    protractor: { active: true, x: 520, y: 340, angle: 0, radius: 175 },
    ruler: { active: false, x: 140, y: 370, angle: 0, lengthCm: 12 },
    eke: { active: false, x: 450, y: 280, angle: 0, sizeCm: 6 }
};
let lastSelectedTool = 'protractor';
let dragging = null; // { toolName, mode: 'move' | 'rotate', offsetX, offsetY }

// Trạng thái bài tập
let currentMode = 'angle';
let stars = 50;
let solved = 0;
let problem = {};

// Âm thanh Web Audio
function playSound(isWin) {
    try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (isWin) {
            [523.25, 659.25, 783.99, 1046.5].forEach((f, i) => {
                const o = audioCtx.createOscillator();
                const g = audioCtx.createGain();
                o.type = 'triangle';
                o.frequency.setValueAtTime(f, audioCtx.currentTime + i * 0.09);
                g.gain.setValueAtTime(0.18, audioCtx.currentTime + i * 0.09);
                g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + i * 0.09 + 0.25);
                o.connect(g); g.connect(audioCtx.destination);
                o.start(audioCtx.currentTime + i * 0.09);
                o.stop(audioCtx.currentTime + i * 0.09 + 0.25);
            });
        } else {
            const o = audioCtx.createOscillator();
            const g = audioCtx.createGain();
            o.type = 'sawtooth';
            o.frequency.setValueAtTime(200, audioCtx.currentTime);
            g.gain.setValueAtTime(0.15, audioCtx.currentTime);
            g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.3);
            o.connect(g); g.connect(audioCtx.destination);
            o.start(); o.stop(audioCtx.currentTime + 0.3);
        }
    } catch(e) {}
}

// Khởi tạo bài toán mới
function generateNewProblem() {
    document.getElementById('feedbackMsg').innerHTML = "";
    if (currentMode === 'angle') {
        const angles = [30, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 135, 140, 150];
        const deg = angles[Math.floor(Math.random() * angles.length)];
        const baseRot = [0, -10, 10, -15, 15][Math.floor(Math.random() * 5)];
        problem = {
            vx: 250 + Math.floor(Math.random() * 120),
            vy: 290 + Math.floor(Math.random() * 50),
            deg: deg,
            baseRot: baseRot,
            type: deg < 90 ? 'nhon' : (deg === 90 ? 'vuong' : 'tu')
        };
        document.getElementById('ansAngle').value = '';
    } else if (currentMode === 'segment') {
        const lengths = [4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 10];
        const lenCm = lengths[Math.floor(Math.random() * lengths.length)];
        const rotDeg = [-20, -10, 0, 10, 15, 25][Math.floor(Math.random() * 6)];
        const x1 = 150, y1 = 220;
        const rad = rotDeg * Math.PI / 180;
        const x2 = x1 + lenCm * PX_PER_CM * Math.cos(rad);
        const y2 = y1 + lenCm * PX_PER_CM * Math.sin(rad);
        problem = { x1, y1, x2, y2, lenCm, rotDeg };
        document.getElementById('ansSegment').value = '';
    } else if (currentMode === 'triangle') {
        const bases = [6, 7, 8, 9, 10];
        const heights = [4, 5, 6];
        const baseCm = bases[Math.floor(Math.random() * bases.length)];
        const heightCm = heights[Math.floor(Math.random() * heights.length)];
        const xA = 160, yA = 320;
        const xB = xA + baseCm * PX_PER_CM, yB = 320;
        const xH = xA + (baseCm * 0.4) * PX_PER_CM, yH = 320;
        const xC = xH, yC = yH - heightCm * PX_PER_CM;
        problem = { xA, yA, xB, yB, xC, yC, xH, yH, baseCm, heightCm, area: (baseCm * heightCm) / 2 };
        document.getElementById('ansBase').value = '';
        document.getElementById('ansHeight').value = '';
        document.getElementById('ansArea').value = '';
    }
    drawAll();
}

function changeMode() {
    currentMode = document.getElementById('modeSelect').value;
    document.getElementById('inputAngleBox').style.display = currentMode === 'angle' ? 'block' : 'none';
    document.getElementById('inputSegmentBox').style.display = currentMode === 'segment' ? 'block' : 'none';
    document.getElementById('inputTriangleBox').style.display = currentMode === 'triangle' ? 'block' : 'none';

    if (currentMode === 'angle') {
        tools.protractor.active = true;
        tools.ruler.active = false;
        tools.eke.active = false;
        lastSelectedTool = 'protractor';
        document.getElementById('missionTitle').innerText = "📋 NHIỆM VỤ 1: ĐO GÓC AOB";
        document.getElementById('missionDesc').innerHTML = "Kéo <b>Tâm thước đo độ</b> trùng với <b>Đỉnh O</b>, xoay thước sao cho vạch 0° trùng với cạnh OA rồi đọc số đo góc.";
    } else if (currentMode === 'segment') {
        tools.protractor.active = false;
        tools.ruler.active = true;
        tools.eke.active = false;
        lastSelectedTool = 'ruler';
        document.getElementById('missionTitle').innerText = "📋 NHIỆM VỤ 2: ĐO ĐỘ DÀI ĐOẠN THẲNG AB";
        document.getElementById('missionDesc').innerHTML = "Kéo <b>Vạch số 0 của Thước thẳng</b> trùng với điểm <b>A</b>, xoay thước dọc theo đoạn AB để đọc độ dài (cm).";
    } else {
        tools.protractor.active = false;
        tools.ruler.active = true;
        tools.eke.active = true;
        lastSelectedTool = 'ruler';
        document.getElementById('missionTitle').innerText = "📋 NHIỆM VỤ 3: ĐO ĐÁY & CHIỀU CAO TAM GIÁC";
        document.getElementById('missionDesc').innerHTML = "Dùng <b>Thước thẳng</b> và <b>Ê-ke</b> để đo độ dài đáy <b>AB (cm)</b> và đường cao <b>CH (cm)</b>, sau đó tính diện tích hình tam giác ABC.";
    }
    updateToolbarButtons();
    generateNewProblem();
}

function toggleTool(name) {
    tools[name].active = !tools[name].active;
    if (tools[name].active) {
        lastSelectedTool = name;
        document.getElementById('angleSlider').value = Math.round(tools[name].angle);
        document.getElementById('angleLabel').innerText = Math.round(tools[name].angle) + '°';
    }
    updateToolbarButtons();
    drawAll();
}

function updateToolbarButtons() {
    document.getElementById('btnProtractor').className = 'btn btn-tool' + (tools.protractor.active ? ' active' : '');
    document.getElementById('btnRuler').className = 'btn btn-tool' + (tools.ruler.active ? ' active' : '');
    document.getElementById('btnEke').className = 'btn btn-tool' + (tools.eke.active ? ' active' : '');
}

function rotateActiveTool(val) {
    const deg = parseFloat(val);
    tools[lastSelectedTool].angle = deg;
    document.getElementById('angleLabel').innerText = Math.round(deg) + '°';
    drawAll();
}

// Nút AI Đặt Thước Mẫu tự động khớp
function autoAlignTool() {
    if (currentMode === 'angle') {
        tools.protractor.active = true;
        lastSelectedTool = 'protractor';
        tools.protractor.x = problem.vx;
        tools.protractor.y = problem.vy;
        tools.protractor.angle = problem.baseRot;
        document.getElementById('angleSlider').value = problem.baseRot;
        document.getElementById('angleLabel').innerText = problem.baseRot + '°';
    } else if (currentMode === 'segment') {
        tools.ruler.active = true;
        lastSelectedTool = 'ruler';
        tools.ruler.x = problem.x1;
        tools.ruler.y = problem.y1;
        tools.ruler.angle = problem.rotDeg;
        document.getElementById('angleSlider').value = problem.rotDeg;
        document.getElementById('angleLabel').innerText = problem.rotDeg + '°';
    } else if (currentMode === 'triangle') {
        tools.ruler.active = true;
        tools.eke.active = true;
        tools.ruler.x = problem.xA;
        tools.ruler.y = problem.yA;
        tools.ruler.angle = 0;
        tools.eke.x = problem.xH;
        tools.eke.y = problem.yH;
        tools.eke.angle = 0;
    }
    updateToolbarButtons();
    drawAll();
}

// ==================== VẼ LƯỚI NỀN & BÀI TOÁN ====================
function drawGrid() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = '#f1f3f5';
    ctx.lineWidth = 1;
    for (let x = 0; x < canvas.width; x += 20) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
    }
    for (let y = 0; y < canvas.height; y += 20) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
    }
}

function drawProblem() {
    ctx.save();
    if (currentMode === 'angle') {
        const { vx, vy, deg, baseRot } = problem;
        const len = 210;
        const rad1 = (baseRot) * Math.PI / 180;
        const rad2 = (baseRot - deg) * Math.PI / 180;

        const xA = vx + len * Math.cos(rad1);
        const yA = vy + len * Math.sin(rad1);
        const xB = vx + len * Math.cos(rad2);
        const yB = vy + len * Math.sin(rad2);

        // Vẽ cung góc nhỏ
        ctx.beginPath();
        ctx.arc(vx, vy, 38, rad2, rad1);
        ctx.fillStyle = 'rgba(255, 193, 7, 0.25)';
        ctx.fill();
        ctx.strokeStyle = '#f59f00';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Vẽ 2 tia OA và OB
        ctx.strokeStyle = '#1864ab';
        ctx.lineWidth = 4;
        ctx.lineCap = 'round';
        ctx.beginPath();
        ctx.moveTo(vx, vy); ctx.lineTo(xA, yA);
        ctx.moveTo(vx, vy); ctx.lineTo(xB, yB);
        ctx.stroke();

        // Điểm đỉnh O, A, B
        ctx.fillStyle = '#e03131';
        ctx.beginPath(); ctx.arc(vx, vy, 6, 0, Math.PI * 2); ctx.fill();
        ctx.font = 'bold 18px sans-serif';
        ctx.fillStyle = '#c92a2a';
        ctx.fillText('O (Đỉnh góc)', vx - 35, vy + 26);
        ctx.fillStyle = '#1864ab';
        ctx.fillText('A', xA + 10, yA + 5);
        ctx.fillText('B', xB + 10, yB - 8);

    } else if (currentMode === 'segment') {
        const { x1, y1, x2, y2 } = problem;
        ctx.strokeStyle = '#2b8a3e';
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(x1, y1); ctx.lineTo(x2, y2);
        ctx.stroke();

        // Hai đầu mút A và B
        ctx.fillStyle = '#e03131';
        ctx.beginPath(); ctx.arc(x1, y1, 6, 0, Math.PI * 2); ctx.fill();
        ctx.beginPath(); ctx.arc(x2, y2, 6, 0, Math.PI * 2); ctx.fill();

        ctx.font = 'bold 18px sans-serif';
        ctx.fillStyle = '#1b4332';
        ctx.fillText('A', x1 - 10, y1 - 12);
        ctx.fillText('B', x2 + 8, y2 - 12);

    } else if (currentMode === 'triangle') {
        const { xA, yA, xB, yB, xC, yC, xH, yH } = problem;
        ctx.fillStyle = 'rgba(116, 192, 252, 0.2)';
        ctx.strokeStyle = '#1971c2';
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.moveTo(xA, yA); ctx.lineTo(xB, yB); ctx.lineTo(xC, yC); ctx.closePath();
        ctx.fill(); ctx.stroke();

        // Đường cao CH nét đứt
        ctx.save();
        ctx.setLineDash([6, 5]);
        ctx.strokeStyle = '#e03131';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(xC, yC); ctx.lineTo(xH, yH);
        ctx.stroke();
        ctx.restore();

        // Ký hiệu vuông góc tại H
        ctx.strokeStyle = '#e03131';
        ctx.lineWidth = 1.5;
        ctx.strokeRect(xH, yH - 12, 12, 12);

        ctx.font = 'bold 17px sans-serif';
        ctx.fillStyle = '#1864ab';
        ctx.fillText('A', xA - 18, yA + 6);
        ctx.fillText('B', xB + 8, yB + 6);
        ctx.fillText('C', xC - 6, yC - 10);
        ctx.fillStyle = '#e03131';
        ctx.fillText('H', xH - 6, yH + 22);
    }
    ctx.restore();
}

// ==================== 1. VẼ THƯỚC ĐO ĐỘ ẢO (PROTRACTOR) ====================
function drawProtractor() {
    if (!tools.protractor.active) return;
    const { x, y, angle, radius } = tools.protractor;

    ctx.save();
    ctx.translate(x, y);
    ctx.rotate(angle * Math.PI / 180);

    // Thân thước bán nguyệt trong suốt
    ctx.beginPath();
    ctx.arc(0, 0, radius, Math.PI, 0, false);
    ctx.lineTo(radius, 22);
    ctx.lineTo(-radius, 22);
    ctx.closePath();
    ctx.fillStyle = 'rgba(255, 243, 191, 0.72)';
    ctx.fill();
    ctx.lineWidth = 2.5;
    ctx.strokeStyle = '#f08c00';
    ctx.stroke();

    // Khoét lỗ bán nguyệt nhỏ bên trong cho dễ nhìn
    ctx.beginPath();
    ctx.arc(0, 0, radius * 0.42, Math.PI, 0, false);
    ctx.closePath();
    ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
    ctx.fill();
    ctx.strokeStyle = '#fcc419';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Đường chuẩn 0° - 180°
    ctx.beginPath();
    ctx.moveTo(-radius, 0); ctx.lineTo(radius, 0);
    ctx.strokeStyle = '#d9480f';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Vạch chia độ từ 0° đến 180°
    for (let deg = 0; deg <= 180; deg += 1) {
        const rad = -deg * Math.PI / 180;
        let tickLen = 5;
        if (deg % 10 === 0) tickLen = 15;
        else if (deg % 5 === 0) tickLen = 10;

        const rOuter = radius;
        const rInner = radius - tickLen;
        ctx.beginPath();
        ctx.moveTo(rOuter * Math.cos(rad), rOuter * Math.sin(rad));
        ctx.lineTo(rInner * Math.cos(rad), rInner * Math.sin(rad));
        ctx.strokeStyle = deg % 10 === 0 ? '#c92a2a' : '#495057';
        ctx.lineWidth = deg % 10 === 0 ? 1.5 : 0.7;
        ctx.stroke();

        // Ghi số đo góc vòng ngoài (ngược chiều kim đồng hồ: 0 -> 180)
        if (deg % 10 === 0) {
            const rText = radius - 26;
            ctx.save();
            ctx.translate(rText * Math.cos(rad), rText * Math.sin(rad));
            ctx.rotate(rad + Math.PI / 2);
            ctx.font = 'bold 11px sans-serif';
            ctx.fillStyle = '#c92a2a';
            ctx.textAlign = 'center';
            ctx.fillText(deg.toString(), 0, 0);
            ctx.restore();
        }
    }

    // Tâm thước đo độ (Crosshair đỏ)
    ctx.beginPath();
    ctx.arc(0, 0, 7, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(224, 49, 49, 0.9)';
    ctx.fill();
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Nút nắm xoay thước bên phải
    ctx.beginPath();
    ctx.arc(radius - 16, 12, 10, 0, Math.PI * 2);
    ctx.fillStyle = '#1971c2';
    ctx.fill();
    ctx.fillStyle = 'white';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('↻', radius - 16, 16);

    ctx.restore();
}

// ==================== 2. VẼ THƯỚC THẲNG ẢO (VIRTUAL RULER CM) ====================
function drawRuler() {
    if (!tools.ruler.active) return;
    const { x, y, angle, lengthCm } = tools.ruler;
    const widthPx = lengthCm * PX_PER_CM;
    const heightPx = 54;

    ctx.save();
    ctx.translate(x, y); // Gốc (0,0) của thước chính là vạch số 0 cm!
    ctx.rotate(angle * Math.PI / 180);

    // Thân thước nhựa trong suốt màu xanh nhạt (vẽ dư 15px bên trái vạch 0)
    ctx.fillStyle = 'rgba(208, 235, 255, 0.8)';
    ctx.strokeStyle = '#1971c2';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(-15, 0, widthPx + 35, heightPx, 8);
    ctx.fill();
    ctx.stroke();

    // Vạch chia cm và mm
    for (let mm = 0; mm <= lengthCm * 10; mm++) {
        const px = (mm / 10) * PX_PER_CM;
        let tickH = 7;
        if (mm % 10 === 0) tickH = 18;
        else if (mm % 5 === 0) tickH = 12;

        ctx.beginPath();
        ctx.moveTo(px, 0);
        ctx.lineTo(px, tickH);
        ctx.strokeStyle = mm % 10 === 0 ? '#0b7285' : '#495057';
        ctx.lineWidth = mm % 10 === 0 ? 1.8 : 0.8;
        ctx.stroke();

        if (mm % 10 === 0) {
            ctx.font = 'bold 13px sans-serif';
            ctx.fillStyle = '#0b7285';
            ctx.textAlign = 'center';
            ctx.fillText((mm / 10).toString(), px, 33);
        }
    }
    ctx.font = 'italic bold 11px sans-serif';
    ctx.fillStyle = '#1864ab';
    ctx.fillText('THƯỚC THẲNG LỚP 5/2 (Đơn vị: cm)', widthPx / 2, 48);

    // Chấm đỏ đánh dấu vạch 0 cm
    ctx.beginPath();
    ctx.arc(0, 0, 6, 0, Math.PI * 2);
    ctx.fillStyle = '#e03131';
    ctx.fill();

    // Nút xoay ở đầu phải của thước
    ctx.beginPath();
    ctx.arc(widthPx + 8, heightPx / 2, 11, 0, Math.PI * 2);
    ctx.fillStyle = '#f08c00';
    ctx.fill();
    ctx.fillStyle = 'white';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('↻', widthPx + 8, heightPx / 2 + 4);

    ctx.restore();
}

// ==================== 3. VẼ THƯỚC Ê-KE VUÔNG GÓC ====================
function drawEke() {
    if (!tools.eke.active) return;
    const { x, y, angle, sizeCm } = tools.eke;
    const sidePx = sizeCm * PX_PER_CM;

    ctx.save();
    ctx.translate(x, y); // Góc vuông của Ê-ke nằm tại (0,0)
    ctx.rotate(angle * Math.PI / 180);

    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(sidePx, 0);
    ctx.lineTo(0, -sidePx);
    ctx.closePath();
    ctx.fillStyle = 'rgba(211, 249, 216, 0.78)';
    ctx.fill();
    ctx.lineWidth = 2.2;
    ctx.strokeStyle = '#2b8a3e';
    ctx.stroke();

    // Vạch chia cm dọc theo cạnh đứng của Ê-ke (để đo chiều cao tam giác/hình thang!)
    for (let cm = 0; cm <= sizeCm; cm++) {
        const py = -cm * PX_PER_CM;
        ctx.beginPath();
        ctx.moveTo(0, py);
        ctx.lineTo(12, py);
        ctx.strokeStyle = '#1b4332';
        ctx.lineWidth = 1.6;
        ctx.stroke();
        if (cm > 0 && cm < sizeCm) {
            ctx.font = 'bold 12px sans-serif';
            ctx.fillStyle = '#1b4332';
            ctx.fillText(cm + 'cm', 16, py + 4);
        }
    }

    // Chấm góc vuông Ê-ke
    ctx.beginPath();
    ctx.arc(0, 0, 6, 0, Math.PI * 2);
    ctx.fillStyle = '#2b8a3e';
    ctx.fill();

    ctx.restore();
}

// ==================== CẢM BIẾN AI KIỂM TRA ĐẶT THƯỚC ====================
function updateAISensor() {
    const sensorBar = document.getElementById('aiSensor');
    if (currentMode === 'angle' && tools.protractor.active) {
        const dist = Math.hypot(tools.protractor.x - problem.vx, tools.protractor.y - problem.vy);
        const angleDiff = Math.abs(tools.protractor.angle - problem.baseRot);
        if (dist < 18 && angleDiff < 5) {
            sensorBar.className = 'ai-sensor-bar aligned';
            sensorBar.innerHTML = `✅ <b>Cảm biến AI: Tuyệt vời!</b> Tâm thước đã trùng khít <b>Đỉnh O</b> và vạch 0° đã thẳng hàng cạnh OA. Em hãy nhìn xem cạnh OB chỉ vào vạch bao nhiêu độ nhé!`;
        } else if (dist < 18) {
            sensorBar.className = 'ai-sensor-bar';
            sensorBar.innerHTML = `🤖 <b>Trợ lý AI:</b> Tâm thước đã đặt đúng Đỉnh O! Hãy chỉnh thanh <b>Xoay thước (${problem.baseRot}°)</b> để vạch số 0° trùng khít với cạnh OA nhé!`;
        } else {
            sensorBar.className = 'ai-sensor-bar';
            sensorBar.innerHTML = `🤖 <b>Trợ lý AI:</b> Hãy kéo <b>chấm đỏ Tâm thước</b> lại gần <b>Đỉnh O</b> (còn cách khoảng ${Math.round(dist)} px) hoặc bấm nút <b>"🧲 AI Đặt Thước Mẫu"</b>.`;
        }
    } else if (currentMode === 'segment' && tools.ruler.active) {
        const dist = Math.hypot(tools.ruler.x - problem.x1, tools.ruler.y - problem.y1);
        const angleDiff = Math.abs(tools.ruler.angle - problem.rotDeg);
        if (dist < 18 && angleDiff < 5) {
            sensorBar.className = 'ai-sensor-bar aligned';
            sensorBar.innerHTML = `✅ <b>Cảm biến AI: Chính xác!</b> Vạch 0 cm đã đặt trùng khít điểm A và thước nằm dọc theo đoạn AB. Hãy đọc số cm tại điểm B!`;
        } else {
            sensorBar.className = 'ai-sensor-bar';
            sensorBar.innerHTML = `🤖 <b>Trợ lý AI:</b> Hãy kéo <b>chấm đỏ vạch 0 cm</b> của Thước thẳng trùng vào điểm <b>A</b> và xoay thước góc <b>${problem.rotDeg}°</b> theo đoạn AB.`;
        }
    } else if (currentMode === 'triangle') {
        sensorBar.className = 'ai-sensor-bar';
        sensorBar.innerHTML = `🤖 <b>Trợ lý AI:</b> Dùng <b>Thước thẳng</b> đo cạnh đáy AB và dùng <b>Thước Ê-ke</b> đo đường cao CH (màu đỏ nét đứt), sau đó lấy <b>(Đáy × Cao) : 2</b> nhé!`;
    }
}

function drawAll() {
    drawGrid();
    drawProblem();
    drawRuler();
    drawEke();
    drawProtractor();
    updateAISensor();
}

// ==================== XỬ LÝ KÉO THẢ CHUỘT & CẢM ỨNG ====================
function getPointerPos(e) {
    const rect = canvas.getBoundingClientRect();
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const clientY = e.touches ? e.touches[0].clientY : e.clientY;
    return {
        x: (clientX - rect.left) * (canvas.width / rect.width),
        y: (clientY - rect.top) * (canvas.height / rect.height)
    };
}

function onPointerDown(e) {
    const pos = getPointerPos(e);

    // Ưu tiên kiểm tra từ thước trên cùng
    const order = ['protractor', 'eke', 'ruler'];
    for (let name of order) {
        const t = tools[name];
        if (!t.active) continue;

        const dx = pos.x - t.x;
        const dy = pos.y - t.y;
        const dist = Math.hypot(dx, dy);

        if (name === 'protractor' && dist <= t.radius + 15) {
            lastSelectedTool = name;
            dragging = { name, offsetX: dx, offsetY: dy };
            e.preventDefault();
            return;
        }
        if (name === 'ruler' && dist <= t.lengthCm * PX_PER_CM + 30) {
            lastSelectedTool = name;
            dragging = { name, offsetX: dx, offsetY: dy };
            e.preventDefault();
            return;
        }
        if (name === 'eke' && dist <= t.sizeCm * PX_PER_CM + 20) {
            lastSelectedTool = name;
            dragging = { name, offsetX: dx, offsetY: dy };
            e.preventDefault();
            return;
        }
    }
}

function onPointerMove(e) {
    if (!dragging) return;
    e.preventDefault();
    const pos = getPointerPos(e);
    const t = tools[dragging.name];
    t.x = pos.x - dragging.offsetX;
    t.y = pos.y - dragging.offsetY;

    // Tự động hút nhẹ (Magnetic Snap) khi kéo gần trúng đỉnh góc hoặc điểm A
    if (dragging.name === 'protractor' && currentMode === 'angle') {
        if (Math.hypot(t.x - problem.vx, t.y - problem.vy) < 15) {
            t.x = problem.vx;
            t.y = problem.vy;
        }
    }
    if (dragging.name === 'ruler' && currentMode === 'segment') {
        if (Math.hypot(t.x - problem.x1, t.y - problem.y1) < 15) {
            t.x = problem.x1;
            t.y = problem.y1;
        }
    }
    drawAll();
}

function onPointerUp() {
    dragging = null;
}

canvas.addEventListener('mousedown', onPointerDown);
canvas.addEventListener('mousemove', onPointerMove);
window.addEventListener('mouseup', onPointerUp);

canvas.addEventListener('touchstart', onPointerDown, { passive: false });
canvas.addEventListener('touchmove', onPointerMove, { passive: false });
window.addEventListener('touchend', onPointerUp);

// ==================== KIỂM TRA ĐÁP ÁN & CẬP NHẬT NHẬN XÉT TT27 ====================
function updateStudentName() {
    const name = document.getElementById('studentName').value || 'Học sinh 5/2';
    document.getElementById('stNameDisplay').innerText = name;
}

function checkAnswer() {
    const fb = document.getElementById('feedbackMsg');
    const stName = document.getElementById('studentName').value || 'Học sinh 5/2';

    if (currentMode === 'angle') {
        const userDeg = parseFloat(document.getElementById('ansAngle').value);
        const userType = document.getElementById('ansAngleType').value;
        if (isNaN(userDeg)) {
            fb.style.color = '#e03131';
            fb.innerText = "⚠️ Em hãy nhập số đo góc mà em đọc được trên thước nhé!";
            return;
        }
        // Cho phép sai số +/- 2 độ khi đọc mắt thường
        if (Math.abs(userDeg - problem.deg) <= 2 && userType === problem.type) {
            playSound(true);
            stars += 10; solved += 1;
            fb.style.color = '#2b8a3e';
            fb.innerHTML = `🎉 Chính xác tuyệt đối! Góc AOB = <b>${problem.deg}°</b> (${problem.type === 'nhon' ? 'Góc nhọn' : problem.type === 'vuong' ? 'Góc vuông' : 'Góc tù'}). Thưởng +10 Sao!`;
            document.getElementById('tt27Text').innerText = `Em ${stName} thao tác thành thạo thước đo góc, đặt đúng tâm thước và nhận diện chính xác góc nhọn, góc vuông, góc tù (Mức: Hoàn thành tốt - TT27).`;
        } else {
            playSound(false);
            fb.style.color = '#d9480f';
            fb.innerHTML = `💡 Chưa chính xác! Hãy bấm nút <b>"🧲 AI Đặt Thước Mẫu"</b> để kiểm tra lại số đo và loại góc nhé!`;
        }
    } else if (currentMode === 'segment') {
        const userLen = parseFloat(document.getElementById('ansSegment').value);
        if (isNaN(userLen)) {
            fb.style.color = '#e03131';
            fb.innerText = "⚠️ Em hãy nhập độ dài đoạn thẳng AB (cm) nhé!";
            return;
        }
        if (Math.abs(userLen - problem.lenCm) <= 0.2) {
            playSound(true);
            stars += 10; solved += 1;
            fb.style.color = '#2b8a3e';
            fb.innerHTML = `🎉 Xuất sắc! Đoạn thẳng AB dài chính xác <b>${problem.lenCm} cm</b>. Thưởng +10 Sao!`;
            document.getElementById('tt27Text').innerText = `Em ${stName} biết sử dụng thước thẳng chia vạch cm để đo chính xác độ dài đoạn thẳng trong mặt phẳng (Mức: Hoàn thành tốt - TT27).`;
        } else {
            playSound(false);
            fb.style.color = '#d9480f';
            fb.innerHTML = `💡 Gợi ý AI: Nhớ đặt vạch số <b>0 cm</b> (chấm đỏ) ngay tại điểm A nhé!`;
        }
    } else if (currentMode === 'triangle') {
        const uBase = parseFloat(document.getElementById('ansBase').value);
        const uHeight = parseFloat(document.getElementById('ansHeight').value);
        const uArea = parseFloat(document.getElementById('ansArea').value);
        if (uBase === problem.baseCm && uHeight === problem.heightCm && uArea === problem.area) {
            playSound(true);
            stars += 15; solved += 1;
            fb.style.color = '#2b8a3e';
            fb.innerHTML = `🎉 Quá giỏi! Đáy = ${problem.baseCm}cm, Cao = ${problem.heightCm}cm => Diện tích S = (${problem.baseCm} × ${problem.heightCm}) : 2 = <b>${problem.area} cm²</b>! (+15 Sao)`;
            document.getElementById('tt27Text').innerText = `Em ${stName} biết phối hợp thước thẳng và ê-ke để đo độ dài đáy, đường cao và vận dụng đúng công thức tính diện tích hình tam giác (Mức: Hoàn thành tốt - TT27).`;
        } else {
            playSound(false);
            fb.style.color = '#d9480f';
            fb.innerHTML = `💡 Gợi ý AI: Hãy bấm <b>"🧲 AI Đặt Thước Mẫu"</b> để đọc số đo Đáy AB và Chiều cao CH trên 2 thước, rồi tính S = (a × h) : 2 nhé!`;
        }
    }

    document.getElementById('starCount').innerText = stars;
    document.getElementById('correctCount').innerText = solved;
}

// Khởi chạy lần đầu
generateNewProblem();
</script>
</body>
</html>
"""

components.html(geometry_app_html, height=650, scrolling=True)
