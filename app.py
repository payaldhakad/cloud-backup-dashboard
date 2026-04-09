import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Cloud Backup Dashboard", page_icon="☁️", layout="wide")

# Title
st.title("☁️ Cloud Backup System Dashboard")
st.markdown("### Secure | Fast | Reliable Data Backup System")

# Sidebar
st.sidebar.title("⚙️ Control Panel")
option = st.sidebar.selectbox("Choose Operation", ["Home", "Backup Data", "Restore Data", "Logs"])

# Home Page
if option == "Home":
    st.header("📌 Project Overview")
    st.write("""
    This system allows users to securely backup their data to the cloud.
    It ensures data safety, fast recovery, and real-time monitoring.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Files Backed Up", "120", "+10 today")
    col2.metric("Storage Used", "2.5 GB", "+500 MB")
    col3.metric("Status", "Active", "Running")

# Backup Section
elif option == "Backup Data":
    st.header("📤 Upload File to Backup")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file:
        st.success("File Selected: " + uploaded_file.name)

        if st.button("Start Backup"):
            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.02)
                progress.progress(i + 1)

            st.success("✅ Backup Completed Successfully!")

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
