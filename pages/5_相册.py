import streamlit as st

# 修改标签页的文字和图标
st.set_page_config(page_title="相册", page_icon="🍰")
st.title("我的相册")

# 把当前图片的索引存储在streamlit的内存中,下面的代码将当前索引存储在内存中的ind变量中
# 如果内存中没有ind,才需要设置为0,否则不要设置ind
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

images = [
    {
        "url": "https://qcloud.dpfile.com/pc/NUY8BJvOEluu1wbLD9ZcWbQvWyBa-TJS3mARmK6juhnd1ZgUQzmGiyWBZdMkONI8.jpg",
        "text": "hellokitty蛋糕"
    },
    {
        "url": "https://ww4.sinaimg.cn/mw690/006upAuggy1hsasfqpq7sj30j60pkwh3.jpg",
        "text": "提子小熊蛋糕"
    },
    {
        "url": "https://qcloud.dpfile.com/pc/2onXQ6LXzvulVVd83Gd6w96bpPZQZakPzKEJed-TjhWjHZ5OokmLsfkH9tmUtyYH.jpg",
        "text": "浪漫玫瑰蛋糕"
    }
]

# url:图片的地址 caption:图片注释介绍
st.image(images[st.session_state["ind"]]["url"], caption=images[st.session_state["ind"]]["text"])

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

# 分列容器 课本106页
c1, c2 = st.columns(2)
with c1:
    st.button("上一张", on_click=nextImg, use_container_width=True)
with c2:
# 按钮 课本73页
    st.button("下一张", on_click=nextImg, use_container_width=True)
