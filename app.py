import streamlit as st
import psutil
import pandas as pd

# Title
st.title("💻 Machine Strength Comparison")

st.write("This dashboard shows system performance during backup")

# Get system data
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# Show metrics
st.subheader("📊 Live Performance")

st.metric("CPU Usage", f"{cpu}%")
st.metric("RAM Usage", f"{ram}%")
st.metric("Disk Usage", f"{disk}%")

# Graph
data = {
    "Component": ["CPU", "RAM", "Disk"],
    "Usage (%)": [cpu, ram, disk]
}

df = pd.DataFrame(data)
st.bar_chart(df.set_index("Component"))

# Performance Check
st.subheader("⚖️ Machine Strength Status")

if cpu < 50 and ram < 50:
    st.success("✅ Machine is Strong for Backup")
elif cpu < 80:
    st.warning("⚠️ Medium Performance Machine")
else:
    st.error("❌ System is Under Heavy Load")
