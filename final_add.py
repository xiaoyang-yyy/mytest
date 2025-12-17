import streamlit as st
import pandas as pd
import plotly.express as px

def get_dataframe_from_excel():
    # 读取Excel数据，处理可能的文件不存在/工作表错误
    try:
        df = pd.read_excel(
            'supermarket_sales.xlsx',
            sheet_name='销售数据',
            skiprows=1,
            index_col='订单号'
        )
    except FileNotFoundError:
        st.error("未找到supermarket_sales.xlsx文件，请确认文件路径正确！")
        return pd.DataFrame()  # 返回空DataFrame避免后续报错
    except ValueError:
        st.error("未找到名为'销售数据'的工作表，请确认Excel文件结构！")
        return pd.DataFrame()
    
    # 处理时间列，生成小时数（兼容空值）
    if "时间" in df.columns:
        df['小时数'] = pd.to_datetime(df["时间"], format="%H:%M:%S", errors='coerce').dt.hour
    else:
        st.warning("Excel中未找到'时间'列，小时数图表将无法生成！")
        df['小时数'] = pd.Series(dtype='int64')  # 初始化空列
    
    return df

def add_sidebar_func(df):
    # 创建侧边栏筛选器
    with st.sidebar:
        st.header("请筛选数据：")
        
        # 处理列不存在/空值的情况
        city_unique = df["城市"].unique() if "城市" in df.columns else []
        city = st.multiselect(
            "请选择城市：",
            options=city_unique,
            default=city_unique
        )
        
        customer_type_unique = df["顾客类型"].unique() if "顾客类型" in df.columns else []
        customer_type = st.multiselect(
            "请选择顾客类型：",
            options=customer_type_unique,
            default=customer_type_unique
        )
        
        gender_unique = df["性别"].unique() if "性别" in df.columns else []
        gender = st.multiselect(
            "请选择性别：",
            options=gender_unique,
            default=gender_unique
        )
    
    # 筛选数据（兼容空列）
    if df.empty:
        return df
    
    # 构建筛选条件（避免列不存在报错）
    conditions = []
    if "城市" in df.columns and len(city) > 0:
        conditions.append("城市 == @city")
    if "顾客类型" in df.columns and len(customer_type) > 0:
        conditions.append("顾客类型 == @customer_type")
    if "性别" in df.columns and len(gender) > 0:
        conditions.append("性别 == @gender")
    
    # 拼接筛选条件
    if conditions:
        df_selection = df.query(" & ".join(conditions))
    else:
        df_selection = df.copy()
    
    return df_selection

def product_line_chart(df):
    # 按产品类型生成销售额条形图（兼容空数据）
    if df.empty or "产品类型" not in df.columns or "总价" not in df.columns:
        return px.bar(title="<b>按产品类型划分的销售额</b>")  # 返回空图表
    
    sales_by_product_line = df.groupby(by=["产品类型"])["总价"].sum().sort_values()
    
    fig_product_sales = px.bar(
        sales_by_product_line,
        x="总价",
        y=sales_by_product_line.index,
        orientation="h",
        title="<b>按产品类型划分的销售额</b>",
    )
    return fig_product_sales

def hour_chart(df):
    # 按小时数生成销售额条形图（兼容空数据）
    if df.empty or "小时数" not in df.columns or "总价" not in df.columns:
        return px.bar(title="<b>按小时数划分的销售额</b>")  # 返回空图表
    
    sales_by_hour = df.groupby(by=["小时数"])["总价"].sum()
    
    fig_hour_sales = px.bar(
        sales_by_hour,
        x=sales_by_hour.index,
        y="总价",
        title="<b>按小时数划分的销售额</b>",
    )
    return fig_hour_sales

def main_page_demo(df):
    """主界面函数（兼容空数据）- 仅保留“销售仪表板”标题"""
    # 仅保留“销售仪表板”标题，删除bar_chart:前缀
    st.title('📊销售仪表板')
    
    # 无数据时提示用户
    if df.empty:
        st.warning("当前筛选条件下无数据，请调整筛选条件或检查数据源！")
        return
    
    # 创建关键指标列
    left_key_col, middle_key_col, right_key_col = st.columns(3)
    
    # 计算关键指标（兼容空列）
    total_sales = int(df["总价"].sum()) if "总价" in df.columns else 0
    average_rating = round(df["评分"].mean(), 1) if ("评分" in df.columns and not df["评分"].isna().all()) else 0.0
    star_rating_string = ":star:" * int(round(average_rating, 0)) if pd.notna(average_rating) else ""
    average_sale_by_transaction = round(df["总价"].mean(), 2) if "总价" in df.columns else 0.0

    # 展示关键指标
    with left_key_col:
        st.subheader("🏅总销售额：")
        st.subheader(f"RMB ¥ {total_sales:,}")

    with middle_key_col:
        st.subheader("🏝顾客评分的平均值：")
        st.subheader(f"{average_rating} {star_rating_string}")

    with right_key_col:
        st.subheader("🥓每单的平均销售额：")
        st.subheader(f"RMB ¥ {average_sale_by_transaction}")

    st.divider()  # 水平分割线

    # 创建图表列
    left_chart_col, right_chart_col = st.columns(2)

    with left_chart_col:
        hour_fig = hour_chart(df)
        st.plotly_chart(hour_fig, use_container_width=True)

    with right_chart_col:
        product_fig = product_line_chart(df)
        st.plotly_chart(product_fig, use_container_width=True)

def run_app():
    """启动应用（主函数）"""
    # 页面配置
    st.set_page_config(
        page_title="销售仪表板",  # 页面标签也仅保留“销售仪表板”
        page_icon=":bar_chart:",
        layout="wide"
    )
    
    # 读取数据
    sale_df = get_dataframe_from_excel()
    
    # 侧边栏筛选
    df_selection = add_sidebar_func(sale_df)
    
    # 渲染主页面
    main_page_demo(df_selection)

# 程序入口
if __name__ == "__main__":
    run_app()
