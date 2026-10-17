import streamlit as st
import random
import re

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
        padding: 16px;
        border-radius: 12px;
        font-size: 1.05rem;
        color: #3b0764;
        margin: 12px 0;
        line-height: 1.65;
    }
    .warn-box {
        background: #fff4e6;
        border-left: 6px solid #f76707;
        padding: 15px;
        border-radius: 12px;
        font-size: 1.02rem;
        color: #d9480f;
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
    .level-badge {
        display: inline-block;
        background: #ebfbee;
        border: 1.5px solid #40c057;
        color: #2b8a3e;
        padding: 4px 10px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 0.88rem;
        margin-bottom: 6px;
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
        "Từ láy miêu tả thiên nhiên": ["xanh biếc", "long lanh", "rì rào", "phấp phới", "chín mọng", "dịu dàng", "rực rỡ", "trong vắt"],
        "Từ gợi tả vẻ đẹp quê hương & trường lớp": ["hiền hòa", "êm đềm", "thơ mộng", "trìu mến", "nhộn nhịp", "tươi mát", "thân thương", "ấm áp"],
        "Biện pháp So sánh & Nhân hóa đắt giá": ["uốn lượn như dải lụa", "ôm ấp bờ bãi", "hát khúc ca vui tươi", "như người mẹ hiền", "vẫy tay chào đón", "mỉm cười trong nắng"]
    }

# ==================== KHO ĐỀ BÀI TỪ DỄ ĐẾN KHÓ ====================
CHALLENGES_BY_LEVEL = {
    "🌱 Mức 1: Khởi động (Dễ - Tả đồ vật, con vật, cây cối quen thuộc)": [
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả một đồ dùng học tập thân thiết với em (cây bút, quyển vở, chiếc cặp sách...).",
            "goi_y_tu": ["xinh xắn", "ngay ngắn", "thơm phức", "người bạn nhỏ", "đồng hành"],
            "mau_nang_cap": "Chiếc cặp sách <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>như một người bạn nhỏ chăm chỉ</strong> luôn cùng em đến trường mỗi ngày."
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả một loài cây hoặc loài hoa trong sân trường Tiểu học Bình Phước mà em yêu thích.",
            "goi_y_tu": ["xanh mát", "rực rỡ", "rung rinh", "tỏa bóng", "vẫy chào"],
            "mau_nang_cap": "Dưới ánh nắng mai, hàng cây phượng vĩ <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>xòe những tán lá xanh rì như chiếc ô khổng lồ</strong> che mát cho chúng em."
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả một con vật nuôi đáng yêu trong gia đình em (chú chó, chú mèo, đàn gà...).",
            "goi_y_tu": ["mượt mà", "tròn xoe", "nhanh nhẹn", "quấn quýt", "đáng yêu"],
            "mau_nang_cap": "Chú mèo mướp có <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>bộ lông vàng mượt mà như nhung và đôi mắt tròn xoe như hai hòn bi ve</strong>."
        }
    ],
    "⭐ Mức 2: Vượt chướng ngại vật (Trung bình - Tả cảnh thiên nhiên, trường lớp, người thân)": [
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả cảnh buổi sáng trên quê hương em, trong đó có dùng ít nhất 1 từ láy.",
            "goi_y_tu": ["trong lành", "long lanh", "rì rào", "dịu dàng", "thức dậy"],
            "mau_nang_cap": "Buổi sáng trên quê hương em thật <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>trong lành và yên bình</strong>, những giọt sương sớm còn <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>đọng long lanh như hạt ngọc</strong> trên lá."
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) miêu tả khung cảnh sân trường Tiểu học Bình Phước vào giờ ra chơi.",
            "goi_y_tu": ["nhộn nhịp", "rộn rã", "tung tăng", "tiếng cười", "náo nhiệt"],
            "mau_nang_cap": "Tiếng trống trường vừa vang lên, sân trường lập tức <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>rộn rã tiếng cười nói như một bầy chim non vỡ tổ</strong>."
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả hình ảnh thầy giáo hoặc cô giáo đang say sưa giảng bài trên lớp.",
            "goi_y_tu": ["ấm áp", "trìu mến", "say sưa", "tận tụy", "dịu hiền"],
            "mau_nang_cap": "Giọng thầy giảng bài <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>ấm áp và truyền cảm</strong>, từng nét chữ phấn trắng <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>hiện lên ngay ngắn, đẹp đẽ</strong> trên bảng đen."
        }
    ],
    "👑 Mức 3: Về đích (Khó - Kết hợp từ láy, so sánh, nhân hóa và bộc lộ cảm xúc)": [
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả dòng sông hoặc cánh đồng lúa quê hương, trong đó có sử dụng cả biện pháp so sánh và nhân hóa.",
            "goi_y_tu": ["hiền hòa", "uốn lượn", "dải lụa", "ôm ấp", "rì rào", "chín vàng"],
            "mau_nang_cap": "Dòng sông quê em <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>hiền hòa uốn lượn như một dải lụa đào</strong>, ngày đêm <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>thầm thì kể chuyện</strong> cho đôi bờ nghe."
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả một cơn mưa rào mùa hạ trên quê hương em và cảm xúc của em khi mưa tạnh.",
            "goi_y_tu": ["ào ạt", "trắng xóa", "tươi tốt", "hả hê", "trong vắt", "cầu vồng"],
            "mau_nang_cap": "Cơn mưa rào <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>ào ạt trút nước mát lành</strong> xuống mặt đất, cây cối trong vườn <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>vẫy tay tắm mưa đầy thích thú</strong>."
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) kể lại một việc làm tốt của em giúp đỡ ông bà, cha mẹ ở nhà và nêu cảm nghĩ của em.",
            "goi_y_tu": ["vui vẻ", "cẩn thận", "ấm áp", "khen ngợi", "tự hào", "yêu thương"],
            "mau_nang_cap": "Nhìn nụ cười <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>hiền hậu và ánh mắt trìu mến</strong> của bà khi em phụ quét nhà, lòng em <strong style='color:#ae3ec9; background:#f3f0ff; padding:1px 5px; border-radius:4px;'>ngập tràn niềm vui ấm áp</strong>."
        }
    ]
}

