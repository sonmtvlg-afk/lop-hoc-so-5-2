import streamlit as st
import streamlit.components.v1 as components

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Phòng Thí Nghiệm Khoa Học 6 Chủ Đề - Lớp 5/2",
    page_icon="🔬",
    layout="wide"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .sci-banner {
        background: linear-gradient(135deg, #099268 0%, #0ca678 50%, #1098ad 100%);
        color: white;
        padding: 18px 24px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 6px 18px rgba(12, 166, 120, 0.28);
        margin-bottom: 12px;
    }
    .sci-banner h1 {
        font-size: 1.8rem;
        margin: 0;
        color: white;
        font-weight: 800;
    }
    .sci-banner p {
        font-size: 1rem;
        margin: 5px 0 0 0;
        color: #e6fcf5;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sci-banner">
    <h1>🔬 PHÒNG THÍ NGHIỆM KHOA HỌC 6 CHỦ ĐỀ - LỚP 5/2</h1>
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn • Chương trình Khoa học Lớp 5</p>
</div>
""", unsafe_allow_html=True)

# ==================== MÔ PHỎNG TƯƠNG TÁC HTML5 CANVAS ====================
science_lab_html = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
    * { box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; user-select: none; }
    body { margin: 0; padding: 0; background: #f8f9fa; color: #212529; }
    .lab-wrapper {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        max-width: 1220px;
        margin: 0 auto;
    }
    .stage-panel {
        flex: 2;
        min-width: 350px;
        background: white;
        border-radius: 16px;
        padding: 14px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border: 2px solid #dee2e6;
    }
    .control-panel {
        flex: 1.1;
        min-width: 310px;
        background: white;
        border-radius: 16px;
        padding: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border: 2px solid #dee2e6;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }
    .station-tabs {
        display: flex;
        gap: 6px;
        margin-bottom: 12px;
        flex-wrap: wrap;
    }
    .tab-btn {
        flex: 1;
        padding: 9px 10px;
        border: 2px solid #96f2d7;
        background: #e6fcf5;
        color: #087f5b;
        font-weight: 800;
        font-size: 0.85rem;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.2s;
        text-align: center;
    }
    .tab-btn.active {
        background: #0ca678;
        color: white;
        border-color: #087f5b;
        box-shadow: 0 4px 10px rgba(12, 166, 120, 0.3);
    }
    canvas {
        width: 100%;
        height: auto;
        background: #1e293b;
        border-radius: 14px;
        border: 3px solid #cbd5e1;
        display: block;
    }
    .ai-explain-box {
        margin-top: 10px;
        padding: 13px 16px;
        border-radius: 12px;
        background: #e3fafc;
        border-left: 6px solid #1098ad;
        color: #0b7285;
        font-size: 0.94rem;
        line-height: 1.45;
    }
    .user-bar {
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
    .ctrl-group {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 12px;
        padding: 12px;
    }
    .ctrl-title {
        font-weight: 800;
        color: #087f5b;
        margin-bottom: 8px;
        font-size: 0.94rem;
    }
    .btn-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
    }
    .act-btn {
        padding: 9px 10px;
        border: 2px solid #ced4da;
        background: white;
        border-radius: 10px;
        font-weight: 700;
        cursor: pointer;
        transition: 0.15s;
        font-size: 0.86rem;
    }
    .act-btn:hover { background: #f1f3f5; transform: translateY(-1px); }
    .act-btn.selected {
        background: #0ca678;
        color: white;
        border-color: #087f5b;
    }
    .switch-box {
        margin-top: 10px;
        background: #fff3bf;
        border: 2px dashed #f59f00;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
    }
    .big-switch {
        width: 100%;
        padding: 13px;
        border: none;
        border-radius: 12px;
        font-weight: 900;
        font-size: 1rem;
        cursor: pointer;
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .big-switch.off { background: #e03131; border: 2px solid #c92a2a; }
    .big-switch.on { background: #2f9e44; border: 2px solid #2b8a3e; }

    input[type="text"], select {
        width: 100%;
        padding: 8px 12px;
        border-radius: 8px;
        border: 2px solid #adb5bd;
        font-weight: bold;
        font-size: 0.92rem;
    }
    .quiz-card {
        background: #fff4e6;
        border: 2px solid #ffa94d;
        border-radius: 12px;
        padding: 12px;
    }
</style>
</head>
<body>

<div class="lab-wrapper">
    <!-- CỘT TRÁI: MÀN HÌNH MÔ PHỎNG -->
    <div class="stage-panel">
        <div class="station-tabs">
            <button id="tab1" class="tab-btn active" onclick="switchStation(1)">⚡ Chủ đề 2: Trạm Điện</button>
            <button id="tab2" class="tab-btn" onclick="switchStation(2)">🧪 Chủ đề 1 & 4: Chất & Vi Khuẩn</button>
            <button id="tab3" class="tab-btn" onclick="switchStation(3)">🌿 Chủ đề 3 & 6: Sinh Vật & Môi Trường</button>
        </div>

        <canvas id="labCanvas" width="760" height="420"></canvas>

        <div id="aiExplain" class="ai-explain-box">
            🤖 <b>Trợ lý Khoa học AI:</b> Chào nhà khoa học nhí <b>Hiểu Minh</b> (Lớp 5/2 - TH Bình Phước)! Hãy chọn trạm thí nghiệm bám sát 6 chủ đề sách giáo khoa Khoa học 5 để bắt đầu nhé!
        </div>
    </div>

    <!-- CỘT PHẢI: ĐIỀU KHIỂN -->
    <div class="control-panel">
        <div class="user-bar">
            <div>👩‍🔬 Nhà khoa học: <span id="scientistName">Hiểu Minh</span></div>
            <div>🌟 <span id="expScore">90</span> Điểm</div>
        </div>

        <div>
            <input type="text" id="nameInput" value="Hiểu Minh" placeholder="Nhập tên học sinh..." oninput="updateName()">
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 1: CHỦ ĐỀ 2 - NĂNG LƯỢNG ĐIỆN -->
        <div id="ctrlStation1" class="ctrl-group">
            <div class="ctrl-title">⚡ Chủ đề 2: Mạch Điện Đơn Giản & Vật Dẫn Điện</div>
            <label style="font-size:0.85rem; font-weight:bold;">1. Nguồn Điện (Bài 8, 9, 11):</label>
            <select id="powerSource" onchange="updateCircuit()" style="margin-bottom:8px; margin-top:4px;">
                <option value="battery">🔋 Pin tiểu (Năng lượng điện hóa)</option>
                <option value="solar">☀️ Năng lượng Mặt trời (Bài 11)</option>
            </select>

            <label style="font-size:0.85rem; font-weight:bold;">2. Thử nghiệm vật liệu (Bài 9):</label>
            <div class="btn-grid" style="margin-top:4px;">
                <button class="act-btn selected" id="mat_copper" onclick="selectMaterial('copper')">🪙 Thanh Đồng</button>
                <button class="act-btn" id="mat_iron" onclick="selectMaterial('iron')">🔩 Đinh Sắt</button>
                <button class="act-btn" id="mat_plastic" onclick="selectMaterial('plastic')">📏 Thước Nhựa</button>
                <button class="act-btn" id="mat_wood" onclick="selectMaterial('wood')">🪵 Gỗ Khô</button>
            </div>

            <div class="switch-box">
                <div style="font-size:0.82rem; font-weight:bold; margin-bottom:5px; color:#5c940d;">BẤM ĐỂ ĐÓNG/MỞ MẠCH ĐIỆN:</div>
                <button id="bigSwitchBtn" class="big-switch off" onclick="toggleSwitch()">🔴 CÔNG TẮC: ĐANG MỞ (Hở mạch)</button>
            </div>
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 2: CHỦ ĐỀ 1 & 4 - CHẤT & VI KHUẨN -->
        <div id="ctrlStation2" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">🧪 Chủ đề 1 & 4: Trạng Thái Chất & Vi Khuẩn</div>
            <label style="font-size:0.85rem; font-weight:bold;">Chọn nội dung thí nghiệm:</label>
            <div class="btn-grid" style="margin-top:6px; margin-bottom:10px;">
                <button class="act-btn selected" id="exp_state" onclick="selectStateExp('state')">🧊 Bài 4: Thể Rắn - Lỏng - Khí</button>
                <button class="act-btn" id="exp_bac" onclick="selectStateExp('bac')">🦠 Bài 19: Vi khuẩn Lên men có ích</button>
            </div>
            <div style="font-size:0.85rem; color:#087f5b; font-weight:bold;">
                👉 Khám phá tính chất của chất và vai trò vi khuẩn trong đời sống.
            </div>
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 3: CHỦ ĐỀ 3 & 6 - SINH VẬT & MÔI TRƯỜNG -->
        <div id="ctrlStation3" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">🌿 Chủ đề 3 & 6: Sinh Vật, Môi Trường & Đất[cite: 9]</div>
            <label style="font-size:0.85rem; font-weight:bold;">Chọn nội dung tìm hiểu:</label>
            <div class="btn-grid" style="margin-top:6px; margin-bottom:10px;">
                <button class="act-btn selected" id="eco_soil" onclick="selectEcoExp('soil')">🌱 Bài 1 & 2: Vai trò & Bảo vệ Đất</button>
                <button class="act-btn" id="eco_food" onclick="selectEcoExp('food')">🐇 Bài 13 & 28: Chuỗi thức ăn tự nhiên</button>
            </div>
            <div style="font-size:0.85rem; color:#087f5b; font-weight:bold;">
                👉 Tìm hiểu về môi trường sống và mối quan hệ giữa các sinh vật[cite: 9].
            </div>
        </div>

        <!-- CÂU HỎI KẾT LUẬN -->
        <div class="quiz-card">
            <div style="font-weight:800; color:#d9480f; margin-bottom:4px;">🧠 Thử Thách Khoa Học Lớp 5:</div>
            <div id="quizQuestion" style="font-size:0.9rem; font-weight:600; margin-bottom:6px;">
                Theo Bài 9 (Chủ đề 2), vật liệu nào dẫn điện giúp bóng đèn sáng?[cite: 9]
            </div>
            <div class="btn-grid" id="quizOptions">
                <button class="act-btn" onclick="answerQuiz(true)">🪙 Thanh đồng & Đinh sắt</button>
                <button class="act-btn" onclick="answerQuiz(false)">📏 Thước nhựa & Gỗ khô</button>
            </div>
            <div id="quizFeedback" style="margin-top:5px; font-size:0.88rem; font-weight:bold;"></div>
        </div>
    </div>
</div>

<script>
const canvas = document.getElementById('labCanvas');
const ctx = canvas.getContext('2d');

let currentStation = 1;
let expScore = 90;
let tick = 0;

// Trạm 1
let circuit = {
    source: 'battery',
    material: 'copper',
    switchClosed: false,
    conductors: ['copper', 'iron'],
    matNames: { copper: 'Thanh Đồng', iron: 'Đinh Sắt', plastic: 'Thước Nhựa', wood: 'Gỗ Khô' }
};

// Trạm 2
let stateBacMode = 'state';

// Trạm 3
let ecoMode = 'soil';

function playTone(win) {
    try {
        const ac = new (window.AudioContext || window.webkitAudioContext)();
        const freqs = win ? [523, 659, 784, 1046] : [220, 160];
        freqs.forEach((f, idx) => {
            const o = ac.createOscillator();
            const g = ac.createGain();
            o.type = win ? 'triangle' : 'sawtooth';
            o.frequency.setValueAtTime(f, ac.currentTime + idx * 0.08);
            g.gain.setValueAtTime(0.15, ac.currentTime + idx * 0.08);
            g.gain.exponentialRampToValueAtTime(0.001, ac.currentTime + idx * 0.08 + 0.22);
            o.connect(g); g.connect(ac.destination);
            o.start(ac.currentTime + idx * 0.08);
            o.stop(ac.currentTime + idx * 0.08 + 0.22);
        });
    } catch(e) {}
}

function updateName() {
    const val = document.getElementById('nameInput').value || 'Hiểu Minh';
    document.getElementById('scientistName').innerText = val;
}

function switchStation(stNum) {
    currentStation = stNum;
    [1, 2, 3].forEach(n => {
        document.getElementById('tab' + n).className = 'tab-btn' + (n === stNum ? ' active' : '');
        document.getElementById('ctrlStation' + n).style.display = (n === stNum ? 'block' : 'none');
    });
    document.getElementById('quizFeedback').innerText = '';

    const qText = document.getElementById('quizQuestion');
    const qOpts = document.getElementById('quizOptions');

    if (stNum === 1) {
        updateCircuitExplanation();
        qText.innerText = "Theo Bài 9 (Chủ đề 2), vật liệu nào dẫn điện giúp bóng đèn sáng?[cite: 9]";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">🪙 Thanh đồng & Đinh sắt</button><button class="act-btn" onclick="answerQuiz(false)">📏 Thước nhựa & Gỗ khô</button>`;
    } else if (stNum === 2) {
        document.getElementById('aiExplain').innerHTML = `🧪 <b>Chủ đề 1 & 4:</b> Khám phá tính chất thể rắn, lỏng, khí của chất (Bài 4) và vi khuẩn lên men có ích trong thực phẩm (Bài 19)[cite: 9].`;
        qText.innerText = "Theo Bài 19 (Chủ đề 4), vi khuẩn nào được ứng dụng để làm sữa chua?[cite: 9]";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">🛡️ Vi khuẩn lên men (Lactic)</button><button class="act-btn" onclick="answerQuiz(false)">🦠 Vi khuẩn gây bệnh tả</button>`;
    } else {
        document.getElementById('aiExplain').innerHTML = `🌿 <b>Chủ đề 3 & 6:</b> Tìm hiểu vai trò của đất đối với cây trồng (Bài 1) và chuỗi thức ăn trong tự nhiên (Bài 13, 28)[cite: 9].`;
        qText.innerText = "Theo Chủ đề 3, sinh vật nào là sinh vật sản xuất trong chuỗi thức ăn?[cite: 9]";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">🌱 Thực vật (Cỏ xanh)</button><button class="act-btn" onclick="answerQuiz(false)">🦊 Động vật ăn thịt</button>`;
    }
}

function answerQuiz(isCorrect) {
    const fb = document.getElementById('quizFeedback');
    const stName = document.getElementById('nameInput').value || 'Hiểu Minh';
    if (isCorrect) {
        playTone(true);
        expScore += 10;
        document.getElementById('expScore').innerText = expScore;
        fb.style.color = '#2b8a3e';
        fb.innerText = `🎉 Chính xác tuyệt vời, em ${stName} nắm rất chắc bài học! (+10 Điểm)`;
    } else {
        playTone(false);
        fb.style.color = '#e03131';
        fb.innerText = `💡 Chưa đúng rồi! Em quan sát kĩ mô hình thí nghiệm để thử lại nhé!`;
    }
}

// Trạm 1 logic
function selectMaterial(mat) {
    circuit.material = mat;
    ['copper', 'iron', 'plastic', 'wood'].forEach(m => {
        document.getElementById('mat_' + m).className = 'act-btn' + (m === mat ? ' selected' : '');
    });
    if (circuit.switchClosed) playTone(circuit.conductors.includes(mat));
    updateCircuitExplanation();
}

function toggleSwitch() {
    circuit.switchClosed = !circuit.switchClosed;
    const btn = document.getElementById('bigSwitchBtn');
    if (circuit.switchClosed) {
        btn.className = 'big-switch on';
        btn.innerText = '🟢 CÔNG TẮC: ĐANG ĐÓNG (Mạch kín)';
        playTone(circuit.conductors.includes(circuit.material));
    } else {
        btn.className = 'big-switch off';
        btn.innerText = '🔴 CÔNG TẮC: ĐANG MỞ (Hở mạch)';
    }
    updateCircuitExplanation();
}

function updateCircuit() {
    circuit.source = document.getElementById('powerSource').value;
    updateCircuitExplanation();
}

function updateCircuitExplanation() {
    const box = document.getElementById('aiExplain');
    const isCond = circuit.conductors.includes(circuit.material);
    const mName = circuit.matNames[circuit.material];

    if (!circuit.switchClosed) {
        box.innerHTML = `🤖 <b>Trạm Điện (Chủ đề 2):</b> Công tắc đang <b>Mở</b>[cite: 9]. Hãy chọn <b>${mName}</b> và bấm nút công tắc màu xanh để đóng mạch điện (Bài 9)[cite: 9]!`;
    } else if (isCond) {
        box.innerHTML = `✅ <b>Đèn Sáng (Bài 9)!</b> <b>${mName}</b> là <b>VẬT DẪN ĐIỆN</b>, cho dòng điện chạy qua làm sáng bóng đèn[cite: 9].`;
    } else {
        box.innerHTML = `⚠️ <b>Đèn Tắt (Bài 9)!</b> <b>${mName}</b> là <b>VẬT CÁCH ĐIỆN</b>, không cho dòng điện chạy qua[cite: 9].`;
    }
}

// Trạm 2 logic
function selectStateExp(mode) {
    stateBacMode = mode;
    document.getElementById('exp_state').className = 'act-btn' + (mode === 'state' ? ' selected' : '');
    document.getElementById('exp_bac').className = 'act-btn' + (mode === 'bac' ? ' selected' : '');
    const box = document.getElementById('aiExplain');
    if (mode === 'state') {
        box.innerHTML = `🧊 <b>Bài 4 (Chủ đề 1):</b> Mô phỏng các trạng thái Rắn (Nước đá), Lỏng (Nước) và Khí (Hơi nước)[cite: 9].`;
    } else {
        box.innerHTML = `🦠 <b>Bài 19 (Chủ đề 4):</b> Vi khuẩn lên men (Lactic) có ích giúp muối dưa chua và làm sữa chua thơm ngon[cite: 9].`;
    }
}

// Trạm 3 logic
function selectEcoExp(mode) {
    ecoMode = mode;
    document.getElementById('eco_soil').className = 'act-btn' + (mode === 'soil' ? ' selected' : '');
    document.getElementById('eco_food').className = 'act-btn' + (mode === 'food' ? ' selected' : '');
    const box = document.getElementById('aiExplain');
    if (mode === 'soil') {
        box.innerHTML = `🌱 <b>Bài 1 & 2 (Chủ đề 1 & 6):</b> Đất cung cấp chất dinh dưỡng, nước và không khí cho cây trồng. Cần chống xói mòn và ô nhiễm đất[cite: 9].`;
    } else {
        box.innerHTML = `🌿 <b>Bài 13 & 28 (Chủ đề 3 & 6):</b> Chuỗi thức ăn tự nhiên bắt đầu từ Thực vật (sản xuất) sang Động vật ăn cỏ và Động vật ăn thịt[cite: 9].`;
    }
}

// Render Canvas 60 FPS
function drawStation1() {
    ctx.fillStyle = '#0f172a'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    const isFlowing = circuit.switchClosed && circuit.conductors.includes(circuit.material);

    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 17px sans-serif';
    ctx.fillText('⚡ CHỦ ĐỀ 2: MẠCH ĐIỆN & VẬT DẪN ĐIỆN (BÀI 9)', 25, 32);

    ctx.strokeStyle = isFlowing ? '#facc15' : '#64748b'; ctx.lineWidth = 6;
    ctx.strokeRect(120, 90, 520, 240);

    if (isFlowing) {
        ctx.fillStyle = '#fef08a';
        const perim = (520 + 240) * 2;
        for (let i = 0; i < 16; i++) {
            let d = ((i * (perim / 16)) + tick * 3.5) % perim;
            let ex = 120, ey = 90;
            if (d < 520) { ex = 120 + d; ey = 90; }
            else if (d < 520 + 240) { ex = 640; ey = 90 + (d - 520); }
            else if (d < 520 * 2 + 240) { ex = 640 - (d - 760); ey = 330; }
            else { ex = 120; ey = 330 - (d - 1280); }
            ctx.beginPath(); ctx.arc(ex, ey, 5, 0, Math.PI * 2); ctx.fill();
        }
    }

    // Nguồn
    ctx.fillStyle = '#1e293b'; ctx.fillRect(75, 155, 90, 110);
    if (circuit.source === 'battery') {
        ctx.fillStyle = '#f97316'; ctx.fillRect(92, 170, 56, 28);
        ctx.fillStyle = '#334155'; ctx.fillRect(92, 198, 56, 55);
        ctx.fillStyle = 'white'; ctx.font = 'bold 13px sans-serif'; ctx.fillText('+ PIN -', 98, 232);
    } else {
        ctx.fillStyle = '#0284c7'; ctx.fillRect(80, 165, 80, 85);
        ctx.fillStyle = '#fde047'; ctx.font = 'bold 22px sans-serif'; ctx.fillText('☀️', 108, 218);
    }

    // Công tắc
    ctx.fillStyle = '#0f172a'; ctx.fillRect(260, 70, 90, 38);
    ctx.strokeStyle = '#f8fafc'; ctx.lineWidth = 5;
    ctx.beginPath(); ctx.moveTo(265, 90);
    if (circuit.switchClosed) ctx.lineTo(345, 90);
    else ctx.lineTo(335, 52);
    ctx.stroke();

    // Đèn
    ctx.fillStyle = '#0f172a'; ctx.fillRect(600, 150, 80, 110);
    if (isFlowing) {
        const grad = ctx.createRadialGradient(640, 200, 10, 640, 200, 65);
        grad.addColorStop(0, 'rgba(253, 224, 71, 0.95)'); grad.addColorStop(1, 'rgba(253, 224, 71, 0)');
        ctx.fillStyle = grad; ctx.beginPath(); ctx.arc(640, 200, 65, 0, Math.PI * 2); ctx.fill();
    }
    ctx.beginPath(); ctx.arc(640, 200, 28, 0, Math.PI * 2);
    ctx.fillStyle = isFlowing ? '#fef08a' : '#475569'; ctx.fill(); ctx.stroke();
    ctx.fillStyle = isFlowing ? '#fde047' : '#cbd5e1'; ctx.font = 'bold 13px sans-serif';
    ctx.fillText(isFlowing ? '💡 ĐÈN SÁNG' : '💡 Đèn tắt', 605, 265);

    // Vật liệu
    ctx.fillStyle = '#1e293b'; ctx.fillRect(280, 300, 200, 60);
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2; ctx.strokeRect(280, 300, 200, 60);
    ctx.fillStyle = '#d97706'; ctx.fillRect(295, 316, 170, 26);
    ctx.fillStyle = 'white'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'center';
    ctx.fillText(circuit.matNames[circuit.material], 380, 334);
    ctx.textAlign = 'left';
}

function drawStation2() {
    ctx.fillStyle = '#0f172a'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 17px sans-serif';
    ctx.fillText(stateBacMode === 'state' ? '🧊 CHỦ ĐỀ 1: TRẠNG THÁI RẮN - LỎNG - KHÍ (BÀI 4)[cite: 9]' : '🦠 CHỦ ĐỀ 4: VI KHUẨN CÓ ÍCH (BÀI 19)[cite: 9]', 25, 32);

    if (stateBacMode === 'state') {
        // Mô phỏng 3 trạng thái chất
        ctx.fillStyle = 'rgba(186, 230, 253, 0.85)'; ctx.fillRect(100, 130, 150, 180);
        ctx.fillStyle = 'white'; ctx.font = 'bold 14px sans-serif'; ctx.fillText('🧊 Thể Rắn (Đá)', 120, 220);

        ctx.fillStyle = 'rgba(56, 189, 248, 0.6)'; ctx.fillRect(305, 130, 150, 180);
        ctx.fillStyle = 'white'; ctx.fillText('💧 Thể Lỏng (Nước)', 318, 220);

        ctx.fillStyle = 'rgba(255, 255, 255, 0.45)'; ctx.fillRect(510, 130, 150, 180);
        ctx.fillStyle = 'white'; ctx.fillText('♨️ Thể Khí (Hơi)', 525, 220);
    } else {
        // Mô phỏng vi khuẩn lên men
        ctx.fillStyle = '#1e293b'; ctx.strokeStyle = '#64748b'; ctx.lineWidth = 6;
        ctx.beginPath(); ctx.arc(380, 220, 120, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
        for (let i = 0; i < 18; i++) {
            let bx = 330 + Math.sin(i + tick * 0.05) * 60;
            let by = 190 + Math.cos(i + tick * 0.05) * 50;
            ctx.fillStyle = '#4ade80';
            ctx.beginPath(); ctx.arc(bx, by, 9, 0, Math.PI * 2); ctx.fill();
        }
        ctx.fillStyle = 'white'; ctx.font = 'bold 16px sans-serif'; ctx.textAlign = 'center';
        ctx.fillText('🛡️ Vi khuẩn Lactic (Lên men sữa chua có ích)', 380, 370);
        ctx.textAlign = 'left';
    }
}

function drawStation3() {
    ctx.fillStyle = '#0284c7'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'white'; ctx.font = 'bold 17px sans-serif';
    ctx.fillText(ecoMode === 'soil' ? '🌱 CHỦ ĐỀ 1 & 6: VAI TRÒ VÀ BẢO VỆ ĐẤT (BÀI 1 & 2)[cite: 9]' : '🌿 CHỦ ĐỀ 3 & 6: CHUỖI THỨC ĂN TỰ NHIÊN (BÀI 13 & 28)[cite: 9]', 25, 32);

    if (ecoMode === 'soil') {
        // Mô phỏng đất trồng cây
        ctx.fillStyle = '#b45309'; ctx.fillRect(0, 280, canvas.width, 140);
        ctx.fillStyle = '#78350f'; ctx.fillRect(0, 340, canvas.width, 80);
        ctx.fillStyle = '#fde047'; ctx.font = 'bold 24px sans-serif'; ctx.fillText('☀️', 620, 90);
        ctx.fillStyle = '#22c55e'; ctx.font = 'bold 50px sans-serif'; ctx.fillText('🌳', 350, 275);
        ctx.fillStyle = 'white'; ctx.font = 'bold 15px sans-serif';
        ctx.fillText('Đất cung cấp chất dinh dưỡng, nước và không khí cho cây phát triển xanh tốt!', 100, 380);
    } else {
        // Chuỗi thức ăn
        ctx.fillStyle = '#16a34a'; ctx.fillRect(0, 310, canvas.width, 110);
        ctx.fillStyle = '#22c55e'; ctx.font = 'bold 45px sans-serif'; ctx.fillText('🌱 Cỏ', 160, 285);
        ctx.fillStyle = 'white'; ctx.font = 'bold 24px sans-serif'; ctx.fillText('➡️', 300, 260);
        ctx.fillStyle = 'white'; ctx.font = 'bold 45px sans-serif'; ctx.fillText('🐇 Thỏ', 390, 285);
        ctx.fillStyle = 'white'; ctx.font = 'bold 24px sans-serif'; ctx.fillText('➡️', 530, 260);
        ctx.fillStyle = '#f97316'; ctx.font = 'bold 45px sans-serif'; ctx.fillText('🦊 Cáo', 610, 285);
    }
}

function animate() {
    tick++;
    if (currentStation === 1) drawStation1();
    else if (currentStation === 2) drawStation2();
    else drawStation3();
    requestAnimationFrame(animate);
}
animate();
</script>
</body>
</html>
"""

components.html(science_lab_html, height=600, scrolling=True)
