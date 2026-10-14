import streamlit as st
import streamlit.components.v1 as components

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Phòng Thí Nghiệm Khoa Học Ảo AI - Lớp 5/2",
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
    <h1>🔬 PHÒNG THÍ NGHIỆM KHOA HỌC ẢO AI - LỚP 5/2</h1>
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn • Khám phá Mạch điện, Thể của Chất & Vòng tuần hoàn Mây Mưa</p>
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
        font-size: 0.88rem;
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
        font-size: 0.95rem;
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
        font-size: 0.95rem;
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
        font-size: 0.88rem;
    }
    .act-btn:hover { background: #f1f3f5; transform: translateY(-1px); }
    .act-btn.selected {
        background: #0ca678;
        color: white;
        border-color: #087f5b;
    }
    /* Nút Công Tắc Rõ Ràng */
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
        transition: 0.2s;
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
    input[type="range"] { width: 100%; margin: 6px 0; }
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
    <!-- CỘT TRÁI: MÀN HÌNH MÔ PHỎNG KHOA HỌC -->
    <div class="stage-panel">
        <div class="station-tabs">
            <button id="tab1" class="tab-btn active" onclick="switchStation(1)">⚡ Trạm 1: Mạch Điện</button>
            <button id="tab2" class="tab-btn" onclick="switchStation(2)">🧊 Trạm 2: Thể Rắn - Lỏng - Khí</button>
            <button id="tab3" class="tab-btn" onclick="switchStation(3)">🌧️ Trạm 3: Mây & Vòng Mưa</button>
        </div>

        <canvas id="labCanvas" width="760" height="430"></canvas>

        <div id="aiExplain" class="ai-explain-box">
            🤖 <b>Trợ lý Khoa học AI:</b> Chào nhà khoa học nhí <b>Hiểu Minh</b>! Hãy chọn vật liệu và bấm nút công tắc màu đỏ bên phải để đóng mạch điện nhé!
        </div>
    </div>

    <!-- CỘT PHẢI: BẢNG ĐIỀU KHIỂN -->
    <div class="control-panel">
        <div class="user-bar">
            <div>👩‍🔬 Nhà khoa học: <span id="scientistName">Hiểu Minh</span></div>
            <div>🌟 <span id="expScore">70</span> Điểm</div>
        </div>

        <div>
            <input type="text" id="nameInput" value="Hiểu Minh" placeholder="Nhập tên học sinh..." oninput="updateName()">
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 1: MẠCH ĐIỆN -->
        <div id="ctrlStation1" class="ctrl-group">
            <div class="ctrl-title">⚡ Bảng Điều Khiển Mạch Điện Lớp 5</div>
            <label style="font-size:0.86rem; font-weight:bold;">1. Nguồn Điện:</label>
            <select id="powerSource" onchange="updateCircuit()" style="margin-bottom:8px; margin-top:4px;">
                <option value="battery">🔋 Pin tiểu 1,5V - 3V</option>
                <option value="solar">☀️ Tấm Pin Năng lượng Mặt trời</option>
            </select>

            <label style="font-size:0.86rem; font-weight:bold;">2. Thả vật liệu vào khe thử:</label>
            <div class="btn-grid" style="margin-top:4px;">
                <button class="act-btn selected" id="mat_copper" onclick="selectMaterial('copper')">🪙 Thanh Đồng</button>
                <button class="act-btn" id="mat_iron" onclick="selectMaterial('iron')">🔩 Đinh Sắt</button>
                <button class="act-btn" id="mat_plastic" onclick="selectMaterial('plastic')">📏 Thước Nhựa</button>
                <button class="act-btn" id="mat_wood" onclick="selectMaterial('wood')">🪵 Gỗ Khô</button>
            </div>

            <div class="switch-box">
                <div style="font-size:0.83rem; font-weight:bold; margin-bottom:5px; color:#5c940d;">BẤM ĐỂ ĐÓNG/MỞ MẠCH ĐIỆN:</div>
                <button id="bigSwitchBtn" class="big-switch off" onclick="toggleSwitch()">🔴 CÔNG TẮC: ĐANG MỞ (Hở mạch)</button>
            </div>
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 2: THỂ RẮN - LỎNG - KHÍ & ĐUN NÓNG -->
        <div id="ctrlStation2" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">🧊 Thí Nghiệm Sự Chuyển Thể (Rắn - Lỏng - Khí)</div>
            <label style="font-size:0.86rem; font-weight:bold;">1. Trạng thái nhiệt độ chất:</label>
            <select id="stateSelect" onchange="changeStateExp()" style="margin-top:4px; margin-bottom:8px;">
                <option value="ice">❄️ Thể Rắn (-10°C đến 0°C): Nước đá</option>
                <option value="water">💧 Thể Lỏng (25°C): Nước trong cốc</option>
                <option value="steam">♨️ Thể Khí (100°C): Hơi nước sôi bay lên</option>
            </select>

            <div class="btn-grid">
                <button class="act-btn" id="heatStateBtn" onclick="toggleStateHeat()">🔥 Bật Đèn Cồn Đun Nóng</button>
                <button class="act-btn" onclick="resetStateExp()">🔄 Làm Lạnh Lại</button>
            </div>
            <div style="margin-top:8px; font-size:0.9rem; font-weight:bold;">
                🌡️ Nhiệt độ hiện tại: <span id="stateTempDisplay" style="color:#e03131;">0°C</span>
            </div>
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 3: MÂY, MƯA & VÒNG TUẦN HOÀN -->
        <div id="ctrlStation3" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">🌧️ Mô Hình Vòng Tuần Hoàn Nước (Mây & Mưa)</div>
            <label style="font-size:0.86rem; font-weight:bold;">☀️ Cường độ nắng bốc hơi nước: <span id="sunVal">50</span>%</label>
            <input type="range" id="sunSlider" min="10" max="100" value="50" oninput="updateRainModel()">

            <label style="font-size:0.86rem; font-weight:bold;">❄️ Độ lạnh tầng mây cao: <span id="coldVal">60</span>%</label>
            <input type="range" id="coldSlider" min="10" max="100" value="60" oninput="updateRainModel()">

            <button class="act-btn" style="width:100%; margin-top:6px; background:#e7f5ff; color:#1864ab; border-color:#74c0fc;" onclick="triggerRainStorm()">🌧️ Kích Hoạt Cơn Mưa Rào</button>
        </div>

        <!-- CÂU HỎI KẾT LUẬN -->
        <div class="quiz-card">
            <div style="font-weight:800; color:#d9480f; margin-bottom:4px;">🧠 Thử Thách Khoa Học Lớp 5:</div>
            <div id="quizQuestion" style="font-size:0.9rem; font-weight:600; margin-bottom:6px;">
                Nước chuyển từ Thể Lỏng sang Thể Khí (hơi nước) khi đạt đến nhiệt độ bao nhiêu?
            </div>
            <div class="btn-grid" id="quizOptions">
                <button class="act-btn" onclick="answerQuiz(true)">♨️ Đạt 100°C (Sôi)</button>
                <button class="act-btn" onclick="answerQuiz(false)">❄️ Đạt 0°C (Đông đặc)</button>
            </div>
            <div id="quizFeedback" style="margin-top:5px; font-size:0.88rem; font-weight:bold;"></div>
        </div>
    </div>
</div>

<script>
const canvas = document.getElementById('labCanvas');
const ctx = canvas.getContext('2d');

let currentStation = 1;
let expScore = 70;
let tick = 0;

// Trạm 1
let circuit = {
    source: 'battery',
    material: 'copper',
    switchClosed: false,
    conductors: ['copper', 'iron'],
    matNames: { copper: 'Thanh Đồng', iron: 'Đinh Sắt', plastic: 'Thước Nhựa', wood: 'Thanh Gỗ Khô' }
};

// Trạm 2 (Thể chất)
let stateLab = {
    mode: 'ice',
    temp: 0,
    heating: false,
    particles: []
};
for (let i = 0; i < 30; i++) {
    stateLab.particles.push({ x: 320 + Math.random() * 120, y: 220 + Math.random() * 100, vx: (Math.random()-0.5)*1, vy: (Math.random()-0.5)*1 });
}

// Trạm 3 (Mây Mưa)
let rainLab = {
    sunPower: 50,
    coldPower: 60,
    vapors: [],
    raindrops: [],
    isRaining: false
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
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">🪙 Thanh đồng & Đinh sắt</button><button class="act-btn" onclick="answerQuiz(false)">📏 Thước nhựa & Gỗ</button>`;
    } else if (stNum === 2) {
        updateStateExplanation();
        qText.innerText = "Nước chuyển từ Thể Lỏng sang Thể Khí (hơi nước) khi đạt đến nhiệt độ bao nhiêu?";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">♨️ Đạt 100°C (Sôi)</button><button class="act-btn" onclick="answerQuiz(false)">❄️ Đạt 0°C (Đông đặc)</button>`;
    } else {
        updateRainModel();
        qText.innerText = "Mây trên bầu trời được hình thành từ quá trình nào của nước?";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">☁️ Hơi nước bay lên gặp lạnh ngưng tụ</button><button class="act-btn" onclick="answerQuiz(false)">🔥 Nước dưới đất tự hóa thành đá</button>`;
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
        fb.innerText = `🎉 Giỏi lắm ${stName}! Em trả lời hoàn toàn chính xác (+10 Điểm)!`;
    } else {
        playTone(false);
        fb.style.color = '#e03131';
        fb.innerText = `💡 Chưa đúng rồi! Em quan sát thí nghiệm trên màn hình để thử lại nhé!`;
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
        box.innerHTML = `🤖 <b>Trợ lý AI:</b> Công tắc đang <b>Mở (Hở mạch)</b>. Em hãy chọn vật liệu <b>${mName}</b> rồi bấm nút <b>Đóng công tắc màu xanh</b> để dòng điện chạy qua nhé!`;
    } else if (isCond) {
        box.innerHTML = `✅ <b>Đèn Sáng Rực!</b> <b>${mName}</b> là <b>VẬT DẪN ĐIỆN</b>, cho phép dòng điện chạy qua mạch kín từ nguồn đến bóng đèn!`;
    } else {
        box.innerHTML = `⚠️ <b>Đèn Tắt!</b> <b>${mName}</b> là <b>VẬT CÁCH ĐIỆN</b>, không cho dòng điện chạy qua. Nhựa và gỗ dùng làm vật liệu cách điện an toàn.`;
    }
}