# ==================== HÀM ĐẾM CÂU & PHÂN TÍCH BÀI VIẾT LỚP 5 ====================
def split_sentences(text):
    # Tách câu dựa trên dấu chấm (.), chấm than (!), chấm hỏi (?), dấu ba chấm (...)
    raw_parts = re.split(r'[.!?…]+', text.strip())
    sentences = [s.strip() for s in raw_parts if len(s.strip()) > 0]
    return sentences

def analyze_student_paragraph(text, challenge_info):
    sentences = split_sentences(text)
    num_sentences = len(sentences)
    text_lower = text.lower()

    # Kiểm tra từ láy / từ gợi tả phổ biến
    good_words = [
        "xanh biếc", "long lanh", "rì rào", "phấp phới", "hiền hòa", "êm đềm", "thơ mộng",
        "trìu mến", "dạt dào", "tươi mát", "nhộn nhịp", "rộn rã", "tung tăng", "ấm áp",
        "mượt mà", "tròn xoe", "xinh xắn", "ngay ngắn", "trong lành", "rực rỡ", "dịu dàng",
        "ào ạt", "thướt tha", "chăm chỉ", "tận tụy", "lung linh", "ngào ngạt", "thơm phức"
    ]
    used_good_words = [w for w in good_words if w in text_lower]

    # Kiểm tra dấu hiệu phép so sánh ("như", "tựa như", "giống như", "là")
    has_simile = any(k in text_lower for k in [" như ", "tựa như", "giống như", "chẳng khác gì"])

    # Kiểm tra lỗi viết hoa đầu câu hoặc thiếu dấu chấm cuối đoạn
    missing_end_punct = not text.strip().endswith(('.', '!', '?', '…'))
    not_capitalized = [idx + 1 for idx, s in enumerate(sentences) if len(s) > 0 and not s[0].isupper()]

    # Kiểm tra lỗi lặp từ đầu câu
    first_words = [s.split()[0].lower() for s in sentences if len(s.split()) > 0]
    repeated_start = len(first_words) != len(set(first_words)) and len(first_words) >= 3

    return {
        "sentences": sentences,
        "count": num_sentences,
        "used_good_words": used_good_words,
        "has_simile": has_simile,
        "missing_end_punct": missing_end_punct,
        "not_capitalized": not_capitalized,
        "repeated_start": repeated_start
    }

