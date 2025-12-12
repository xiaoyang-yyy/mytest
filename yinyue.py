import streamlit as st

# 设置网页标签标题和图标
st.set_page_config(page_title="简易音乐播放器", page_icon="🎵")
st.title("🎵 简易音乐播放器") 


# 初始化音乐索引（存到session_state，切换页面不重置）
if 'music_ind' not in st.session_state:
    st.session_state['music_ind'] = 0

# 音乐列表：包含封面、歌名、歌手、时长、音频链接
music_list = [
    {
        "audio_url": "https://music.163.com/song/media/outer/url?id=2653714443.mp3",  # 音频链接
        "title": "晴天",
        "artist": "GYBeat",
        "duration": "4:28",
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

# 切换音乐的函数
def switch_music(direction):
    """direction: 'prev'上一首 / 'next'下一首"""
    if direction == "prev":
        st.session_state['music_ind'] = (st.session_state['music_ind'] - 1) % len(music_list)
    else:
        st.session_state['music_ind'] = (st.session_state['music_ind'] + 1) % len(music_list)


# 布局：封面+音乐信息 横向排列
col1, col2 = st.columns([1, 2])
with col1:
    # 显示当前音乐封面
    st.image(
        music_list[st.session_state["music_ind"]]["cover"],
        caption="专辑封面",
        width=150
    )

with col2:
    # 显示音乐信息（歌名、歌手、时长）：把name改成title，singer改成artist
    st.subheader(music_list[st.session_state["music_ind"]]["title"])
    st.write(f"歌手: {music_list[st.session_state['music_ind']]['artist']}")
    st.write(f"时长: {music_list[st.session_state['music_ind']]['duration']}")


# 切换按钮（上一首/下一首）
btn_col1, btn_col2 = st.columns(2)
with btn_col1:
    st.button("◀️ 上一首", on_click=switch_music, args=("prev",), use_container_width=True)
with btn_col2:
    st.button("▶️ 下一首", on_click=switch_music, args=("next",), use_container_width=True)


# 音频播放控件
st.audio(
    music_list[st.session_state["music_ind"]]["audio_url"],
    format="audio/mp3",
    start_time=0
)
