# NOTE:
# This file is the original Streamlit prototype.
# Not used in production. Kept for reference.

import streamlit as st
import pandas as pd
import plotly.express as px

from preprocessing import preprocess_data
from classical_model import run_classical_models
from quantum_model import run_quantum_model


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Hybrid Quantum–Classical Anomaly Dashboard",
    layout="wide"
)

SAMPLE_SIZE = 100   # SAME subset for all models

st.title("🌍 Hybrid Quantum–Classical Anomaly Detection Dashboard")
st.caption("Classical ML + Quantum Feature Encoding for Environmental Data")

# -------------------------------------------------
# SESSION STATE INITIALIZATION
# -------------------------------------------------
if "df_scaled" not in st.session_state:
    st.session_state.df_scaled = None

if "classical_results" not in st.session_state:
    st.session_state.classical_results = None

if "q_labels" not in st.session_state:
    st.session_state.q_labels = None

if "q_scores" not in st.session_state:
    st.session_state.q_scores = None

# -------------------------------------------------
# DATASET UPLOAD
# -------------------------------------------------
st.subheader("📂 Upload Dataset")

uploaded_file = st.file_uploader("Upload Dataset (.xlsx)", type=["xlsx"])

if uploaded_file:
    with open("temp.xlsx", "wb") as f:
        f.write(uploaded_file.getbuffer())

    df_full = preprocess_data("temp.xlsx")

    # SAME subset for fair comparison
    st.session_state.df_scaled = df_full.iloc[:SAMPLE_SIZE]

    st.success(f"Dataset preprocessed (first {SAMPLE_SIZE} samples used)")
    st.info(f"Current Dataset: {uploaded_file.name}")

    st.subheader("🔧 Preprocessed Data (Subset)")
    st.dataframe(st.session_state.df_scaled.head())

# -------------------------------------------------
# QUANTUM ENCODING SELECTION  ⭐ PANEL SUGGESTION
# -------------------------------------------------
st.subheader("⚛️ Quantum Feature Encoding")

encoding_type = st.selectbox(
    "Select Encoding Technique",
    ["ZZ", "Z", "PAULI"]
)

st.caption(
    "ZZ → entanglement-based | "
    "Z → simple phase encoding | "
    "PAULI → richer non-linear encoding"
)

# -------------------------------------------------
# RUN CLASSICAL MODELS
# -------------------------------------------------
if st.session_state.df_scaled is not None:
    if st.button("Run Classical Models (Isolation Forest + LOF)"):
        st.session_state.classical_results = run_classical_models(
            st.session_state.df_scaled
        )
        st.success("Classical models executed on same subset")

# -------------------------------------------------
# RUN QUANTUM MODEL
# -------------------------------------------------
if st.session_state.df_scaled is not None:
    if st.button("Run Quantum Model"):
        q_labels, q_scores = run_quantum_model(
            st.session_state.df_scaled,
            sample_size=SAMPLE_SIZE,
            encoding=encoding_type
        )
        st.session_state.q_labels = q_labels
        st.session_state.q_scores = q_scores
        st.success(f"Quantum model executed using {encoding_type} encoding")

# -------------------------------------------------
# COMPARISON METRICS
# -------------------------------------------------
comparison = {}

if st.session_state.classical_results is not None:
    for model, labels in st.session_state.classical_results.items():
        comparison[model] = (labels == -1).sum()

if st.session_state.q_labels is not None:
    comparison[f"Quantum ({encoding_type})"] = (st.session_state.q_labels == -1).sum()

# -------------------------------------------------
# KPI SECTION
# -------------------------------------------------
st.subheader("🚦 System Health Overview")

col1, col2, col3 = st.columns(3)

total_points = len(st.session_state.df_scaled) if st.session_state.df_scaled is not None else 0
classical_anoms = comparison.get("Isolation Forest", 0)
quantum_anoms = list(comparison.values())[-1] if comparison else 0

risk = "LOW"
if quantum_anoms > classical_anoms and quantum_anoms > 0:
    risk = "HIGH"

col1.metric("Total Samples (Subset)", total_points)
col2.metric("Classical Anomalies", classical_anoms)
col3.metric("Risk Level", risk)

st.info(
    f"""
    ℹ️ **Fair Comparison**  
    All models are evaluated on the same {SAMPLE_SIZE}-sample subset.
    Quantum encoding used: **{encoding_type}FeatureMap**
    """
)

# -------------------------------------------------
# MODEL COMPARISON BAR CHART
# -------------------------------------------------
if comparison:
    st.subheader("📊 Model-wise Anomaly Comparison")

    fig_bar = px.bar(
        x=list(comparison.keys()),
        y=list(comparison.values()),
        labels={"x": "Model", "y": "Anomaly Count"},
        title="Classical vs Quantum Anomaly Detection",
        color=list(comparison.keys())
    )

    st.plotly_chart(fig_bar, use_container_width=True)

# -------------------------------------------------
# FEATURE SPACE SCATTER (QUANTUM VIEW)
# -------------------------------------------------
if st.session_state.df_scaled is not None and st.session_state.q_labels is not None:
    df_plot = st.session_state.df_scaled.copy()
    df_plot["Quantum"] = st.session_state.q_labels

    st.subheader("🔬 Feature Space Visualization (Quantum Anomalies)")

    fig_scatter = px.scatter(
        df_plot,
        x="PH_AVG",
        y="DO_AVG",
        color=df_plot["Quantum"].map({1: "Normal", -1: "Quantum Anomaly"}),
        title=f"Quantum Anomalies using {encoding_type} Encoding",
        hover_data=["TEMP_AVG"]
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

# -------------------------------------------------
# QUANTUM-ONLY INSIGHT
# -------------------------------------------------
if st.session_state.q_labels is not None and st.session_state.classical_results is not None:
    iso_labels = st.session_state.classical_results["Isolation Forest"]

    quantum_only = ((st.session_state.q_labels == -1) & (iso_labels == 1)).sum()

    st.markdown("### ⚛️ Quantum Advantage Insight")
    st.info(
        f"""
        **{quantum_only} data points** were detected as anomalies **only by the Quantum model**
        using **{encoding_type} encoding**.

        👉 Indicates higher sensitivity to subtle deviations  
        👉 Missed by classical distance-based models
        """
    )

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("---")
st.markdown(
"""
### 🧠 Interpretation
- Classical models detect coarse statistical anomalies  
- Quantum feature encoding projects data into Hilbert space  
- Quantum kernel + One-Class SVM detects subtle deviations  

✅ Improvements implemented based on panel feedback
"""
)
