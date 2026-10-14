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
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn • Khám phá Năng lượng, Sự biến đổi chất & Môi trường xanh</p>
</div>
""", unsafe_allow_html=True)

# ==================== MÔ PHỎNG KHOA HỌC TƯƠNG TÁC HTML5 CANVAS + AI ====================
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
        flex-wrap: wrap;
    }
    .tab-btn {
        flex: 1;
        padding: 10px 12px;
        border: 2px solid #96f2d7;
        background: #e6fcf5;
        color: #087f5b;
        font-weight: 800;
        font-size: 0.93rem;
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
        font-size: 0.96rem;
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
        font-size: 0.96rem;
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
        font-size: 0.9rem;
    }
    .act-btn:hover { background: #f1f3f5; transform: translateY(-1px); }
    .act-btn.selected {
        background: #0ca678;
        color: white;
        border-color: #087f5b;
    }
    .switch-btn {
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 10px;
        font-weight: 800;
        font-size: 1rem;
        cursor: pointer;
        color: white;
        background: #e03131;
        margin-top: 6px;
    }
    .switch-btn.on { background: #2f9e44; }
    input[type="text"], select {
        width: 100%;
        padding: 8px 12px;
        border-radius: 8px;
        border: 2px solid #adb5bd;
        font-weight: bold;
        font-size: 0.95rem;
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
    <!-- CỘT TRÁI: MÀN HÌNH MÔ PHỎNG THÍ NGHIỆM TRỰC QUAN -->
    <div class="stage-panel">
        <div class="station-tabs">
            <button id="tab1" class="tab-btn active" onclick="switchStation(1)">⚡ Trạm 1: Mạch Điện & Vật Dẫn Điện</button>
            <button id="tab2" class="tab-btn" onclick="switchStation(2)">🧪 Trạm 2: Sự Biến Đổi Của Chất</button>
            <button id="tab3" class="tab-btn" onclick="switchStation(3)">🌍 Trạm 3: Khí Hậu & Năng Lượng Xanh</button>
        </div>

        <canvas id="labCanvas" width="760" height="440"></canvas>

        <div id="aiExplain" class="ai-explain-box">
            🤖 <b>Trợ lý Khoa học AI:</b> Chào nhà khoa học nhí <b>Hiểu Minh</b>! Hãy chọn vật liệu lắp vào mạch điện và bấm <b>Đóng Công Tắc</b> để xem dòng điện chạy qua như thế nào nhé!
        </div>
    </div>

    <!-- CỘT PHẢI: BẢNG ĐIỀU KHIỂN THÍ NGHIỆM & THỬ THÁCH -->
    <div class="control-panel">
        <div class="user-bar">
            <div>👩‍🔬 Nhà khoa học: <span id="scientistName">Hiểu Minh</span></div>
            <div>🌟 <span id="expScore">60</span> Điểm Khám Phá</div>
        </div>

        <div>
            <input type="text" id="nameInput" value="Hiểu Minh" placeholder="Nhập tên học sinh..." oninput="updateName()">
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 1: MẠCH ĐIỆN -->
        <div id="ctrlStation1" class="ctrl-group">
            <div class="ctrl-title">⚡ Bảng Điều Khiển Mạch Điện Lớp 5</div>
            <label style="font-size:0.88rem; font-weight:bold;">1. Chọn Nguồn Năng Lượng:</label>
            <select id="powerSource" onchange="updateCircuit()" style="margin-bottom:8px; margin-top:4px;">
                <option value="battery">🔋 Pin tiểu 1,5V - 3V</option>
                <option value="solar">☀️ Pin Năng lượng Mặt trời (Năng lượng sạch)</option>
            </select>

            <label style="font-size:0.88rem; font-weight:bold;">2. Thả vật liệu vào khe thử (Dẫn điện hay Cách điện?):</label>
            <div class="btn-grid" style="margin-top:6px;">
                <button class="act-btn selected" id="mat_copper" onclick="selectMaterial('copper')">🪙 Thanh Đồng</button>
                <button class="act-btn" id="mat_iron" onclick="selectMaterial('iron')">🔩 Đinh Sắt</button>
                <button class="act-btn" id="mat_plastic" onclick="selectMaterial('plastic')">📏 Thước Nhựa</button>
                <button class="act-btn" id="mat_wood" onclick="selectMaterial('wood')">🪵 Gỗ Khô</button>
                <button class="act-btn" id="mat_saltwater" onclick="selectMaterial('saltwater')">🧂 Nước Muối</button>
                <button class="act-btn" id="mat_rubber" onclick="selectMaterial('rubber')">🧤 Cục Tẩy Cao Su</button>
            </div>

            <button id="switchBtn" class="switch-btn" onclick="toggleSwitch()">🔘 CÔNG TẮC ĐANG MỞ (Bấm để Đóng mạch)</button>
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 2: BIẾN ĐỔI CHẤT -->
        <div id="ctrlStation2" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">🧪 Bảng Pha Trộn & Đun Nóng Chất</div>
            <label style="font-size:0.88rem; font-weight:bold;">1. Chọn Thí Nghiệm Trong Cốc Thủy Tinh:</label>
            <select id="chemSelect" onchange="changeChemExperiment()" style="margin-top:4px; margin-bottom:10px;">
                <option value="sugar">1. Hòa tan Đường vào Nước (Dung dịch)</option>
                <option value="sand">2. Trộn Cát vào Nước (Hỗn hợp không tan)</option>
                <option value="oil">3. Đổ Dầu ăn vào Nước (Hỗn hợp tách lớp)</option>
                <option value="baking">4. Pha Giấm ăn + Baking Soda (Biến đổi Hóa học)</option>
                <option value="state">5. Đun nóng Nước đá -> Nước lỏng -> Hơi nước</option>
            </select>

            <div class="btn-grid">
                <button class="act-btn" onclick="stirBeaker()">🥄 Khuấy Đều Cốc</button>
                <button class="act-btn" id="heatBtn" onclick="toggleHeat()">🔥 Bật Đèn Cồn Đun Nóng</button>
            </div>

            <div style="margin-top:10px; font-size:0.9rem; font-weight:bold;">
                🌡️ Nhiệt độ trong cốc: <span id="tempDisplay" style="color:#e03131;">25°C</span>
            </div>
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 3: MÔI TRƯỜNG & KHÍ HẬU -->
        <div id="ctrlStation3" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">🌍 Điều Chỉnh Hệ Sinh Thái & Năng Lượng</div>
            <label style="font-size:0.88rem; font-weight:bold;">🌳 Số lượng Cây xanh trồng mới: <span id="treeVal">50</span> cây</label>
            <input type="range" id="treeSlider" min="0" max="100" value="50" oninput="updateEco()">

            <label style="font-size:0.88rem; font-weight:bold;">☀️ Lắp đặt Điện Gió & Mặt Trời: <span id="cleanVal">40</span>%</label>
            <input type="range" id="cleanSlider" min="0" max="100" value="40" oninput="updateEco()">

            <label style="font-size:0.88rem; font-weight:bold;">🏭 Khí thải Nhà máy & Xe cộ: <span id="smokeVal">50</span>%</label>
            <input type="range" id="smokeSlider" min="0" max="100" value="50" oninput="updateEco()">

            <button class="act-btn selected" style="width:100%; margin-top:6px;" onclick="setGreenIdeal()">🌱 Cân Bằng Xanh Lý Tưởng Cho Trái Đất</button>
        </div>

        <!-- CÂU HỎI KẾT LUẬN KHOA HỌC NHANH -->
        <div class="quiz-card">
            <div style="font-weight:800; color:#d9480f; margin-bottom:4px;">🧠 Thử Thách Quan Sát Thí Nghiệm:</div>
            <div id="quizQuestion" style="font-size:0.92rem; font-weight:600; margin-bottom:8px;">
                Sau khi thử nghiệm ở Trạm 1, đố em vật liệu nào dưới đây cho dòng điện chạy qua làm sáng bóng đèn?
            </div>
            <div class="btn-grid" id="quizOptions">
                <button class="act-btn" onclick="answerQuiz(true)">🪙 Thanh đồng & Đinh sắt</button>
                <button class="act-btn" onclick="answerQuiz(false)">📏 Thước nhựa & Gỗ khô</button>
            </div>
            <div id="quizFeedback" style="margin-top:6px; font-size:0.9rem; font-weight:bold;"></div>
        </div>
    </div>
</div>

<script>
const canvas = document.getElementById('labCanvas');
const ctx = canvas.getContext('2d');

let currentStation = 1;
let expScore = 60;
let tick = 0;

// Trạng thái Trạm 1 (Mạch điện)
let circuit = {
    source: 'battery',
    material: 'copper',
    switchClosed: false,
    conductors: ['copper', 'iron', 'saltwater'],
    matNames: {
        copper: 'Thanh Đồng (Kim loại)',
        iron: 'Đinh Sắt (Kim loại)',
        plastic: 'Thước Nhựa',
        wood: 'Thanh Gỗ Khô',
        saltwater: 'Cốc Nước Muối',
        rubber: 'Cục Tẩy Cao Su'
    }
};

// Trạng thái Trạm 2 (Hóa học & Chất)
let chem = {
    type: 'sugar',
    stirring: 0,
    heating: false,
    temp: 25,
    bubbles: []
};
for (let i = 0; i < 25; i++) {
    chem.bubbles.push({ x: 300 + Math.random() * 160, y: 220 + Math.random() * 140, r: 3 + Math.random() * 5, s: 0.6 + Math.random() * 1.2 });
}

// Trạng thái Trạm 3 (Môi trường)
let eco = {
    trees: 50,
    clean: 40,
    smoke: 50,
    earthTemp: 28.5
};

// Âm thanh hiệu ứng
function playTone(win) {
    try {
        const ac = new (window.AudioContext || window.webkitAudioContext)();
        const freqs = win ? [523, 659, 784, 1046] : [240, 180];
        freqs.forEach((f, idx) => {
            const osc = ac.createOscillator();
            const g = ac.createGain();
            osc.type = win ? 'triangle' : 'sawtooth';
            osc.frequency.setValueAtTime(f, ac.currentTime + idx * 0.08);
            g.gain.setValueAtTime(0.15, ac.currentTime + idx * 0.08);
            g.gain.exponentialRampToValueAtTime(0.001, ac.currentTime + idx * 0.08 + 0.22);
            osc.connect(g); g.connect(ac.destination);
            osc.start(ac.currentTime + idx * 0.08);
            osc.stop(ac.currentTime + idx * 0.08 + 0.22);
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
        qText.innerText = "Qua thí nghiệm Trạm 1, vật liệu nào dưới đây là VẬT DẪN ĐIỆN giúp bóng đèn phát sáng?";
        qOpts.innerHTML = `
            <button class="act-btn" onclick="answerQuiz(true)">🪙 Thanh đồng & Đinh sắt</button>
            <button class="act-btn" onclick="answerQuiz(false)">📏 Thước nhựa & Cao su</button>
        `;
    } else if (stNum === 2) {
        updateChemExplanation();
        qText.innerText = "Khi pha Giấm ăn với Baking Soda làm sủi bọt khí CO₂ mới, đó là hiện tượng gì?";
        qOpts.innerHTML = `
            <button class="act-btn" onclick="answerQuiz(true)">🧪 Sự biến đổi Hóa học</button>
            <button class="act-btn" onclick="answerQuiz(false)">🧊 Chỉ là sự nóng chảy</button>
        `;
    } else {
        updateEco();
        qText.innerText = "Giải pháp nào giúp giảm nhiệt độ Trái Đất và bảo vệ môi trường bền vững nhất?";
        qOpts.innerHTML = `
            <button class="act-btn" onclick="answerQuiz(true)">🌱 Trồng cây & Dùng điện mặt trời</button>
            <button class="act-btn" onclick="answerQuiz(false)">🏭 Tăng khói bụi nhà máy</button>
        `;
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
        fb.innerText = `🎉 Xuất sắc quá ${stName} ơi! Em đã rút ra kết luận khoa học hoàn toàn chính xác (+10 Điểm)!`;
    } else {
        playTone(false);
        fb.style.color = '#e03131';
        fb.innerText = `💡 Chưa đúng rồi! Em hãy nhìn lại hiện tượng trên màn hình thí nghiệm để chọn lại nhé!`;
    }
}

// ==================== LOGIC TRẠM 1: MẠCH ĐIỆN ====================
function selectMaterial(mat) {
    circuit.material = mat;
    ['copper', 'iron', 'plastic', 'wood', 'saltwater', 'rubber'].forEach(m => {
        document.getElementById('mat_' + m).className = 'act-btn' + (m === mat ? ' selected' : '');
    });
    if (circuit.switchClosed) {
        playTone(circuit.conductors.includes(mat));
    }
    updateCircuitExplanation();
}

function toggleSwitch() {
    circuit.switchClosed = !circuit.switchClosed;
    const btn = document.getElementById('switchBtn');
    if (circuit.switchClosed) {
        btn.className = 'switch-btn on';
        btn.innerText = '⚡ CÔNG TẮC ĐANG ĐÓNG (Bấm để Ngắt điện)';
        playTone(circuit.conductors.includes(circuit.material));
    } else {
        btn.className = 'switch-btn';
        btn.innerText = '🔘 CÔNG TẮC ĐANG MỞ (Bấm để Đóng mạch)';
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
        box.innerHTML = `🤖 <b>Trợ lý Khoa học AI:</b> Hiện tại <b>Mạch điện đang hở</b> (Công tắc mở). Em hãy chọn vật liệu <b>${mName}</b> và bấm <b>Đóng Công Tắc</b> để kiểm tra tính dẫn điện nhé!`;
    } else if (isCond) {
        box.innerHTML = `✅ <b>Kết luận AI: Bóng đèn SÁNG RỰC & Quạt QUAY!</b> Vì <b>${mName}</b> là <b>VẬT DẪN ĐIỆN</b>, cho phép dòng điện (các hạt màu vàng) chạy qua mạch kín từ nguồn điện đến bóng đèn!`;
    } else {
        box.innerHTML = `⚠️ <b>Kết luận AI: Bóng đèn KHÔNG SÁNG!</b> Vì <b>${mName}</b> là <b>VẬT CÁCH ĐIỆN</b>, dòng điện không thể đi qua được. Nhờ tính chất này, nhựa và cao su thường dùng làm vỏ bọc dây điện để đảm bảo an toàn!`;
    }
}

// ==================== VẼ TRẠM 1: MẠCH ĐIỆN SỐNG ĐỘNG ====================
function drawStation1() {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const isFlowing = circuit.switchClosed && circuit.conductors.includes(circuit.material);

    // Tiêu đề trên Canvas
    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 18px sans-serif';
    ctx.fillText('⚡ SƠ ĐỒ MẠCH ĐIỆN THỰC HÀNH (KHOA HỌC LỚP 5)', 25, 35);

    // Khung dây dẫn hình chữ nhật: (120, 100) -> (640, 360)
    ctx.strokeStyle = isFlowing ? '#facc15' : '#64748b';
    ctx.lineWidth = 6;
    ctx.strokeRect(120, 100, 520, 260);

    // Hiệu ứng hạt electron chạy quanh dây khi mạch kín
    if (isFlowing) {
        ctx.fillStyle = '#fef08a';
        const perim = (520 + 260) * 2;
        for (let i = 0; i < 18; i++) {
            let d = ((i * (perim / 18)) + tick * 3.5) % perim;
            let ex = 120, ey = 100;
            if (d < 520) { ex = 120 + d; ey = 100; }
            else if (d < 520 + 260) { ex = 640; ey = 100 + (d - 520); }
            else if (d < 520 * 2 + 260) { ex = 640 - (d - 780); ey = 360; }
            else { ex = 120; ey = 360 - (d - 1300); }

            ctx.beginPath();
            ctx.arc(ex, ey, 5, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // 1. Nguồn điện bên trái (120, 230)
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(75, 165, 90, 130);
    if (circuit.source === 'battery') {
        ctx.fillStyle = '#f97316';
        ctx.fillRect(92, 180, 56, 35);
        ctx.fillStyle = '#334155';
        ctx.fillRect(92, 215, 56, 65);
        ctx.fillStyle = '#e2e8f0';
        ctx.fillRect(108, 170, 24, 10);
        ctx.fillStyle = 'white';
        ctx.font = 'bold 14px sans-serif';
        ctx.fillText('+ PIN -', 96, 245);
    } else {
        // Tấm pin mặt trời
        ctx.fillStyle = '#0284c7';
        ctx.fillRect(80, 180, 80, 95);
        ctx.strokeStyle = '#bae6fd';
        ctx.lineWidth = 2;
        ctx.strokeRect(80, 180, 80, 95);
        ctx.fillStyle = '#fde047';
        ctx.font = 'bold 24px sans-serif';
        ctx.fillText('☀️', 105, 165);
        ctx.fillStyle = 'white';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('PIN MẶT TRỜI', 82, 295);
    }

    // 2. Công tắc ở cạnh trên (300, 100)
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(260, 80, 90, 40);
    ctx.fillStyle = '#ef4444';
    ctx.beginPath(); ctx.arc(265, 100, 7, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.arc(345, 100, 7, 0, Math.PI * 2); ctx.fill();

    ctx.strokeStyle = '#f8fafc';
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(265, 100);
    if (circuit.switchClosed) {
        ctx.lineTo(345, 100);
    } else {
        ctx.lineTo(335, 62);
    }
    ctx.stroke();
    ctx.fillStyle = '#cbd5e1';
    ctx.font = 'bold 14px sans-serif';
    ctx.fillText(circuit.switchClosed ? 'Công tắc: ĐÓNG' : 'Công tắc: MỞ', 255, 50);

    // 3. Bóng đèn & Quạt nhỏ bên phải (640, 230)
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(600, 160, 80, 130);

    if (isFlowing) {
        const grad = ctx.createRadialGradient(640, 210, 10, 640, 210, 75);
        grad.addColorStop(0, 'rgba(253, 224, 71, 0.95)');
        grad.addColorStop(1, 'rgba(253, 224, 71, 0)');
        ctx.fillStyle = grad;
        ctx.beginPath(); ctx.arc(640, 210, 75, 0, Math.PI * 2); ctx.fill();
    }

    ctx.beginPath();
    ctx.arc(640, 210, 32, 0, Math.PI * 2);
    ctx.fillStyle = isFlowing ? '#fef08a' : '#475569';
    ctx.fill();
    ctx.lineWidth = 3;
    ctx.strokeStyle = isFlowing ? '#facc15' : '#94a3b8';
    ctx.stroke();

    ctx.fillStyle = '#94a3b8';
    ctx.fillRect(626, 240, 28, 20);
    ctx.fillStyle = isFlowing ? '#fde047' : '#cbd5e1';
    ctx.font = 'bold 14px sans-serif';
    ctx.fillText(isFlowing ? '💡 ĐÈN SÁNG!' : '💡 Đèn tắt', 602, 285);

    // 4. Khe thử Vật Dẫn Điện / Vật Cách Điện ở cạnh dưới (380, 360)
    ctx.fillStyle = '#1e293b';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.fillRect(280, 325, 200, 70);
    ctx.strokeRect(280, 325, 200, 70);

    const matColors = {
        copper: '#d97706', iron: '#94a3b8', plastic: '#38bdf8',
        wood: '#854d0e', saltwater: '#22d3ee', rubber: '#f43f5e'
    };
    ctx.fillStyle = matColors[circuit.material];
    ctx.fillRect(300, 345, 160, 28);

    ctx.fillStyle = 'white';
    ctx.font = 'bold 14px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(circuit.matNames[circuit.material], 380, 364);
    ctx.fillStyle = isFlowing ? '#4ade80' : '#f87171';
    ctx.fillText(circuit.conductors.includes(circuit.material) ? '👉 VẬT DẪN ĐIỆN' : '👉 VẬT CÁCH ĐIỆN', 380, 315);
    ctx.textAlign = 'left';
}

// ==================== LOGIC & VẼ TRẠM 2: BIẾN ĐỔI CHẤT ====================
function changeChemExperiment() {
    chem.type = document.getElementById('chemSelect').value;
    chem.stirring = 0;
    updateChemExplanation();
}

function stirBeaker() {
    chem.stirring = 60;
    playTone(true);
    updateChemExplanation();
}

function toggleHeat() {
    chem.heating = !chem.heating;
    const btn = document.getElementById('heatBtn');
    btn.className = 'act-btn' + (chem.heating ? ' selected' : '');
    btn.innerText = chem.heating ? '🔥 Đang Đun Nóng (Bấm để Tắt)' : '🔥 Bật Đèn Cồn Đun Nóng';
    updateChemExplanation();
}

function updateChemExplanation() {
    const box = document.getElementById('aiExplain');
    if (chem.type === 'sugar') {
        box.innerHTML = `🧪 <b>Trợ lý AI:</b> Khi khuấy <b>Đường vào Nước</b>, các hạt đường phân tán đều và tan hoàn toàn tạo thành <b>DUNG DỊCH nước đường</b> đồng nhất (Khi đun nóng đường càng tan nhanh hơn!).`;
    } else if (chem.type === 'sand') {
        box.innerHTML = `🧪 <b>Trợ lý AI:</b> <b>Cát không tan trong nước!</b> Dù em có khuấy mạnh thì sau đó hạt cát vẫn lắng xuống đáy cốc. Đây là một <b>HỖN HỢP</b>, ta có thể tách cát ra bằng cách lọc hoặc lắng gạn.`;
    } else if (chem.type === 'oil') {
        box.innerHTML = `🧪 <b>Trợ lý AI:</b> <b>Dầu ăn nhẹ hơn nước và không tan trong nước</b> nên luôn nổi lên tạo thành một lớp màu vàng phía trên mặt nước!`;
    } else if (chem.type === 'baking') {
        box.innerHTML = `🎉 <b>Sự Biến Đổi Hóa Học!</b> Khi đổ <b>Giấm ăn vào Baking Soda</b>, chúng phản ứng tạo ra chất mới là <b>khí Cacbon đioxit (CO₂)</b> sủi bọt trắng xóa khắp cốc!`;
    } else {
        box.innerHTML = `🌡️ <b>Sự Chuyển Thể Của Nước (Biến đổi Vật lý):</b> Hãy bấm <b>"🔥 Bật Đèn Cồn"</b>! Dưới 0°C nước ở thể rắn (nước đá), nóng lên chuyển thành thể lỏng, và đạt <b>100°C nước sôi bốc hơi</b> mạnh thành thể khí!`;
    }
}

function drawStation2() {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    if (chem.heating && chem.temp < 100) chem.temp += 0.25;
    else if (!chem.heating && chem.temp > 25) chem.temp -= 0.15;
    document.getElementById('tempDisplay').innerText = Math.round(chem.temp) + '°C';

    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 18px sans-serif';
    ctx.fillText('🧪 PHÒNG THÍ NGHIỆM DUNG DỊCH & SỰ BIẾN ĐỔI CỦA CHẤT', 25, 35);

    // Bàn thí nghiệm
    ctx.fillStyle = '#334155';
    ctx.fillRect(150, 370, 460, 18);

    // Cốc thủy tinh (Beaker): x=280..480, y=120..350
    ctx.fillStyle = 'rgba(56, 189, 248, 0.35)';
    ctx.fillRect(285, 180, 190, 165);

    // Vẽ hiện tượng bên trong cốc
    if (chem.type === 'oil') {
        ctx.fillStyle = 'rgba(250, 204, 21, 0.85)';
        ctx.fillRect(285, 155, 190, 35);
        ctx.fillStyle = '#fef08a';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Lớp Dầu ăn nổi phía trên', 305, 177);
    } else if (chem.type === 'sand') {
        ctx.fillStyle = '#d97706';
        for (let i = 0; i < 45; i++) {
            let sy = chem.stirring > 0 ? (220 + (i * 19 + tick * 3) % 120) : (330 + (i % 12));
            ctx.fillRect(295 + (i * 3.8), sy, 4, 4);
        }
    } else if (chem.type === 'baking' || chem.temp >= 85) {
        // Sủi bọt khí CO2 hoặc nước sôi
        ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
        chem.bubbles.forEach(b => {
            b.y -= b.s * (chem.temp >= 85 ? 2.2 : 1.5);
            if (b.y < 165) b.y = 340;
            ctx.beginPath(); ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2); ctx.fill();
        });
    } else if (chem.type === 'state' && chem.temp < 40) {
        // Viên nước đá nổi
        ctx.fillStyle = 'rgba(224, 242, 254, 0.85)';
        ctx.fillRect(320, 175, 45, 35);
        ctx.fillRect(390, 178, 45, 35);
    }

    if (chem.stirring > 0) {
        chem.stirring--;
        ctx.strokeStyle = '#e2e8f0';
        ctx.lineWidth = 5;
        let sx = 380 + Math.sin(tick * 0.3) * 45;
        ctx.beginPath(); ctx.moveTo(380, 90); ctx.lineTo(sx, 320); ctx.stroke();
    }

    // Thành cốc thủy tinh và vạch chia ml
    ctx.strokeStyle = '#e2e8f0';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(280, 120); ctx.lineTo(280, 350); ctx.lineTo(480, 350); ctx.lineTo(480, 120);
    ctx.stroke();

    ctx.fillStyle = '#cbd5e1';
    ctx.font = '12px sans-serif';
    [100, 200, 300].forEach((ml, i) => {
        let my = 310 - i * 50;
        ctx.fillText(ml + ' ml', 490, my + 4);
        ctx.beginPath(); ctx.moveTo(465, my); ctx.lineTo(480, my); ctx.stroke();
    });

    // Ngọn lửa đèn cồn bên dưới
    if (chem.heating) {
        ctx.fillStyle = '#f97316';
        ctx.beginPath();
        ctx.arc(380, 362, 18 + Math.sin(tick * 0.4) * 4, Math.PI, 0);
        ctx.fill();
        ctx.fillStyle = '#fef08a';
        ctx.beginPath();
        ctx.arc(380, 362, 10, Math.PI, 0);
        ctx.fill();
    }
}

// ==================== LOGIC & VẼ TRẠM 3: KHÍ HẬU & MÔI TRƯỜNG ====================
function updateEco() {
    eco.trees = parseInt(document.getElementById('treeSlider').value);
    eco.clean = parseInt(document.getElementById('cleanSlider').value);
    eco.smoke = parseInt(document.getElementById('smokeSlider').value);

    document.getElementById('treeVal').innerText = eco.trees;
    document.getElementById('cleanVal').innerText = eco.clean;
    document.getElementById('smokeVal').innerText = eco.smoke;

    // Công thức mô phỏng nhiệt độ và chất lượng không khí
    let temp = 27.0 + (eco.smoke * 0.06) - (eco.trees * 0.03) - (eco.clean * 0.02);
    eco.earthTemp = Math.max(24.0, Math.min(34.0, temp));

    const box = document.getElementById('aiExplain');
    if (eco.earthTemp <= 26.5) {
        box.innerHTML = `🌱 <b>Môi trường Xanh Lý Tưởng (Nhiệt độ: ${eco.earthTemp.toFixed(1)}°C):</b> Nhờ trồng nhiều cây xanh hấp thụ khí CO₂ và dùng điện mặt trời, điện gió, bầu khí quyển rất trong lành!`;
    } else if (eco.earthTemp <= 29.0) {
        box.innerHTML = `🌤️ <b>Môi trường Trung bình (Nhiệt độ: ${eco.earthTemp.toFixed(1)}°C):</b> Hãy trồng thêm cây xanh và giảm khí thải nhà máy để ngăn chặn hiệu ứng nhà kính nhé!`;
    } else {
        box.innerHTML = `🔥 <b>Cảnh báo Hiệu ứng Nhà kính (${eco.earthTemp.toFixed(1)}°C):</b> Khói bụi CO₂ quá cao làm Trái Đất nóng lên! Hãy tăng diện tích rừng và năng lượng tái tạo ngay!`;
    }
}

function setGreenIdeal() {
    document.getElementById('treeSlider').value = 90;
    document.getElementById('cleanSlider').value = 85;
    document.getElementById('smokeSlider').value = 10;
    playTone(true);
    updateEco();
}

function drawStation3() {
    // Màu bầu trời phụ thuộc độ ô nhiễm
    const skyR = Math.min(200, 30 + eco.smoke * 1.4);
    const skyG = Math.max(110, 190 - eco.smoke * 0.8);
    const skyB = Math.max(120, 245 - eco.smoke * 1.1);
    ctx.fillStyle = `rgb(${skyR}, ${skyG}, ${skyB})`;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Mặt trời
    ctx.fillStyle = '#fde047';
    ctx.beginPath(); ctx.arc(650, 75, 38, 0, Math.PI * 2); ctx.fill();

    // Mặt đất xanh hoặc khô cằn
    ctx.fillStyle = eco.trees > 40 ? '#2f9e44' : '#b45309';
    ctx.fillRect(0, 310, canvas.width, 130);

    // Dòng sông
    ctx.fillStyle = eco.smoke < 50 ? '#0ea5e9' : '#64748b';
    ctx.fillRect(0, 365, canvas.width, 75);

    // Vẽ Cây xanh theo số lượng thanh trượt
    const numTrees = Math.floor(eco.trees / 8);
    for (let i = 0; i < numTrees; i++) {
        let tx = 40 + i * 42;
        ctx.fillStyle = '#78350f';
        ctx.fillRect(tx - 4, 275, 8, 35);
        ctx.fillStyle = '#16a34a';
        ctx.beginPath(); ctx.arc(tx, 265, 20, 0, Math.PI * 2); ctx.fill();
    }

    // Vẽ Tua-bin Điện gió khi Clean Energy > 20
    if (eco.clean >= 25) {
        [520, 610].forEach(wx => {
            ctx.strokeStyle = '#f8fafc';
            ctx.lineWidth = 4;
            ctx.beginPath(); ctx.moveTo(wx, 310); ctx.lineTo(wx, 190); ctx.stroke();
            for (let b = 0; b < 3; b++) {
                let ang = (tick * 0.04) + (b * Math.PI * 2 / 3);
                ctx.beginPath();
                ctx.moveTo(wx, 190);
                ctx.lineTo(wx + Math.cos(ang) * 42, 190 + Math.sin(ang) * 42);
                ctx.stroke();
            }
        });
    }

    // Khói nhà máy khi Smoke cao
    if (eco.smoke > 20) {
        ctx.fillStyle = '#475569';
        ctx.fillRect(670, 230, 55, 80);
        ctx.fillStyle = 'rgba(71, 85, 105, 0.65)';
        for (let s = 0; s < 4; s++) {
            let sy = 215 - ((tick + s * 30) % 120);
            ctx.beginPath(); ctx.arc(695 - s * 10, sy, 18 + s * 4, 0, Math.PI * 2); ctx.fill();
        }
    }

    // Bảng chỉ số nhiệt kế Trái Đất
    ctx.fillStyle = 'rgba(15, 23, 42, 0.8)';
    ctx.fillRect(20, 20, 320, 55);
    ctx.fillStyle = eco.earthTemp > 29 ? '#f87171' : '#4ade80';
    ctx.font = 'bold 18px sans-serif';
    ctx.fillText(`🌡️ Nhiệt độ Trái Đất: ${eco.earthTemp.toFixed(1)}°C`, 35, 53);
}

// Vòng lặp hoạt hình 60 FPS
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

components.html(science_lab_html, height=640, scrolling=True)
