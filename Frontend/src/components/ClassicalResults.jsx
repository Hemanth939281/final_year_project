import api from "../../api/api";
import { useState } from "react";

export default function ClassicalResults({ setData }) {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const runClassical = async () => {
    setLoading(true);

    try {
      const res = await api.post("/classical/run");

      setResults(res.data);

      // 🔥 THIS WAS MISSING
      setData(res.data);

    } catch (err) {
      console.error("Classical error:", err);
      alert("Error running classical models");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 text-indigo-400">
        🧠 Classical Models
      </h2>

      <button
        onClick={runClassical}
        disabled={loading}
        className="w-full bg-indigo-600 hover:bg-indigo-700 transition-all duration-200 py-3 rounded-xl font-medium disabled:opacity-50"
      >
        {loading ? "Running..." : "Run Classical Models"}
      </button>

      {results && (
        <div className="mt-6 space-y-2 text-gray-300">
          <p>
            Isolation Forest Anomalies:{" "}
            <span className="font-bold text-white">
              {results["Isolation Forest"]}
            </span>
          </p>

          <p>
            LOF Anomalies:{" "}
            <span className="font-bold text-white">
              {results["LOF"]}
            </span>
          </p>
        </div>
      )}
    </div>
  );
}
