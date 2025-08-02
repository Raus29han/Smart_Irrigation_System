import streamlit as st
import numpy as np
import pandas as pd
import joblib
from datetime import datetime
import os

# Constants
HISTORY_FILE = "prediction_history.csv"

# Page configuration
st.set_page_config(
    page_title="Smart Irrigation System",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load model
model = joblib.load("Farm_Irrigation_System.pkl")

# Title and description
st.markdown("""
<h1 style="color:#4CAF50;text-align:center;">🌿 Smart Irrigation System Dashboard</h1>
<p style="text-align:center;font-size:18px;">Control your farm's sprinklers with the power of Machine Learning.</p>
""", unsafe_allow_html=True)

# Sidebar input
st.sidebar.header("Sensor Input (Scaled: 0 to 1)")
sensor_values = []
with st.sidebar:
    for i in range(20):
        val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        sensor_values.append(val)

# Sensor input chart
sensor_df = pd.DataFrame({
    "Sensor": [f"Sensor {i}" for i in range(20)],
    "Value": sensor_values
})

with st.expander("📈 Visualize Sensor Input Data", expanded=True):
    col_plot1, col_plot2 = st.columns(2)
    with col_plot1:
        st.markdown("### 🔹 Line Chart of Sensor Values")
        st.line_chart(sensor_df.set_index("Sensor"))
    with col_plot2:
        st.markdown("### 🔸 Bar Chart of Sensor Values")
        st.bar_chart(sensor_df.set_index("Sensor"))

# Define logging function
def log_history(sensor_values, prediction, num_sprinklers):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = {
        "timestamp": timestamp,
        **{f"Sensor_{i}": sensor_values[i] for i in range(20)},
        **{f"Sprinkler_{i}": prediction[i] for i in range(num_sprinklers)}
    }
    df = pd.DataFrame([record])
    if os.path.exists(HISTORY_FILE):
        df.to_csv(HISTORY_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(HISTORY_FILE, index=False)

# Prediction
if st.sidebar.button("Predict Sprinkler Status"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    num_sprinklers = len(prediction)  # ✅ defined here after prediction

    st.success("✅ Prediction Completed!")

    # Log the prediction
    log_history(sensor_values, prediction, num_sprinklers)

    # Output UI
    st.markdown("## 🔧 Sprinkler Status by Parcel")
    col1, col2, col3 = st.columns(3)
    for i, status in enumerate(prediction):
        status_text = "💧 ON" if status == 1 else "❌ OFF"
        color = "#4CAF50" if status == 1 else "#F44336"
        box = f"""
        <div style="padding: 10px; border-radius: 10px; background-color:{color}; color:white; margin:5px;">
            <h4>Parcel {i}</h4>
            <p style="font-size:20px;">{status_text}</p>
        </div>
        """
        if i % 3 == 0:
            col1.markdown(box, unsafe_allow_html=True)
        elif i % 3 == 1:
            col2.markdown(box, unsafe_allow_html=True)
        else:
            col3.markdown(box, unsafe_allow_html=True)
else:
    st.info(" ⬅️ Adjust the sensors on the sidebar and click **Predict Sprinkler Status**.")

# Historical prediction chart
if os.path.exists(HISTORY_FILE):
    history_df = pd.read_csv(HISTORY_FILE)

    # Dynamically get sprinkler columns
    sprinkler_columns = [col for col in history_df.columns if col.startswith("Sprinkler_")]

    if sprinkler_columns:
        st.markdown("### 🕒 Historical Sprinkler Activation")
        selected_sprinkler = st.selectbox("Select Sprinkler", sprinkler_columns)
        time_series = history_df[["timestamp", selected_sprinkler]].copy()
        time_series["timestamp"] = pd.to_datetime(time_series["timestamp"])
        st.line_chart(data=time_series.set_index("timestamp"))
    else:
        st.warning("No sprinkler data found in the log.")


    with open(HISTORY_FILE, "rb") as f:
        st.download_button("📥 Download CSV History", f, file_name="irrigation_log.csv")

# Footer
st.markdown("""
<hr style="border: 1px solid #ccc;">
<p style="text-align:center;font-size:14px;">
    Developed by <b>Raushan Kumar</b> | Powered by <i>Streamlit & Scikit-learn</i>
</p>
""", unsafe_allow_html=True)
