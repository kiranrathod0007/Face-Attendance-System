import streamlit as st
import subprocess
import pandas as pd
import os
import sys
import time

st.set_page_config(page_title="Face Attendance System", layout="centered")

st.title("🧠 Face Recognition Attendance System")
st.markdown("Automatic Punch-In / Punch-Out using face recognition.")

if st.button("📷 Start Camera & Mark Attendance"):
    st.info("Camera started. Please face the camera...")

    subprocess.run([sys.executable, "recognize_face.py"])

    # Wait briefly for file to be written
    time.sleep(1)

    if os.path.exists("last_action.txt"):
        with open("last_action.txt", "r") as f:
            msg = f.read()

        if "Punch-In" in msg:
            st.success(f"✅ {msg}")
        else:
            st.info(f"🔵 {msg}")

        os.remove("last_action.txt")
    else:
        st.warning("No attendance was marked.")

st.divider()

if os.path.exists("attendance.csv"):
    st.subheader("📋 Attendance Records")
    df = pd.read_csv("attendance.csv")
    df = df.iloc[::-1]   # reverse rows
    st.dataframe(df)
else:
    st.warning("attendance.csv not found")
