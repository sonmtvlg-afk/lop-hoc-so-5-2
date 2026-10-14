import streamlit as st
import random
import time

# ==================== CẤU HÌNH TRANG & GIAO DIỆN ====================
st.set_page_config(
    page_title="Lớp Học Số Thông Minh AI - Lớp 5/2",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS tạo giao diện hiện đại, thu hút học sinh tiểu học
st.markdown("""
<style>
    .main-banner {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #00b4db 100%);
        color: white;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        margin-bottom: 20px;
    }
    .main-banner h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
    }
    .main-banner p {
        margin: 8px 0 0 0;
        font-size: 1.1rem;
        color: #e0f7fa;
    }
    .stat-card {
        background: white;
        padding: 18px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
        border-bottom: 5px solid #00b4db;
    }
    .stat-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #1e3c72;
    }
    .stat-label {
        font-size: 0.95rem;
        color: #555;
    }
    .ai-box {
        background: linear-gradient(135deg, #f3e7e9 0%, #e3eeff 99%, #e3eeff 100%);
        border-left: 6px solid #4facfe;
        padding: 18px;
        border-radius: 12px;
        margin: 15px 0;
        color: #1e293b;
        font-size: 1.05rem;
    }
    .badge-item {
        display: inline-block;
        background: #fff8e1;
        border: 2px solid #ffc107;
        color: #b28704;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: bold;
        margin: 4px;
        font-size: 0.9rem;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(10, 28px);
        grid-gap: 4px;
        justify-content: center;
        margin: 15px auto;
    }
    .grid-cell {
        width: 28px;
        height: 28px;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ==================== KHỞI TẠO DỮ LIỆU PHIÊN (SESSION STATE) ====================
if "student_name" not in st.session_state:
    st.session_state.student_name = "Học sinh Tiêu biểu"
if "student_group" not in st.session_state:
    st.session_state.student_group = "Tổ 1"
if "avatar" not in st.session_state:
    st.session_state.avatar = "🦸‍♂️"
if "xp" not in st.session_state:
    st.session_state.xp = 120
if "trees" not in st.session_state:
    st.session_state.trees = 3
if "streak" not in st.session_state:
    st.session_state.streak = 2
if "level" not in st.session_state:
    st.session_state.level = "Cơ bản"
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "math_correct" not in st.session_state:
    st.session_state.math_correct = 4
if "viet_correct" not in st.session_state:
    st.session_state.viet_correct = 3
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "group_scores" not in st.session_state:
    st.session_state.group_scores = {
        "Tổ 1": 450,
        "Tổ 2": 420,
        "Tổ 3": 480,
        "Tổ 4": 410
    }

# ==================== NGÂN HÀNG CÂU HỎI THÍCH ỨNG (ADAPTIVE BANK) ====================
QUESTIONS = [
    {
        "subject": "Toán học Xanh",
        "difficulty": "Cơ bản",
        "question": "🌱 Để phủ xanh góc sân trường Bình Phước A, lớp 5/2 trồng 100 cây hoa, trong đó có 35 cây hoa mười giờ. Tỉ số phần trăm của số cây hoa mười giờ so với tổng số cây là bao nhiêu?",
        "options": ["A. 0,35%", "B. 3,5%", "C. 35%", "D. 65%"],
        "correct": "C. 35%",
        "ai_hint": "💡 **Trợ lý AI gợi ý:** Phân số chỉ số cây hoa mười giờ là 35/100. Khi mẫu số đã là 100, tử số chính là giá trị phần trăm!",
        "ai_explain": "🌟 **AI Giải thích:** 35 trên 100 cây tương ứng với phân số thập phân 35/100 = 0,35 = 35%. Trồng cây giúp giảm nhiệt độ sân trường và bảo vệ môi trường!"
    },
    {
        "subject": "Toán học Xanh",
        "difficulty": "Vận dụng",
        "question": "♻️ Trong phong trào 'Kế hoạch nhỏ - Phân loại rác nhựa', Tổ 1 thu gom được 4,5 kg giấy vụn, Tổ 2 thu gom được nhiều hơn Tổ 1 là 1,25 kg. Hỏi cả hai tổ thu gom được bao nhiêu ki-lô-gam giấy vụn?",
        "options": ["A. 5,75 kg", "B. 10,25 kg", "C. 9,75 kg", "D. 8,5 kg"],
        "correct": "B. 10,25 kg",
        "ai_hint": "💡 **Trợ lý AI gợi ý:** Đây là bài toán 2 bước tính! Bước 1: Tính số giấy vụn của Tổ 2 (4,5 + 1,25). Bước 2: Cộng số giấy của cả hai tổ lại nhé!",
        "ai_explain": "🌟 **AI Giải thích:** Tổ 2 thu được: 4,5 + 1,25 = 5,75 (kg). Cả hai tổ thu được: 4,5 + 5,75 = 10,25 (kg). Tái chế giấy giúp cứu hàng chục cây xanh!"
    },
    {
        "subject": "Tiếng Việt Sáng Tạo",
        "difficulty": "Cơ bản",
        "question": "📚 Trong câu: 'Dòng sông Mang Thít hiền hòa ôm ấp những vườn cây trái sum suê.', biện pháp nghệ thuật nào đã được sử dụng?",
        "options": ["A. So sánh", "B. Nhân hóa", "C. Điệp từ", "D. Đảo ngữ"],
        "correct": "B. Nhân hóa",
        "ai_hint": "💡 **Trợ lý AI gợi ý:** Hãy chú ý các từ 'hiền hòa', 'ôm ấp'. Đó vốn là tính cách và hành động của con người được gán cho dòng sông!",
        "ai_explain": "🌟 **AI Giải thích:** Tác giả dùng từ chỉ phẩm chất và hành động của con người ('hiền hòa', 'ôm ấp') để miêu tả dòng sông, giúp cảnh vật quê hương Vĩnh Long trở nên gần gũi, có hồn hơn."
    },
    {
        "subject": "Toán học Xanh",
        "difficulty": "Nâng cao",
        "question": "⚡ Trường Tiểu học lắp đặt hệ thống đèn LED năng lượng mặt trời giúp giảm 25% lượng điện tiêu thụ mỗi tháng. Biết trước đây trường dùng 400 kWh điện/tháng. Hỏi hiện nay trường tiết kiệm được bao nhiêu kWh điện mỗi tháng?",
        "options": ["A. 100 kWh", "B. 300 kWh", "C. 25 kWh", "D. 150 kWh"],
        "correct": "A. 100 kWh",
        "ai_hint": "💡 **Trợ lý AI gợi ý:** Muốn tìm 25% của 400 kWh, em lấy 400 chia cho 100 rồi nhân với 25 (hoặc nhận xét 25% = 1/4).",
        "ai_explain": "🌟 **AI Giải thích:** Lượng điện tiết kiệm được là: 400 × 25 : 100 = 100 (kWh). Sử dụng năng lượng sạch là hành động thiết thực chống biến đổi khí hậu!"
    },
    {
        "subject": "Tiếng Việt Sáng Tạo",
        "difficulty": "Vận dụng",
        "question": "🌿 Từ 'xanh' trong câu: 'Tuổi trẻ học đường cùng chung tay vì một tương lai xanh.' được dùng theo nghĩa gốc hay nghĩa chuyển?",
        "options": ["A. Nghĩa gốc (chỉ màu sắc của lá cây)", "B. Nghĩa chuyển (chỉ sự trong lành, bền vững, thân thiện với môi trường)"],
        "correct": "B. Nghĩa chuyển (chỉ sự trong lành, bền vững, thân thiện với môi trường)",
        "ai_hint": "💡 **Trợ lý AI gợi ý:** 'Tương lai' không phải là một vật thể có thể sơn màu xanh lá. Từ 'xanh' ở đây ẩn dụ cho điều gì tốt đẹp?",
        "ai_explain": "🌟 **AI Giải thích:** Từ 'xanh' được dùng theo nghĩa chuyển, biểu tượng cho lối sống sinh thái, phát triển bền vững và hài hòa với thiên nhiên."
    }
]

# ==================== THANH BÊN (SIDEBAR): HỒ SƠ HỌC SINH ====================
with st.sidebar:
    st.markdown("### 🏫 TRƯỜNG TH BÌNH PHƯỚC A")
    st.caption("Mô hình Lớp học số thông minh - Lớp 5/2")
    st.markdown("---")
    
    st.subheader("👤 Hồ sơ Học sinh Số")
    st.session_state.avatar = st.selectbox(
        "Chọn Nhân vật đồng hành:",
        ["🦸‍♂️ Siêu nhân Toán học", "🧚‍♀️ Tiên nữ Tiếng Việt", "🤖 Robot AI Thông thái", "🌱 Đại sứ Môi trường"]
    )
    st.session_state.student_name = st.text_input("Họ và tên học sinh:", st.session_state.student_name)
    st.session_state.student_group = st.selectbox("Thuộc Tổ thi đua:", ["Tổ 1", "Tổ 2", "Tổ 3", "Tổ 4"])
    
    st.markdown("---")
    st.markdown("#### 🏆 Huy hiệu Đạt được")
    badges = []
    if st.session_state.xp >= 100:
        badges.append("🌟 Tân binh Lớp học số")
    if st.session_state.math_correct >= 3:
        badges.append("🧮 Chiến binh Toán học")
    if st.session_state.trees >= 4:
        badges.append("🌳 Đại sứ Xanh")
    if st.session_state.streak >= 3:
        badges.append("🔥 Chuỗi Thắng Lợi")
        
    for b in badges:
        st.markdown(f'<span class="badge-item">{b}</span>', unsafe_allow_html=True)
        
    st.markdown("---")
    st.info("👨‍🏫 **GVCN & Tổ khối trưởng:**\nThầy Huỳnh Minh Sơn\n\n🎯 *Định hướng Chương trình GDPT 2018 & Thông tư 27*")

# ==================== BANNER CHÍNH & THỐNG KÊ GAME HÓA ====================
st.markdown(f"""
<div class="main-banner">
    <h1>🚀 MATH & VIET FUN ACADEMY AI - LỚP 5/2</h1>
    <p>Mô hình Lớp học số thông minh tích hợp Trí tuệ nhân tạo (AI) & Gamification phát triển năng lực toàn diện</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">{st.session_state.avatar.split()[0]} {st.session_state.student_name}</div>
        <div class="stat-label">Đội viên {st.session_state.student_group} - Lớp 5/2</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">⭐ {st.session_state.xp} XP</div>
        <div class="stat-label">Điểm Kinh Nghiệm Tích Lũy</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">🌳 {st.session_state.trees} Cây xanh</div>
        <div class="stat-label">Vườn Trường Tri Thức Xanh</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">🔥 Chuỗi {st.session_state.streak}</div>
        <div class="stat-label">Cấp độ AI: {st.session_state.level}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==================== CÁC PHÂN KHU CHỨC NĂNG (4 TABS) ====================
tab1, tab2, tab3, tab4 = st.tabs([
    "🔬 1. Phòng Thí Nghiệm Toán Trực Quan (Visual Lab)",
    "🎮 2. Đấu Trường AI Thích Ứng (Toán & Tiếng Việt)",
    "🤖 3. Trợ Lý AI Giải Đáp & Rèn Chữ Giữ Nết",
    "📊 4. Bảng Thi Đua Tổ & Đánh Giá Thông Tư 27 (Dành cho GV)"
])

# -------------------- TAB 1: PHÒNG THÍ NGHIỆM TOÁN HỌC TRỰC QUAN --------------------
with tab1:
    st.subheader("🔬 Mô hình hóa Trực quan: Phân số - Số thập phân - Tỉ số phần trăm")
    st.write("Giúp học sinh lớp 5 nhìn thấy bản chất toán học qua lưới 100 ô vuông sinh thái thay vì học vẹt công thức.")
    
    col_left, col_right = st.columns([1, 1.3])
    
    with col_left:
        st.markdown("#### ⚙️ Điều khiển Mô hình")
        mode = st.radio(
            "Chọn chủ đề khám phá:",
            ["Mô hình Lưới 100 (Phân số thập phân & Phần trăm)", "Mô hình So sánh & Quy đồng Phân số"],
            horizontal=False
        )
        
        if mode == "Mô hình Lưới 100 (Phân số thập phân & Phần trăm)":
            green_cells = st.slider("🌱 Số ô trồng Cây Xanh (Tử số):", 0, 100, 45)
            solar_cells = st.slider("☀️ Số ô lắp Điện Mặt Trời:", 0, 100 - green_cells, 25)
            empty_cells = 100 - green_cells - solar_cells
            
            st.markdown(f"""
            <div class="ai-box">
                🤖 <b>Trợ lý AI Phân tích Trực quan:</b><br>
                • <b>Diện tích Cây Xanh:</b> Phân số <b>{green_cells}/100</b> = Số thập phân <b>{green_cells/100:.2f}</b> = Tỉ số phần trăm <b>{green_cells}%</b><br>
                • <b>Diện tích Điện Mặt Trời:</b> Phân số <b>{solar_cells}/100</b> = Số thập phân <b>{solar_cells/100:.2f}</b> = Tỉ số phần trăm <b>{solar_cells}%</b><br>
                • <b>Tổng diện tích Xanh hóa:</b> <b>{green_cells + solar_cells}%</b> sân trường (Còn lại <b>{empty_cells}%</b> sân chơi).
            </div>
            """, unsafe_allow_html=True)
        else:
            tu = st.slider("Chọn Tử số:", 1, 12, 3)
            mau = st.slider("Chọn Mẫu số:", max(tu, 1), 12, 4)
            he_so = st.slider("Nhân cả tử và mẫu với (Quy đồng):", 1, 5, 2)
            st.markdown(f"""
            <div class="ai-box">
                🤖 <b>Trợ lý AI Giải thích Tính chất cơ bản của Phân số:</b><br>
                Khi nhân cả tử và mẫu của phân số <b>{tu}/{mau}</b> với <b>{he_so}</b>, ta được phân số mới <b>{tu*he_so}/{mau*he_so}</b>.<br>
                👉 Dù số phần chia nhỏ hơn gấp {he_so} lần, nhưng <b>giá trị thực tế không đổi ({tu/mau:.2f} = {tu/mau*100:.1f}%)</b>!
            </div>
            """, unsafe_allow_html=True)

    with col_right:
        if mode == "Mô hình Lưới 100 (Phân số thập phân & Phần trăm)":
            st.markdown("#### 🗺️ Bản đồ Sinh thái Sân trường (100 ô vuông đơn vị)")
            cells_html = '<div class="grid-container">'
            for i in range(100):
                if i < green_cells:
                    cells_html += '<div class="grid-cell" style="background:#2ecc71; color:white;">🌱</div>'
                elif i < green_cells + solar_cells:
                    cells_html += '<div class="grid-cell" style="background:#f1c40f; color:#333;">☀️</div>'
                else:
                    cells_html += '<div class="grid-cell" style="background:#ecf0f1; color:#95a5a6;">⬜</div>'
            cells_html += '</div>'
            st.markdown(cells_html, unsafe_allow_html=True)
            st.caption("Chú thích: 🌱 Cây xanh | ☀️ Điện mặt trời | ⬜ Sân sinh hoạt")
        else:
            st.markdown("#### 📊 Trực quan hóa Thanh Phân số tương đương")
            st.write(f"**Phân số ban đầu ({tu}/{mau}):**")
            bar1 = "🟩 " * tu + "⬜ " * (mau - tu)
            st.markdown(f"<div style='font-size:26px; letter-spacing:3px;'>{bar1}</div>", unsafe_allow_html=True)
            
            st.write(f"**Phân số sau khi nhân cả tử và mẫu với {he_so} ({tu*he_so}/{mau*he_so}):**")
            bar2 = "🟦 " * (tu * he_so) + "⬜ " * ((mau - tu) * he_so)
            st.markdown(f"<div style='font-size:18px; letter-spacing:1px;'>{bar2}</div>", unsafe_allow_html=True)
            st.progress(tu / mau)

# -------------------- TAB 2: ĐẤU TRƯỜNG AI THÍCH ỨNG --------------------
with tab2:
    st.subheader("🎮 Đấu Trường Thử Thách AI Thích Ứng (Adaptive Learning)")
    st.write("Hệ thống AI tự động điều chỉnh câu hỏi và đưa ra gợi ý dẫn dắt (Scaffolding) khi học sinh gặp khó khăn.")
    
    current_q = QUESTIONS[st.session_state.q_index]
    
    col_q, col_status = st.columns([2, 1])
    with col_q:
        st.markdown(f"**Môn học:** `{current_q['subject']}` | **Mức độ năng lực:** `{current_q['difficulty']}`")
        st.markdown(f"### Câu hỏi {st.session_state.q_index + 1}/{len(QUESTIONS)}:")
        st.info(current_q["question"])
        
        user_choice = st.radio(
            "Chọn đáp án của em:",
            current_q["options"],
            key=f"q_radio_{st.session_state.q_index}"
        )
        
        c_btn1, c_btn2, c_btn3 = st.columns(3)
        with c_btn1:
            if st.button("✅ Nộp bài & Kiểm tra", use_container_width=True):
                if user_choice == current_q["correct"]:
                    st.balloons()
                    st.success("🎉 Chính xác tuyệt đối! Em được thưởng +20 XP và trồng thêm +1 Cây xanh cho lớp 5/2!")
                    st.markdown(f'<div class="ai-box">{current_q["ai_explain"]}</div>', unsafe_allow_html=True)
                    st.session_state.xp += 20
                    st.session_state.trees += 1
                    st.session_state.streak += 1
                    st.session_state.group_scores[st.session_state.student_group] += 20
                    if "Toán" in current_q["subject"]:
                        st.session_state.math_correct += 1
                    else:
                        st.session_state.viet_correct += 1
                    
                    # Nâng cấp độ thích ứng
                    if st.session_state.streak >= 3:
                        st.session_state.level = "Vận dụng cao 🌟"
                    elif st.session_state.streak >= 2:
                        st.session_state.level = "Vận dụng 🚀"
                    st.session_state.show_hint = False
                else:
                    st.session_state.streak = 0
                    st.session_state.level = "Cơ bản"
                    st.session_state.show_hint = True
                    st.warning("Chưa chính xác rồi! Đừng lo, hãy xem gợi ý từng bước của Trợ lý AI bên dưới để thử lại nhé!")
        
        with c_btn2:
            if st.button("💡 Xin gợi ý từ AI", use_container_width=True):
                st.session_state.show_hint = True
                
        with c_btn3:
            if st.button("⏭️ Câu tiếp theo", use_container_width=True):
                st.session_state.q_index = (st.session_state.q_index + 1) % len(QUESTIONS)
                st.session_state.show_hint = False
                st.rerun()

        if st.session_state.show_hint:
            st.markdown(f'<div class="ai-box">{current_q["ai_hint"]}</div>', unsafe_allow_html=True)

    with col_status:
        st.markdown("#### 🧠 Trạng thái AI Cá nhân hóa")
        st.write(f"**Độ khó hiện tại:** `{st.session_state.level}`")
        st.write(f"**Số câu Toán hoàn thành:** {st.session_state.math_correct} câu")
        st.write(f"**Số câu Tiếng Việt hoàn thành:** {st.session_state.viet_correct} câu")
        st.progress(min(st.session_state.xp / 250, 1.0))
        st.caption(f"Tiến độ chinh phục Huy hiệu Đại Kiện Tướng: {st.session_state.xp}/250 XP")

# -------------------- TAB 3: TRỢ LÝ AI GIẢI ĐÁP & RÈN CHỮ GIỮ NẾT --------------------
with tab3:
    st.subheader("🤖 Trợ Lý AI Giải Đáp Tư Duy & Góc 'Rèn Chữ - Giữ Nết'")
    col_ai1, col_ai2 = st.columns(2)
    
    with col_ai1:
        st.markdown("#### 💬 Hỏi - Đáp thông minh cùng Trợ lý AI Lớp 5/2")
        topic_ask = st.selectbox(
            "Chọn vấn đề em cần Trợ lý AI hướng dẫn nhanh:",
            [
                "Cách chuyển phân số bất kỳ sang tỉ số phần trăm dễ nhớ nhất?",
                "Mẹo đặt tính cộng, trừ hai số thập phân không bao giờ nhầm?",
                "Cách tìm từ đồng nghĩa và từ đa nghĩa trong Tiếng Việt 5?",
                "Bí quyết rèn chữ đẹp, giữ vở sạch để rèn tính kiên trì, tỉ mỉ?"
            ]
        )
        
        ai_responses = {
            "Cách chuyển phân số bất kỳ sang tỉ số phần trăm dễ nhớ nhất?": 
                "🤖 **Trợ lý AI Lớp 5/2:** Có 2 cách cực kỳ dễ nhớ!\n"
                "1. **Cách 1 (Nhẩm nhanh):** Nếu mẫu số là ước của 100 (như 2, 4, 5, 10, 20, 25, 50), em nhân cả tử và mẫu để mẫu số thành 100. Ví dụ: 3/4 = 75/100 = 75%.\n"
                "2. **Cách 2 (Tổng quát):** Lấy tử số chia cho mẫu số (ra số thập phân), sau đó nhân nhẩm với 100 và viết thêm ký hiệu **%** vào bên phải!",
            "Mẹo đặt tính cộng, trừ hai số thập phân không bao giờ nhầm?":
                "🤖 **Trợ lý AI Lớp 5/2:** Quy tắc vàng là **'Dấu phẩy thẳng hàng'**!\n"
                "• Bước 1: Viết các dấu phẩy của các số thẳng cột dọc với nhau trước.\n"
                "• Bước 2: Nếu phần thập phân bên nào ngắn hơn, em có thể viết thêm chữ số 0 vào bên phải cho bằng nhau rồi cộng/trừ như số tự nhiên!",
            "Cách tìm từ đồng nghĩa và từ đa nghĩa trong Tiếng Việt 5?":
                "🤖 **Trợ lý AI Lớp 5/2:**\n"
                "• **Từ đồng nghĩa:** Là những từ khác nhau về âm đọc nhưng giống hoặc gần giống nhau về nghĩa (Ví dụ: *chăm chỉ, siêng năng, cần cù*).\n"
                "• **Từ đa nghĩa:** Chỉ là 1 từ duy nhất nhưng có nghĩa gốc và nghĩa chuyển (Ví dụ: *'chân bàn'*, *'chân núi'* được chuyển nghĩa từ *'đôi chân'*).",
            "Bí quyết rèn chữ đẹp, giữ vở sạch để rèn tính kiên trì, tỉ mỉ?":
                "🤖 **Trợ lý AI Lớp 5/2:** Rèn chữ chính là rèn tính kiên nhẫn và cẩn thận!\n"
                "• Ngồi thẳng lưng, mắt cách vở 25–30cm.\n"
                "• Chú ý độ cao con chữ (chữ hoa 2,5 ô li; chữ l, b, h, g, y cao 2,5 ô li) và khoảng cách giữa các chữ bằng 1 thân con chữ *o*."
        }
        st.markdown(f'<div class="ai-box">{ai_responses[topic_ask]}</div>', unsafe_allow_html=True)

    with col_ai2:
        st.markdown("#### ✍️ Cam kết 'Rèn Chữ - Luyện Nết - Làm Việc Tốt'")
        st.write("Đánh dấu các mục tiêu rèn luyện phẩm chất mỗi ngày của học sinh lớp 5/2:")
        c1 = st.checkbox("Trình bày vở Toán và Tiếng Việt sạch đẹp, rõ ràng, thẳng cột (+10 XP)")
        c2 = st.checkbox("Tự giác hoàn thành bài tập và giúp đỡ bạn cùng tổ (+10 XP)")
        c3 = st.checkbox("Tắt quạt, tắt đèn khi ra khỏi lớp và bỏ rác đúng nơi quy định (+10 XP)")
        
        if st.button("🌟 Xác nhận Hoàn thành Mục tiêu Rèn luyện"):
            bonus = (10 if c1 else 0) + (10 if c2 else 0) + (10 if c3 else 0)
            if bonus > 0:
                st.session_state.xp += bonus
                st.session_state.group_scores[st.session_state.student_group] += bonus
                st.toast(f"Tuyệt vời! Em đã cộng thêm {bonus} XP cho bản thân và {st.session_state.student_group}!", icon="🎉")
                st.success(f"Đã ghi nhận +{bonus} XP vào Bảng Thi Đua Tổ!")
            else:
                st.warning("Hãy chọn ít nhất 1 mục tiêu em đã hoàn thành hôm nay nhé!")

# -------------------- TAB 4: BẢNG THI ĐUA TỔ & ĐÁNH GIÁ THÔNG TƯ 27 --------------------
with tab4:
    st.subheader("📊 Bảng Theo Dõi Thi Đua Tổ Em & Trợ Lý AI Đánh Giá Thông Tư 27")
    st.write("Công cụ tự động hóa dành cho Giáo viên chủ nhiệm: Tổng hợp điểm thi đua các tổ và sinh nhận xét cá nhân hóa theo Thông tư 27/2020/TT-BGDĐT.")
    
    col_dash1, col_dash2 = st.columns([1.1, 1.2])
    
    with col_dash1:
        st.markdown("#### 🏆 Bảng Theo Dõi Thi Đua Tổ - Lớp 5/2")
        for grp, score in sorted(st.session_state.group_scores.items(), key=lambda x: x[1], reverse=True):
            st.write(f"**{grp}** — `{score} điểm thi đua`")
            st.progress(min(score / 600, 1.0))
            
        st.caption("💡 Điểm số tự động cập nhật theo thời gian thực mỗi khi học sinh trong tổ giải đúng bài tập hoặc hoàn thành mục tiêu rèn luyện.")

    with col_dash2:
        st.markdown("#### 📝 AI Tự động Sinh Nhận xét Học sinh (Chuẩn Thông tư 27)")
        
        # Đánh giá tự động dựa trên dữ liệu học tập
        if st.session_state.xp >= 140:
            muc_dat = "Hoàn thành tốt (HTT)"
            nhan_xet_toan = f"Em {st.session_state.student_name} nắm rất vững kiến thức về phân số, số thập phân và tỉ số phần trăm; biết vận dụng linh hoạt vào giải toán có lời văn thực tiễn."
            nhan_xet_tv = "Đọc hiểu tốt, nhận diện chính xác biện pháp tu từ và sử dụng từ ngữ giàu hình ảnh."
            nhan_xet_nl = "Thể hiện rõ năng lực tự chủ, tự học, năng lực số và ý thức trách nhiệm bảo vệ môi trường; tích cực đóng góp vào thành tích chung của " + st.session_state.student_group + "."
        else:
            muc_dat = "Hoàn thành (HT)"
            nhan_xet_toan = f"Em {st.session_state.student_name} bước đầu nắm được quy tắc chuyển đổi phân số thập phân và tỉ số phần trăm; cần rèn luyện thêm kỹ năng tính toán cẩn thận hơn."
            nhan_xet_tv = "Hiểu nội dung bài đọc, biết phân biệt nghĩa của từ; cần mạnh dạn hơn khi phát biểu xây dựng bài."
            nhan_xet_nl = "Có ý thức tự giác học tập trên lớp học số, hòa đồng với bạn bè trong " + st.session_state.student_group + "."

        st.success(f"**Mức độ đánh giá đề xuất:** {muc_dat}")
        
        report_text = (
            f"HỌ VÀ TÊN HỌC SINH: {st.session_state.student_name} ({st.session_state.student_group} - Lớp 5/2)\n"
            f"1. Môn Toán: {nhan_xet_toan}\n"
            f"2. Môn Tiếng Việt: {nhan_xet_tv}\n"
            f"3. Năng lực & Phẩm chất (TT27): {nhan_xet_nl}\n"
            f"4. Xếp loại định kỳ đề xuất: {muc_dat}"
        )
        st.text_area("Bản nhận xét tự động (Giáo viên có thể sao chép vào sổ theo dõi):", report_text, height=160)
