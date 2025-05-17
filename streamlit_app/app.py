import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_preprocessing import load_data, preprocess_data
from src.bug_predictor import train_model, predict_bug_probability
from src.visualization import plot_risk_heatmap

import streamlit as st
import pandas as pd

st.title("🐞 AutoBugPredictX – AI-Powered Bug Prediction for QA")

uploaded_file = st.file_uploader("Upload your test logs (CSV format)", type=["csv"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.success("✅ File uploaded successfully.")
else:
    st.info("📂 No file uploaded. Using sample dataset.")
    sample_csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_test_logs.csv')
    df = pd.read_csv(sample_csv_path)

st.write("### Uploaded Data Preview", df.head())

# Preprocessing
X, y = preprocess_data(df)

# Model training
model = train_model(X, y)

# Predictions
df['predicted_bug_probability'] = predict_bug_probability(model, X)

st.write("### Prediction Results", df[['module_name', 'predicted_bug_probability']])

# Visualization
st.write("### Risk Heatmap")
plot = plot_risk_heatmap(df)
st.pyplot(plot)

# Download option
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Predictions CSV",
    data=csv,
    file_name='bug_predictions.csv',
    mime='text/csv',
)