# ==================== TIÊU ĐỀ TRANG ====================
st.markdown("""
<div class="main-banner">
    <h1>✍️ XƯỞNG SÁNG TÁC & LUYỆN CÂU TIẾNG VIỆT 5/2</h1>
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn • Nâng cấp câu văn cùng Trợ lý Học sinh lớp 5</p>
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
    st.write("Em hãy lựa chọn các từ ngữ giàu hình ảnh dưới đây để làm cho bài tập làm văn (tả cảnh, tả người, tả đồ vật) trở nên sinh động hơn:")

    selected_topic = st.selectbox(
        "🎯 Chọn chủ đề luyện từ:",
        list(st.session_state.vocabulary_bank.keys())
    )

    st.write("")
    st.markdown("#### 💎 Các từ ngữ gợi ý đắt giá:")
    badges_html = "".join([f'<span class="vocab-badge">{word}</span>' for word in st.session_state.vocabulary_bank[selected_topic]])
    st.markdown(f"<div style='padding:15px; background:white; border-radius:12px; border:2px solid #dee2e6;'>{badges_html}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 💡 Bí quyết từ Trợ lý Học sinh lớp 5:")
    st.info(f"Khi viết văn miêu tả (tả dòng sông quê hương, cánh đồng lúa, hay mái trường Bình Phước), việc kết hợp **{selected_topic}** sẽ giúp câu văn của em có hồn, giàu cảm xúc và hay hơn rất nhiều!")

# ------------------------------------------------------------------------------
# TAB 2: TRẠM BÁC SĨ SỬA CÂU (SMART SENTENCE DOCTOR)
# ------------------------------------------------------------------------------
with tab2:
    st.subheader("🩺 Trạm 'Bác Sĩ Sửa Câu'")
    st.write("Em hãy nhập một câu văn đơn giản hoặc câu văn bị lặp từ của mình vào đây. Trợ lý Học sinh lớp 5 sẽ giúp em 'gọt giũa' thành một câu văn giàu hình ảnh hơn!")

    user_sentence = st.text_input("✍️ Nhập câu văn của em:", "Con sông quê em rất đẹp. Con sông chảy hiền hòa.")

    if st.button("🩺 Nhờ Trợ Lý Nâng Cấp Câu Văn", use_container_width=True):
        if user_sentence.strip() != "":
            st.session_state.stars += 5
            st.balloons()
            
            version1 = 'Dòng sông quê em <strong style="color:#ae3ec9; background-color:#f3f0ff; padding:2px 6px; border-radius:4px;">hiền hòa uốn lượn như dải lụa mềm mại, ôm ấp lấy những xóm làng trù phú</strong>.'
            version2 = 'Từ trên cao nhìn xuống, con sông <strong style="color:#ae3ec9; background-color:#f3f0ff; padding:2px 6px; border-radius:4px;">khoác lên mình tấm áo xanh biếc, rợp bóng dừa nước mát rượi</strong>.'
            
            st.markdown(f"""
            <div class="ai-box">
                🤗 <b>Nhận xét từ Trợ lý Học sinh lớp 5 dành cho bạn {st.session_state.student_name}:</b><br><br>
                • <b>Câu gốc của bạn:</b> <span style="color:#e03131;">"{user_sentence}"</span> <i>(Câu đã rõ ý nhưng còn hơi ngắn và lặp từ)</i><br><br>
                • <b>Gợi ý sửa lại cho hay hơn <span style="color:#7048e8;">(Phần chữ tô màu nổi bật là phần được thêm vào)</span>:</b><br>
                1. {version1}<br>
                2. {version2}<br><br>
                💡 <i><b>Mẹo nhỏ:</b> Bạn chỉ cần thay từ lặp bằng từ đồng nghĩa (con sông -> dòng sông) và thêm từ láy, hình ảnh so sánh ("như dải lụa") là câu văn sáng bừng lên ngay!</i>
            </div>
            """, unsafe_allow_html=True)
            st.success("Tuyệt vời! Em được thưởng +5 Sao Ngôn Từ ⭐")
        else:
            st.warning("Bạn hãy nhập câu văn vào ô trống trước khi bấm nút nhé!")

# ------------------------------------------------------------------------------
# TAB 3: THỬ THÁCH SÁNG TÁC ĐOẠN VĂN NHANH (CÓ RÀNG BUỘC 3 - 5 CÂU)
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("🏆 Thử Thách Sáng Tác Đoạn Văn Nhanh (Từ 3 đến 5 câu)")
    st.write("Hãy chọn mức độ thử thách từ dễ đến khó và viết một đoạn văn đúng **từ 3 đến 5 câu** (nhớ chấm câu cuối mỗi câu nhé!).")

    level_choice = st.selectbox(
        "🎚️ Chọn mức độ thử thách:",
        list(CHALLENGES_BY_LEVEL.keys())
    )

    if "level_last" not in st.session_state or st.session_state.level_last != level_choice:
        st.session_state.level_last = level_choice
        st.session_state.challenge_idx = 0

    current_list = CHALLENGES_BY_LEVEL[level_choice]
    current_item = current_list[st.session_state.challenge_idx % len(current_list)]

    st.markdown(f'<div class="level-badge">{level_choice}</div>', unsafe_allow_html=True)
    st.info(f"📌 **Đề bài:** {current_item['de_bai']}")

    goi_y_badges = "".join([f'<span class="vocab-badge">{w}</span>' for w in current_item["goi_y_tu"]])
    st.markdown(f"💡 **Từ ngữ gợi ý bạn có thể dùng:** {goi_y_badges}", unsafe_allow_html=True)
    st.write("")

    paragraph_input = st.text_area(
        "📝 Viết đoạn văn của bạn vào đây (Nhớ viết từ 3 đến 5 câu và đặt dấu chấm '.' cuối mỗi câu):",
        height=140,
        placeholder="Ví dụ: Sáng sớm, bầu trời quê em trong xanh và cao vời vợi. Những giọt sương đêm còn đọng long lanh trên phiến lá như những hạt ngọc nhỏ. Gió thổi rì rào qua hàng dừa xanh mát. Em rất yêu vẻ đẹp bình yên của quê hương mình."
    )

    # Bộ đếm số câu trực tiếp giúp học sinh dễ theo dõi
    live_sentences = split_sentences(paragraph_input)
    st.caption(f"📊 **Số câu hiện tại bạn đã viết:** `{len(live_sentences)} câu` *(Yêu cầu hợp lệ: từ 3 đến 5 câu)*")

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        submit_btn = st.button("✅ Nộp Bài & Xem Nhận Xét", use_container_width=True)
    with col_btn2:
        if st.button("🎲 Đổi Đề Bài Khác Cùng Mức Độ", use_container_width=True):
            st.session_state.challenge_idx += 1
            st.rerun()

    if submit_btn:
        result = analyze_student_paragraph(paragraph_input, current_item)
        c_count = result["count"]

        # RÀNG BUỘC SỐ CÂU TỪ 3 - 5 CÂU
        if c_count < 3:
            st.markdown(f"""
            <div class="warn-box">
                ⚠️ <b>Nhận xét từ Trợ lý Học sinh lớp 5:</b><br>
                Bạn <b>{st.session_state.student_name}</b> ơi, đoạn văn của bạn hiện mới có <b>{c_count} câu</b> (chưa đủ yêu cầu từ <b>3 đến 5 câu</b>).<br><br>
                👉 <b>Cách sửa cực dễ:</b> Bạn hãy viết thêm khoảng <b>{3 - c_count} câu nữa</b> để miêu tả thêm chi tiết hoặc nêu cảm nghĩ của bạn ở cuối đoạn, và nhớ đặt dấu chấm (<b>.</b>) để tách các câu nhé!
            </div>
            """, unsafe_allow_html=True)
        elif c_count > 5:
            st.markdown(f"""
            <div class="warn-box">
                ⚠️ <b>Nhận xét từ Trợ lý Học sinh lớp 5:</b><br>
                Bạn <b>{st.session_state.student_name}</b> viết rất nhiệt tình nhưng đoạn văn đang có tới <b>{c_count} câu</b> (vượt quá quy định <b>3 đến 5 câu</b> mất rồi!).<br><br>
                👉 <b>Cách sửa cực dễ:</b> Bạn hãy rút gọn lại hoặc gộp các câu ngắn gần ý nhau lại sao cho cả đoạn chỉ gói gọn trong <b>3 đến 5 câu văn</b> thật súc tích nhé!
            </div>
            """, unsafe_allow_html=True)
        else:
            # ĐẠT YÊU CẦU TỪ 3 - 5 CÂU -> CHẤM ĐIỂM & NHẬN XÉT GẦN GŨI
            st.session_state.stars += 15
            st.balloons()
            st.success(f"🎉 Hoan hô bạn {st.session_state.student_name}! Bạn đã viết đúng yêu cầu ({c_count} câu văn) và nhận được +15 Sao Ngôn Từ ⭐!")

            # Tạo lời khen gần gũi
            praise_points = []
            praise_points.append(f"Bạn viết đúng số câu quy định (<b>{c_count} câu</b>), các câu sắp xếp rất hợp lý.")
            if result["used_good_words"]:
                words_str = ", ".join([f"<b>'{w}'</b>" for w in result["used_good_words"]])
                praise_points.append(f"Bạn đã biết dùng từ ngữ gợi tả rất hay trong bài như: {words_str}.")
            if result["has_simile"]:
                praise_points.append("Bạn đã khéo léo đưa hình ảnh <b>so sánh</b> vào bài giúp câu văn sinh động hơn hẳn!")

            # Tạo lời góp ý sửa chữa nhẹ nhàng, dễ hiểu cho học sinh lớp 5
            fix_points = []
            if result["not_capitalized"]:
                cau_loi = ", ".join([f"câu số {i}" for i in result["not_capitalized"]])
                fix_points.append(f"Chữ cái đầu tiên ở <b>{cau_loi}</b> chưa được viết hoa. Bạn nhớ viết hoa chữ cái đầu mỗi câu sau dấu chấm nhé!")
            if result["missing_end_punct"]:
                fix_points.append("Cuối đoạn văn bạn quên đặt dấu chấm (<b>.</b>) rồi. Nhớ đặt dấu chấm kết thúc câu cuối cùng nha!")
            if not result["used_good_words"]:
                goi_y_them = ", ".join([f"<b>{w}</b>" for w in current_item["goi_y_tu"][:3]])
                fix_points.append(f"Câu văn của bạn đã rõ ý rồi, nhưng để bài văn bay bổng hơn, bạn thử thêm các từ láy hoặc từ gợi tả như: {goi_y_them} vào nhé!")
            if not result["has_simile"]:
                fix_points.append("Bạn thử thêm từ <b>'như'</b> để tạo một hình ảnh so sánh xem sao, chắc chắn bài văn sẽ cuốn hút hơn nhiều đấy!")
            if result["repeated_start"]:
                fix_points.append("Một số câu trong bài đang bắt đầu bằng từ giống nhau. Bạn thử đổi cách mở đầu câu (ví dụ thêm từ chỉ thời gian: <i>Sáng sớm, Nhìn từ xa, Em rất thích...</i>) để tránh lặp từ nhé!")

            if not fix_points:
                fix_points.append("Đoạn văn của bạn trình bày rất chỉn chu, viết hoa và đặt dấu câu đầy đủ. Hãy phát huy nhé!")

            praise_html = "".join([f"<li>{p}</li>" for p in praise_points])
            fix_html = "".join([f"<li>{f}</li>" for f in fix_points])

            st.markdown(f"""
            <div class="ai-box">
                🌟 <b>Nhận xét từ Trợ lý Học sinh lớp 5 dành cho bạn {st.session_state.student_name}:</b><br><br>
                👍 <b>Điểm đáng khen của bạn:</b>
                <ul style="margin-top:4px; margin-bottom:10px;">{praise_html}</ul>
                ✍️ <b>Gợi ý nhỏ để bạn sửa bài hay hơn nữa:</b>
                <ul style="margin-top:4px; margin-bottom:10px;">{fix_html}</ul>
                💎 <b>Câu văn mẫu gợi ý cho đề bài này:</b><br>
                👉 <i>"{current_item['mau_nang_cap']}"</i>
            </div>
            """, unsafe_allow_html=True)
