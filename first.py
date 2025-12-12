# 导入所需库
import streamlit as st
import pandas as pd
from datetime import datetime

# 页面基础配置
st.set_page_config(
    page_title="我的春日花房",  # 页面标题
    page_icon="🌸",  # 页面图标
    layout="centered",  # 居中布局
    initial_sidebar_state="collapsed"  # 折叠侧边栏
)

# 自定义CSS样式
st.markdown("""
    <style>
    .stApp {
        background-color: #fcf1f7; /* 背景色：蜜桃粉 */
        color: #8b5a89; /* 文字色：豆沙紫 */
        font-family: "Microsoft YaHei"; /* 字体：微软雅黑 */
    }
    .stTitle {
        color: #d63384; /* 标题色：玫粉色 */
        text-align: center; /* 标题居中 */
        letter-spacing: 0.2rem; /* 标题字间距 */
    }
    .stHeader {
        color: #d63384; /* 二级标题色 */
        margin-top: 1.5rem; /* 标题上边距 */
    }
    .stMetric {
        background-color: #ffffff; /* 指标卡片背景 */
        padding: 1rem; /* 内边距 */
        border-radius: 0.8rem; /* 圆角 */
        border: 1px solid #f8d7da; /* 边框 */
    }
    .stDataFrame {
        background-color: #ffffff; /* 表格背景 */
        border-radius: 0.8rem; /* 圆角 */
        border: 1px solid #f8d7da; /* 边框 */
    }
    .stCode {
        background-color: #ffffff !important; /* 代码块背景 */
        border: 1px solid #f8d7da !important; /* 边框 */
        color: #8b5a89 !important; /* 代码文字色 */
    }
    </style>
""", unsafe_allow_html=True)  # 允许解析HTML/CSS

# 主标题
st.title("🌸 我的春日花房")
st.caption("—— 温柔养花日常")  # 副标题

# 花材状态指标
st.header("🌿 花材状态")
col1, col2 = st.columns(2)  # 创建两列布局
with col1:
    # 展示玫瑰开放度
    st.metric(label="玫瑰开放度", value="85%", delta="+5%")
with col2:
    # 展示洋桔梗存活天数
    st.metric(label="洋桔梗存活天数", value="18天", delta="+3天")

# 花材清单表格
st.header("📜 花材清单")
# 定义花材数据
flower_data = {
    "品种": ["粉玫瑰", "洋桔梗", "小苍兰"],
    "购入日期": ["2025-11-11", "2025-11-05", "2025-11-10"],
    "状态": ["✅ 盛放中", "✅ 状态良好", "⚠️ 轻微枯萎"],
    "花语": ["初恋/温柔", "真诚的爱", "纯洁/幸福"]
}
# 转换为DataFrame
flower_df = pd.DataFrame(flower_data)
# 展示表格（宽度适配页面）
st.dataframe(flower_df, use_container_width=True)

# 花艺配色代码
st.header("🎨 温柔配色")
# 定义配色代码内容
color_code = '''
# 春日粉色系花艺配色（RGB）
pink_rose = (245, 183, 197)  # 粉玫瑰
eucalyptus = (162, 180, 165) # 尤加利
# 搭配公式：粉+浅绿=温柔感拉满
color_match = pink_rose + eucalyptus
print("春日配色：", color_match)
'''
# 展示代码块（Python语法高亮）
st.code(color_code, language="python")

# 养花小记
st.header("💡 养花小记")
# 展示养花贴士（含当前日期）
st.markdown(f"""
- 玫瑰斜剪根部45°，每日换水更持久
- 洋桔梗喜凉，避免阳光直射
- 今日日记：{datetime.now().strftime('%m月%d日')} 给小苍兰剪了枯萎花瓣
""")

