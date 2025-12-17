# 导入streamlit库（用于快速搭建网页应用）
import streamlit as st

# 配置网页基础信息：标签页标题+图标
st.set_page_config(page_title="简易音乐播放器", page_icon="🎵")
# 设置网页主标题
st.title("🎵 简易音乐播放器") 

# 初始化播放索引：用session_state保存，切换/刷新页面不重置
# 如果内存中没有music_ind，就初始化为0（默认播放第一首）
if 'music_ind' not in st.session_state:
    st.session_state['music_ind'] = 0

# 音乐列表：存储每首歌的音频链接、标题、歌手、时长、封面链接
music_list = [
    {
        "audio_url": "https://music.163.com/song/media/outer/url?id=2653714443.mp3",  # 音频播放链接
        "title": "晴天",          # 歌曲名
        "artist": "GYBeat",       # 歌手名
        "duration": "4:28",       # 歌曲时长
        "cover": "http://p1.music.126.net/-79-XFhWolhMzGESC8ifkg==/109951170218252280.jpg?param=130y130"  # 封面图链接
    },
    {
        "audio_url": "https://music.163.com/song/media/outer/url?id=3327141886.mp3",
        "title": "大东北我的家乡",
        "artist": "袁娅维",
        "duration": "4:35",
        "cover": "http://p2.music.126.net/EDhgL1S2DLGVE_5cjU-hfQ==/109951172410328709.jpg?param=130y130"
    },
    {
        "audio_url": "https://music.163.com/song/media/outer/url?id=2161991028.mp3",
        "title": "江南雪",
        "artist": "礼越",
        "duration": "3:56",
        "cover": "http://p2.music.126.net/RFbUrR2x2JEMB0WGYvwVQg==/109951169642392307.jpg?param=130y130"
    }
]

# 切换音乐的函数：根据方向（上一首/下一首）更新播放索引
# direction参数：prev=上一首，next=下一首
def switch_music(direction):
    if direction == "prev":
        # 上一首：索引-1，取模实现循环（第一首切上一首到最后一首）
        st.session_state['music_ind'] = (st.session_state['music_ind'] - 1) % len(music_list)
    else:
        # 下一首：索引+1，取模实现循环（最后一首切下一首到第一首）
        st.session_state['music_ind'] = (st.session_state['music_ind'] + 1) % len(music_list)

# 布局：分两列显示（左列封面，右列歌曲信息）
col1, col2 = st.columns([1, 2])
with col1:
    # 显示当前播放歌曲的封面图，宽度150px，添加"专辑封面"说明
    st.image(
        music_list[st.session_state["music_ind"]]["cover"],
        caption="专辑封面",
        width=150
    )

with col2:
    # 显示当前歌曲的标题、歌手、时长
    st.subheader(music_list[st.session_state["music_ind"]]["title"])  # 歌曲标题（加粗）
    st.write(f"歌手: {music_list[st.session_state['music_ind']]['artist']}")  # 歌手名
    st.write(f"时长: {music_list[st.session_state['music_ind']]['duration']}")  # 歌曲时长

# 布局：分两列放切换按钮（上一首/下一首）
btn_col1, btn_col2 = st.columns(2)
with btn_col1:
    # 上一首按钮：点击触发switch_music函数，传参数"prev"，按钮宽度适配列宽
    st.button("◀️ 上一首", on_click=switch_music, args=("prev",), use_container_width=True)
with btn_col2:
    # 下一首按钮：点击触发switch_music函数，传参数"next"
    st.button("▶️ 下一首", on_click=switch_music, args=("next",), use_container_width=True)

# 音频播放控件：加载当前歌曲的音频链接，格式为mp3，从0秒开始播放
st.audio(
    music_list[st.session_state["music_ind"]]["audio_url"],
    format="audio/mp3",
    start_time=0
)
