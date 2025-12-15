import streamlit as st

# 页面基础配置
st.set_page_config(page_title="电影世界", page_icon="🎬", layout="wide")

# 注入CSS样式，将按钮设置为粉色
st.markdown("""
    <style>
    /* 针对所有按钮的基础样式 */
    div.stButton > button {
        background-color: #ffc0cb; /* 浅粉色 */
        color: black;
        border: none;
        border-radius: 5px;
    }
    /* 按钮悬浮效果 */
    div.stButton > button:hover {
        background-color: #ff99cc; /* 悬浮加深粉色 */
    }
    </style>
    """, unsafe_allow_html=True)

st.title('甜心格格第五部')

# 替换为Streamlit支持的视频格式（MP4/WebM/MOV等）
video_arr = [
    {
        'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',  # 示例MP4链接
        'title': '甜心格格第五部-第1集'
    },
    {
        'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title': '甜心格格第五部-第2集'
    },
    {
        'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title': '甜心格格第五部-第3集'
    },
    {
        'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title': '甜心格格第五部-第4集'
    },
    {
        'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title': '甜心格格第五部-第5集'
    }
]

# 初始化session_state的索引
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 显示当前集数标题
st.subheader(video_arr[st.session_state['ind']]['title'])

# 显示视频
st.video(video_arr[st.session_state['ind']]['url'], autoplay=True)

# 定义切换集数的函数
def play(i):
    st.session_state['ind'] = int(i)

# 横向排列按钮（一排最多5个）
cols = st.columns(min(len(video_arr), 5))
for i, col in enumerate(cols):
    with col:
        st.button(f'第{i + 1}集', use_container_width=True, on_click=play, args=(i,))
