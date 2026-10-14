import streamlit as st

# ==================== CẤU HÌNH TRANG (TỐI ƯU CHO ĐIỆN THOẠI & MÁY TÍNH) ====================
st.set_page_config(
    page_title="Ngôi Nhà Số Lớp 5/2 - Trường Tiểu học Bình Phước",
    page_icon="🌟",
    layout="centered"
)

# Giao diện CSS tối giản, chữ to, nút bấm lớn, màu sắc tươi sáng
st.markdown("""
<style>
    .header-box {
        background: linear-gradient(135deg, #0072ff 0%, #00c6ff 100%);
        color: white;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(0, 114, 255, 0.25);
    }
    .header-box h1 {
        font-size: 1.8rem;
        margin: 0;
        color: white;
        font-weight: 800;
    }
    .header-box p {
        font-size: 1.05rem;
        margin: 6px 0 0 0;
        color: #e6f7ff;
        font-weight: 600;
    }
    .score-banner {
        background: #fff9db;
        border: 2px solid #ffd43b;
        border-radius: 14px;
        padding: 12px;
        text-align: center;
        font-size: 1.15rem;
        font-weight: bold;
        color: #d9480f;
        margin-bottom: 18px;
    }
    .visual-card {
        background: #f8f9fa;
        border: 2px solid #dee2e6;
        border-radius: 14px;
        padding: 18px;
        margin: 12px 0;
    }
    .ai-helper {
        background: #e7f5ff;
        border-left: 6px solid #1c7ed6;
        padding: 15px;
        border-radius: 10px;
        font-size: 1.05rem;
        color: #1864ab;
        margin: 12px 0;
    }
    .parent-card {
        background: #ebfbee;
        border-left: 6px solid #2b8a3e;
        padding: 16px;
        border-radius: 10px;
        font-size: 1.05rem;
        color: #1b4332;
        margin: 12px 0;
    }
    .cert-box {
        background: linear-gradient(135deg, #fffdf0 0%, #fff3bf 100%);
        border: 3px dashed #f59f00;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== KHỞI TẠO DỮ LIỆU ĐƠN GIẢN ====================
if "name" not in st.session_state:
    st.session_state.name = "Minh Khôi"
if "group" not in st.session_state:
    st.session_state.group = "Tổ 1"
if "stars" not in st.session_state:
    st.session_state.stars = 50
if "trees" not in st.session_state:
    st.session_state.trees = 2
if "q_idx" not in st.session_state:
    st.session_state.q_idx = 0
if "hint_on" not in st.session_state:
    st.session_state.hint_on = False
if "group_points" not in st.session_state:
    st.session_state.group_points = {"Tổ 1": 150, "Tổ 2": 140, "Tổ 3": 160, "Tổ 4": 130}

# ==================== TIÊU ĐỀ CHÍNH ====================
st.markdown("""
<div class="header-box">
    <h1>🌟 NGÔI NHÀ SỐ LỚP 5/2</h1>
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn</p>
</div>
""", unsafe_allow_html=True)

# ==================== BƯỚC 1: NHẬP TÊN NHANH TRÊN MÀN HÌNH CHÍNH ====================
col_info1, col_info2 = st.columns([1.5, 1])
with col_info1:
    st.session_state.name = st.text_input("👦👧 Họ và tên học sinh:", st.session_state.name)
with col_info2:
    st.session_state.group = st.selectbox("🚩 Tổ thi đua:", ["Tổ 1", "Tổ 2", "Tổ 3", "Tổ 4"])

st.markdown(f"""
<div class="score-banner">
    👤 Học sinh: {st.session_state.name} ({st.session_state.group}) &nbsp;|&nbsp; 
    ⭐ {st.session_state.stars} Sao chăm ngoan &nbsp;|&nbsp; 
    🌱 {st.session_state.trees} Cây xanh
</div>
""", unsafe_allow_html=True)

# ==================== MENU CHÍNH DẠNG 3 TAB LỚN DỄ BẤM ====================
tab_hs, tab_ph, tab_bv = st.tabs([
    "🎒 1. GÓC HỌC SINH",
    "👨‍👩‍👧 2. GÓC PHỤ HUYNH",
    "🏆 3. BẢNG VÀNG & NHẬN XÉT"
])

# ==============================================================================
# TAB 1: GÓC HỌC SINH (TRỰC QUAN & TRÒ CHƠI AI)
# ==============================================================================
with tab_hs:
    st.subheader("🍕 Phần 1: Nhìn Hình Hiểu Ngay (Toán Lớp 5)")
    st.write("Kéo thanh trượt để xem mối liên hệ giữa **Phân số – Số thập phân – Phần trăm**:")

    example_type = st.radio(
        "Chọn mô hình gần gũi:",
        ["🍕 Chia bánh Pizza (Hiểu Phân số)", "🔋 Sạc Pin Năng Lượng Mặt Trời (Hiểu Phần trăm %)"],
        horizontal=True
    )

    if "Pizza" in example_type:
        total_slices = st.slider("Chia chiếc bánh thành mấy phần bằng nhau (Mẫu số)?", 2, 10, 4)
        eaten_slices = st.slider("Em lấy mấy phần bánh (Tử số)?", 1, total_slices, 3)

        pizza_visual = "🍕 " * eaten_slices + "⚪ " * (total_slices - eaten_slices)
        decimal_val = eaten_slices / total_slices
        percent_val = decimal_val * 100

        st.markdown(f"""
        <div class="visual-card" style="text-align:center;">
            <div style="font-size: 2.2rem; margin-bottom: 10px;">{pizza_visual}</div>
            <h4>Phân số: <b>{eaten_slices}/{total_slices}</b> chiếc bánh &nbsp;=&nbsp; Số thập phân: <b>{decimal_val:.2f}</b> &nbsp;=&nbsp; Tỉ số phần trăm: <b>{percent_val:.0f}%</b></h4>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="ai-helper">
            🤖 <b>Trợ lý AI Lớp 5/2 giải thích cực dễ:</b><br>
            Chiếc bánh được cắt thành <b>{total_slices} phần bằng nhau</b>. Em lấy <b>{eaten_slices} phần</b>, ta viết là phân số <b>{eaten_slices}/{total_slices}</b>. Nếu đổi ra phần trăm, phần bánh của em chiếm <b>{percent_val:.0f}%</b> cả chiếc bánh!
        </div>
        """, unsafe_allow_html=True)

    else:
        battery = st.slider("Kéo để sạc Pin Năng lượng xanh (%):", 10, 100, 75, step=5)
        filled_blocks = battery // 10
        battery_bar = "🟩" * filled_blocks + "⬜" * (10 - filled_blocks)

        st.markdown(f"""
        <div class="visual-card" style="text-align:center;">
            <div style="font-size: 2rem; letter-spacing: 3px; margin-bottom: 10px;">{battery_bar} ⚡</div>
            <h4>Mức Pin: <b>{battery}%</b> &nbsp;=&nbsp; Phân số thập phân: <b>{battery}/100</b> &nbsp;=&nbsp; Số thập phân: <b>{battery/100:.2f}</b></h4>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="ai-helper">
            🤖 <b>Trợ lý AI Lớp 5/2 giải thích cực dễ:</b><br>
            Cứ thấy ký hiệu <b>%</b> nghĩa là chia cho 100! Vậy <b>{battery}%</b> chính là <b>{battery} phần trên 100 phần</b> ({battery}/100), hay viết gọn dưới dạng số thập phân là <b>{battery/100:.2f}</b>.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🎮 Phần 2: Đố Vui Thông Minh Cùng Trợ Lý AI")

    QUESTIONS = [
        {
            "mon": "Toán 5",
            "cau_hoi": "Câu 1: Phân số 3/4 khi chuyển sang tỉ số phần trăm sẽ bằng bao nhiêu?",
            "dap_an": ["A. 34%", "B. 75%", "C. 25%", "D. 43%"],
            "dung": "B. 75%",
            "goi_y": "💡 Mẹo từ AI: 1/4 chiếc bánh là 25%. Vậy 3 phần như thế (3 × 25%) là bao nhiêu nhỉ?",
            "giai_thich": "Hoan hô! 3/4 = 75/100 = 75%. Em tính nhẩm rất nhanh!"
        },
        {
            "mon": "Toán 5 (Gắn với Thực tế)",
            "cau_hoi": "Câu 2: Mẹ đi chợ mua 1,5 kg cam và 2,25 kg xoài. Hỏi túi trái cây của mẹ nặng tất cả bao nhiêu ki-lô-gam?",
            "dap_an": ["A. 3,75 kg", "B. 3,30 kg", "C. 2,40 kg", "D. 4,25 kg"],
            "dung": "A. 3,75 kg",
            "goi_y": "💡 Mẹo từ AI: Đặt dấu phẩy thẳng cột nhau: 1,50 + 2,25 rồi cộng từ phải sang trái nhé!",
            "giai_thich": "Chính xác! 1,5 + 2,25 = 3,75 kg. Em đã biết giúp mẹ tính toán khi đi chợ rồi đấy!"
        },
        {
            "mon": "Tiếng Việt 5",
            "cau_hoi": "Câu 3: Từ nào dưới đây đồng nghĩa với từ 'Kiên trì'?",
            "dap_an": ["A. Nhút nhát", "B. Bền bỉ", "C. Vội vàng", "D. Lười biếng"],
            "dung": "B. Bền bỉ",
            "goi_y": "💡 Mẹo từ AI: Khi rèn chữ đẹp mỗi ngày, chúng ta cần sự nhẫn nại, không bỏ cuộc. Từ nào mang ý nghĩa đó?",
            "giai_thich": "Tuyệt vời! 'Kiên trì' và 'Bền bỉ' đều chỉ đức tính nhẫn nại, cố gắng đến cùng."
        },
        {
            "mon": "Giáo dục Môi trường Xanh",
            "cau_hoi": "Câu 4: Lớp 5/2 Trường Tiểu học Bình Phước thu gom được 20 kg giấy vụn. Biết cứ 10 kg giấy tái chế giúp cứu được 1 cây xanh. Hỏi lớp mình đã cứu được mấy cây xanh?",
            "dap_an": ["A. 1 cây xanh", "B. 2 cây xanh", "C. 5 cây xanh", "D. 10 cây xanh"],
            "dung": "B. 2 cây xanh",
            "goi_y": "💡 Mẹo từ AI: Lấy 20 kg chia cho 10 kg em sẽ tìm ra số cây xanh được cứu nhé!",
            "giai_thich": "Xuất sắc! 20 : 10 = 2 cây xanh. Tiết kiệm giấy là bảo vệ thiên nhiên!"
        }
    ]

    q = QUESTIONS[st.session_state.q_idx]
    st.markdown(f"**Chủ đề: {q['mon']}**")
    st.info(f"##### {q['cau_hoi']}")

    choice = st.radio("👉 Chọn đáp án của em:", q["dap_an"], key=f"ans_{st.session_state.q_idx}")

    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("✅ Kiểm tra", use_container_width=True):
            if choice == q["dung"]:
                st.balloons()
                st.success(f"🎉 {q['giai_thich']} (+10 Sao ⭐, +1 Cây xanh 🌱)")
                st.session_state.stars += 10
                st.session_state.trees += 1
                st.session_state.group_points[st.session_state.group] += 10
                st.session_state.hint_on = False
            else:
                st.session_state.hint_on = True
                st.warning("Chưa đúng rồi! Em xem gợi ý của Trợ lý AI ở dưới để chọn lại nhé!")

    with b2:
        if st.button("💡 Xem gợi ý AI", use_container_width=True):
            st.session_state.hint_on = True

    with b3:
        if st.button("➡️ Câu tiếp theo", use_container_width=True):
            st.session_state.q_idx = (st.session_state.q_idx + 1) % len(QUESTIONS)
            st.session_state.hint_on = False
            st.rerun()

    if st.session_state.hint_on:
        st.markdown(f'<div class="ai-helper">{q["goi_y"]}</div>', unsafe_allow_html=True)

# ==============================================================================
# TAB 2: GÓC PHỤ HUYNH (ĐỒNG HÀNH CÙNG CON ĐƠN GIẢN, DỄ HIỂU)
# ==============================================================================
with tab_ph:
    st.subheader("👨‍👩‍👧 Cẩm Nang AI: 5 Phút Đồng Hành Cùng Con Mỗi Tối")
    st.write("Giúp quý phụ huynh lớp 5/2 (Trường Tiểu học Bình Phước) nắm bắt nhanh nội dung con đang học và cách đố vui cùng con tại nhà.")

    topic_ph = st.selectbox(
        "📌 Chọn nội dung con đang học trong tuần:",
        [
            "1. Toán: Cộng, trừ và nhân nhẩm Số thập phân",
            "2. Toán: Hiểu nhanh về Tỉ số phần trăm (%)",
            "3. Tiếng Việt: Đọc hiểu & Mở rộng vốn từ, Luyện câu",
            "4. Rèn chữ - Giữ nết: Rèn tính cẩn thận, kiên trì cho con"
        ]
    )

    guides = {
        "1. Toán: Cộng, trừ và nhân nhẩm Số thập phân": {
            "meo": "Chỉ cần nhắc con câu thần chú: <b>'Cộng trừ số thập phân: Dấu phẩy phải thẳng hàng!'</b>",
            "ung_dung": "Khi đi chợ hoặc xem hóa đơn tiền điện/nước, ba mẹ hãy nhờ con cộng nhẩm giúp 2 món hàng lẻ (ví dụ: 12,5 nghìn đồng + 5,5 nghìn đồng) để con thấy Toán học rất gần gũi.",
            "khen": "Khi con tính đúng, ba mẹ hãy khen: <i>'Con tính nhẩm nhanh quá, mai mốt đi siêu thị làm trợ lý cho mẹ nhé!'</i>"
        },
        "2. Toán: Hiểu nhanh về Tỉ số phần trăm (%)": {
            "meo": "Giải thích cho con: <b>100% là toàn bộ</b>, <b>50% là một nửa (1/2)</b>, còn <b>25% là một phần tư (1/4)</b>.",
            "ung_dung": "Chỉ vào phần trăm pin điện thoại của ba mẹ hoặc biển 'Giảm giá 50%' ngoài cửa hàng và hỏi con: <i>'Áo này 100 ngàn mà giảm 50% thì mẹ phải trả bao nhiêu tiền?'</i>",
            "khen": "Khích lệ sự tự tin của con bằng những câu hỏi thực tế nhẹ nhàng trong bữa cơm gia đình."
        },
        "3. Tiếng Việt: Đọc hiểu & Mở rộng vốn từ, Luyện câu": {
            "meo": "Khuyến khích con đọc to 1 đoạn văn ngắn mỗi tối (khoảng 3-5 phút) và hỏi con: <i>'Câu nào trong bài làm con thích nhất?'</i>",
            "ung_dung": "Tập cho con thói quen nói trọn câu, dùng từ ngữ lễ phép và giàu hình ảnh khi kể chuyện ở trường cho ông bà, cha mẹ nghe.",
            "khen": "Ghi nhận sự tiến bộ khi con đọc trôi chảy hơn hoặc biết dùng từ hay."
        },
        "4. Rèn chữ - Giữ nết: Rèn tính cẩn thận, kiên trì cho con": {
            "meo": "Rèn chữ không phải để đi thi viết chữ đẹp, mà là để <b>rèn tính kiên nhẫn, tỉ mỉ và chỉn chu</b> trong mọi việc.",
            "ung_dung": "Ba mẹ chỉ cần nhắc con ngồi thẳng lưng, nơi học tập đủ ánh sáng và viết nắn nót từng con số, chữ cái trong bài tập hàng ngày.",
            "khen": "Khen ngợi ngay khi thấy trang vở hôm nay của con sạch sẽ, ít tẩy xóa hơn hôm qua."
        }
    }

    g = guides[topic_ph]
    st.markdown(f"""
    <div class="parent-card">
        💡 <b>1. Cách nhắc bài cực dễ cho con:</b><br>{g['meo']}<br><br>
        🏠 <b>2. Gợi ý trò chuyện cùng con ở nhà:</b><br>{g['ung_dung']}<br><br>
        ❤️ <b>3. Lời khen khích lệ con (Theo tinh thần Thông tư 27):</b><br>{g['khen']}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("✅ Góc Phối Hợp Gia Đình & Nhà Trường")
    st.write("Quý phụ huynh cùng con đánh dấu những thói quen tốt con đã thực hiện tại nhà hôm nay để cộng Sao cho Tổ của con:")

    hab1 = st.checkbox("📖 Tự giác hoàn thành bài tập và chuẩn bị sách vở cho ngày mai (+5 Sao)")
    hab2 = st.checkbox("✍️ Trình bày vở sạch đẹp, chữ viết rõ ràng, cẩn thận (+5 Sao)")
    hab3 = st.checkbox("🌱 Phụ giúp ông bà, cha mẹ việc nhà vừa sức (quét nhà, nhặt rau, tắt điện quạt khi không dùng) (+5 Sao)")

    if st.button("💌 Gửi Xác Nhận & Cộng Sao Cho Con", use_container_width=True):
        added = (5 if hab1 else 0) + (5 if hab2 else 0) + (5 if hab3 else 0)
        if added > 0:
            st.session_state.stars += added
            st.session_state.group_points[st.session_state.group] += added
            st.balloons()
            st.success(f"Cảm ơn quý phụ huynh! Hệ thống đã cộng thêm +{added} Sao chăm ngoan cho em {st.session_state.name} và {st.session_state.group}!")
        else:
            st.info("Hãy đánh dấu ít nhất 1 việc tốt con đã làm hôm nay nhé!")

# ==============================================================================
# TAB 3: BẢNG VÀNG LỚP 5/2 & NHẬN XÉT THÔNG TƯ 27
# ==============================================================================
with tab_bv:
    st.subheader("🏆 Bảng Theo Dõi Thi Đua Tổ - Lớp 5/2")
    st.write("Điểm số của các Tổ tự động tăng lên mỗi khi học sinh giải đúng bài tập hoặc làm việc tốt ở nhà:")

    for grp_name, pts in sorted(st.session_state.group_points.items(), key=lambda x: x[1], reverse=True):
        st.write(f"**{grp_name}**: `{pts} Sao thi đua` ⭐")
        st.progress(min(pts / 250, 1.0))

    st.markdown("---")
    st.subheader("📜 Phiếu Khen Thưởng & Nhận Xét Tự Động (Chuẩn Thông Tư 27)")

    danh_hieu = "CHIẾN BINH HỌC TẬP XUẤT SẮC 🌟" if st.session_state.stars >= 60 else "CHÁU NGOAN CHĂM HỌC 🌱"
    muc_tt27 = "Hoàn thành tốt (HTT)" if st.session_state.stars >= 60 else "Hoàn thành (HT)"

    st.markdown(f"""
    <div class="cert-box">
        <h4>TRƯỜNG TIỂU HỌC BÌNH PHƯỚC</h4>
        <h3>🏅 GIẤY KHEN ĐIỆN TỬ LỚP 5/2</h3>
        <p>Giáo viên chủ nhiệm <b>Huỳnh Minh Sơn</b> khen tặng em:</p>
        <h2 style="color:#d9480f; margin: 5px 0;">{st.session_state.name} ({st.session_state.group})</h2>
        <p>Đã đạt danh hiệu: <b>{danh_hieu}</b></p>
        <p>Thành tích: Tích lũy <b>{st.session_state.stars} Sao chăm ngoan</b> và đóng góp <b>{st.session_state.trees} Cây xanh</b> cho lớp học số.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    nhan_xet_tt27 = (
        f"📋 TRƯỜNG TIỂU HỌC BÌNH PHƯỚC - LỚP 5/2 (GVCN: Huỳnh Minh Sơn)\n"
        f"NHẬN XÉT ĐÁNH GIÁ THƯỜNG XUYÊN (THÔNG TƯ 27) - EM {st.session_state.name.upper()} ({st.session_state.group}):\n"
        f"• Mức độ đạt được: {muc_tt27}\n"
        f"• Kiến thức & Kỹ năng: Nắm vững kiến thức Toán và Tiếng Việt lớp 5 thông qua mô hình trực quan; biết vận dụng tính toán vào tình huống thực tế.\n"
        f"• Năng lực & Phẩm chất: Có ý thức tự học trên không gian số, rèn luyện tính kiên trì, cẩn thận và tích cực phối hợp tốt giữa gia đình và nhà trường."
    )
    st.text_area("📌 Nội dung nhận xét (Giáo viên & Phụ huynh có thể sao chép gửi qua Zalo):", nhan_xet_tt27, height=150)