// ==================== TRẠM 2 LOGIC (THỂ CHẤT) ====================
function changeStateExp() {
    stateLab.mode = document.getElementById('stateSelect').value;
    if (stateLab.mode === 'ice') stateLab.temp = -5;
    else if (stateLab.mode === 'water') stateLab.temp = 25;
    else stateLab.temp = 100;
    stateLab.heating = false;
    document.getElementById('heatStateBtn').innerText = '🔥 Bật Đèn Cồn Đun Nóng';
    updateStateExplanation();
}

function toggleStateHeat() {
    stateLab.heating = !stateLab.heating;
    const btn = document.getElementById('heatStateBtn');
    btn.className = 'act-btn' + (stateLab.heating ? ' selected' : '');
    btn.innerText = stateLab.heating ? '🔥 Đang đun nóng...' : '🔥 Bật Đèn Cồn Đun Nóng';
    updateStateExplanation();
}

function resetStateExp() {
    stateLab.mode = 'ice';
    stateLab.temp = -5;
    stateLab.heating = false;
    document.getElementById('stateSelect').value = 'ice';
    document.getElementById('heatStateBtn').innerText = '🔥 Bật Đèn Cồn Đun Nóng';
    updateStateExplanation();
}

function updateStateExplanation() {
    const box = document.getElementById('aiExplain');
    if (stateLab.temp < 0) {
        box.innerHTML = `❄️ <b>Thể Rắn (Nước đá):</b> Ở dưới 0°C, các phân tử nước liên kết chặt chẽ với nhau đứng yên một chỗ thành khối cứng rắn.`;
    } else if (stateLab.temp < 100) {
        box.innerHTML = `💧 <b>Thể Lỏng (Nước):</b> Từ 0°C đến dưới 100°C, các hạt nước trượt lên nhau, giữ thể lỏng chảy được và tràn đầy cốc.`;
    } else {
        box.innerHTML = `♨️ <b>Thể Khí (Hơi nước):</b> Đạt 100°C nước sôi, các phân tử chuyển động rất nhanh bay hơi mạnh mẽ lên không trung thành thể khí!`;
    }
}

