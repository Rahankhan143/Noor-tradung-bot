import streamlit as st
import random
import time

st.set_page_config(page_title="ICT Trading Bot Dashboard", layout="wide")

st.title("🤖 প্রফেশনাল ICT & AI ট্রেডিং ড্যাশবোর্ড")
st.markdown("---")

# টপ মেট্রিক কার্ড (ব্যালেন্স ও প্রফিট)
col1, col2, col3, col4 = st.columns(4)
col1.metric("অ্যাকাউন্ট ব্যালেন্স", "$10,250.00", "+$250.00")
col2.metric("রানিং প্রফিট ($P/L)", "$45.50", "🟢 Active")
col3.metric("বর্তমান পেয়ার", "XAUUSDm (GOLD)", "M5 TF")
col4.metric("বটের অবস্থা", "RUNNING", "🟢 Connected")

st.markdown("### 📊 লাইভ মার্কেট ও সিগন্যাল স্ট্যাটাস")

# গ্রাফ সিমুলেশন
chart_data = [random.randint(1950, 1980) for _ in range(20)]
st.line_chart(chart_data)
