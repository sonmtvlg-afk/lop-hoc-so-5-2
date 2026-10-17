import streamlit as st
import streamlit.components.v1 as components

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Phòng Thí Nghiệm Khoa Học Lớp 5 - TH Bình Phước",
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
        padding: 16px 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 6px 18px rgba(12, 166, 120, 0.28);
        margin-bottom: 10px;
    }
    .sci-banner h1 {
        font-size: 1.7rem;
        margin: 0;
        color: white;
        font-weight: 800;
    }
    .sci-banner p {
        font-size: 0.95rem;
        margin: 4px 0 0 0;
        color: #e6fcf5;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sci-banner">
    <h1>🔬 PHÒNG THÍ NGHIỆM KHOA HỌC TRỌNG TÂM - LỚP 5/2</h1>
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn • Đồ họa sắc nét, trực quan cho học sinh</p>
</div>
""", unsafe_allow_html=True)

# ==================== MÔ PHỎNG TƯƠNG TÁC HTML5 CANVAS SẮC NÉT ====================
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
        gap: 8px;
        margin-bottom: 12px;
    }
    .tab-btn {
        flex: 1;
        padding: 12px;
        border: 2px solid #96f2d7;
        background: #e6fcf5;
        color: #087f5b;
        font-weight: 800;
        font-size: 0.95rem;
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
        background: #0f172a;
        border-radius: 14px;
        border: 3px solid #cbd5e1;
        display: block;
    }
    .ai-explain-box {
        margin-top: 10px;
        padding: 14px 18px;
        border-radius: 12px;
        background: #e3fafc;
        border-left: 6px solid #1098ad;
        color: #0b7285;
        font-size: 1rem;
        font-weight: 600;
        line-height: 1.5;
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
        font-size: 1rem;
        color: #d9480f;
    }
    .ctrl-group {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 12px;
        padding: 14px;
    }
    .ctrl-title {
        font-weight: 800;
        color: #087f5b;
        margin-bottom: 10px;
        font-size: 1.05rem;
    }
    .btn-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
    }
    .act-btn {
        padding: 11px 12px;
        border: 2px solid #ced4da;
        background: white;
        border-radius: 10px;
        font-weight: 700;
        cursor: pointer;
        transition: 0.15s;
        font-size: 0.95rem;
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
        padding: 14px;
        border: none;
        border-radius: 12px;
        font-weight: 900;
        font-size: 1.05rem;
        cursor: pointer;
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .big-switch.off { background: #e03131; border: 2px solid #c92a2a; }
    .big-switch.on { background: #2f9e44; border: 2px solid #2b8a3e; }

    input[type="text"], select {
        width: 100%;
        padding: 10px 12px;
        border-radius: 8px;
        border: 2px solid #adb5bd;
        font-weight: bold;
        font-size: 1rem;
    }
    .quiz-card {
        background: #fff4e6;
        border: 2px solid #ffa94d;
        border-radius: 12px;
        padding: 14px;
    }
</style>
</head>
<body>

<div class="lab-wrapper">
    <!-- CỘT TRÁI: MÀN HÌNH MÔ PHỎNG SẮC NÉT -->
    <div class="stage-panel">
        <div class="station-tabs">
            <button id="tab1" class="tab-btn active" onclick="switchStation(1)">⚡ Trạm 1: Năng Lượng Điện</button>
            <button id="tab2" class="tab-btn" onclick="switchStation(2)">👶 Trạm 2: Phát Triển & Sức Khỏe</button>
        </div>

        <canvas id="labCanvas" width="760" height="420"></canvas>

        <div id="aiExplain" class="ai-explain-box">
            🤖 <b>Trợ lý Khoa học AI:</b> Chào nhà khoa học nhí <b>Hiểu Minh</b>! Hãy chọn trạm thí nghiệm để quan sát hình ảnh mô phỏng trực quan và sắc nét nhất nhé!
        </div>
    </div>

    <!-- CỘT PHẢI: ĐIỀU KHIỂN RÕ RÀNG -->
    <div class="control-panel">
        <div class="user-bar">
            <div>👩‍🔬 Học sinh: <span id="scientistName">Hiểu Minh</span></div>
            <div>🌟 <span id="expScore">95</span> Điểm</div>
        </div>

        <div>
            <input type="text" id="nameInput" value="Hiểu Minh" placeholder="Nhập tên học sinh..." oninput="updateName()">
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 1: NĂNG LƯỢNG ĐIỆN -->
        <div id="ctrlStation1" class="ctrl-group">
            <div class="ctrl-title">⚡ Chủ đề 2: Mạch Điện Đơn Giản (Bài 9)</div>
            <label style="font-size:0.92rem; font-weight:bold;">1. Chọn Nguồn Điện:</label>
            <select id="powerSource" onchange="updateCircuit()" style="margin-bottom:10px; margin-top:4px;">
                <option value="battery">🔋 Pin tiểu 1,5V - 3V</option>
                <option value="solar">☀️ Tấm Pin Năng lượng Mặt trời (Bài 11)</option>
            </select>

            <label style="font-size:0.92rem; font-weight:bold;">2. Chọn vật liệu thử nghiệm (Bài 9)[cite: 9]:</label>
            <div class="btn-grid" style="margin-top:6px;">
                <button class="act-btn selected" id="mat_copper" onclick="selectMaterial('copper')">🪙 Thanh Đồng</button>
                <button class="act-btn" id="mat_iron" onclick="selectMaterial('iron')">🔩 Đinh Sắt</button>
                <button class="act-btn" id="mat_plastic" onclick="selectMaterial('plastic')">📏 Thước Nhựa</button>
                <button class="act-btn" id="mat_wood" onclick="selectMaterial('wood')">🪵 Gỗ Khô</button>
            </div>

            <div class="switch-box">
                <div style="font-size:0.88rem; font-weight:bold; margin-bottom:6px; color:#5c940d;">BẤM ĐỂ ĐÓNG/MỞ MẠCH ĐIỆN:</div>
                <button id="bigSwitchBtn" class="big-switch off" onclick="toggleSwitch()">🔴 CÔNG TẮC: ĐANG MỞ (Hở mạch)</button>
            </div>
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 2: PHÁT TRIỂN & SỨC KHỎE -->
        <div id="ctrlStation2" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">👶 Chủ đề 5: Con Người & Sức Khỏe (Bài 23 & 25)[cite: 9]</div>
            <label style="font-size:0.92rem; font-weight:bold;">Chọn nội dung tìm hiểu:</label>
            <div class="btn-grid" style="margin-top:6px; margin-bottom:10px;">
                <button class="act-btn selected" id="health_dev" onclick="selectHealthMode('dev')">👶 Giai Đoạn Phát Triển (Bài 23)[cite: 9]</button>
                <button class="act-btn" id="health_care" onclick="selectHealthMode('care')">💪 Chăm Sức Khỏe Tuổi Dậy Thì (Bài 25)[cite: 9]</button>
            </div>
            <div style="font-size:0.9rem; color:#087f5b; font-weight:bold;" id="healthSubDesc">
                👉 Quan sát các mốc phát triển chiều cao và thể chất con người.
            </div>
        </div>

        <!-- CÂU HỎI TRỌNG TÂM -->
        <div class="quiz-card">
            <div style="font-weight:800; color:#d9480f; margin-bottom:6px; font-size:1rem;">🧠 Thử Thách Khoa Học Trọng Tâm:</div>
            <div id="quizQuestion" style="font-size:0.95rem; font-weight:600; margin-bottom:8px;">
                Theo Bài 9 (Chủ đề 2), vật liệu nào dẫn điện giúp bóng đèn sáng?[cite: 9]
            </div>
            <div class="btn-grid" id="quizOptions">
                <button class="act-btn" onclick="answerQuiz(true)">🪙 Thanh đồng & Đinh sắt</button>
                <button class="act-btn" onclick="answerQuiz(false)">📏 Thước nhựa & Gỗ khô</button>
            </div>
            <div id="quizFeedback" style="margin-top:6px; font-size:0.92rem; font-weight:bold;"></div>
        </div>
    </div>
</div>

<script>
const canvas = document.getElementById('labCanvas');
const ctx = canvas.getContext('2d');

let currentStation = 1;
let expScore = 95;
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
let healthMode = 'dev'; // 'dev' hoặc 'care'

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
    [1, 2].forEach(n => {
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
    } else {
        updateHealthExplanation();
        qText.innerText = "Theo Chủ đề 5, việc làm nào cần thiết để chăm sóc sức khỏe tuổi dậy thì (Bài 25)?[cite: 9]";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">🧼 Vệ sinh sạch sẽ & dinh dưỡng đủ chất</button><button class="act-btn" onclick="answerQuiz(false)">🍕 Ăn đồ mỡ & thức khuya</button>`;
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
        fb.innerText = `🎉 Chính xác tuyệt vời, em ${stName} rất am hiểu kiến thức trọng tâm! (+10 Điểm)`;
    } else {
        playTone(false);
        fb.style.color = '#e03131';
        fb.innerText = `💡 Chưa đúng rồi! Em quan sát kĩ hình minh họa để thử lại nhé!`;
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
        box.innerHTML = `🤖 <b>Trạm Điện (Trọng tâm Chủ đề 2):</b> Công tắc đang <b>Mở</b>[cite: 9]. Hãy chọn <b>${mName}</b> và bấm nút công tắc màu xanh lớn để đóng mạch điện (Bài 9)[cite: 9]!`;
    } else if (isCond) {
        box.innerHTML = `✅ <b>Đèn Sáng Rực (Bài 9)!</b> <b>${mName}</b> là <b>VẬT DẪN ĐIỆN</b>, cho dòng điện chạy qua làm sáng bóng đèn[cite: 9].`;
    } else {
        box.innerHTML = `⚠️ <b>Đèn Tắt (Bài 9)!</b> <b>${mName}</b> là <b>VẬT CÁCH ĐIỆN</b>, dòng điện không thể đi qua[cite: 9].`;
    }
}

// Trạm 2 logic
function selectHealthMode(mode) {
    healthMode = mode;
    document.getElementById('health_dev').className = 'act-btn' + (mode === 'dev' ? ' selected' : '');
    document.getElementById('health_care').className = 'act-btn' + (mode === 'care' ? ' selected' : '');
    updateHealthExplanation();
}

function updateHealthExplanation() {
    const box = document.getElementById('aiExplain');
    const subDesc = document.getElementById('healthSubDesc');
    if (healthMode === 'dev') {
        subDesc.innerText = "👉 Quan sát các mốc phát triển chiều cao và thể chất con người.";
        box.innerHTML = `👶 <b>Bài 23 (Chủ đề 5):</b> Con người lớn lên qua các giai đoạn: Sơ sinh ➡️ Trẻ em ➡️ Tuổi dậy thì (phát triển mạnh mẽ về chiều cao, cân nặng) ➡️ Trưởng thành ➡️ Tuổi già[cite: 9].`;
    } else {
        subDesc.innerText = "👉 Tìm hiểu cách giữ vệ sinh và dinh dưỡng tuổi dậy thì.";
        box.innerHTML = `💪 <b>Bài 25 (Chủ đề 5):</b> Chăm sóc sức khỏe tuổi dậy thì: Vệ sinh cá nhân sạch sẽ, ăn uống đầy đủ chất dinh dưỡng (4 nhóm chất), tập thể thao và giữ tinh thần vui tươi[cite: 9].`;
    }
}

// Render Canvas 60 FPS cực sắc nét
function drawStation1() {
    ctx.fillStyle = '#0f172a'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    const isFlowing = circuit.switchClosed && circuit.conductors.includes(circuit.material);

    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 18px sans-serif';
    ctx.fillText('⚡ MẠCH ĐIỆN ĐƠN GIẢN & VẬT DẪN ĐIỆN (BÀI 9)[cite: 9]', 25, 35);

    ctx.strokeStyle = isFlowing ? '#facc15' : '#64748b'; ctx.lineWidth = 6;
    ctx.strokeRect(100, 90, 560, 240);

    if (isFlowing) {
        ctx.fillStyle = '#fef08a';
        const perim = (560 + 240) * 2;
        for (let i = 0; i < 18; i++) {
            let d = ((i * (perim / 18)) + tick * 4) % perim;
            let ex = 100, ey = 90;
            if (d < 560) { ex = 100 + d; ey = 90; }
            else if (d < 560 + 240) { ex = 660; ey = 90 + (d - 560); }
            else if (d < 560 * 2 + 240) { ex = 660 - (d - 800); ey = 330; }
            else { ex = 100; ey = 330 - (d - 1360); }
            ctx.beginPath(); ctx.arc(ex, ey, 5.5, 0, Math.PI * 2); ctx.fill();
        }
    }

    // Nguồn
    ctx.fillStyle = '#1e293b'; ctx.fillRect(60, 150, 90, 120);
    if (circuit.source === 'battery') {
        ctx.fillStyle = '#f97316'; ctx.fillRect(77, 165, 56, 30);
        ctx.fillStyle = '#334155'; ctx.fillRect(77, 195, 56, 60);
        ctx.fillStyle = 'white'; ctx.font = 'bold 14px sans-serif'; ctx.fillText('+ PIN -', 82, 232);
    } else {
        ctx.fillStyle = '#0284c7'; ctx.fillRect(65, 160, 80, 90);
        ctx.fillStyle = '#fde047'; ctx.font = 'bold 24px sans-serif'; ctx.fillText('☀️', 92, 215);
    }

    // Công tắc
    ctx.fillStyle = '#0f172a'; ctx.fillRect(250, 70, 100, 40);
    ctx.strokeStyle = '#f8fafc'; ctx.lineWidth = 5;
    ctx.beginPath(); ctx.moveTo(255, 90);
    if (circuit.switchClosed) ctx.lineTo(345, 90);
    else ctx.lineTo(335, 50);
    ctx.stroke();

    // Đèn
    ctx.fillStyle = '#0f172a'; ctx.fillRect(610, 145, 90, 120);
    if (isFlowing) {
        const grad = ctx.createRadialGradient(655, 205, 12, 655, 205, 75);
        grad.addColorStop(0, 'rgba(253, 224, 71, 0.95)'); grad.addColorStop(1, 'rgba(253, 224, 71, 0)');
        ctx.fillStyle = grad; ctx.beginPath(); ctx.arc(655, 205, 75, 0, Math.PI * 2); ctx.fill();
    }
    ctx.beginPath(); ctx.arc(655, 205, 30, 0, Math.PI * 2);
    ctx.fillStyle = isFlowing ? '#fef08a' : '#475569'; ctx.fill(); ctx.stroke();
    ctx.fillStyle = isFlowing ? '#fde047' : '#cbd5e1'; ctx.font = 'bold 14px sans-serif';
    ctx.fillText(isFlowing ? '💡 ĐÈN SÁNG' : '💡 Đèn tắt', 615, 275);

    // Vật liệu thử
    ctx.fillStyle = '#1e293b'; ctx.fillRect(270, 300, 220, 60);
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2; ctx.strokeRect(270, 300, 220, 60);
    ctx.fillStyle = '#d97706'; ctx.fillRect(285, 316, 190, 28);
    ctx.fillStyle = 'white'; ctx.font = 'bold 15px sans-serif'; ctx.textAlign = 'center';
    ctx.fillText(circuit.matNames[circuit.material], 380, 335);
    ctx.textAlign = 'left';
}

function drawStation2() {
    ctx.fillStyle = '#0f172a'; ctx.fillRect(0, 0, canvas.width, canvas.height);

    if (healthMode === 'dev') {
        ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 17px sans-serif';
        ctx.fillText('👶 CHỦ ĐỀ 5: CÁC GIAI ĐOẠN PHÁT TRIỂN (BÀI 23)[cite: 9]', 25, 35);

        const stages = [
            { label: 'Sơ sinh', icon: '👶', x: 100 },
            { label: 'Trẻ em', icon: '🧒', x: 250 },
            { label: 'Tuổi dậy thì', icon: '🧑‍🎓', x: 400 },
            { label: 'Trưởng thành', icon: '👨‍💼', x: 550 },
            { label: 'Tuổi già', icon: '🧓', x: 680 }
        ];

        stages.forEach((s, idx) => {
            let isHighlight = idx === 2; // Nhấn mạnh tuổi dậy thì lớp 5
            ctx.fillStyle = isHighlight ? '#0ca678' : '#334155';
            ctx.beginPath(); ctx.arc(s.x, 210, isHighlight ? 46 : 38, 0, Math.PI * 2); ctx.fill();
            ctx.strokeStyle = isHighlight ? '#fde047' : '#64748b'; ctx.lineWidth = isHighlight ? 4 : 2; ctx.stroke();

            ctx.font = 'bold 30px sans-serif'; ctx.textAlign = 'center';
            ctx.fillText(s.icon, s.x, 221);

            ctx.fillStyle = isHighlight ? '#fde047' : 'white'; ctx.font = 'bold 14px sans-serif';
            ctx.fillText(s.label, s.x, 280);
            ctx.textAlign = 'left';
        });
    } else {
        ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 17px sans-serif';
        ctx.fillText('💪 CHỦ ĐỀ 5: CHĂM SÓC SỨC KHỎE TUỔI DẬY THÌ (BÀI 25)[cite: 9]', 25, 35);

        const cares = [
            { title: '🧼 VỆ SINH SẠCH SẼ', desc: 'Tắm giặt, thay đồ hàng ngày', x: 180 },
            { title: '🥗 DINH DƯỠNG ĐỦ CHẤT', desc: 'Ăn đủ 4 nhóm chất, uống nhiều nước', x: 380 },
            { title: '⚽ THỂ THAO & TINH THẦN', desc: 'Tập thể dục, ngủ đủ giấc, vui tươi', x: 580 }
        ];

        cares.forEach(c => {
            ctx.fillStyle = '#1e293b'; ctx.strokeStyle = '#0ca678'; ctx.lineWidth = 3;
            ctx.fillRect(c.x - 85, 120, 170, 180);
            ctx.strokeRect(c.x - 85, 120, 170, 180);

            ctx.fillStyle = '#fde047'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'center';
            ctx.fillText(c.title, c.x, 155);

            ctx.fillStyle = 'white'; ctx.font = '13px sans-serif';
            ctx.fillText(c.desc.slice(0, 18), c.x, 195);
            ctx.fillText(c.desc.slice(18), c.x, 220);
            ctx.textAlign = 'left';
        });
    }
}

function animate() {
    tick++;
    if (currentStation === 1) drawStation1();
    else drawStation2();
    requestAnimationFrame(animate);
}
animate();
</script>
</body>
</html>
"""

components.html(science_lab_html, height=600, scrolling=True)