// ==================== TRẠM 3 LOGIC (MÂY MƯA) ====================
function updateRainModel() {
    rainLab.sunPower = parseInt(document.getElementById('sunSlider').value);
    rainLab.coldPower = parseInt(document.getElementById('coldSlider').value);
    document.getElementById('sunVal').innerText = rainLab.sunPower;
    document.getElementById('coldVal').innerText = rainLab.coldPower;
}

function triggerRainStorm() {
    rainLab.isRaining = true;
    playTone(true);
    document.getElementById('aiExplain.innerHTML').innerHTML = `🌧️ <b>Vòng Tuần Hoàn Nước:</b> Nơi mặt đất nhận nhiệt độ cao từ mặt trời làm nước bay hơi $\rightarrow$ gặp tầng mây lạnh ngưng tụ thành hạt nước nặng $\rightarrow$ rơi xuống thành những cơn mưa rào tưới mát đồng ruộng!`;
    setTimeout(() => { rainLab.isRaining = false; }, 4000);
}

// ==================== VẼ ĐỒ HỌA 60 FPS ====================
function drawStation1() {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    const isFlowing = circuit.switchClosed && circuit.conductors.includes(circuit.material);

    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 17px sans-serif';
    ctx.fillText('⚡ SƠ ĐỒ MẠCH ĐIỆN THỰC HÀNH', 25, 32);

    ctx.strokeStyle = isFlowing ? '#facc15' : '#64748b';
    ctx.lineWidth = 6;
    ctx.strokeRect(120, 95, 520, 250);

    if (isFlowing) {
        ctx.fillStyle = '#fef08a';
        const perim = (520 + 250) * 2;
        for (let i = 0; i < 16; i++) {
            let d = ((i * (perim / 16)) + tick * 3.5) % perim;
            let ex = 120, ey = 95;
            if (d < 520) { ex = 120 + d; ey = 95; }
            else if (d < 520 + 250) { ex = 640; ey = 95 + (d - 520); }
            else if (d < 520 * 2 + 250) { ex = 640 - (d - 770); ey = 345; }
            else { ex = 120; ey = 345 - (d - 1290); }
            ctx.beginPath(); ctx.arc(ex, ey, 5, 0, Math.PI * 2); ctx.fill();
        }
    }

    // Nguồn
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(75, 160, 90, 120);
    if (circuit.source === 'battery') {
        ctx.fillStyle = '#f97316'; ctx.fillRect(92, 175, 56, 30);
        ctx.fillStyle = '#334155'; ctx.fillRect(92, 205, 56, 60);
        ctx.fillStyle = 'white'; ctx.font = 'bold 13px sans-serif'; ctx.fillText('+ PIN -', 98, 242);
    } else {
        ctx.fillStyle = '#0284c7'; ctx.fillRect(80, 170, 80, 90);
        ctx.fillStyle = '#fde047'; ctx.font = 'bold 22px sans-serif'; ctx.fillText('☀️', 108, 225);
    }

    // Công tắc
    ctx.fillStyle = '#0f172a'; ctx.fillRect(260, 75, 90, 38);
    ctx.strokeStyle = '#f8fafc'; ctx.lineWidth = 5;
    ctx.beginPath(); ctx.moveTo(265, 95);
    if (circuit.switchClosed) ctx.lineTo(345, 95);
    else ctx.lineTo(335, 55);
    ctx.stroke();

    // Đèn
    ctx.fillStyle = '#0f172a'; ctx.fillRect(600, 155, 80, 120);
    if (isFlowing) {
        const grad = ctx.createRadialGradient(640, 205, 10, 640, 205, 70);
        grad.addColorStop(0, 'rgba(253, 224, 71, 0.95)'); grad.addColorStop(1, 'rgba(253, 224, 71, 0)');
        ctx.fillStyle = grad; ctx.beginPath(); ctx.arc(640, 205, 70, 0, Math.PI * 2); ctx.fill();
    }
    ctx.beginPath(); ctx.arc(640, 205, 30, 0, Math.PI * 2);
    ctx.fillStyle = isFlowing ? '#fef08a' : '#475569'; ctx.fill();
    ctx.stroke();
    ctx.fillStyle = isFlowing ? '#fde047' : '#cbd5e1'; ctx.font = 'bold 13px sans-serif';
    ctx.fillText(isFlowing ? '💡 ĐÈN SÁNG' : '💡 Đèn tắt', 605, 275);

    // Vật liệu
    ctx.fillStyle = '#1e293b'; ctx.fillRect(280, 310, 200, 65);
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2; ctx.strokeRect(280, 310, 200, 65);
    ctx.fillStyle = '#d97706'; ctx.fillRect(295, 328, 170, 28);
    ctx.fillStyle = 'white'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'center';
    ctx.fillText(circuit.matNames[circuit.material], 380, 347);
    ctx.textAlign = 'left';
}

