import streamlit as st
import base64

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
