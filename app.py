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
    <h1>🔬 PHÒNG THÍ NGHIỆM KHOA HỌC LỚP 5 - LỚP 5/2</h1>
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn • Chủ đề: Năng lượng, Vi khuẩn & Sức khỏe, Sinh vật & Môi trường</p>
</div>
""", unsafe_allow_html=True)

# ==================== MÔ PHỎNG KHOA HỌC TƯƠNG TÁC HTML5 CANVAS ====================
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
            <button id="tab1" class="tab-btn active" onclick="switchStation(1)">⚡ Trạm 1: Năng Lượng & Mạch Điện</button>
            <button id="tab2" class="tab-btn" onclick="switchStation(2)">🦠 Trạm 2: Vi Khuẩn & Sức Khỏe</button>
            <button id="tab3" class="tab-btn" onclick="switchStation(3)">🌿 Trạm 3: Sinh Vật & Chuỗi Thức Ăn</button>
        </div>

        <canvas id="labCanvas" width="760" height="420"></canvas>

        <div id="aiExplain" class="ai-explain-box">
            🤖 <b>Trợ lý Khoa học AI:</b> Chào nhà khoa học nhí <b>Hiểu Minh</b> (Lớp 5/2 - TH Bình Phước)! Hãy chọn trạm thí nghiệm để bắt đầu khám phá nhé!
        </div>
    </div>

    <!-- CỘT PHẢI: ĐIỀU KHIỂN -->
    <div class="control-panel">
        <div class="user-bar">
            <div>👩‍🔬 Nhà khoa học: <span id="scientistName">Hiểu Minh</span></div>
            <div>🌟 <span id="expScore">80</span> Điểm</div>
        </div>

        <div>
            <input type="text" id="nameInput" value="Hiểu Minh" placeholder="Nhập tên học sinh..." oninput="updateName()">
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 1: NĂNG LƯỢNG & MẠCH ĐIỆN -->
        <div id="ctrlStation1" class="ctrl-group">
            <div class="ctrl-title">⚡ Trạm 1: Năng Lượng Điện</div>
            <label style="font-size:0.85rem; font-weight:bold;">1. Nguồn Điện:</label>
            <select id="powerSource" onchange="updateCircuit()" style="margin-bottom:8px; margin-top:4px;">
                <option value="battery">🔋 Pin tiểu (Hóa năng -> Điện năng)</option>
                <option value="solar">☀️ Tấm Pin Mặt Trời (Quang năng -> Điện năng)</option>
            </select>

            <label style="font-size:0.85rem; font-weight:bold;">2. Thử nghiệm vật liệu:</label>
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

        <!-- ĐIỀU KHIỂN TRẠM 2: VI KHUẨN & SỨC KHỎE -->
        <div id="ctrlStation2" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">🦠 Trạm 2: Vi Khuẩn Có Lợi & Có Hại</div>
            <label style="font-size:0.85rem; font-weight:bold;">Chọn nhóm vi khuẩn quan sát dưới kính hiển vi:</label>
            <div class="btn-grid" style="margin-top:6px; margin-bottom:10px;">
                <button class="act-btn selected" id="bac_good" onclick="selectBacteria('good')">🛡️ Vi khuẩn Lên men (Có lợi)</button>
                <button class="act-btn" id="bac_bad" onclick="selectBacteria('bad')">🦠 Vi khuẩn Gây bệnh (Có hại)</button>
            </div>

            <button class="act-btn" style="width:100%; background:#e7f5ff; color:#1864ab; border-color:#74c0fc;" onclick="triggerDisinfect()">🧼 Thao tác Rửa tay diệt khuẩn / Vệ sinh an toàn</button>
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 3: SINH VẬT & MÔI TRƯỜNG (CHUỖI THỨC ĂN) -->
        <div id="ctrlStation3" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">🌿 Trạm 3: Sinh Vật & Chuỗi Thức Ăn Tự Nhiên</div>
            <label style="font-size:0.85rem; font-weight:bold;">Chọn mắt xích trong hệ sinh thái:</label>
            <div class="btn-grid" style="margin-top:6px; margin-bottom:10px;">
                <button class="act-btn selected" id="eco_grass" onclick="selectEco('grass')">🌱 Thực vật (Sản xuất)</button>
                <button class="act-btn" id="eco_rabbit" onclick="selectEco('rabbit')">🐇 Thỏ (Ăn thực vật)</button>
                <button class="act-btn" id="eco_fox" onclick="selectEco('fox')">🦊 Cáo / Diều hâu (Ăn thịt)</button>
            </div>
            <div style="font-size:0.85rem; color:#087f5b; font-weight:bold;">
                👉 Chuỗi thức ăn mẫu: Cỏ ➡️ Thỏ ➡️ Cáo (Năng lượng truyền từ mặt trời qua sinh vật).
            </div>
        </div>

        <!-- CÂU HỎI KẾT LUẬN -->
        <div class="quiz-card">
            <div style="font-weight:800; color:#d9480f; margin-bottom:4px;">🧠 Thử Thách Khoa Học Lớp 5:</div>
            <div id="quizQuestion" style="font-size:0.9rem; font-weight:600; margin-bottom:6px;">
                Vật liệu nào dưới đây là VẬT DẪN ĐIỆN giúp bóng đèn phát sáng ở Trạm 1?
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
let expScore = 80;
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
let bacteriaLab = {
    type: 'good',
    disinfected: false
};

// Trạm 3
let ecoLab = {
    selected: 'grass'
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
        qText.innerText = "Vật liệu nào dưới đây là VẬT DẪN ĐIỆN giúp bóng đèn phát sáng?";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">🪙 Thanh đồng & Đinh sắt</button><button class="act-btn" onclick="answerQuiz(false)">📏 Thước nhựa & Gỗ khô</button>`;
    } else if (stNum === 2) {
        document.getElementById('aiExplain').innerHTML = `🦠 <b>Trợ lý AI:</b> Vi khuẩn có ở khắp mọi nơi! Vi khuẩn có lợi giúp làm sữa chua, lên men thức ăn; vi khuẩn có hại gây bệnh tiêu hóa và truyền nhiễm.`;
        qText.innerText = "Vi khuẩn nào dưới đây có lợi được ứng dụng để làm sữa chua?";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">🛡️ Vi khuẩn lên men (Lactic)</button><button class="act-btn" onclick="answerQuiz(false)">🦠 Vi khuẩn tả / lỵ</button>`;
    } else {
        document.getElementById('aiExplain').innerHTML = `🌿 <b>Trợ lý AI:</b> Trong chuỗi thức ăn, thực vật là sinh vật sản xuất tự tổng hợp chất dinh dưỡng nhờ ánh sáng mặt trời để nuôi động vật!`;
        qText.innerText = "Trong chuỗi thức ăn (Cỏ ➡️ Thỏ ➡️ Cáo), sinh vật nào đóng vai trò là sinh vật sản xuất?";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">🌱 Thực vật (Cỏ)</button><button class="act-btn" onclick="answerQuiz(false)">🦊 Cáo</button>`;
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
        fb.innerText = `🎉 Chính xác tuyệt vời, em ${stName} rất am hiểu khoa học! (+10 Điểm)`;
    } else {
        playTone(false);
        fb.style.color = '#e03131';
        fb.innerText = `💡 Chưa đúng rồi! Em quan sát kĩ mô hình thí nghiệm để thử lại nhé!`;
    }
}

// ==================== TRẠM 1 LOGIC ====================
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
        box.innerHTML = `🤖 <b>Trợ lý AI:</b> Công tắc đang <b>Mở</b>. Hãy chọn <b>${mName}</b> và bấm nút công tắc màu xanh để đóng mạch điện!`;
    } else if (isCond) {
        box.innerHTML = `✅ <b>Đèn Sáng!</b> <b>${mName}</b> là <b>VẬT DẪN ĐIỆN</b>, cho dòng điện chạy qua làm sáng bóng đèn.`;
    } else {
        box.innerHTML = `⚠️ <b>Đèn Tắt!</b> <b>${mName}</b> là <b>VẬT CÁCH ĐIỆN</b>, không cho dòng điện chạy qua.`;
    }
}

// ==================== TRẠM 2 LOGIC (VI KHUẨN) ====================
function selectBacteria(type) {
    bacteriaLab.type = type;
    bacteriaLab.disinfected = false;
    document.getElementById('bac_good').className = 'act-btn' + (type === 'good' ? ' selected' : '');
    document.getElementById('bac_bad').className = 'act-btn' + (type === 'bad' ? ' selected' : '');
    
    const box = document.getElementById('aiExplain');
    if (type === 'good') {
        box.innerHTML = `🛡️ <b>Vi khuẩn có lợi:</b> Thường dùng trong chế biến thực phẩm như lên men sữa chua, muối dưa cà, giúp ích cho hệ tiêu hóa của con người.`;
    } else {
        box.innerHTML = `🦠 <b>Vi khuẩn có hại:</b> Gây ôi thiu thức ăn và các bệnh truyền nhiễm đường ruột. Cần ăn chín uống sôi và rửa tay sạch sẽ!`;
    }
}

function triggerDisinfect() {
    bacteriaLab.disinfected = true;
    playTone(true);
    document.getElementById('aiExplain').innerHTML = `🧼 <b>Đã Vệ Sinh Sạch Sẽ!</b> Xà phòng và nước sạch tiêu diệt phần lớn vi khuẩn có hại trên tay, bảo vệ sức khỏe cơ thể.`;
    setTimeout(() => { bacteriaLab.disinfected = false; }, 4000);
}

// ==================== TRẠM 3 LOGIC (SINH VẬT & MÔI TRƯỜNG) ====================
function selectEco(item) {
    ecoLab.selected = item;
    ['grass', 'rabbit', 'fox'].forEach(i => {
        document.getElementById('eco_' + i).className = 'act-btn' + (i === item ? ' selected' : '');
    });
    const box = document.getElementById('aiExplain');
    if (item === 'grass') {
        box.innerHTML = `🌱 <b>Thực vật (Cỏ):</b> Là sinh vật sản xuất, tự tổng hợp chất hữu cơ từ ánh sáng mặt trời, nước và chất khoáng.`;
    } else if (item === 'rabbit') {
        box.innerHTML = `🐇 <b>Động vật ăn cỏ (Thỏ):</b> Là sinh vật tiêu thụ bậc 1, sử dụng năng lượng tích lũy từ thực vật để sinh trưởng.`;
    } else {
        box.innerHTML = `🦊 <b>Động vật ăn thịt (Cáo/Diều hâu):</b> Là sinh vật tiêu thụ bậc 2, đứng ở mắt xích cao hơn trong chuỗi thức ăn tự nhiên.`;
    }
}

// ==================== VẼ ĐỒ HỌA 60 FPS ====================
function drawStation1() {
    ctx.fillStyle = '#0f172a'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    const isFlowing = circuit.switchClosed && circuit.conductors.includes(circuit.material);

    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 17px sans-serif';
    ctx.fillText('⚡ TRẠM 1: MẠCH ĐIỆN & NĂNG LƯỢNG', 25, 32);

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
    ctx.fillText('🦠 TRẠM 2: VI KHUẨN DƯỚI KÍNH HIỂN VI & SỨC KHỎE', 25, 32);

    // Thấu kính kính hiển vi
    ctx.fillStyle = '#1e293b'; ctx.strokeStyle = '#64748b'; ctx.lineWidth = 8;
    ctx.beginPath(); ctx.arc(380, 220, 140, 0, Math.PI * 2); ctx.fill(); ctx.stroke();

    // Vẽ các vi khuẩn
    for (let i = 0; i < 22; i++) {
        let bx = 300 + Math.sin(i * 15 + tick * 0.05) * 80 + (i * 7) % 40;
        let by = 180 + Math.cos(i * 12 + tick * 0.05) * 70 + (i * 9) % 35;
        
        ctx.fillStyle = bacteriaLab.type === 'good' ? '#4ade80' : '#f87171';
        if (bacteriaLab.disinfected) ctx.fillStyle = '#94a3b8'; // Bị tiêu diệt

        ctx.beginPath(); ctx.arc(bx, by, bacteriaLab.type === 'good' ? 10 : 8, 0, Math.PI * 2); ctx.fill();
    }

    ctx.fillStyle = 'white'; ctx.font = 'bold 15px sans-serif'; ctx.textAlign = 'center';
    ctx.fillText(bacteriaLab.type === 'good' ? '🛡️ Vi khuẩn Lên men (Lactic - Có lợi)' : '🦠 Vi khuẩn Gây bệnh đường ruột (Có hại)', 380, 385);
    if (bacteriaLab.disinfected) {
        ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 18px sans-serif';
        ctx.fillText('🧼 Xà phòng đã tiêu diệt vi khuẩn có hại!', 380, 80);
    }
    ctx.textAlign = 'left';
}

function drawStation3() {
    ctx.fillStyle = '#0284c7'; ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Mặt trời
    ctx.fillStyle = '#fde047'; ctx.beginPath(); ctx.arc(620, 70, 35, 0, Math.PI * 2); ctx.fill();

    // Mặt đất sinh thái
    ctx.fillStyle = '#16a34a'; ctx.fillRect(0, 310, canvas.width, 110);
    ctx.fillStyle = '#15803d'; ctx.fillRect(0, 355, canvas.width, 65);

    ctx.fillStyle = 'white'; ctx.font = 'bold 17px sans-serif';
    ctx.fillText('🌿 TRẠM 3: CHUỖI THỨC ĂN TRONG TỰ NHIÊN', 25, 32);

    // Vẽ các sinh vật minh họa chuỗi thức ăn: Cỏ -> Thỏ -> Cáo
    // 1. Cỏ
    ctx.fillStyle = ecoLab.selected === 'grass' ? '#fde047' : '#22c55e';
    ctx.font = 'bold 45px sans-serif'; ctx.fillText('🌱', 150, 300);
    ctx.fillStyle = 'white'; ctx.font = 'bold 14px sans-serif'; ctx.fillText('Thực vật (Cỏ)', 125, 335);

    ctx.fillStyle = 'white'; ctx.font = 'bold 24px sans-serif'; ctx.fillText('➡️', 290, 275);

    // 2. Thỏ
    ctx.fillStyle = ecoLab.selected === 'rabbit' ? '#fde047' : 'white';
    ctx.font = 'bold 45px sans-serif'; ctx.fillText('🐇', 380, 295);
    ctx.fillStyle = 'white'; ctx.font = 'bold 14px sans-serif'; ctx.fillText('Động vật ăn cỏ (Thỏ)', 340, 335);

    ctx.fillStyle = 'white'; ctx.font = 'bold 24px sans-serif'; ctx.fillText('➡️', 510, 275);

    // 3. Cáo
    ctx.fillStyle = ecoLab.selected === 'fox' ? '#fde047' : '#f97316';
    ctx.font = 'bold 45px sans-serif'; ctx.fillText('🦊', 590, 295);
    ctx.fillStyle = 'white'; ctx.font = 'bold 14px sans-serif'; ctx.fillText('Động vật ăn thịt (Cáo)', 550, 335);
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
