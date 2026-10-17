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
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn • Tích hợp Chủ đề Năng lượng & Chủ đề Con người và Sức khỏe</p>
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
        font-size: 0.82rem;
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
        font-size: 0.85rem;
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
            <button id="tab1" class="tab-btn active" onclick="switchStation(1)">⚡ Trạm 1: Năng Lượng Điện</button>
            <button id="tab2" class="tab-btn" onclick="switchStation(2)">👶 Trạm 2: Các Giai Đoạn Phát Triển</button>
            <button id="tab3" class="tab-btn" onclick="switchStation(3)">💪 Trạm 3: Sức Khỏe Tuổi Dậy Thì</button>
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
            <div>🌟 <span id="expScore">95</span> Điểm</div>
        </div>

        <div>
            <input type="text" id="nameInput" value="Hiểu Minh" placeholder="Nhập tên học sinh..." oninput="updateName()">
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 1: NĂNG LƯỢNG ĐIỆN (GIỮ NGUYÊN) -->
        <div id="ctrlStation1" class="ctrl-group">
            <div class="ctrl-title">⚡ Chủ đề 2: Mạch Điện Đơn Giản & Vật Dẫn Điện</div>
            <label style="font-size:0.85rem; font-weight:bold;">1. Nguồn Điện (Bài 8, 9, 11):</label>
            <select id="powerSource" onchange="updateCircuit()" style="margin-bottom:8px; margin-top:4px;">
                <option value="battery">🔋 Pin tiểu (Năng lượng điện hóa)</option>
                <option value="solar">☀️ Năng lượng Mặt trời (Bài 11)</option>
            </select>

            <label style="font-size:0.85rem; font-weight:bold;">2. Thử nghiệm vật liệu (Bài 9)[cite: 9]:</label>
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

        <!-- ĐIỀU KHIỂN TRẠM 2: CHỦ ĐỀ 5 - CÁC GIAI ĐOẠN PHÁT TRIỂN CHÍNH (BÀI 23) -->
        <div id="ctrlStation2" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">👶 Chủ đề 5: Các Giai Đoạn Phát Triển (Bài 23)[cite: 9]</div>
            <label style="font-size:0.85rem; font-weight:bold;">Chọn giai đoạn vòng đời con người:</label>
            <div class="btn-grid" style="margin-top:6px; margin-bottom:10px;">
                <button class="act-btn selected" id="stage_kid" onclick="selectStage('kid')">👶 Trẻ em & Thiếu nhi</button>
                <button class="act-btn" id="stage_pub" onclick="selectStage('pub')">🧑‍🎓 Tuổi dậy thì (Lớp 5)</button>
                <button class="act-btn" id="stage_adult" onclick="selectStage('adult')">👨‍💼 Người trưởng thành</button>
                <button class="act-btn" id="stage_old" onclick="selectStage('old')">🧓 Tuổi già</button>
            </div>
            <div style="font-size:0.85rem; color:#087f5b; font-weight:bold;">
                👉 Cơ thể con người lớn lên, thay đổi về chiều cao, cân nặng và trí tuệ qua từng thời kỳ.
            </div>
        </div>

        <!-- ĐIỀU KHIỂN TRẠM 3: CHỦ ĐỀ 5 - CHĂM SÓC SỨC KHỎE TUỔI DẬY THÌ (BÀI 25) -->
        <div id="ctrlStation3" class="ctrl-group" style="display:none;">
            <div class="ctrl-title">💪 Chủ đề 5: Chăm Sóc Sức Khỏe Tuổi Dậy Thì (Bài 25)[cite: 9]</div>
            <label style="font-size:0.85rem; font-weight:bold;">Chọn nội dung chăm sóc sức khỏe:</label>
            <div class="btn-grid" style="margin-top:6px; margin-bottom:10px;">
                <button class="act-btn selected" id="hl_hygiene" onclick="selectHealth('hygiene')">🧼 Vệ sinh cá nhân & Thay đổi thể chất</button>
                <button class="act-btn" id="hl_mental" onclick="selectHealth('mental')">🧠 Dinh dưỡng & Sức khỏe tinh thần</button>
            </div>
            <div style="font-size:0.85rem; color:#087f5b; font-weight:bold;">
                👉 Tuổi dậy thì cần ăn uống đầy đủ dưỡng chất, tập thể dục và giữ tinh thần thoải mái.
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
let humanStage = 'kid';

