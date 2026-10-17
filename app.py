import streamlit as st
import random
import re

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Xưởng Sáng Tác & Thử Thách Tiếng Việt Lớp 5/2 - TH Bình Phước",
    page_icon="✍️",
    layout="centered"
)

# Giao diện CSS tươi sáng, chữ to rõ ràng, chuẩn font tiếng Việt
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
        line-height: 1.7;
    }
    .upgrade-paragraph-box {
        background: #ffffff;
        border: 2px dashed #ae3ec9;
        padding: 16px 18px;
        border-radius: 10px;
        margin-top: 8px;
        font-size: 1.08rem;
        line-height: 1.8;
        color: #212529;
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
    .alert-red-box {
        background: #fff5f5;
        border: 2.5px solid #ff6b6b;
        border-radius: 12px;
        padding: 16px;
        color: #c92a2a;
        font-weight: bold;
        text-align: center;
        font-size: 1.1rem;
        margin: 12px 0;
    }
    .success-flower-box {
        background: #ebfbee;
        border: 2.5px solid #51cf66;
        border-radius: 12px;
        padding: 16px;
        color: #2b8a3e;
        font-weight: bold;
        text-align: center;
        font-size: 1.15rem;
        margin: 12px 0;
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
    .hl-edit {
        color: #ae3ec9;
        background-color: #f3f0ff;
        font-weight: 700;
        padding: 1px 5px;
        border-radius: 4px;
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

# ==================== KHO ĐỀ BÀI TỪ DỄ ĐẾN KHÓ (TAB SÁNG TÁC) ====================
CHALLENGES_BY_LEVEL = {
    "🌱 Mức 1: Khởi động (Dễ - Tả đồ vật, con vật, cây cối quen thuộc)": [
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả một đồ dùng học tập thân thiết với em (cây bút, quyển vở, chiếc cặp sách...).",
            "goi_y_tu": ["xinh xắn", "ngay ngắn", "thơm phức", "người bạn nhỏ", "đồng hành"],
            "loai": "do_vat"
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả một loài cây hoặc loài hoa trong sân trường Tiểu học Bình Phước mà em yêu thích.",
            "goi_y_tu": ["xanh mát", "rực rỡ", "rung rinh", "tỏa bóng", "vẫy chào"],
            "loai": "cay_coi"
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả một con vật nuôi đáng yêu trong gia đình em (chú chó, chú mèo, đàn gà...).",
            "goi_y_tu": ["mượt mà", "tròn xoe", "nhanh nhẹn", "quấn quýt", "đáng yêu"],
            "loai": "con_vat"
        }
    ],
    "⭐ Mức 2: Vượt chướng ngại vật (Trung bình - Tả cảnh thiên nhiên, trường lớp, người thân)": [
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả cảnh buổi sáng trên quê hương em, trong đó có dùng ít nhất 1 từ láy.",
            "goi_y_tu": ["trong lành", "long lanh", "rì rào", "dịu dàng", "thức dậy"],
            "loai": "canh_vat"
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) miêu tả khung cảnh sân trường Tiểu học Bình Phước vào giờ ra chơi.",
            "goi_y_tu": ["nhộn nhịp", "rộn rã", "tung tăng", "tiếng cười", "náo nhiệt"],
            "loai": "truong_lop"
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả hình ảnh thầy giáo hoặc cô giáo đang say sưa giảng bài trên lớp.",
            "goi_y_tu": ["ấm áp", "trìu mến", "say sưa", "tận tụy", "dịu hiền"],
            "loai": "con_nguoi"
        }
    ],
    "👑 Mức 3: Về đích (Khó - Kết hợp từ láy, so sánh, nhân hóa và bộc lộ cảm xúc)": [
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả dòng sông hoặc cánh đồng lúa quê hương, trong đó có sử dụng cả biện pháp so sánh và nhân hóa.",
            "goi_y_tu": ["hiền hòa", "uốn lượn", "dải lụa", "ôm ấp", "rì rào", "chín vàng"],
            "loai": "canh_vat"
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) tả một cơn mưa rào mùa hạ trên quê hương em và cảm xúc của em khi mưa tạnh.",
            "goi_y_tu": ["ào ạt", "trắng xóa", "tươi tốt", "hả hê", "trong vắt", "cầu vồng"],
            "loai": "canh_vat"
        },
        {
            "de_bai": "Em hãy viết một đoạn văn ngắn (từ 3 đến 5 câu) kể lại một việc làm tốt của em giúp đỡ ông bà, cha mẹ ở nhà và nêu cảm nghĩ của em.",
            "goi_y_tu": ["vui vẻ", "cẩn thận", "ấm áp", "khen ngợi", "tự hào", "yêu thương"],
            "loai": "con_nguoi"
        }
    ]
}

