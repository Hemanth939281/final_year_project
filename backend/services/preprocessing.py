import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(file_path):
    df = pd.read_excel(file_path)

    # Replace BDL with NaN
    df = df.replace("BDL", np.nan)

    # Convert all columns to numeric
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Fill missing values with mean
    df = df.fillna(df.mean())

    # Select required features
    df_selected = df[
        ["PH_MIN", "PH_MAX", "DO_MIN", "DO_MAX", "Temp_MIN", "Temp_MAX"]
    ]

    # Feature engineering
    df_selected["PH_AVG"] = (df_selected["PH_MIN"] + df_selected["PH_MAX"]) / 2
    df_selected["DO_AVG"] = (df_selected["DO_MIN"] + df_selected["DO_MAX"]) / 2
    df_selected["TEMP_AVG"] = (df_selected["Temp_MIN"] + df_selected["Temp_MAX"]) / 2

    df_final = df_selected[["PH_AVG", "DO_AVG", "TEMP_AVG"]]

    # Scaling
    scaler = MinMaxScaler()
    df_scaled = pd.DataFrame(
        scaler.fit_transform(df_final),
        columns=df_final.columns
    )

    return df_scaled
