import streamlit as st
import joblib
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Flood Prediction System",
    layout="centered"
)

# -----------------------------
# LOAD LIGHTWEIGHT MODEL
# -----------------------------
model = joblib.load("model_ui.joblib")

st.title("🌊 Flood Probability Prediction System")
st.write(
    "This system predicts flood probability using environmental and "
    "infrastructural risk indicators."
)

st.divider()

# -----------------------------
# USER INPUTS (KEY FEATURES)
# -----------------------------
st.subheader("Input Parameters (0 = Low, 10 = High)")

MonsoonIntensity = st.slider("Monsoon Intensity", 0, 10, 5)
TopographyDrainage = st.slider("Topography Drainage", 0, 10, 5)
RiverManagement = st.slider("River Management", 0, 10, 5)
Deforestation = st.slider("Deforestation", 0, 10, 5)
Urbanization = st.slider("Urbanization", 0, 10, 5)
ClimateChange = st.slider("Climate Change Impact", 0, 10, 5)
DrainageSystems = st.slider("Drainage Systems", 0, 10, 5)
PopulationScore = st.slider("Population Pressure", 0, 10, 5)

st.divider()

# -----------------------------
# BUILD FULL FEATURE SET
# (MATCH TRAINING FEATURES)
# -----------------------------
input_data = pd.DataFrame([{
    "MonsoonIntensity": MonsoonIntensity,
    "TopographyDrainage": TopographyDrainage,
    "RiverManagement": RiverManagement,
    "Deforestation": Deforestation,
    "Urbanization": Urbanization,
    "ClimateChange": ClimateChange,
    "DamsQuality": 5,
    "Siltation": 5,
    "AgriculturalPractices": 5,
    "Encroachments": 5,
    "IneffectiveDisasterPreparedness": 5,
    "DrainageSystems": DrainageSystems,
    "CoastalVulnerability": 5,
    "Landslides": 5,
    "Watersheds": 5,
    "DeterioratingInfrastructure": 5,
    "PopulationScore": PopulationScore,
    "WetlandLoss": 5,
    "InadequatePlanning": 5,
    "PoliticalFactors": 5
}])

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("Predict Flood Probability"):
    probability = model.predict(input_data)[0]

    # Clamp probability to [0, 1]
    probability = max(0.0, min(1.0, probability))

    st.success(f"🌧️ Flood Probability: **{probability:.2f}**")

    st.progress(probability)

    st.caption(
        "Probability range: 0 → Very Low Risk | 1 → Very High Risk"
    )