# ==================== KHO TRÒ CHƠI THỬ THÁCH TỪ NGỮ (TAB 1) ====================
MINI_GAMES = {
    "🎯 Dạng 1: Phân Biệt Từ Láy Miêu tả Thiên Nhiên": {
        "cau_hoi": "Đâu là từ láy dùng để miêu tả vẻ đẹp long lanh, trong suốt của giọt sương sớm?",
        "dap_an_dung": "Long lanh",
        "dap_an_sai": ["Rào rạt", "Ầm ĩ", "Vội vã"]
    },
    "🎯 Dạng 2: Giải Mã Biện Pháp So Sánh": {
        "cau_hoi": "Trong câu: 'Dòng sông quê em hiền hòa uốn lượn như dải lụa mềm mại', tác giả sử dụng biện pháp nghệ thuật gì?",
        "dap_an_dung": "So sánh",
        "dap_an_sai": ["Nhân hóa", "Điệp từ", "Ẩn dụ"]
    },
    "🎯 Dạng 3: Truy Tìm Từ Gợi Tả Vẻ Đẹp Quê Hương": {
        "cau_hoi": "Từ nào dưới đây là từ gợi tả sự bình yên, nhẹ nhàng của làng quê?",
        "dap_an_dung": "Êm đềm",
        "dap_an_sai": ["Náo nhiệt", "Hối hả", "Ồn ào"]
    },
    "🎯 Dạng 4: Nhận Diện Biện Pháp Nhân Hóa": {
        "cau_hoi": "Câu thơ: 'Đàn gà con mới nở / Tìm mồi bên mẹ cha' kết hợp với hình ảnh 'gọi nhau', 'cục tác' thể hiện biện pháp gì?",
        "dap_an_dung": "Nhân hóa (gọi vật như người)",
        "dap_an_sai": ["So sánh ngang bằng", "Liệt kê đơn thuần", "Đảo ngữ"]
    }
}

# ==================== HÀM HỖ TRỢ XỬ LÝ VĂN BẢN ====================
def split_sentences(text):
    raw_parts = re.split(r'[.!?…]+', text.strip())
    sentences = [s.strip() for s in raw_parts if len(s.strip()) > 0]
    return sentences

