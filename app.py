import streamlit as st
import time
import random
import pandas as pd

# Page Config
st.set_page_config(page_title="Cloud Backup Dashboard", page_icon="☁️", layout="wide")

# Title
st.title("☁️ Cloud Backup System Dashboard")
st.markdown("### Secure | Fast | Intelligent Backup System")

# Sidebar
st.sidebar.title("⚙️ Control Panel")
option = st.sidebar.selectbox("Choose Operation", ["Home", "Backup Data", "Restore Data", "Logs"])

# Home Page
if option == "Home":
    st.header("📌 Project Overview")

    st.write("This system provides smart cloud backup with AI suggestions and security monitoring.")

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Files Backed Up", "120", "+10 today")
    col2.metric("Storage Used", "2.5 GB", "+500 MB")
    col3.metric("Status", "Active")

    # AI Suggestion
    st.subheader("🤖 AI Smart Suggestions")
    files = ["video.mp4", "data.csv", "project.zip", "image.png"]
    suggestion = random.choice(files)
    st.info(f"⚠️ Recommended to backup: {suggestion}")

    # Security Meter
    st.subheader("🔐 Security Level")
    security = st.slider("Security Level", 0, 100, 70)

    if security < 40:
        st.error("Low Security ❌")
    elif security < 70:
        st.warning("Medium Security ⚠️")
    else:
        st.success("High Security ✅")

    # Storage Chart
    st.subheader("📊 Storage Usage")
    data = pd.DataFrame({
        "Storage": ["Used", "Free"],
        "Value": [2.5, 5]
    })
    st.bar_chart(data.set_index("Storage"))

# Backup Section
elif option == "Backup Data":
    st.header("📤 Upload File to Backup")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file:
        st.success("File Selected: " + uploaded_file.name)

        if st.button("Start Backup"):
            status = st.empty()

            for i in range(100):
                time.sleep(0.03)
                status.text(f"Uploading... {i+1}%")

            st.success("✅ Backup Completed Securely!")

# Restore Section
elif option == "Restore Data":
    st.header("📥 Restore Your Files")

    file_name = st.text_input("Enter file name to restore")

    if st.button("Restore"):
        if file_name:
            st.info("Restoring file...")
            time.sleep(2)
            st.success("✅ File Restored Successfully!")
        else:
            st.warning("Please enter file name")

# Logs Section
elif option == "Logs":
    st.header("📜 System Logs")

    st.text_area("Logs",
    """[INFO] Backup started...
[INFO] File uploaded successfully
[INFO] Backup completed
[INFO] Restore request received""",
    height=200)
