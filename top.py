import streamlit as st
import pandas as pd
import streamlit as st
import base64

st.title("选项卡简单示例")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["个人简历生成器", "美食地图", "蛋糕甜度档案","音乐播放器","相册","视频播放器"])

with tab1:
    
        # 页面配置
    st.set_page_config(
        page_title="个人简历生成器",
        page_icon="📄",
        layout="wide"
    )

    # 清新风样式配置（删除HTML注释）
    st.markdown("""
        <style>
        .stApp { 
            background-color: #f8fafc; 
            color: #2d3748; 
            font-family: "Inter", "Microsoft YaHei", sans-serif;
        }
        .stTextInput>div>div>input, 
        .stTextArea>div>div>textarea, 
        .stSelectbox>div>div>select, 
        .stRadio>div>div { 
            background-color: #ffffff; 
            color: #2d3748; 
            border: 1px solid #e2e8f0; 
            border-radius: 6px;
            padding: 8px 12px;
        }
        .stRadio [role="radiogroup"] { gap: 16px; }
        .stSlider>div>div>div { color: #48bb78; }
        .stFileUploader>div>div { border: 1px dashed #94a3b8; border-radius: 6px; }
        .preview-card { 
            background-color: #ffffff; 
            padding: 30px; 
            border-radius: 12px; 
            border: 1px solid #e2e8f0;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        .avatar-container { 
            width: 140px; 
            height: 180px; 
            border: 2px solid #e6f7ef; 
            border-radius: 8px;
            display: flex; 
            align-items: center; 
            justify-content: center;
            overflow: hidden;
            background-color: #f0fdf4;
        }
        .avatar-img { 
            max-width: 100%; 
            max-height: 100%; 
            object-fit: cover;
            border-radius: 6px;
        }
        .preview-title {
            color: #16a34a;
            font-weight: 600;
            border-bottom: 2px solid #e6f7ef;
            padding-bottom: 12px;
            margin-bottom: 24px;
        }
        .info-label {
            color: #0f766e;
            font-weight: 500;
        }
        .info-value {
            color: #2d3748;
            margin-left: 4px;
        }
        .hr-line {
            border: none; 
            border-top: 1px solid #e6f7ef; 
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # 页面标题
    st.title("📄 个人简历生成器")

    # 列布局
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        name = st.text_input("姓名", key="name", placeholder="请输入你的姓名")
        address = st.text_input("意向职位", key="address", placeholder="请输入意向职位")
        phone = st.text_input("联系电话", key="phone", placeholder="请输入手机号")
        wechat = st.text_input("微信号", key="wechat", placeholder="请输入微信号")
        email = st.text_input("电子邮箱", key="email", placeholder="请输入邮箱地址")
        id_card = st.text_input("身份证号码", key="id_card", placeholder="选填")
        birthdate = st.date_input("出生日期", value=None, key="birthdate")
        
        gender = st.radio("性别", ["男", "女", "其他"], horizontal=True, key="gender")
        education = st.selectbox("学历", ["初中", "高中", "专科", "本科", "硕士", "博士"], key="education")
        exp_position = st.selectbox(
            "期望职位", 
            ["请选择选项", "前端开发", "后端开发", "产品经理", "UI设计"], 
            key="exp_position"
        )
        skills = st.multiselect(
            "技能（可多选）", 
            ["Python", "Java", "HTML/CSS", "JavaScript", "SQL"], 
            key="skills"
        )
        work_exp = st.radio("工作经验", ["0年", "1年", "2年以上"], horizontal=True, key="work_exp")
        exp_salary = st.slider(
            "期望薪资（元/月）", 
            min_value=5000, 
            max_value=50000, 
            value=[10000, 20000], 
            key="exp_salary"
        )
        intro = st.text_area(
            "个人简介", 
            placeholder="请介绍你的专业背景、职业优势、项目经验等", 
            height=120, 
            key="intro"
        )
        avatar = st.file_uploader(
            "上传个人照片", 
            type=["jpg", "jpeg", "png"], 
            help="建议尺寸：140×180px，限制200KB以内", 
            key="avatar"
        )

    with col2:
        st.subheader("👀 简历实时预览")
        # 处理照片
        avatar_html = '<span style="color:#64748b; font-size:14px;">点击上传照片</span>'
        if avatar:
            avatar_bytes = avatar.getvalue()
            avatar_base64 = base64.b64encode(avatar_bytes).decode("utf-8")
            avatar_html = f'<img src="data:image/{avatar.type.split("/")[-1]};base64,{avatar_base64}" class="avatar-img">'
        
        # 预览HTML（删除所有注释）
        preview_html = f"""
        <div class="preview-card" style="height: 100%;">
            <h3 class="preview-title">📋 个人简历</h3>
            <div style="display: flex; gap: 30px; margin-bottom: 28px; align-items: flex-start;">
                <div style="flex: 1;">
                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px;">
                        <div>
                            <span class="info-label">👤 姓名：</span>
                            <span class="info-value">{st.session_state.name or '未填写'}</span>
                        </div>
                        <div>
                            <span class="info-label">⚧️ 性别：</span>
                            <span class="info-value">{st.session_state.gender}</span>
                        </div>
                        <div>
                            <span class="info-label">🎂 出生日期：</span>
                            <span class="info-value">{st.session_state.birthdate or '未填写'}</span>
                        </div>
                        <div>
                            <span class="info-label">🆔 身份证号：</span>
                            <span class="info-value">{st.session_state.id_card or '未填写'}</span>
                        </div>
                        <div>
                            <span class="info-label">💼 意向职位：</span>
                            <span class="info-value">{st.session_state.address or '未填写'}</span>
                        </div>
                        <div>
                            <span class="info-label">📞 联系电话：</span>
                            <span class="info-value">{st.session_state.phone or '未填写'}</span>
                        </div>
                        <div>
                            <span class="info-label">💬 微信：</span>
                            <span class="info-value">{st.session_state.wechat or '未填写'}</span>
                        </div>
                        <div>
                            <span class="info-label">✉️ 邮箱：</span>
                            <span class="info-value">{st.session_state.email or '未填写'}</span>
                        </div>
                    </div>
                </div>
                <div style="flex-shrink: 0;">
                    <div class="avatar-container">
                        {avatar_html}
                    </div>
                    <p style="text-align: center; margin-top: 8px; color: #64748b; font-size: 12px;">
                        建议尺寸140×180px
                    </p>
                </div>
            </div>
            <hr class="hr-line">
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-bottom: 28px;">
                <div>
                    <p>
                        <span class="info-label">🎓 学历：</span>
                        <span class="info-value">{st.session_state.education}</span>
                    </p>
                    <p>
                        <span class="info-label">💪 工作经验：</span>
                        <span class="info-value">{st.session_state.work_exp}</span>
                    </p>
                    <p>
                        <span class="info-label">🎯 期望职位：</span>
                        <span class="info-value">{st.session_state.exp_position}</span>
                    </p>
                    <p>
                        <span class="info-label">💰 期望薪资：</span>
                        <span class="info-value">{st.session_state.exp_salary[0]}-{st.session_state.exp_salary[1]}元/月</span>
                    </p>
                </div>
                <div>
                    <p style="margin-bottom: 12px;">
                        <span class="info-label">🛠️ 技能掌握：</span>
                        <span class="info-value">{', '.join(st.session_state.skills) if st.session_state.skills else '未填写'}</span>
                    </p>
                </div>
            </div>
            <hr class="hr-line">
            <div>
                <h4 style="color: #0f766e; margin-bottom: 12px; font-weight: 600;">✍️ 个人简介</h4>
                <p style="line-height: 1.8; color: #475569; padding: 12px; background-color: #f0fdf4; border-radius: 6px;">
                    {st.session_state.intro or '暂无简介，可在左侧表单填写个人专业背景、职业优势等信息'}
                </p>
            </div>
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

    # 底部提示
    st.markdown("---")
    st.caption("🖼️ 照片限制200KB以内（JPG/PNG） | 🎨 清新风简历样式，填写信息实时预览")

with tab2:
    # 定义数据
    data = {
    '月份': ['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'],  
    '陶鲜生肉蟹煲（大唐天城店）': [200, 150, 180, 120, 350, 560, 150, 270, 190, 190, 180, 196],
    '黄蜀郎鸡公煲（相思湖北路）': [120, 160, 123, 168, 179, 138, 140, 128, 159, 128, 216, 289],  
    '海底捞火锅（安吉万达店）': [128, 156, 189, 212, 234, 257, 198, 221, 176, 205, 243, 169],
    '大熊熊螺蛳粉（朝阳店）': [145, 172, 201, 228, 193, 251, 184, 217, 162, 239, 196, 248],
    '苏格里岛自助海鲜烤肉(百盛步行街广场店)': [137, 165, 214, 188, 225, 209, 241, 179, 232, 195, 253, 158],
    
    }

    # 创建DataFrame并设置序号索引
    df = pd.DataFrame(data)
    df.index = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12], name='序号')
    df.ind = pd.Series([4.2, 4.5, 4.0, 4.7, 4.3, 4.4, 4.6, 4.1, 4.8, 4.2, 4.5, 4.0],name='评分')
    # 地图（补充门店名称，方便识别坐标对应门店）
    st.header("🍱门店位置分布")
    map_data = pd.DataFrame({
        "latitude": [22.845278, 22.848285, 22.869457, 22.811946, 22.815216],
        "longitude": [108.322789, 108.236054, 108.293125, 108.393064, 108.321190],
        "门店名称": [
            "陶鲜生肉蟹煲（大唐天城店）",
            "黄蜀郎鸡公煲（相思湖北路）",
            "海底捞火锅（安吉万达店）",
            "大熊熊螺蛳粉（朝阳店）",
            "苏格里岛自助海鲜烤肉(百盛步行街广场店)"
        ]
    })
    st.map(map_data, zoom=11)  # 调整zoom，让所有门店坐标都清晰显示

    # 展示数据表格（优化宽度）
    st.header("🍥门店数据")
    st.dataframe(df, use_container_width=True)

    st.subheader("🍨各门店月度数据趋势")
    st.line_chart(df, x="月份", y=df.columns[1:], use_container_width=True)  # 指定y轴为所有门店列，更清晰


    st.subheader("🍩各月度门店评分")
    # 通过x指定月份所在这一列为条形图的x轴
    st.bar_chart(df, x='月份')

    st.subheader("🍹用餐高峰时段")
    # 通过x指定月份所在这一列为面积图的x轴
    st.area_chart(df, x='月份')