def upgrade_sentence_by_student_idea(sentence, idx, total_sentences, topic_type):
    s = sentence.strip()
    if not s:
        return ""

    if not s[0].isupper():
        s = f'<span class="hl-edit">{s[0].upper()}</span>' + s[1:]
    else:
        s = s[0] + s[1:]

    replacements = [
        (r'\brất đẹp\b', '<span class="hl-edit">đẹp dịu dàng và rực rỡ biết bao</span>'),
        (r'\brất xinh\b', '<span class="hl-edit">xinh xắn và đáng yêu vô cùng</span>'),
        (r'\brất to\b', '<span class="hl-edit">to lớn, vươn cao vững chãi</span>'),
        (r'\brất mát\b', '<span class="hl-edit">mát rượi, xua tan cái nắng trưa hè</span>'),
        (r'\brất vui\b', '<span class="hl-edit">vui tươi, rộn rã tiếng cười</span>'),
        (r'\brất hiền\b', '<span class="hl-edit">hiền từ và ấm áp</span>'),
        (r'\brất nhanh\b', '<span class="hl-edit">nhanh thoăn thoắt</span>'),
        (r'\brất thơm\b', '<span class="hl-edit">tỏa hương thơm ngát dễ chịu</span>'),
        (r'\brất sạch\b', '<span class="hl-edit">sạch bong, gọn gàng và ngăn nắp</span>'),
        (r'\bmàu xanh\b', '<span class="hl-edit">khoác lên mình màu xanh biếc tươi mát</span>'),
        (r'\bmàu đỏ\b', '<span class="hl-edit">rực lên sắc đỏ tươi thắm</span>'),
        (r'\bmàu vàng\b', '<span class="hl-edit">óng ánh sắc vàng tươi rực rỡ</span>'),
        (r'\bchảy êm đềm\b', '<span class="hl-edit">hiền hòa uốn lượn như dải lụa mềm mại</span>'),
        (r'\bgiảng bài\b', '<span class="hl-edit">say sưa giảng bài với giọng nói ấm áp, truyền cảm</span>'),
        (r'\bra chơi\b', '<span class="hl-edit">ùa ra sân chơi tung tăng như bầy chim non</span>')
    ]

    modified = False
    for pattern, repl in replacements:
        if re.search(pattern, s, flags=re.IGNORECASE):
            s = re.sub(pattern, repl, s, count=1, flags=re.IGNORECASE)
            modified = True

    s_lower = sentence.lower()
    if idx == 0 and not modified:
        if len(sentence.split()) < 10 and not any(s_lower.startswith(w) for w in ["vào", "buổi", "sáng", "trên", "ở", "trong", "nhìn"]):
            s = f'<span class="hl-edit">Mỗi khi ngắm nhìn,</span> {s[0].lower() + s[1:]}'
    elif idx == 1 and not modified:
        if "như" not in s_lower:
            if topic_type == "do_vat":
                s = f'{s} <span class="hl-edit">trông thật xinh xắn như một người bạn nhỏ thân thiết</span>'
            elif topic_type == "cay_coi":
                s = f'{s} <span class="hl-edit">đang khẽ đung đưa trong gió như vẫy tay chào chúng em</span>'
            elif topic_type == "con_vat":
                s = f'{s} <span class="hl-edit">với dáng vẻ nhanh nhẹn và vô cùng đáng yêu</span>'
            elif topic_type == "truong_lop":
                s = f'<span class="hl-edit">Khắp sân trường,</span> {s[0].lower() + s[1:]} <span class="hl-edit">tạo nên bầu không khí vô cùng nhộn nhịp</span>'
            elif topic_type == "con_nguoi":
                s = f'{s} <span class="hl-edit">với ánh mắt trìu mến và nụ cười hiền hậu</span>'
            else:
                s = f'<span class="hl-edit">Nhìn từ xa,</span> {s[0].lower() + s[1:]} <span class="hl-edit">đẹp tựa như một bức tranh thiên nhiên tươi sáng</span>'
    elif idx == total_sentences - 1:
        if any(k in s_lower for k in ["yêu", "thích", "quý", "nhớ", "tự hào", "vui", "hứa", "mong"]):
            if not modified:
                s = f'{s} <span class="hl-edit">và luôn trân trọng những hình ảnh thân thương này</span>'
        else:
            if topic_type == "do_vat":
                s = f'{s}. <span class="hl-edit">Em rất yêu quý và luôn giữ gìn người bạn nhỏ này thật cẩn thận</span>'
            elif topic_type in ["cay_coi", "canh_vat", "truong_lop"]:
                s = f'{s}. <span class="hl-edit">Ngắm nhìn khung cảnh ấy, lòng em lại trào dâng niềm yêu mến và tự hào biết bao</span>'
            else:
                s = f'{s}. <span class="hl-edit">Em cảm thấy trong lòng thật vui và ngập tràn niềm hạnh phúc ấm áp</span>'

    return s + "."

def build_upgraded_paragraph_from_student(text, challenge_info):
    sentences = split_sentences(text)
    total = len(sentences)
    topic_type = challenge_info.get("loai", "canh_vat")
    upgraded_list = []
    for i, sent in enumerate(sentences):
        upgraded_list.append(upgrade_sentence_by_student_idea(sent, i, total, topic_type))
    return " ".join(upgraded_list)

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

# ==================== 4 TAB CHỨC NĂNG CHÍNH (ĐÚNG THỨ TỰ YÊU CẦU) ====================
tab1, tab2, tab3, tab4 = st.tabs([
    "🎮 1. Thử Thách Tương Tác Từ Ngữ",
    "📖 2. Kho Từ Láy & Biện Pháp Tu Từ",
    "🩺 3. Trạm 'Bác Sĩ Sửa Câu'",
    "🏆 4. Thử Thách Sáng Tác Đoạn Văn Nhanh"
])

