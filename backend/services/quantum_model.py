# from qiskit.circuit.library import ZZFeatureMap, ZFeatureMap, PauliFeatureMap
# from qiskit_machine_learning.kernels import FidelityQuantumKernel
# from sklearn.svm import OneClassSVM


# def get_feature_map(map_type, feature_dim):
#     if map_type == "Z":
#         return ZFeatureMap(
#             feature_dimension=feature_dim,
#             reps=2
#         )
#     elif map_type == "PAULI":
#         return PauliFeatureMap(
#             feature_dimension=feature_dim,
#             reps=2,
#             paulis=["X", "Y", "Z"]
#         )
#     else:  # DEFAULT = ZZ
#         return ZZFeatureMap(
#             feature_dimension=feature_dim,
#             reps=2,
#             entanglement="full"
#         )

# def run_quantum_model(df_scaled, sample_size=10, encoding="ZZ"):
#     X = df_scaled[["PH_AVG", "DO_AVG", "TEMP_AVG"]].values
#     X_small = X[:sample_size]

#     feature_map = get_feature_map(encoding, feature_dim=3)

#     quantum_kernel = FidelityQuantumKernel(
#     feature_map=feature_map
# )


#     q_svm = OneClassSVM(
#         kernel=quantum_kernel.evaluate,
#         nu=0.05
#     )

#     q_svm.fit(X_small)

#     q_labels = q_svm.predict(X_small)
#     q_scores = q_svm.decision_function(X_small)

#     return q_labels, q_scores
import numpy as np
from sklearn.svm import OneClassSVM

def run_quantum_model(df_scaled, encoding="ZZ"):
    X = df_scaled[["PH_AVG", "DO_AVG", "TEMP_AVG"]].values

    # Simulated quantum-like nonlinear encoding
    if encoding == "Z":
        X_transformed = np.sin(X * np.pi)
    elif encoding == "PAULI":
        X_transformed = np.cos(X * np.pi)
    else:  # ZZ
        X_transformed = np.sin(X * np.pi) * np.cos(X * np.pi)

    model = OneClassSVM(kernel="rbf", nu=0.05)
    model.fit(X_transformed)

    q_labels = model.predict(X_transformed)
    q_scores = model.decision_function(X_transformed)

    return q_labels, q_scores
