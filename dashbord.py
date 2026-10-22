import streamlit as st
import json
import os
import time

st.set_page_config(page_title="ICT Trading Bot Dashboard", layout="wide")

st.title("🤖 প্রফেশনাল ICT & AI ট্রেডিং ড্যাশবোর্ড (LIVE)")
st.markdown("---")

# JSON ফাইল থেকে ডেটা লোড করার ফাংশন
def load_bot_data():
    file_path = "bot_data.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    # ডিফোল্ট ডেটা (ফাইল না পাওয়া গেলে)
    return {
        "balance": "10,000.00",
        "running_pl": "0.00",
        "symbol": "XAUUSDm",
        "timeframe": "M5",
        "bot_status": "WAITING_FOR_BOT",
        "signal": "NO_SIGNAL",
        "zone": "SCANNING..."
    }

data = load_bot_data()

# টপ মেট্রিক কার্ড
col1, col2, col3, col4 = st.columns(4)
col1.metric("অ্যাকাউন্ট ব্যালেন্স", f"${data['balance']}")
col2.metric("রানিং প্রফিট ($P/L)", f"${data['running_pl']}", "🟢 Active" if float(data['running_pl']) >= 0 else "🔴 Loss")
col3.metric("বর্তমান পেয়ার", f"{data['symbol']} ({data['timeframe']})")
col4.metric("বটের অবস্থা", data['bot_status'], "🟢 Connected" if data['bot_status'] == "RUNNING" else "🟡 Idle")

st.markdown("---")

# লাইভ স্ট্যাটাস বক্স
col_a, col_b = st.columns(2)
with col_a:
    st.subheader("📌 বর্তমান ট্রেডিং জোন")
    st.info(f"Zone: {data['zone']}")

with col_b:
    st.subheader("🎯 সাম্প্রতিক সিগন্যাল")
    st.success(f"Signal: {data['signal']}")

# লাইভ অটো-রিফ্রেশ (প্রতি ৫ সেকেন্ড পর পর পেজ আপডেট হবে)
time.sleep(5)
st.rerun()
