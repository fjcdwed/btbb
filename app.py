# 移动端优化
st.set_page_config(
    page_title="📱 BTC Trading Mobile",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 移动端CSS优化
st.markdown("""
<style>
    .main {
        padding: 0.5rem;
        max-width: 100%;
    }
    .stButton > button {
        width: 100%;
        height: 3.5rem;
        font-size: 1.3rem;
        font-weight: bold;
        border-radius: 15px;
        border: none;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .price-display {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
        padding: 1rem;
        border-radius: 15px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .signal-display {
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .signal-long {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
    }
    .signal-short {
        background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        color: white;
    }
    .signal-hold {
        background: linear-gradient(135deg, #6c757d 0%, #adb5bd 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# 主应用
st.title("📱 BTC Trading Mobile")
st.markdown("---")

# 模拟实时数据
price = 88603.01 + np.random.normal(0, 100)
change = np.random.normal(0, 1.5)
volume = np.random.randint(40000000000, 60000000000)
high_24h = price * 1.02
low_24h = price * 0.98

# 显示价格
st.markdown(f'''
<div class="price-display">
    ${price:,.2f}
    <div style="font-size: 1rem; margin-top: 0.5rem;">
        {change:+.2f}% (24h)
    </div>
</div>
''', unsafe_allow_html=True)

# 生成信号
signal_type = np.random.choice(["LONG", "SHORT", "HOLD"])
confidence = np.random.uniform(0.3, 1.0) if signal_type != "HOLD" else 0.0

# 显示信号
if signal_type == "LONG":
    st.markdown(f'''
    <div class="signal-display signal-long">
        <h2>🟢 做多信号 (LONG)</h2>
        <p>置信度: {confidence:.1%}</p >
        <p>建议: 考虑买入</p >
    </div>
    ''', unsafe_allow_html=True)
elif signal_type == "SHORT":
    st.markdown(f'''
    <div class="signal-display signal-short">
        <h2>🔴 做空信号 (SHORT)</h2>
        <p>置信度: {confidence:.1%}</p >
        <p>建议: 考虑卖出</p >
    </div>
    ''', unsafe_allow_html=True)
else:
    st.markdown(f'''
    <div class="signal-display signal-hold">
        <h2>⚪ 观望信号 (HOLD)</h2>
        <p>建议: 保持观望</p >
        <p>等待更明确的信号</p >
    </div>
    ''', unsafe_allow_html=True)

# 关键指标网格
col1, col2 = st.columns(2)
with col1:
    st.markdown(f'''
    <div style="background: white; padding: 1rem; border-radius: 15px; margin: 0.5rem 0; box-shadow: 0 5px 15px rgba(0,0,0,0.1); text-align: center;">
        <div style="font-size: 1.8rem; font-weight: bold; color: #2c3e50;">${high_24h:,.0f}</div>
        <div style="font-size: 0.9rem; color: #7f8c8d; margin-top: 0.5rem;">24小时最高</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown(f'''
    <div style="background: white; padding: 1rem; border-radius: 15px; margin: 0.5rem 0; box-shadow: 0 5px 15px rgba(0,0,0,0.1); text-align: center;">
        <div style="font-size: 1.8rem; font-weight: bold; color: #2c3e50;">{volume/1e9:.1f}B</div>
        <div style="font-size: 0.9rem; color: #7f8c8d; margin-top: 0.5rem;">成交量</div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <div style="background: white; padding: 1rem; border-radius: 15px; margin: 0.5rem 0; box-shadow: 0 5px 15px rgba(0,0,0,0.1); text-align: center;">
        <div style="font-size: 1.8rem; font-weight: bold; color: #2c3e50;">${low_24h:,.0f}</div>
        <div style="font-size: 0.9rem; color: #7f8c8d; margin-top: 0.5rem;">24小时最低</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown(f'''
    <div style="background: white; padding: 1rem; border-radius: 15px; margin: 0.5rem 0; box-shadow: 0 5px 15px rgba(0,0,0,0.1); text-align: center;">
        <div style="font-size: 1.8rem; font-weight: bold; color: #2c3e50;">{confidence:.1%}</div>
        <div style="font-size: 0.9rem; color: #7f8c8d; margin-top: 0.5rem;">信号置信度</div>
    </div>
    ''', unsafe_allow_html=True)

# 交易建议
with st.expander("💡 交易建议", expanded=False):
    if signal_type == "LONG":
        st.success("🟢 建议做多")
        st.write(f"入场价位: ${price*1.001:,.2f}")
        st.write(f"止损位: ${price*0.99:,.2f}")
        st.write(f"目标位: ${price*1.02:,.2f}")
    elif signal_type == "SHORT":
        st.error("🔴 建议做空")
        st.write(f"入场价位: ${price*0.999:,.2f}")
        st.write(f"止损位: ${price*1.01:,.2f}")
        st.write(f"目标位: ${price*0.98:,.2f}")
    else:
        st.warning("⚪ 建议观望")
        st.write("等待更明确的信号")

# 刷新按钮
if st.button("🔄 刷新数据", key="refresh_mobile", help="点击刷新最新数据"):
    st.experimental_rerun()

# 底部信息
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: #666; font-size: 0.9rem;'>
    <p>🔄 最后更新: {datetime.now().strftime('%H:%M:%S')}</p >
    <p>⚠️ 风险提示: 本系统仅供参考，不构成投资建议</p >
    <p>📱 专为移动端优化设计</p >
</div>
""", unsafe_allow_html=True)
```