function drawStation2() {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    if (stateLab.heating && stateLab.temp < 100) stateLab.temp += 0.3;
    document.getElementById('stateTempDisplay').innerText = Math.round(stateLab.temp) + '°C';

    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 17px sans-serif';
    ctx.fillText('🧊 SỰ CHUYỂN THỂ (RẮN - LỎNG - KHÍ)', 25, 32);

    // Bàn
    ctx.fillStyle = '#334155'; ctx.fillRect(180, 350, 400, 16);

    // Cốc thủy tinh
    ctx.strokeStyle = '#e2e8f0'; ctx.lineWidth = 4;
    ctx.beginPath(); ctx.moveTo(290, 150); ctx.lineTo(290, 330); ctx.lineTo(470, 330); ctx.lineTo(470, 150); ctx.stroke();

    if (stateLab.temp <= 0) {
        // Khối nước đá thể rắn
        ctx.fillStyle = 'rgba(186, 230, 253, 0.9)';
        ctx.fillRect(320, 210, 110, 110);
        ctx.fillStyle = '#0369a1'; ctx.font = 'bold 14px sans-serif'; ctx.fillText('🧊 THỂ RẮN (Đá cứng)', 305, 195);
    } else if (stateLab.temp < 100) {
        // Thể lỏng
        ctx.fillStyle = 'rgba(56, 189, 248, 0.65)';
        ctx.fillRect(292, 210, 176, 118);
        ctx.fillStyle = '#e0f2fe'; ctx.font = 'bold 14px sans-serif'; ctx.fillText('💧 THỂ LỎNG (Nước)', 315, 195);
    } else {
        // Thể khí (Hơi nước bay lên)
        ctx.fillStyle = 'rgba(56, 189, 248, 0.4)'; ctx.fillRect(292, 210, 176, 118);
        ctx.fillStyle = 'rgba(255, 255, 255, 0.75)';
        for (let i = 0; i < 8; i++) {
            let hy = 180 - ((tick * 1.5 + i * 25) % 130);
            ctx.beginPath(); ctx.arc(330 + (i * 15) % 90, hy, 10, 0, Math.PI * 2); ctx.fill();
        }
        ctx.fillStyle = '#fde047'; ctx.font = 'bold 14px sans-serif'; ctx.fillText('♨️ THỂ KHÍ (Hơi nước sôi)', 295, 135);
    }

    if (stateLab.heating) {
        ctx.fillStyle = '#f97316';
        ctx.beginPath(); ctx.arc(380, 342, 16 + Math.sin(tick * 0.4) * 4, Math.PI, 0); ctx.fill();
    }
}