with tab3:

    # 使用st.markdown插入HTML/CSS，unsafe_allow_html=True允许解析HTML
    st.markdown("""
        <style>
        /* 定位进度条元素：streamlit默认进度条的层级选择器 */
        .stProgress > div > div > div > div {
            background-color: #ff85a2; /* 粉色色值（可按需修改） */
        }
        /* 优化metric组件样式，增强视觉区分 */
        .stMetric {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 0.5rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # 页面基础配置
    st.set_page_config(
        page_title="蛋糕甜度档案",  # 浏览器标签页标题
        page_icon="🍰",  # 浏览器标签页图标（蛋糕emoji）
        layout="wide"  # 页面布局：宽屏模式（适配更多内容）
    )

    # 蛋糕基础信息字典：存储蛋糕核心属性，键值对结构便于调用
    cake_info = {
        "蛋糕名称": "云朵蛋糕",  # 蛋糕具体名称
        "档案ID": "CAKE2025001",  # 唯一标识ID（按年份+序号命名）
        "制作日期": "2025-06-10",  # 蛋糕制作时间
        "甜度状态": "适中",  # 甜度当前状态（适中/过甜/偏淡）
        "所属系列": "低糖系列",  # 蛋糕分类系列
        "烘焙师": "李师傅",  # 制作人员
        "蛋糕重量": 500,  # 新增：蛋糕重量（g），用于metric计算
        "目标甜度": 80  # 新增：目标甜度评分，用于metric对比
    }

    # 甜度核心指标列表：每个元素是元组（指标名称, 当前值, 调整幅度）
    sweetness_metrics = [
        ("蔗糖含量", 65, -5),  # 蔗糖占比65%，较之前降低5%
        ("果糖占比", 40, +2),  # 果糖占比40%，较之前提升2%
        ("整体甜度评分", 78, 0),  # 综合甜度78分，无调整
    ]

    # 甜度调整任务列表：存储需要执行的甜度优化任务
    sweetness_tasks = [
        ("降低蔗糖用量", "2025-06-08", "已完成", "简单"),  # 任务1：降蔗糖（已完成，难度简单）
        ("增加天然果糖", "2025-06-09", "进行中", "中等"),  # 任务2：加果糖（进行中，难度中等）
        ("口感甜度校准", "2025-06-11", "未完成", "困难")   # 任务3：校准口感（未完成，难度困难）
    ]

    # 甜度计算核心代码字符串：存储Python函数
    sweetness_code = '''def calculate_sweetness(sugar, fructose, weight):
        """计算蛋糕整体甜度评分（0-100分）"""
        # 甜度系数：蔗糖1.0（基准），果糖1.2（更甜）
        total_sweet = (sugar * 1.0) + (fructose * 1.2)
        # 按蛋糕重量归一化（以500g为基准，避免重量影响甜度判断）
        sweetness_score = (total_sweet / weight) * 100
        # 返回四舍五入到1位小数的评分（结果更简洁）
        return round(sweetness_score, 1)

    # 示例调用
    current_score = calculate_sweetness(sugar=65, fructose=40, weight=500)
    print(f"当前蛋糕甜度评分：{current_score}分")
    '''

    # Title（一级标题）
    st.title(f"🍰 {cake_info['蛋糕名称']} 甜度档案系统")

    # Header（二级标题，替代原subheader，更符合层级规范）
    st.header("📝 基础档案信息")

    # Markdown（富文本）：补充档案说明
    st.markdown("""
    该档案记录了低糖系列蛋糕的甜度核心数据，包含**基础信息、甜度指标、调整任务**等模块，
    所有数据均基于标准化烘焙流程采集，可作为甜度优化的核心参考依据。
    """)

    # 分4列展示基础信息，结合text（st.write）使用
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write(f"**档案ID**：{cake_info['档案ID']}")  # Text（基础文本）
    with col2:
        st.write(f"**制作日期**：{cake_info['制作日期']}")
    with col3:
        st.write(f"**甜度状态**：{cake_info['甜度状态']}")
    with col4:
        st.write(f"**烘焙师**：{cake_info['烘焙师']}")

    # Header：甜度核心指标
    st.header("🍬 甜度核心指标")

    # Metric组件（关键：展示核心数值+对比）
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        st.metric(
            label="当前甜度评分",
            value=f"{sweetness_metrics[2][1]}分",
            delta=f"{sweetness_metrics[2][1] - cake_info['目标甜度']}分",
            delta_color="inverse"
        )
    with metric_col2:
        st.metric(
            label="蛋糕重量",
            value=f"{cake_info['蛋糕重量']}g",
            delta="0g",
            help="以500g为基准重量，用于甜度归一化计算"
        )
    with metric_col3:
        st.metric(
            label="目标甜度评分",
            value=f"{cake_info['目标甜度']}分",
            delta="参考值",
        )

    # 详细甜度指标展示（结合progress和text）
    st.subheader("详细甜度占比")
    for name, value, adjust in sweetness_metrics:
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            st.write(f"**{name}**")  # Text
        with col2:
            st.progress(value/100, text=f"{value}%")  # Progress
        with col3:
            if adjust < 0:
                st.success(f"{adjust}%")  # Text（带状态色）
            elif adjust > 0:
                st.warning(f"+{adjust}%")
            else:
                st.info(f"{adjust}%")

    # Header：甜度调整任务
    st.header("📋 甜度调整任务清单")

    # Table组件（核心：结构化展示数据）
    st.table([["任务名称", "开始日期", "状态", "难度"]] + sweetness_tasks)

    # Header：核心计算逻辑
    st.header("💻 甜度计算核心代码")

    # Code组件（语法高亮+行号）
    st.code(sweetness_code, language="python", line_numbers=True)

    # 页脚（Markdown+Text）
    st.divider()
    st.markdown("""
    > **版权信息** © 2025 烘焙研发部  
    > **数据更新时间**：2025-06-10  
    > **系统说明**：本系统基于Streamlit构建，所有甜度指标均为实测数据
    """)
with tab4:

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

with tab5:
    
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

with tab6:
    

    # ===================== 页面基础配置与样式设置 =====================
    # 页面基础配置：修改标题和图标更贴合甜心格格主题
    st.set_page_config(page_title="甜心格格放映室", page_icon="🎀", layout="wide")

    # 注入CSS样式，将按钮设置为粉色，同时优化简介区域的样式
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
        /* 简介和人物介绍区域的容器样式 */
        .intro-container {
            background-color: #fdf2f8; /* 淡粉色背景，贴合主题 */
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

    # ===================== 页面标题与主题内容 =====================
    st.title('🎀 甜心格格第五部')

    # ---- 添加甜心格格简介和人物介绍 ----
    # 使用分栏布局，将简介和人物介绍并列显示（更紧凑）
    col1, col2 = st.columns(2)

    with col1:
        # 甜心格格作品简介
        st.markdown('<div class="intro-container">', unsafe_allow_html=True)
        st.subheader('📖 作品简介')
        st.write("""
        《甜心格格》是一部经典的国产原创3D动画，以古代宫廷为背景，讲述了甜丝丝格格与身边小伙伴们的欢乐日常。
        第五部延续了前作轻松幽默的风格，融入了更多成长、友谊与勇气的故事线，展现了格格们在宫廷中发生的一系列有趣又暖心的故事，
        既保留了传统国风元素，又传递了积极向上的价值观。
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # 主要人物介绍
        st.markdown('<div class="intro-container">', unsafe_allow_html=True)
        st.subheader('👑 主要人物')
        st.write("""
        - **甜丝丝**：主角，性格活泼开朗、天真烂漫，充满好奇心，常常闹出各种有趣的笑话，但心地善良、乐于助人。
        - **心柔柔**：丝丝的好友，出身书香门第，聪明伶俐、温柔懂事，偶尔会有点小较真，是丝丝的“小军师”。
        - **华伦**：外国公爵的儿子，聪明机智，擅长发明创造，经常用新奇的想法帮助小伙伴解决问题。
        - **武状元**：性格憨厚耿直，武功高强，十分讲义气，是小伙伴们的“保护神”。
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # ===================== 视频数据定义 =====================
    # 替换为Streamlit支持的视频格式（MP4/WebM/MOV等）
    video_arr = [
        {
            'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',  # 示例MP4链接
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

    # ===================== 会话状态初始化 =====================
    # 初始化session_state的索引（用于记录当前播放的集数）
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0  # 默认显示第1集

    # ===================== 视频播放区域 =====================
    # 显示当前集数标题
    st.subheader(video_arr[st.session_state['ind']]['title'])

    # 显示视频
    st.video(video_arr[st.session_state['ind']]['url'], autoplay=True)

    # ===================== 集数切换功能 =====================
    # 定义切换集数的函数
    def play(i):
        st.session_state['ind'] = int(i)

    # 横向排列按钮（一排最多5个）
    cols = st.columns(min(len(video_arr), 5))
    for i, col in enumerate(cols):
        with col:
            st.button(f'第{i + 1}集', use_container_width=True, on_click=play, args=(i,))
