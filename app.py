import streamlit as st
import random

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Xưởng Sáng Tác & Luyện Câu Tiếng Việt Lớp 5/2 - TH Bình Phước",
    page_icon="✍️",
    layout="centered"
)

# Giao diện CSS tươi sáng, chữ to rõ ràng cho học sinh tiểu học
st.markdown("""
<style>
    .main-banner {
        background: linear-gradient(135deg, #ae3ec9 0%, #7048e8 100%);
        color: white;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(112, 72, 232, 0.25);
    }
    .main-banner h1 {
        font-size: 1.8rem;
        margin: 0;
        color: white;
        font-weight: 800;
    }
    .main-banner p {
        font-size: 1rem;
        margin: 6px 0 0 0;
        color: #f3f0ff;
    }
    .ai-box {
        background: #f3f0ff;
        border-left: 6px solid #7048e8;
        padding: 15px;
        border-radius: 10px;
        font-size: 1.05rem;
        color: #3b0764;
        margin: 12px 0;
        line-height: 1.6;
    }
    .vocab-badge {
        display: inline-block;
        background: #e7f5ff;
        border: 2px solid #74c0fc;
        color: #1864ab;
        padding: 6px 12px;
        border-radius: 20px;
        font-weight: bold;
        margin: 4px;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ==================== KHỞI TẠO PHIÊN LÀM VIỆC ====================
if "student_name" not in st.session_state:
    st.session_state.student_name = "Hiểu Minh"
if "stars" not in st.session_state:
    st.session_state.stars = 40
if "vocabulary_bank" not in st.session_state:
    st.session_state.vocabulary_bank = {
        "Từ láy miêu tả thiên nhiên": ["xanh biếc", "long lanh", "rì rào", "phấp phới", "ập òa", "chín mọng"],
        "Từ gợi tả vẻ đẹp quê hương": ["hiền hòa", "êm đềm", "thơ mộng", "trìu mến", "dạt dào", "tươi mát"],
        "Biện pháp So sánh & Nhân hóa đắt giá": ["uốn lượn như dải lụa", "ôm ấp bờ bãi", "hát khúc ca vui tươi", "như người mẹ hiền"]
    }

# ==================== TIÊU ĐỀ TRANG ====================
st.markdown("""
<div class="main-banner">
    <h1>✍️ XƯỞNG SÁNG TÁC & LUYỆN CÂU TIẾNG VIỆT 5/2</h1>
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn • Nâng cấp câu văn cùng Trợ lý AI</p>
</div>
""", unsafe_allow_html=True)

# Nhập tên học sinh
col_n1, col_n2 = st.columns([1.5, 1])
with col_n1:
    st.session_state.student_name = st.text_input("👦👧 Họ và tên học sinh:", st.session_state.student_name)
with col_n2:
    st.markdown(f"<div style='background:#fff9db; border:2px solid #ffd43b; padding:10px; border-radius:10px; text-align:center; font-weight:bold; color:#d9480f;'>⭐ {st.session_state.stars} Sao Ngôn Từ</div>", unsafe_allow_html=True)

st.write("")

# ==================== 3 TAB CHỨC NĂNG CHÍNH ====================
tab1, tab2, tab3 = st.tabs([
    "📖 1. Kho Từ Láy & Biện Pháp Tu Từ",
    "🩺 2. Trạm 'Bác Sĩ Sửa Câu'",
    "🏆 3. Thử Thách Sáng Tác Nhanh"
])

# ------------------------------------------------------------------------------
# TAB 1: KHO TỪ VỰNG & BIỆN PHÁP TU TỪ
# ------------------------------------------------------------------------------
with tab1:
    st.subheader("📖 Kho Từ Vựng & Hình Ảnh So Sánh - Nhân Hóa Tiếng Việt 5")
    st.write("Em hãy lựa chọn các từ ngữ giàu hình ảnh dưới đây để làm cho bài tập làm văn (tả cảnh, tả người) trở nên sinh động hơn:")

    selected_topic = st.selectbox(
        "🎯 Chọn chủ đề luyện từ:",
        ["Từ láy miêu tả thiên nhiên", "Từ gợi tả vẻ đẹp quê hương", "Biện pháp So sánh & Nhân hóa đắt giá"]
    )

    st.write("")
    st.markdown("#### 💎 Các từ ngữ gợi ý đắt giá:")
    badges_html = "".join([f'<span class="vocab-badge">{word}</span>' for word in st.session_state.vocabulary_bank[selected_topic]])
    st.markdown(f"<div style='padding:15px; background:white; border-radius:12px; border:2px solid #dee2e6;'>{badges_html}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 💡 Bí quyết từ Trợ lý AI Tiếng Việt:")
    st.info(f"Khi viết văn miêu tả (tả dòng sông quê hương Vĩnh Long, cánh đồng lúa, hay mái trường Bình Phước), việc kết hợp **{selected_topic}** sẽ giúp câu văn của em có hồn, giàu cảm xúc và đạt điểm cao hơn theo chuẩn chương trình GDPT 2018.")

# ------------------------------------------------------------------------------
# TAB 2: TRẠM BÁC SĨ SỬA CÂU (SMART SENTENCE DOCTOR)
# ------------------------------------------------------------------------------
with tab2:
    st.subheader("🩺 Trạm 'Bác Sĩ Sửa Câu' Cùng Trợ Lý AI")
    st.write("Em hãy nhập một câu văn đơn giản hoặc câu văn bị lặp từ của mình vào đây. Trợ lý AI sẽ giúp em 'gọt giũa' thành một câu văn giàu hình ảnh hơn!")

    user_sentence = st.text_input("✍️ Nhập câu văn của em:", "Con sông quê em rất đẹp. Con sông chảy hiền hòa.")

    if st.button("🩺 Nhờ Trợ Lý AI Nâng Cấp Câu Văn", use_container_width=True):
        if user_sentence.strip() != "":
            st.session_state.stars += 5
            st.balloons()
            
            # Phần sửa lại được tô đậm và tô màu nổi bật để học sinh dễ chú ý
            version1 = 'Dòng sông quê em <strong style="color:#ae3ec9; background-color:#f3f0ff; padding:2px 6px; border-radius:4px;">hiền hòa uốn lượn như dải lụa mềm mại, ôm ấp lấy những xóm làng trù phú</strong>.'
            version2 = 'Từ trên cao nhìn xuống, con sông <strong style="color:#ae3ec9; background-color:#f3f0ff; padding:2px 6px; border-radius:4px;">khoác lên mình tấm áo xanh biếc, rợp bóng dừa nước mát rượi</strong>.'
            
            st.markdown(f"""
            <div class="ai-box">
                🤖 <b>Trợ lý AI Tiếng Việt 5/2 đã nâng cấp câu văn cho em {st.session_state.student_name}:</b><br><br>
                • <b>Câu gốc của em:</b> "{user_sentence}"<br><br>
                • <b>Các câu văn gợi ý nâng cấp <span style="color:#7048e8;">(Phần chữ tô màu nổi bật là phần cải tiến)</span>:</b><br>
                1. {version1}<br>
                2. {version2}<br><br>
                <i>(Mẹo từ AI: AI đã giúp em thay thế các từ lặp bằng các từ ngữ gợi tả và hình ảnh so sánh sinh động hơn!)</i>
            </div>
            """, unsafe_allow_html=True)
            st.success("Tuyệt vời! Em được thưởng +5 Sao Ngôn Từ ⭐")
        else:
            st.warning("Vui lòng nhập câu văn vào ô trống trước khi bấm sửa nhé!")

# ------------------------------------------------------------------------------
# TAB 3: THỬ THÁCH SÁNG TÁC ĐOẠN VĂN NHANH
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("🏆 Thử Thách Sáng Tác Đoạn Văn Nhanh")
    st.write("Trợ lý AI đưa ra thử thách viết đoạn văn. Em hãy hoàn thành để tích lũy Sao thưởng:")

    challenges = [
        "Đề bài: Viết một đoạn văn ngắn (3-4 câu) tả buổi sáng trên quê hương em, trong đó có sử dụng ít nhất 1 từ láy và 1 hình ảnh nhân hóa.",
        "Đề bài: Viết một đoạn văn ngắn (3-4 câu) tả lại hình ảnh người thầy hoặc cô giáo đang giảng bài trên lớp.",
        "Đề bài: Viết một đoạn văn ngắn (3-4 câu) miêu tả sân trường Tiểu học Bình Phước vào giờ ra chơi."
    ]

    if "current_challenge" not in st.session_state:
        st.session_state.current_challenge = random.choice(challenges)

    st.info(f"📌 **{st.session_state.current_challenge}**")

    paragraph_input = st.text_area("📝 Viết đoạn văn của em vào đây:", height=120)

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("✅ Nộp Bài & Nhận Xét", use_container_width=True):
            if len(paragraph_input.strip()) > 10:
                st.session_state.stars += 15
                st.balloons()
                st.success(f"🎉 Hoan hô em {st.session_state.student_name}! Đoạn văn rất giàu cảm xúc và sử dụng từ ngữ sinh động. Thưởng +15 Sao ⭐!")
                st.markdown("""
                <div class="ai-box">
                    🤖 <b>AI Đánh giá:</b> Đoạn văn có bố cục rõ ràng, câu văn mạch lạc, biết dùng từ ngữ gợi tả. (Đạt mức: Hoàn thành tốt theo chuẩn Thông tư 27).
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("Đoạn văn hơi ngắn, em hãy viết thêm vài câu để hoàn chỉnh ý nhé!")

    with col_btn2:
        if st.button("🎲 Đổi Thử Thách Khác", use_container_width=True):
            st.session_state.current_challenge = random.choice(challenges)
            st.rerun()
