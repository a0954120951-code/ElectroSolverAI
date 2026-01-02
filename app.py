import streamlit as st

# 1. 設定網頁基本外觀 (標題、圖示)
st.set_page_config(
    page_title="基本電學解題高手",
    page_icon="⚡",
    layout="centered"
)

# 2. 注入 CSS 美化 (這是為了模仿您原本 HTML 想要的那種筆記本風格)
# Streamlit 允許我們用這種方式微調字體和顏色
st.markdown("""
    <style>
    /* 引入您原本喜歡的字體 (Noto Sans TC) */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap');
    
    /* 設定全站字體 */
    html, body, [class*="css"] {
        font-family: 'Noto Sans TC', sans-serif;
    }
    
    /* 讓按鈕變漂亮 */
    .stButton>button {
        background-color: #e74c3c;
        color: white;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #c0392b;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 程式主畫面
st.title("⚡ 基本電學解題高手")
st.markdown("### 專為電機科學生設計的 AI 助教")
st.info("💡 說明：請輸入題目，AI 會幫你列出詳細的計算步驟。")

# 4. 輸入區
question = st.text_area(
    "請在下方貼上題目：", 
    height=150, 
    placeholder="例如：如圖所示，求 2Ω 電阻上的電壓降為何？..."
)

# 5. 互動按鈕
if st.button("開始解題"):
    if not question:
        st.warning("⚠️ 請先輸入題目喔！")
    else:
        # --- 這裡未來會接上 Google AI 的大腦 ---
        st.success("收到題目！正在分析中...")
        
        # 模擬 AI 的回答 (展示 LaTeX 排版效果)
        st.markdown("---")
        st.subheader("📝 解析步驟：")
        
        # 這裡展示 Streamlit 最強大的功能：數學公式不斷行
        st.markdown("""
        1. 根據 **克希荷夫電壓定律 (KVL)**，我們可以列出迴路方程式。
        2. 假設電流為 $I$，則迴路電壓方程式為：
           $$10V - I \\times 2\\Omega - I \\times 3\\Omega = 0$$
        3. 整理後得到：
           $$5I = 10 \\Rightarrow I = 2A$$
        4. 所以 $2\\Omega$ 電阻上的壓降 $V_{2\\Omega}$ 為：
           $$V = I \\times R = 2A \\times 2\\Omega = 4V$$
        """)
        
        st.balloons() # 給學生一點鼓勵的特效