# ------------------------------------------------------------------------------
# TAB 1: THỬ THÁCH TƯƠNG TÁC TỪ NGỮ (ÔN TẬP THẺ ĐÚNG/SAI, TUYÊN DƯƠNG/BÁO ĐỘNG ĐỎ)
# ------------------------------------------------------------------------------
with tab1:
    st.subheader("🎮 Thử Thách Tương Tác: Ôn Tập Từ Ngữ & Biện Pháp Tu Từ")
    st.write("Em hãy thử tài lựa chọn thẻ đáp án chính xác cho các câu hỏi ôn tập dưới đây[cite: 1]. Chọn đúng sẽ nhận được hoa tươi và lời tuyên dương[cite: 1], chọn sai sẽ kích hoạt báo động đỏ và yêu cầu làm lại[cite: 1]!")

    if "game_key" not in st.session_state:
        st.session_state.game_key = list(MINI_GAMES.keys())[0]
    if "game_status" not in st.session_state:
        st.session_state.game_status = "playing"

    chosen_game_key = st.selectbox(
        "🗂️ Chọn dạng bài tập tương tác:",
        list(MINI_GAMES.keys()),
        key="select_game_type"
    )

    if chosen_game_key != st.session_state.game_key:
        st.session_state.game_key = chosen_game_key
        st.session_state.game_status = "playing"
        current_data = MINI_GAMES[chosen_game_key]
        all_opts = [current_data["dap_an_dung"]] + current_data["dap_an_sai"]
        random.shuffle(all_opts)
        st.session_state.shuffled_options = all_opts

    if "shuffled_options" not in st.session_state:
        current_data = MINI_GAMES[chosen_game_key]
        all_opts = [current_data["dap_an_dung"]] + current_data["dap_an_sai"]
        random.shuffle(all_opts)
        st.session_state.shuffled_options = all_opts

    current_data = MINI_GAMES[st.session_state.game_key]

    st.markdown(f"""
    <div style="background:#e7f5ff; border:2px solid #74c0fc; border-radius:12px; padding:16px; margin:10px 0; font-size:1.1rem; color:#1864ab; font-weight:bold;">
        ❓ {current_data['cau_hoi']}
    </div>
    """, unsafe_allow_html=True)

    st.write("👇 **Hãy bấm chọn thẻ đáp án bên dưới:**")

    cols = st.columns(len(st.session_state.shuffled_options))
    for idx, opt in enumerate(st.session_state.shuffled_options):
        with cols[idx]:
            if st.button(f"🏷️ {opt}", key=f"btn_opt_{idx}", use_container_width=True):
                if opt == current_data["dap_an_dung"]:
                    st.session_state.game_status = "success"
                    st.session_state.stars += 10
                else:
                    st.session_state.game_status = "fail"

    if st.session_state.game_status == "success":
        st.markdown(f"""
        <div class="success-flower-box">
            🌸🌺🌷 TUYỆT VỜI! XUẤT SẮC QUÁ BẠN {st.session_state.student_name.upper()}! 🌷🌺🌸<br>
            Bạn đã chọn thẻ đáp án <b>CHÍNH XÁC</b>[cite: 1]! Nhận ngay <b>+10 Sao Ngôn Từ ⭐</b> và những đóa hoa tươi thắm từ thầy cô[cite: 1]!
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
        if st.button("🔄 Chơi Thử Thách Khác Ngay", use_container_width=True):
            st.session_state.game_status = "playing"
            random.shuffle(st.session_state.shuffled_options)
            st.rerun()

    elif st.session_state.game_status == "fail":
        st.markdown(f"""
        <div class="alert-red-box">
            🚨 BÁO ĐỘNG ĐỎ! CHƯA CHÍNH XÁC RỒI BẠN {st.session_state.student_name.upper()}! 🚨<br>
            Thẻ đáp án vừa chọn chưa đúng[cite: 1]. Hệ thống kích hoạt chế độ báo động đỏ[cite: 1], yêu cầu bạn hít thở sâu và suy nghĩ kỹ để <b>làm lại từ đầu</b> nhé[cite: 1]!
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 Thử Lại Ngay Lập Tức", use_container_width=True):
            st.session_state.game_status = "playing"
            random.shuffle(st.session_state.shuffled_options)
            st.rerun()

# ------------------------------------------------------------------------------
# TAB 2: KHO TỪ VỰNG & BIỆN PHÁP TU TỪ
# ------------------------------------------------------------------------------
with tab2:
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
# TAB 3: TRẠM BÁC SĨ SỬA CÂU (SMART SENTENCE DOCTOR)
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("🩺 Trạm 'Bác Sĩ Sửa Câu'")
    st.write("Em hãy nhập một câu văn đơn giản hoặc câu văn bị lặp từ của mình vào đây. Trợ lý Học sinh lớp 5 sẽ giúp em 'gọt giũa' thành một câu văn giàu hình ảnh hơn!")

    user_sentence = st.text_input("✍️ Nhập câu văn của em:", "Con sông quê em rất đẹp. Con sông chảy hiền hòa.")

    if st.button("🩺 Nhờ Trợ Lý Nâng Cấp Câu Văn", use_container_width=True):
        if user_sentence.strip() != "":
            st.session_state.stars += 5
            st.balloons()
            
            student_sents = split_sentences(user_sentence)
            upgraded_single = " ".join([upgrade_sentence_by_student_idea(s, idx, len(student_sents), "canh_vat") for idx, s in enumerate(student_sents)])
            
            st.markdown(f"""
            <div class="ai-box">
                🤗 <b>Đoạn câu đã được chỉnh sửa hoàn chỉnh cho bạn {st.session_state.student_name}:</b>
                <div class="upgrade-paragraph-box">{upgraded_single}</div>
            </div>
            """, unsafe_allow_html=True)
            st.success("Tuyệt vời! Em được thưởng +5 Sao Ngôn Từ ⭐")
        else:
            st.warning("Bạn hãy nhập câu văn vào ô trống trước khi bấm nút nhé!")

# ------------------------------------------------------------------------------
# TAB 4: THỬ THÁCH SÁNG TÁC ĐOẠN VĂN NHANH
# ------------------------------------------------------------------------------
with tab4:
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
        placeholder="Ví dụ: Buổi sáng quê em rất đẹp. Gió thổi rất mát qua hàng cây. Ông mặt trời tỏa nắng màu vàng trên cánh đồng. Em rất yêu quê hương của em."
    )

    live_sentences = split_sentences(paragraph_input)
    st.caption(f"📊 **Số câu hiện tại bạn đã viết:** `{len(live_sentences)} câu` *(Yêu cầu hợp lệ: từ 3 đến 5 câu)*")

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        submit_btn = st.button("✅ Nộp Bài & Xem Đoạn Văn Hoàn Chỉnh", use_container_width=True)
    with col_btn2:
        if st.button("🎲 Đổi Đề Bài Khác Cùng Mức Độ", use_container_width=True):
            st.session_state.challenge_idx += 1
            st.rerun()

    if submit_btn:
        c_count = len(live_sentences)

        if c_count < 3:
            st.markdown(f"""
            <div class="warn-box">
                ⚠️ <b>Nhắc nhở từ Trợ lý Học sinh lớp 5:</b><br>
                Bạn <b>{st.session_state.student_name}</b> ơi, đoạn văn của bạn hiện mới có <b>{c_count} câu</b> (chưa đủ yêu cầu từ <b>3 đến 5 câu</b>).<br>
                👉 Bạn hãy viết thêm khoảng <b>{3 - c_count} câu nữa</b> và nhớ đặt dấu chấm (<b>.</b>) cuối mỗi câu nhé!
            </div>
            """, unsafe_allow_html=True)
        elif c_count > 5:
            st.markdown(f"""
            <div class="warn-box">
                ⚠️ <b>Nhắc nhở từ Trợ lý Học sinh lớp 5:</b><br>
                Đoạn văn của bạn <b>{st.session_state.student_name}</b> đang có <b>{c_count} câu</b> (vượt quá quy định <b>3 đến 5 câu</b>).<br>
                👉 Bạn hãy rút gọn lại để đoạn văn chỉ gói gọn trong <b>3 đến 5 câu</b> thôi nhé!
            </div>
            """, unsafe_allow_html=True)
        else:
            st.session_state.stars += 15
            st.balloons()
            st.success(f"🎉 Hoan hô bạn {st.session_state.student_name}! Bạn đã hoàn thành đoạn văn ({c_count} câu) và nhận được +15 Sao Ngôn Từ ⭐!")

            upgraded_full_paragraph = build_upgraded_paragraph_from_student(paragraph_input, current_item)

            st.markdown(f"""
            <div class="ai-box">
                💎 <b>Đoạn văn chỉnh sửa hoàn chỉnh của bạn {st.session_state.student_name}:</b>
                <div class="upgrade-paragraph-box">
                    {upgraded_full_paragraph}
                </div>
            </div>
            """, unsafe_allow_html=True)
