import streamlit as st
import streamlit.components.v1 as components

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Phòng Thí Nghiệm Mạch Điện Lớp 5 - TH Bình Phước",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .sci-banner {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #00b4db 100%);
        color: white;
        padding: 16px 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 6px 18px rgba(0, 180, 219, 0.3);
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
        color: #e0f7fa;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sci-banner">
    <h1>⚡ PHÒNG THÍ NGHIỆM MẠCH ĐIỆN CHI TIẾT - LỚP 5/2</h1>
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn • Mô hình Mạch điện & Vật dẫn điện</p>
</div>
""", unsafe_allow_html=True)

# ==================== MÔ PHỎNG MẠCH ĐIỆN 60 FPS CỰC KỲ CHI TIẾT ====================
circuit_lab_html = """
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
        gap: 14px;
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
        color: #1e3c72;
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
        font-size: 0.92rem;
    }
    .act-btn:hover { background: #f1f3f5; transform: translateY(-1px); }
    .act-btn.selected {
        background: #00b4db;
        color: white;
        border-color: #0072ff;
    }
    .switch-box {
        margin-top: 12px;
        background: #fff3bf;
        border: 2px dashed #f59f00;
        border-radius: 12px;
        padding: 14px;
        text-align: center;
    }
    .big-switch {
        width: 100%;
        padding: 16px;
        border: none;
        border-radius: 12px;
        font-weight: 900;
        font-size: 1.1rem;
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
    <!-- CỘT TRÁI: MÀN HÌNH MÔ PHỎNG MẠCH ĐIỆN -->
    <div class="stage-panel">
        <canvas id="circuitCanvas" width="760" height="420"></canvas>

        <div id="aiциони" class="ai-explain-box">
            🤖 <b>Trợ lý Khoa học AI:</b> Chào nhà khoa học nhí <b>Hiểu Minh</b>! Hãy chọn nguồn điện, chọn vật liệu thử nghiệm và bấm nút công tắc lớn bên dưới để quan sát bóng đèn phát sáng nhé!
        </div>
    </div>

    <!-- CỘT PHẢI: ĐIỀU KHIỂN CHI TIẾT -->
    <div class="control-panel">
        <div class="user-bar">
            <div>👩‍🔬 Học sinh: <span id="scientistName">Hiểu Minh</span></div>
            <div>⭐ <span id="expScore">100</span> Điểm</div>
        </div>

        <div>
            <input type="text" id="nameInput" value="Hiểu Minh" placeholder="Nhập tên học sinh..." oninput="updateName()">
        </div>

        <!-- BẢNG ĐIỀU KHIỂN MẠCH ĐIỆN CHI TIẾT -->
        <div class="ctrl-group">
            <div class="ctrl-title">⚡ Bảng Điều Khiển Mạch Điện</div>
            
            <label style="font-size:0.92rem; font-weight:bold;">1. Chọn Nguồn Cấp Điện:</label>
            <select id="powerSource" onchange="updateCircuit()" style="margin-bottom:10px; margin-top:4px;">
                <option value="battery">🔋 Pin tiểu 1,5V (Nguồn điện hóa học)</option>
                <option value="solar">☀️ Tấm Pin Năng lượng Mặt trời (Bài 11)</option>
            </select>

            <label style="font-size:0.92rem; font-weight:bold;">2. Thả Vật Liệu Vào Khe Thử Nghiệm:</label>
            <div class="btn-grid" style="margin-top:6px;">
                <button class="act-btn selected" id="mat_copper" onclick="selectMaterial('copper')">🪙 Thanh Đồng</button>
                <button class="act-btn" id="mat_iron" onclick="selectMaterial('iron')">🔩 Đinh Sắt</button>
                <button class="act-btn" id="mat_saltwater" onclick="selectMaterial('saltwater')">🧂 Nước Muối</button>
                <button class="act-btn" id="mat_plastic" onclick="selectMaterial('plastic')">📏 Thước Nhựa</button>
                <button class="act-btn" id="mat_wood" onclick="selectMaterial('wood')">🪵 Gỗ Khô</button>
                <button class="act-btn" id="mat_rubber" onclick="selectMaterial('rubber')">🧤 Cục Tẩy Cao Su</button>
            </div>

            <div class="switch-box">
                <div style="font-size:0.88rem; font-weight:bold; margin-bottom:6px; color:#5c940d;">BẤM ĐỂ ĐÓNG/MỞ CÔNG TẮC:</div>
                <button id="bigSwitchBtn" class="big-switch off" onclick="toggleSwitch()">🔴 CÔNG TẮC: ĐANG MỞ (Hở mạch)</button>
            </div>
        </div>

        <!-- CÂU HỎI TRỌNG TÂM MẠCH ĐIỆN -->
        <div class="quiz-card">
            <div style="font-weight:800; color:#d9480f; margin-bottom:6px; font-size:1rem;">🧠 Thử Thách Mạch Điện Đơn Giản:</div>
            <div style="font-size:0.92rem; font-weight:600; margin-bottom:8px;">
                Theo Bài 9, vật liệu nào là vật dẫn điện giúp bóng đèn phát sáng?
            </div>
            <div class="btn-grid">
                <button class="act-btn" onclick="answerQuiz(true)">🪙 Thanh đồng & Đinh sắt</button>
                <button class="act-btn" onclick="answerQuiz(false)">📏 Thước nhựa & Gỗ khô</button>
            </div>
            <div id="quizFeedback" style="margin-top:6px; font-size:0.92rem; font-weight:bold;"></div>
        </div>
    </div>
</div>

<script>
const canvas = document.getElementById('circuitCanvas');
const ctx = canvas.getContext('2d');

let expScore = 100;
let tick = 0;

let circuit = {
    source: 'battery',
    material: 'copper',
    switchClosed: false,
    conductors: ['copper', 'iron', 'saltwater'],
    matNames: {
        copper: 'Thanh Đồng (Kim loại)',
        iron: 'Đinh Sắt (Kim loại)',
        saltwater: 'Cốc Nước Muối',
        plastic: 'Thước Nhựa',
        wood: 'Gỗ Khô',
        rubber: 'Cục Tẩy Cao Su'
    }
};

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

function selectMaterial(mat) {
    circuit.material = mat;
    ['copper', 'iron', 'saltwater', 'plastic', 'wood', 'rubber'].forEach(m => {
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
    const box = document.getElementById('aiциони');
    const isCond = circuit.conductors.includes(circuit.material);
    const mName = circuit.matNames[circuit.material];

    if (!circuit.switchClosed) {
        box.innerHTML = `🤖 <b>Trợ lý AI:</b> Công tắc đang <b>Mở (Hở mạch)</b>. Hãy chọn <b>${mName}</b> và bấm nút công tắc lớn màu xanh để đóng mạch điện nhé!`;
    } else if (isCond) {
        box.innerHTML = `✅ <b>ĐÈN SÁNG RỰC & QUAY TÍT!</b> <b>${mName}</b> là <b>VẬT DẪN ĐIỆN</b>, cho phép dòng điện (các hạt electron vàng) chạy qua mạch kín từ nguồn đến bóng đèn!`;
    } else {
        box.innerHTML = `⚠️ <b>BÓNG ĐÈN TẮT!</b> <b>${mName}</b> là <b>VẬT CÁCH ĐIỆN</b>, dòng điện không thể đi qua được. Nhựa, gỗ và cao su giúp cách điện an toàn cho con người.`;
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
        fb.innerText = `🎉 Chính xác tuyệt vời, em ${stName} nắm rất chắc kiến thức Bài 9! (+10 Điểm)`;
    } else {
        playTone(false);
        fb.style.color = '#e03131';
        fb.innerText = `💡 Chưa đúng rồi! Em kiểm tra lại thí nghiệm xem vật nào làm đèn sáng nhé!`;
    }
}

// ==================== VẼ ĐỒ HỌA MẠCH ĐIỆN CHI TIẾT 60 FPS ====================
function drawCircuitLab() {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const isFlowing = circuit.switchClosed && circuit.conductors.includes(circuit.material);

    // Tiêu đề trực quan trên Canvas
    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 18px sans-serif';
    ctx.fillText('⚡ SƠ ĐỒ MẠCH ĐIỆN ĐƠN GIẢN & VẬT DẪN ĐIỆN', 25, 35);

    // Khung dây dẫn chính hình chữ nhật: (100, 90) -> (660, 340)
    ctx.strokeStyle = isFlowing ? '#facc15' : '#64748b';
    ctx.lineWidth = 7;
    ctx.strokeRect(100, 90, 560, 250);

    // Hiệu ứng hạt điện động chạy quanh dây khi mạch kín
    if (isFlowing) {
        ctx.fillStyle = '#fef08a';
        const perim = (560 + 250) * 2;
        for (let i = 0; i < 20; i++) {
            let d = ((i * (perim / 20)) + tick * 4.5) % perim;
            let ex = 100, ey = 90;
            if (d < 560) { ex = 100 + d; ey = 90; }
            else if (d < 560 + 250) { ex = 660; ey = 90 + (d - 560); }
            else if (d < 560 * 2 + 250) { ex = 660 - (d - 810); ey = 340; }
            else { ex = 100; ey = 340 - (d - 1370); }
            ctx.beginPath(); ctx.arc(ex, ey, 6, 0, Math.PI * 2); ctx.fill();
        }
    }

    // 1. Nguồn Điện bên trái (60, 150)
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(55, 150, 90, 120);
    if (circuit.source === 'battery') {
        ctx.fillStyle = '#f97316'; ctx.fillRect(72, 165, 56, 30);
        ctx.fillStyle = '#334155'; ctx.fillRect(72, 195, 56, 60);
        ctx.fillStyle = 'white'; ctx.font = 'bold 14px sans-serif'; ctx.fillText('+ PIN -', 78, 232);
    } else {
        ctx.fillStyle = '#0284c7'; ctx.fillRect(60, 160, 80, 90);
        ctx.fillStyle = '#fde047'; ctx.font = 'bold 24px sans-serif'; ctx.fillText('☀️', 87, 215);
    }

    // 2. Công Tắc ở cạnh trên (240, 90)
    ctx.fillStyle = '#0f172a'; ctx.fillRect(230, 70, 120, 40);
    ctx.fillStyle = circuit.switchClosed ? '#2f9e44' : '#e03131';
    ctx.beginPath(); ctx.arc(242, 90, 8, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.arc(338, 90, 8, 0, Math.PI * 2); ctx.fill();

    ctx.strokeStyle = '#f8fafc'; ctx.lineWidth = 6;
    ctx.beginPath(); ctx.moveTo(242, 90);
    if (circuit.switchClosed) {
        ctx.lineTo(338, 90);
    } else {
        ctx.lineTo(328, 48);
    }
    ctx.stroke();

    ctx.fillStyle = '#cbd5e1'; ctx.font = 'bold 13px sans-serif';
    ctx.fillText(circuit.switchClosed ? 'Công tắc: ĐÓNG' : 'Công tắc: MỞ', 235, 45);

    // 3. Bóng Đèn & Quạt bên phải (660, 150)
    ctx.fillStyle = '#1e293b'; ctx.fillRect(610, 145, 100, 130);

    if (isFlowing) {
        const grad = ctx.createRadialGradient(660, 200, 15, 660, 200, 85);
        grad.addColorStop(0, 'rgba(253, 224, 71, 0.95)');
        grad.addColorStop(1, 'rgba(253, 224, 71, 0)');
        ctx.fillStyle = grad; ctx.beginPath(); ctx.arc(660, 200, 85, 0, Math.PI * 2); ctx.fill();
    }

    ctx.beginPath(); ctx.arc(660, 200, 34, 0, Math.PI * 2);
    ctx.fillStyle = isFlowing ? '#fef08a' : '#475569';
    ctx.fill(); ctx.lineWidth = 3;
    ctx.strokeStyle = isFlowing ? '#facc15' : '#94a3b8'; ctx.stroke();

    ctx.fillStyle = '#94a3b8'; ctx.fillRect(646, 234, 28, 22);
    ctx.fillStyle = isFlowing ? '#fde047' : '#cbd5e1'; ctx.font = 'bold 14px sans-serif';
    ctx.fillText(isFlowing ? '💡 ĐÈN SÁNG' : '💡 Đèn tắt', 620, 285);

    // 4. Khe Thử Nghiệm Vật Liệu ở cạnh dưới (380, 340)
    ctx.fillStyle = '#1e293b'; ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2;
    ctx.fillRect(260, 305, 240, 70);
    ctx.strokeRect(260, 305, 240, 70);

    const matColors = {
        copper: '#d97706', iron: '#64748b', saltwater: '#06b6d4',
        plastic: '#38bdf8', wood: '#854d0e', rubber: '#f43f5e'
    };
    ctx.fillStyle = matColors[circuit.material];
    ctx.fillRect(280, 323, 200, 34);

    ctx.fillStyle = 'white'; ctx.font = 'bold 15px sans-serif'; ctx.textAlign = 'center';
    ctx.fillText(circuit.matNames[circuit.material], 380, 345);

    ctx.fillStyle = isFlowing ? '#4ade80' : '#f87171'; ctx.font = 'bold 14px sans-serif';
    ctx.fillText(isFlowing ? '👉 VẬT DẪN ĐIỆN' : '👉 VẬT CÁCH ĐIỆN', 380, 292);
    ctx.textAlign = 'left';
}

function animate() {
    tick++;
    drawCircuitLab();
    requestAnimationFrame(animate);
}
animate();
</script>
</body>
</html>
"""

components.html(circuit_lab_html, height=600, scrolling=True)