function drawStation3() {
    ctx.fillStyle = '#0284c7'; // Bầu trời xanh
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Mặt trời
    ctx.fillStyle = '#fde047'; ctx.beginPath(); ctx.arc(620, 75, 35, 0, Math.PI * 2); ctx.fill();

    // Mặt đất & Dòng sông
    ctx.fillStyle = '#16a34a'; ctx.fillRect(0, 310, canvas.width, 120);
    ctx.fillStyle = '#0284c7'; ctx.fillRect(0, 360, canvas.width, 70);

    ctx.fillStyle = 'white'; ctx.font = 'bold 17px sans-serif';
    ctx.fillText('🌧️ VÒNG TUẦN HOÀN CỦA NƯỚC (MÂY & MƯA)', 25, 32);

    // Mây ngưng tụ trên cao
    ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
    [200, 360, 520].forEach((mx, idx) => {
        ctx.beginPath(); ctx.arc(mx, 130, 30 + idx*4, 0, Math.PI * 2); ctx.fill();
        ctx.beginPath(); ctx.arc(mx + 25, 120, 25, 0, Math.PI * 2); ctx.fill();
    });

    // Hiệu ứng hạt mưa rơi
    if (rainLab.isRaining || tick % 120 < 40) {
        ctx.strokeStyle = '#bae6fd'; ctx.lineWidth = 2;
        for (let r = 0; r < 30; r++) {
            let rx = (r * 28 + tick * 6) % canvas.width;
            let ry = (tick * 8 + r * 15) % 320;
            ctx.beginPath(); ctx.moveTo(rx, ry); ctx.lineTo(rx - 2, ry + 12); ctx.stroke();
        }
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

components.html(science_lab_html, height=620, scrolling=True)