// Trạm 3
let healthMode = 'hygiene';

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
        document.getElementById('aiExplain').innerHTML = `👶 <b>Bài 23 (Chủ đề 5):</b> Con người trải qua các giai đoạn: Sơ sinh, Trẻ em, Thiếu niên, Tuổi dậy thì, Trưởng thành và Tuổi già[cite: 9].`;
        qText.innerText = "Theo Bài 23 (Chủ đề 5), giai đoạn nào cơ thể có sự phát triển mạnh mẽ nhất về chiều cao và tâm sinh lý?[cite: 9]";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">🧑‍🎓 Tuổi dậy thì</button><button class="act-btn" onclick="answerQuiz(false)">🧓 Tuổi già</button>`;
    } else {
        document.getElementById('aiExplain').innerHTML = `💪 <b>Bài 25 (Chủ đề 5):</b> Chăm sóc sức khỏe tuổi dậy thì bao gồm giữ vệ sinh cơ thể, ăn uống đủ chất, ngủ đủ giấc và giữ tinh thần vui tươi[cite: 9].`;
        qText.innerText = "Theo Bài 25 (Chủ đề 5), việc làm nào cần thiết để chăm sóc cơ thể tuổi dậy thì?[cite: 9]";
        qOpts.innerHTML = `<button class="act-btn" onclick="answerQuiz(true)">🧼 Vệ sinh sạch sẽ & dinh dưỡng đủ chất</button><button class="act-btn" onclick="answerQuiz(false)"> thức khuya & bỏ bữa</button>`;
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
function selectStage(st) {
    humanStage = st;
    ['kid', 'pub', 'adult', 'old'].forEach(s => {
        document.getElementById('stage_' + s).className = 'act-btn' + (s === st ? ' selected' : '');
    });
    const box = document.getElementById('aiExplain');
    if (st === 'kid') {
        box.innerHTML = `👶 <b>Giai đoạn Trẻ em & Thiếu nhi:</b> Cơ thể phát triển chiều cao, cân nặng nhanh chóng, học tập và vui chơi tích cực.`;
    } else if (st === 'pub') {
        box.innerHTML = `🧑‍🎓 <b>Tuổi dậy thì (Học sinh lớp 5):</b> Giai đoạn chuyển tiếp quan trọng từ trẻ em thành người lớn, phát triển mạnh về chiều cao, cân nặng và bắt đầu có sự thay đổi tâm sinh lý[cite: 9].`;
    } else if (st === 'adult') {
        box.innerHTML = `👨‍💼 <b>Người trưởng thành:</b> Cơ thể đạt sự phát triển hoàn thiện nhất, có khả năng lao động, lập gia đình và gánh vác trách nhiệm xã hội.`;
    } else {
        box.innerHTML = `🧓 <b>Tuổi già:</b> Các cơ quan trong cơ thể dần lão hóa, cần được chăm sóc sức khỏe và nghỉ ngơi hợp lý.`;
    }
}

// Trạm 3 logic
function selectHealth(mode) {
    healthMode = mode;
    document.getElementById('hl_hygiene').className = 'act-btn' + (mode === 'hygiene' ? ' selected' : '');
    document.getElementById('hl_mental').className = 'act-btn' + (mode === 'mental' ? ' selected' : '');
    const box = document.getElementById('aiExplain');
    if (mode === 'hygiene') {
        box.innerHTML = `🧼 <b>Vệ sinh & Thể chất (Bài 25):</b> Tắm giặt thường xuyên, giữ vệ sinh sạch sẽ, mặc quần áo thoáng mát và tập thể dục đều đặn[cite: 9].`;
    } else {
        box.innerHTML = `🧠 <b>Dinh dưỡng & Tinh thần (Bài 25):</b> Ăn đủ 4 nhóm chất, uống đủ nước, ngủ đủ giấc và giữ tinh thần lạc quan, chia sẻ với ba mẹ thầy cô[cite: 9].`;
    }
}

// Render Canvas 60 FPS
function drawStation1() {
    ctx.fillStyle = '#0f172a'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    const isFlowing = circuit.switchClosed && circuit.conductors.includes(circuit.material);

    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 17px sans-serif';
    ctx.fillText('⚡ CHỦ ĐỀ 2: MẠCH ĐIỆN & VẬT DẪN ĐIỆN (BÀI 9)[cite: 9]', 25, 32);

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
    ctx.fillText('👶 CHỦ ĐỀ 5: CÁC GIAI ĐOẠN PHÁT TRIỂN CHÍNH CỦA CON NGƯỜI (BÀI 23)[cite: 9]', 25, 32);

    // Sơ đồ các cột mốc phát triển
    const stages = [
        { id: 'kid', label: 'Trẻ em', icon: '👶', x: 120 },
        { id: 'pub', label: 'Tuổi dậy thì', icon: '🧑‍🎓', x: 300 },
        { id: 'adult', label: 'Trưởng thành', icon: '👨‍💼', x: 480 },
        { id: 'old', label: 'Tuổi già', icon: '🧓', x: 640 }
    ];

    stages.forEach(s => {
        let isSel = humanStage === s.id;
        ctx.fillStyle = isSel ? '#0ca678' : '#334155';
        ctx.beginPath(); ctx.arc(s.x, 210, isSel ? 45 : 36, 0, Math.PI * 2); ctx.fill();
        ctx.strokeStyle = isSel ? '#fde047' : '#64748b'; ctx.lineWidth = isSel ? 4 : 2; ctx.stroke();

        ctx.font = 'bold 32px sans-serif'; ctx.textAlign = 'center';
        ctx.fillText(s.icon, s.x, 222);

        ctx.fillStyle = isSel ? '#fde047' : 'white'; ctx.font = 'bold 15px sans-serif';
        ctx.fillText(s.label, s.x, 285);
        ctx.textAlign = 'left';
    });
}

function drawStation3() {
    ctx.fillStyle = '#0f172a'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 17px sans-serif';
    ctx.fillText('💪 CHỦ ĐỀ 5: CHĂM SÓC SỨC KHỎE TUỔI DẬY THÌ (BÀI 25)[cite: 9]', 25, 32);

    // Minh họa chăm sóc sức khỏe (Vệ sinh, Dinh dưỡng, Thể thao)
    const tips = [
        { title: '🧼 Vệ sinh cá nhân', desc: 'Tắm gội sạch sẽ hàng ngày, mặc quần áo thoáng mát.', x: 150 },
        { title: '🥗 Dinh dưỡng đủ chất', desc: 'Ăn đủ 4 nhóm chất, uống đủ nước, hạn chế đồ ăn nhanh.', x: 380 },
        { title: '⚽ Thể thao & Tinh thần', desc: 'Tập thể dục, ngủ đủ giấc, giữ tinh thần vui tươi, lạc quan.', x: 610 }
    ];

    tips.forEach(t => {
        ctx.fillStyle = '#1e293b'; ctx.strokeStyle = '#0ca678'; ctx.lineWidth = 3;
        ctx.fillRect(t.x - 100, 110, 200, 180);
        ctx.strokeRect(t.x - 100, 110, 200, 180);

        ctx.fillStyle = '#fde047'; ctx.font = 'bold 16px sans-serif'; ctx.textAlign = 'center';
        ctx.fillText(t.title, t.x, 145);

        ctx.fillStyle = 'white'; ctx.font = '13px sans-serif';
        // Tự động ngắt dòng đơn giản
        ctx.fillText(t.desc.slice(0, 22), t.x, 185);
        ctx.fillText(t.desc.slice(22), t.x, 210);
        ctx.textAlign = 'left';
    });
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
