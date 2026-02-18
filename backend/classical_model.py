from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

def run_classical_models(df_scaled):
    results = {}

    # 1️⃣ Isolation Forest
    iso = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )
    iso.fit(df_scaled)

    results["Isolation Forest"] = iso.predict(df_scaled)

    # 2️⃣ Local Outlier Factor (LOF)
    lof = LocalOutlierFactor(
        n_neighbors=20,
        contamination=0.05
    )

    results["LOF"] = lof.fit_predict(df_scaled)

    return results
