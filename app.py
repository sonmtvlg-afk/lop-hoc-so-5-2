import streamlit as st
import streamlit.components.v1 as components
import random

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Vương Quốc Tri Thức Lớp 5/2 - TH Bình Phước",
    page_icon="🐉",
    layout="centered"
)

# ==================== HÀM PHÁT ÂM THANH TRÒ CHƠI (KHÔNG CẦN FILE MP3) ====================
def play_sound(sound_type="win"):
    if sound_type == "win":
        js = """
        <script>
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const notes = [523.25, 659.25, 783.99, 1046.50];
        notes.forEach((freq, idx) => {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, ctx.currentTime + idx * 0.1);
            gain.gain.setValueAtTime(0.2, ctx.currentTime + idx * 0.1);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + idx * 0.1 + 0.25);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(ctx.currentTime + idx * 0.1);
            osc.stop(ctx.currentTime + idx * 0.1 + 0.25);
        });
        </script>
        """
    else:
        js = """
        <script>
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, ctx.currentTime);
        osc.frequency.setValueAtTime(160, ctx.currentTime + 0.15);
        gain.gain.setValueAtTime(0.15, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.35);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.35);
        </script>
        """
    components.html(js, height=0)

# ==================== GIAO DIỆN CSS GAME HÓA RỰC RỠ ====================
st.markdown("""
<style>
    .game-header {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        padding: 22px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(37, 117, 252, 0.3);
        margin-bottom: 15px;
    }
    .game-header h1 {
        font-size: 1.85rem;
        margin: 0;
        color: #fff;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .pet-arena {
        background: linear-gradient(135deg, #fff6e5 0%, #ffe8cc 100%);
        border: 3px solid #ffa94d;
        border-radius: 18px;
        padding: 16px;
        text-align: center;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(255, 169, 77, 0.2);
    }
    .pet-avatar {
        font-size: 4.2rem;
        margin: 5px 0;
        animation: bounce 1.5s infinite alternate;
    }
    @keyframes bounce {
        from { transform: translateY(0px); }
        to { transform: translateY(-8px); }
    }
    .quest-card {
        background: #ffffff;
        border: 3px solid #74c0fc;
        border-radius: 18px;
        padding: 20px;
        margin: 12px 0;
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    }
    .ai-bubble {
        background: #e3fafc;
        border-left: 6px solid #15aabf;
        padding: 15px;
        border-radius: 12px;
        color: #0b7285;
        font-size: 1.05rem;
        margin-top: 12px;
    }
    .item-badge {
        display: inline-block;
        background: #f3f0ff;
        border: 2px solid #845ef7;
        color: #5f3dc4;
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: bold;
        margin: 4px;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ==================== MÁY SINH ĐỀ AI VÔ HẠN (INFINITE GENERATOR) ====================
def generate_infinite_question(topic_choice):
    friends = ["Minh Khôi", "Bảo Ngọc", "Gia Huy", "Thanh Thảo", "Tuấn Kiệt", "Phương Anh"]
    friend = random.choice(friends)

    if topic_choice == "🎲 Ngẫu nhiên tổng hợp (Thú vị nhất)":
        topic = random.choice(["thap_phan", "phan_tram", "hinh_hoc", "thuc_te", "tieng_viet"])
    elif "Số thập phân" in topic_choice:
        topic = "thap_phan"
    elif "Tỉ số phần trăm" in topic_choice:
        topic = "phan_tram"
    elif "Hình học" in topic_choice:
        topic = "hinh_hoc"
    elif "Toán Thực tế" in topic_choice:
        topic = "thuc_te"
    else:
        topic = "tieng_viet"

    # 1. CHỦ ĐỀ SỐ THẬP PHÂN (SINH TỰ ĐỘNG VÔ HẠN)
    if topic == "thap_phan":
        a = round(random.uniform(2.5, 25.5), 1)
        b = round(random.uniform(1.25, 14.75), 2)
        op = random.choice(["+", "-"])
        if op == "+" or a < b:
            ans = round(a + b, 2)
            q_text = f"⚡ **Thử thách Tia Chớp:** Bạn {friend} thực hiện phép tính cộng hai số thập phân: **{a} + {b}**. Kết quả đúng là bao nhiêu?"
            hint = f"💡 **AI gợi ý:** Đặt dấu phẩy thẳng cột! Viết **{a:.2f} + {b:.2f}**, cộng từ phải sang trái nhé!"
            explain = f"🌟 **AI Giải chi tiết:** Ta có {a:.2f} + {b:.2f} = **{ans}**."
        else:
            ans = round(a - b, 2)
            q_text = f"⚡ **Thử thách Tia Chớp:** Bạn {friend} có sợi dây dài **{a} m**, cắt bớt đi **{b} m**. Hỏi sợi dây còn lại dài bao nhiêu mét?"
            hint = f"💡 **AI gợi ý:** Viết thêm chữ số 0 vào phần thập phân để trừ: **{a:.2f} - {b:.2f}**."
            explain = f"🌟 **AI Giải chi tiết:** Độ dài còn lại là: {a:.2f} - {b:.2f} = **{ans} m**."

        wrongs = [round(ans + 1.1, 2), round(abs(ans - 0.5), 2), round(ans + 0.25, 2)]
        opts = [f"{ans}", f"{wrongs[0]}", f"{wrongs[1]}", f"{wrongs[2]}"]
        random.shuffle(opts)
        return {"title": "🧮 Toán 5: Số Thập Phân", "q": q_text, "opts": opts, "ans": f"{ans}", "hint": hint, "exp": explain}

    # 2. CHỦ ĐỀ TỈ SỐ PHẦN TRĂM (SINH TỰ ĐỘNG VÔ HẠN)
    elif topic == "phan_tram":
        total = random.choice([40, 50, 80, 100, 120, 200, 300, 400, 500])
        pct = random.choice([10, 15, 20, 25, 30, 40, 50, 75])
        ans = int(total * pct / 100)
        q_text = f"🌱 **Chiến dịch Xanh:** Trường Tiểu học Bình Phước trồng **{total} cây xanh**, trong đó lớp 5/2 chăm sóc **{pct}%** số cây. Hỏi lớp 5/2 chăm sóc bao nhiêu cây xanh?"
        hint = f"💡 **AI gợi ý:** Muốn tìm **{pct}%** của **{total}**, em lấy **{total} : 100 × {pct}** nhé!"
        explain = f"🌟 **AI Giải chi tiết:** Số cây lớp 5/2 chăm sóc là: {total} : 100 × {pct} = **{ans} (cây)**."
        wrongs = [ans + 5, max(1, ans - 4), ans + 10]
        opts = [f"{ans} cây", f"{wrongs[0]} cây", f"{wrongs[1]} cây", f"{wrongs[2]} cây"]
        random.shuffle(opts)
        return {"title": "🌱 Toán 5: Tỉ Số Phần Trăm", "q": q_text, "opts": opts, "ans": f"{ans} cây", "hint": hint, "exp": explain}

    # 3. CHỦ ĐỀ HÌNH HỌC LỚP 5 (TAM GIÁC, HÌNH THANG)
    elif topic == "hinh_hoc":
        shape = random.choice(["tam_giac", "hinh_thang"])
        if shape == "tam_giac":
            day = random.choice([6, 8, 10, 12, 14, 16])
            cao = random.choice([4, 5, 7, 9, 10])
            ans = int(day * cao / 2)
            q_text = f"📐 **Kiến trúc sư Nhí:** Một bồn hoa hình tam giác ở sân trường Tiểu học Bình Phước có độ dài đáy là **{day} m** và chiều cao là **{cao} m**. Diện tích bồn hoa đó là:"
            hint = f"💡 **AI gợi ý:** Diện tích hình tam giác = **(Đáy × Chiều cao) : 2** = ({day} × {cao}) : 2."
            explain = f"🌟 **AI Giải chi tiết:** Diện tích bồn hoa là: ({day} × {cao}) : 2 = **{ans} m²**."
        else:
            day_lon = random.choice([10, 12, 15, 18])
            day_be = day_lon - random.choice([2, 4, 6])
            cao = random.choice([4, 6, 8, 10])
            ans = int((day_lon + day_be) * cao / 2)
            q_text = f"📐 **Kiến trúc sư Nhí:** Một mảnh vườn hình thang có đáy lớn **{day_lon} m**, đáy bé **{day_be} m** và chiều cao **{cao} m**. Diện tích mảnh vườn là:"
            hint = f"💡 **AI gợi ý:** Muốn tính diện tích hình thang, đáy lớn đáy nhỏ ta mang cộng vào, thế rồi nhân với chiều cao, chia đôi lấy nửa: **({day_lon} + {day_be}) × {cao} : 2**."
            explain = f"🌟 **AI Giải chi tiết:** Diện tích hình thang là: ({day_lon} + {day_be}) × {cao} : 2 = **{ans} m²**."
        wrongs = [ans * 2, ans + 6, max(2, ans - 5)]
        opts = [f"{ans} m²", f"{wrongs[0]} m²", f"{wrongs[1]} m²", f"{wrongs[2]} m²"]
        random.shuffle(opts)
        return {"title": "📐 Toán 5: Hình Học Trực Quan", "q": q_text, "opts": opts, "ans": f"{ans} m²", "hint": hint, "exp": explain}

    # 4. TOÁN THỰC TẾ ĐI CHỢ & TIẾT KIỆM
    elif topic == "thuc_te":
        price = random.choice([40, 60, 80, 100, 120, 150, 200])
        discount = random.choice([10, 20, 25, 50])
        saved = int(price * discount / 100)
        pay = price - saved
        q_text = f"🛒 **Siêu thị Thông minh:** Bạn {friend} cùng mẹ đi mua một quyển sách giá **{price}.000 đồng**. Nhân dịp lễ, nhà sách giảm giá **{discount}%**. Hỏi mẹ phải trả bao nhiêu tiền?"
        hint = f"💡 **AI gợi ý:** Bước 1: Tìm số tiền được giảm ({price} × {discount} : 100 = {saved} nghìn). Bước 2: Lấy giá gốc trừ đi số tiền được giảm!"
        explain = f"🌟 **AI Giải chi tiết:** Số tiền được giảm là {saved}.000đ. Số tiền mẹ phải trả là: {price}.000 - {saved}.000 = **{pay}.000 đồng**."
        wrongs = [f"{saved}.000 đồng", f"{pay + 10}.000 đồng", f"{max(10, pay - 10)}.000 đồng"]
        opts = [f"{pay}.000 đồng"] + wrongs
        random.shuffle(opts)
        return {"title": "🛒 Toán Thực Tế Cuộc Sống", "q": q_text, "opts": opts, "ans": f"{pay}.000 đồng", "hint": hint, "exp": explain}

    # 5. KHO TRÒ CHƠI VUA TIẾNG VIỆT ĐA DẠNG
    else:
        tv_bank = [
            {
                "q": "📚 **Vua Tiếng Việt:** Câu ca dao *'Có công mài sắt, có ngày nên kim'* khuyên chúng ta rèn luyện đức tính gì?",
                "ans": "Kiên trì, nhẫn nại, không ngại khó",
                "w": ["Làm việc thật nhanh", "Thích sưu tầm kim loại", "Chỉ làm việc khi có người nhắc"],
                "hint": "💡 **AI gợi ý:** Từ một thanh sắt to mài thành chiếc kim nhỏ đòi hỏi sự bền bỉ giống như khi các em rèn chữ đẹp mỗi ngày!",
                "exp": "🌟 **AI Giải thích:** Câu tục ngữ khuyên chúng ta kiên trì, nhẫn nại thì việc khó đến mấy cũng sẽ thành công."
            },
            {
                "q": "📚 **Thám tử Ngôn từ:** Trong câu *'Những chú ong chăm chỉ bay đi tìm mật ngọt'*, tác giả đã dùng biện pháp nghệ thuật gì?",
                "ans": "Nhân hóa (gọi ong là 'chú', tả tính nết 'chăm chỉ')",
                "w": ["So sánh", "Điệp từ", "Đảo ngữ"],
                "hint": "💡 **AI gợi ý:** 'Chú' và 'chăm chỉ' vốn là từ dùng cho con người nhưng lại được dùng để tả con ong!",
                "exp": "🌟 **AI Giải thích:** Biện pháp nhân hóa giúp hình ảnh chú ong trở nên sinh động, gần gũi với học sinh."
            },
            {
                "q": "📚 **Mở rộng Vốn từ:** Dòng nào dưới đây gồm toàn các **từ đồng nghĩa** với từ *'Hạnh phúc'*?",
                "ans": "Sungk sướng, viên mãn, phúc hậu (niềm vui lớn)",
                "w": ["Buồn bã, ủ rũ, lo âu", "Nhanh nhẹn, tháo vát, hoạt bát", "Cao ráo, mảnh mai, vạm vỡ"],
                "hint": "💡 **AI gợi ý:** Hãy tìm những từ cùng chỉ trạng thái vui vẻ, mãn nguyện trong cuộc sống!",
                "exp": "🌟 **AI Giải thích:** Từ đồng nghĩa là những từ có nghĩa giống hoặc gần giống nhau."
            },
            {
                "q": "📚 **Từ đa nghĩa:** Từ **'chân'** trong câu nào dưới đây được dùng theo **nghĩa gốc**?",
                "ans": "Bạn Nam chạy nhanh nên đôi chân rất khỏe.",
                "w": ["Chân bàn học lớp 5/2 làm bằng sắt rất chắc chắn.", "Đám mây trắng bồng bềnh dưới chân núi.", "Chân tường lớp học được sơn màu xanh sạch đẹp."],
                "hint": "💡 **AI gợi ý:** Nghĩa gốc của từ 'chân' là bộ phận cơ thể của người hoặc động vật dùng để đi, đứng!",
                "exp": "🌟 **AI Giải thích:** 'Đôi chân' của bạn Nam là nghĩa gốc, còn chân bàn, chân núi, chân tường là nghĩa chuyển."
            },
            {
                "q": "📚 **Điền từ Tinh tế:** Điền từ thích hợp vào câu tục ngữ: *'Một cây làm chẳng nên non / Ba cây chụm lại nên ... cao'*?",
                "ans": "hòn núi",
                "w": ["cánh rừng", "bầu trời", "biển rộng"],
                "hint": "💡 **AI gợi ý:** Từ nào đồng nghĩa với từ 'non' (núi) ở câu trên và tạo vần lưng với từ 'non'?",
                "exp": "🌟 **AI Giải thích:** 'Ba cây chụm lại nên hòn núi cao' ca ngợi sức mạnh của tinh thần đoàn kết trong tập thể lớp 5/2!"
            },
            {
                "q": "📚 **Luyện câu Lớp 5:** Cặp quan hệ từ nào phù hợp nhất để nối câu chỉ **Nguyên nhân - Kết quả**: *'... bạn Lan chịu khó rèn chữ mỗi ngày ... vở của bạn ấy rất sạch đẹp.'*?",
                "ans": "Nhờ ... nên ...",
                "w": ["Tuy ... nhưng ...", "Nếu ... thì ...", "Không những ... mà còn ..."],
                "hint": "💡 **AI gợi ý:** Việc chịu khó rèn chữ mang lại kết quả tốt đẹp, ta dùng cặp từ nào để khen ngợi?",
                "exp": "🌟 **AI Giải thích:** Cặp quan hệ từ 'Nhờ... nên...' biểu thị quan hệ nguyên nhân dẫn đến kết quả tích cực."
            }
        ]
        item = random.choice(tv_bank)
        opts = [item["ans"]] + item["w"]
        random.shuffle(opts)
        return {"title": "📚 Đấu Trường Vua Tiếng Việt 5", "q": item["q"], "opts": opts, "ans": item["ans"], "hint": item["hint"], "exp": item["exp"]}

# ==================== KHỞI TẠO TRẠNG THÁI GAME ====================
if "student" not in st.session_state:
    st.session_state.student = "Minh Khôi"
if "group" not in st.session_state:
    st.session_state.group = "Tổ 1"
if "xp" not in st.session_state:
    st.session_state.xp = 40
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "chests" not in st.session_state:
    st.session_state.chests = 1
if "inventory" not in st.session_state:
    st.session_state.inventory = ["🌟 Huy hiệu Tân Binh 5/2"]
if "current_q" not in st.session_state:
    st.session_state.current_q = generate_infinite_question("🎲 Ngẫu nhiên tổng hợp (Thú vị nhất)")
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "answered" not in st.session_state:
    st.session_state.answered = False
if "group_scores" not in st.session_state:
    st.session_state.group_scores = {"Tổ 1": 210, "Tổ 2": 190, "Tổ 3": 220, "Tổ 4": 180}

# ==================== TÍNH CẤP ĐỘ TIẾN HÓA LINH VẬT ====================
def get_pet_stage(xp):
    if xp < 60:
        return "🥚", "Cấp 1: Trứng Thần Kỳ", 60
    elif xp < 120:
        return "🐣", "Cấp 2: Rồng Con Hiếu Học", 120
    elif xp < 200:
        return "🦖", "Cấp 3: Chiến Binh Rồng Xanh", 200
    elif xp < 300:
        return "🐉", "Cấp 4: Rồng Lửa Tri Thức", 300
    else:
        return "👑🐉", "Cấp Tối Thượng: Thần Rồng Bình Phước", 500

pet_icon, pet_title, next_xp = get_pet_stage(st.session_state.xp)

# ==================== HEADER & HỒ SƠ NHANH ====================
st.markdown("""
<div class="game-header">
    <h1>🐉 VƯƠNG QUỐC TRI THỨC LỚP 5/2</h1>
    <p>Trường Tiểu học Bình Phước • GVCN: Thầy Huỳnh Minh Sơn</p>
</div>
""", unsafe_allow_html=True)

c_info1, c_info2 = st.columns([1.5, 1])
with c_info1:
    st.session_state.student = st.text_input("👦👧 Tên nhà thám hiểm nhí:", st.session_state.student)
with c_info2:
    st.session_state.group = st.selectbox("🚩 Chiến đội:", ["Tổ 1", "Tổ 2", "Tổ 3", "Tổ 4"])

# ==================== KHU VỰC NUÔI LINH VẬT (PET ARENA) ====================
st.markdown(f"""
<div class="pet-arena">
    <div style="font-weight:bold; color:#d9480f;">LINH VẬT ĐỒNG HÀNH CỦA {st.session_state.student.upper()} ({st.session_state.group})</div>
    <div class="pet-avatar">{pet_icon}</div>
    <h3 style="margin:4px 0; color:#e67700;">{pet_title}</h3>
    <p style="margin:4px 0; font-size:1.05rem;">
        ⚡ Năng lượng: <b>{st.session_state.xp}/{next_xp} XP</b> &nbsp;|&nbsp;
        🔥 Chuỗi thắng: <b>{st.session_state.streak} liên tiếp</b> &nbsp;|&nbsp;
        🎁 Rương kho báu: <b>{st.session_state.chests} rương</b>
    </p>
</div>
""", unsafe_allow_html=True)

st.progress(min(st.session_state.xp / next_xp, 1.0))

# Nút mở Rương Kho Báu Ngẫu Nhiên
if st.session_state.chests > 0:
    if st.button(f"🎁 MỞ RƯƠNG KHO BÁU BÍ MẬT ({st.session_state.chests} rương đang chờ!)", use_container_width=True):
        rewards = [
            "🗡️ Kiếm Ánh Sáng Toán Học",
            "🛡️ Khiên Tiếng Việt Bất Bại",
            "💎 Viên Ngọc Kiên Trì (Rèn Chữ Đẹp)",
            "🌱 Chồi Non Bảo Vệ Môi Trường",
            "🦉 Cú Mèo Thông Thái AI",
            "👑 Vương Miện Sao Chăm Ngoan"
        ]
        avail = [r for r in rewards if r not in st.session_state.inventory]
        new_item = random.choice(avail) if avail else "🌟 Siêu Cúp Vinh Quang (+30 XP)"
        if new_item not in st.session_state.inventory:
            st.session_state.inventory.append(new_item)
        st.session_state.chests -= 1
        st.session_state.xp += 15
        play_sound("win")
        st.balloons()
        st.success(f"🎉 Chúc mừng! Em mở rương nhận được vật phẩm quý hiếm: **{new_item}** và **+15 XP**!")

# Hiển thị bộ sưu tập vật phẩm
inv_html = "".join([f'<span class="item-badge">{item}</span>' for item in st.session_state.inventory])
st.markdown(f"**🎒 Túi đồ Sưu tầm:** {inv_html}", unsafe_allow_html=True)
st.write("")

# ==================== 4 TAB TRẢI NGHIỆM SỐNG ĐỘNG ====================
tab1, tab2, tab3, tab4 = st.tabs([
    "⚔️ 1. ĐẤU TRƯỜNG VÔ HẠN",
    "🤖 2. HỎI ĐÁP AI MỌI BÀI TOÁN",
    "🎨 3. TRỰC QUAN HÓA",
    "🏆 4. GÓC PHỤ HUYNH & GV"
])

# ==============================================================================
# TAB 1: ĐẤU TRƯỜNG SINH ĐỀ VÔ HẠN (KHÔNG BAO GIỜ LẶP LẠI)
# ==============================================================================
with tab1:
    st.subheader("⚔️ Máy Sinh Đề Thông Minh Vô Hạn (Mỗi lần bấm 1 đề mới!)")

    topic_sel = st.selectbox(
        "🎯 Chọn vùng đất thử thách:",
        [
            "🎲 Ngẫu nhiên tổng hợp (Thú vị nhất)",
            "🧮 Chuyên đề 1: Cộng, trừ Số thập phân (Vô hạn đề)",
            "🌱 Chuyên đề 2: Tỉ số phần trăm % (Vô hạn đề)",
            "📐 Chuyên đề 3: Hình học Lớp 5 - Tam giác, Hình thang (Vô hạn đề)",
            "🛒 Chuyên đề 4: Toán Thực tế Đi chợ & Tiết kiệm (Vô hạn đề)",
            "📚 Chuyên đề 5: Đấu trường Vua Tiếng Việt 5"
        ]
    )

    if st.button("🔄 Sinh Câu Hỏi Mới Tinh Ngay Lập Tức!", use_container_width=True):
        st.session_state.current_q = generate_infinite_question(topic_sel)
        st.session_state.show_hint = False
        st.session_state.answered = False
        st.rerun()

    q_data = st.session_state.current_q

    st.markdown(f"""
    <div class="quest-card">
        <div style="color:#1971c2; font-weight:bold; margin-bottom:6px;">{q_data['title']}</div>
        <div style="font-size:1.18rem;">{q_data['q']}</div>
    </div>
    """, unsafe_allow_html=True)

    user_ans = st.radio("👉 Chọn đáp án để giúp Linh Vật tiến hóa:", q_data["opts"], key=f"q_{q_data['q']}")

    col_b1, col_b2, col_b3 = st.columns(3)
    with col_b1:
        if st.button("⚡ Tung Chiêu (Nộp bài)", use_container_width=True):
            if user_ans == q_data["ans"]:
                play_sound("win")
                st.balloons()
                st.session_state.xp += 20
                st.session_state.streak += 1
                st.session_state.group_scores[st.session_state.group] += 20
                st.session_state.answered = True
                if st.session_state.streak % 3 == 0:
                    st.session_state.chests += 1
                    st.toast("🎁 Chuỗi 3 câu đúng liên tiếp! Em được thưởng +1 Rương Kho Báu!", icon="🎉")
                st.success(f"🎉 Chính xác! Linh vật nhận +20 XP! (Chuỗi thắng: {st.session_state.streak})")
                st.markdown(f'<div class="ai-bubble">{q_data["exp"]}</div>', unsafe_allow_html=True)
            else:
                play_sound("lose")
                st.session_state.streak = 0
                st.session_state.show_hint = True
                st.warning("Chưa trúng mục tiêu rồi! Hãy xem Trợ lý AI mách nước ở dưới nhé!")

    with col_b2:
        if st.button("💡 AI Mách Nước", use_container_width=True):
            st.session_state.show_hint = True

    with col_b3:
        if st.button("➡️ Sang Câu Mới", use_container_width=True):
            st.session_state.current_q = generate_infinite_question(topic_sel)
            st.session_state.show_hint = False
            st.session_state.answered = False
            st.rerun()

    if st.session_state.show_hint:
        st.markdown(f'<div class="ai-bubble">{q_data["hint"]}</div>', unsafe_allow_html=True)

# ==============================================================================
# TAB 2: TRỢ LÝ AI GIẢI ĐÁP MỌI BÀI TOÁN TỰ NHẬP
# ==============================================================================
with tab2:
    st.subheader("🤖 Trợ Lý AI Lớp 5/2: Em Hỏi Bất Kỳ – AI Hướng Dẫn Từng Bước")
    st.write("Không giới hạn câu hỏi! Học sinh và phụ huynh có thể tự nhập số liệu bài toán ở nhà để AI giảng bài ngay:")

    ai_mode = st.selectbox(
        "📌 Chọn dạng bài em muốn AI giảng giải chi tiết:",
        [
            "1. Tìm Tỉ số phần trăm của hai số bất kỳ (Ví dụ: 15 và 60)",
            "2. Tính diện tích Hình thang / Hình tam giác / Hình tròn với số đo bất kỳ",
            "3. Giải bài toán Giảm giá % khi đi siêu thị",
            "4. Tra cứu nhanh Từ đồng nghĩa, Trái nghĩa & Mẹo Rèn chữ đẹp"
        ]
    )

    if "1." in ai_mode:
        c1, c2 = st.columns(2)
        with c1:
            so_a = st.number_input("Nhập số thứ nhất (a):", value=18.0, step=1.0)
        with c2:
            so_b = st.number_input("Nhập số thứ hai (b - khác 0):", value=72.0, min_value=0.1, step=1.0)
        if st.button("🤖 AI Hướng dẫn từng bước giải"):
            thuong = so_a / so_b
            ty_so = thuong * 100
            st.markdown(f"""
            <div class="ai-bubble">
                🤖 <b>Trợ lý AI Lớp 5/2 hướng dẫn giải bài toán tìm tỉ số phần trăm của {so_a:g} và {so_b:g}:</b><br><br>
                • <b>Bước 1 (Tìm thương):</b> Lấy {so_a:g} chia cho {so_b:g} ta được: <b>{so_a:g} : {so_b:g} = {thuong:.4f}</b><br>
                • <b>Bước 2 (Nhân nhẩm với 100 và viết ký hiệu %):</b> Lấy {thuong:.4f} × 100 = <b>{ty_so:.2f}%</b>.<br>
                👉 <b>Đáp số: {ty_so:.2f}%</b>
            </div>
            """, unsafe_allow_html=True)

    elif "2." in ai_mode:
        hinh = st.radio("Chọn hình cần tính:", ["Hình thang", "Hình tam giác", "Hình tròn"], horizontal=True)
        if hinh == "Hình thang":
            d1 = st.number_input("Đáy lớn:", value=12.0)
            d2 = st.number_input("Đáy bé:", value=8.0)
            h = st.number_input("Chiều cao:", value=5.0)
            dt = (d1 + d2) * h / 2
            st.markdown(f"""
            <div class="ai-bubble">
                🤖 <b>Lời giải chi tiết từ AI:</b><br>
                • Tổng độ dài hai đáy là: {d1:g} + {d2:g} = {d1+d2:g}<br>
                • Diện tích hình thang là: ({d1:g} + {d2:g}) × {h:g} : 2 = <b>{dt:g} (đơn vị diện tích)</b>
            </div>
            """, unsafe_allow_html=True)
        elif hinh == "Hình tam giác":
            d = st.number_input("Độ dài đáy:", value=10.0)
            h = st.number_input("Chiều cao:", value=6.0)
            st.markdown(f"""
            <div class="ai-bubble">
                🤖 <b>Lời giải chi tiết từ AI:</b><br>
                • Diện tích hình tam giác là: ({d:g} × {h:g}) : 2 = <b>{d*h/2:g} (đơn vị diện tích)</b>
            </div>
            """, unsafe_allow_html=True)
        else:
            r = st.number_input("Bán kính hình tròn (r):", value=5.0)
            st.markdown(f"""
            <div class="ai-bubble">
                🤖 <b>Lời giải chi tiết từ AI:</b><br>
                • <b>Chu vi hình tròn:</b> {r:g} × 2 × 3,14 = <b>{r*2*3.14:.2f}</b><br>
                • <b>Diện tích hình tròn:</b> {r:g} × {r:g} × 3,14 = <b>{r*r*3.14:.2f}</b>
            </div>
            """, unsafe_allow_html=True)

    elif "3." in ai_mode:
        gia = st.number_input("Giá gốc món hàng (nghìn đồng):", value=150.0, step=10.0)
        giam = st.slider("Mức giảm giá (%):", 5, 80, 20, step=5)
        tien_giam = gia * giam / 100
        con_lai = gia - tien_giam
        st.markdown(f"""
        <div class="ai-bubble">
            🤖 <b>Trợ lý AI giải bài toán thực tế:</b><br>
            • Số tiền được giảm ({giam}%) là: {gia:g} × {giam} : 100 = <b>{tien_giam:g} nghìn đồng</b><br>
            • Số tiền thực tế cần trả là: {gia:g} - {tien_giam:g} = <b>{con_lai:g} nghìn đồng</b>
        </div>
        """, unsafe_allow_html=True)

    else:
        tu_khoa = st.selectbox("Chọn chủ đề từ vựng cần tra cứu:", ["Chăm chỉ / Kiên trì", "Bảo vệ môi trường", "Đoàn kết yêu thương", "Bí quyết Rèn chữ đẹp Lớp 5/2"])
        tu_dien = {
            "Chăm chỉ / Kiên trì": "• **Từ đồng nghĩa:** Siêng năng, cần cù, chịu khó, bền bỉ, nhẫn nại.\n• **Từ trái nghĩa:** Lười biếng, biếng nhác, nản lòng.\n• **Đặt câu mẫu:** *Nhờ kiên trì rèn chữ mỗi ngày, nét chữ của em ngày càng thanh thoát.*",
            "Bảo vệ môi trường": "• **Từ ngữ mở rộng:** Sinh thái, phủ xanh, năng lượng sạch, tái chế, trong lành.\n• **Đặt câu mẫu:** *Chúng em phân loại rác thải nhựa để góp phần bảo vệ môi trường xanh - sạch - đẹp.*",
            "Đoàn kết yêu thương": "• **Thành ngữ - Tục ngữ:** *Lá lành đùm lá rách; Một con ngựa đau cả tàu bỏ cỏ; Đoàn kết là sức mạnh.*\n• **Đặt câu mẫu:** *Tập thể lớp 5/2 luôn đoàn kết, giúp đỡ nhau cùng tiến bộ.*",
            "Bí quyết Rèn chữ đẹp Lớp 5/2": "• **Quy tắc vàng:** Lưng thẳng, mắt cách vở 25-30cm. Chữ cái cao 2,5 ô li (h, k, l, b, g, y) viết đều nét, khoảng cách giữa các chữ bằng 1 con chữ *o*."
        }
        st.info(tu_dien[tu_khoa])

# ==============================================================================
# TAB 3: TRỰC QUAN HÓA TOÁN HỌC SINH ĐỘNG
# ==============================================================================
with tab3:
    st.subheader("🎨 Phòng Thí Nghiệm Trực Quan (Nhìn Hình Hiểu Bản Chất)")
    tu = st.slider("🍕 Chọn số phần bánh em có (Tử số):", 1, 10, 3)
    mau = st.slider("🍽️ Tổng số phần bánh bằng nhau (Mẫu số):", tu, 10, 4)

    icons = "🍕 " * tu + "⚪ " * (mau - tu)
    st.markdown(f"""
    <div class="quest-card" style="text-align:center;">
        <div style="font-size:2.3rem;">{icons}</div>
        <h3>Phân số: <b>{tu}/{mau}</b> &nbsp;=&nbsp; Số thập phân: <b>{tu/mau:.2f}</b> &nbsp;=&nbsp; Phần trăm: <b>{tu/mau*100:.1f}%</b></h3>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# TAB 4: BẢNG THI ĐUA TỔ & PHIẾU NHẬN XÉT THÔNG TƯ 27
# ==============================================================================
with tab4:
    st.subheader("🏆 Bảng Thi Đua Các Tổ - Lớp 5/2 (Trường Tiểu học Bình Phước)")
    for g_name, g_score in sorted(st.session_state.group_scores.items(), key=lambda x: x[1], reverse=True):
        st.write(f"**{g_name}**: `{g_score} XP` 🔥")
        st.progress(min(g_score / 400, 1.0))

    st.markdown("---")
    st.subheader("👨‍👩‍👧 Góc Phụ Huynh Phối Hợp & Đánh Giá Thông Tư 27")
    c_ph1 = st.checkbox("📖 Con tự giác hoàn thành bài và chuẩn bị sách vở (+15 XP)")
    c_ph2 = st.checkbox("✍️ Con rèn chữ cẩn thận, giữ vở sạch đẹp (+15 XP)")
    if st.button("💌 Phụ huynh Xác nhận & Thưởng Năng lượng cho Linh vật", use_container_width=True):
        bonus = (15 if c_ph1 else 0) + (15 if c_ph2 else 0)
        if bonus > 0:
            play_sound("win")
            st.session_state.xp += bonus
            st.session_state.group_scores[st.session_state.group] += bonus
            st.balloons()
            st.success(f"Đã cộng +{bonus} XP giúp Linh vật của {st.session_state.student} mau tiến hóa!")

    muc_tt27 = "Hoàn thành tốt (HTT)" if st.session_state.xp >= 80 else "Hoàn thành (HT)"
    nhan_xet = (
        f"TRƯỜNG TIỂU HỌC BÌNH PHƯỚC - LỚP 5/2 (GVCN: Huỳnh Minh Sơn)\n"
        f"• Học sinh: {st.session_state.student} ({st.session_state.group}) | Cấp độ: {pet_title}\n"
        f"• Đánh giá Thông tư 27: {muc_tt27}\n"
        f"• Nhận xét: Tích cực tham gia giải toán và rèn luyện Tiếng Việt trên hệ thống AI thích ứng; nắm vững kiến thức số thập phân, tỉ số phần trăm và hình học; có ý thức rèn chữ, giữ vở và phối hợp tốt giữa gia đình - nhà trường."
    )
    st.text_area("📋 Bản nhận xét tự động (Sao chép gửi Zalo Phụ huynh):", nhan_xet, height=135)
