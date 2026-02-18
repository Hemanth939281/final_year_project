// import { useState } from "react";
// import api from "../../api/api";

// export default function QuantumResults({ setData }) {
//   const [results, setResults] = useState(null);
//   const [loading, setLoading] = useState(false);

//   const runQuantum = async () => {
//     try {
//       setLoading(true);

//       const res = await api.post("/quantum/run", {
//         encoding: "ZZ",
//       });

//       setResults(res.data);
//       setData(res.data);
//     } catch (error) {
//       console.error("Quantum error:", error);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="w-full">
//       <h2 className="text-2xl font-semibold text-purple-400 mb-4">
//         ⚛️ Quantum Model
//       </h2>

//       <button
//         onClick={runQuantum}
//         disabled={loading}
//         className="w-full bg-purple-600 hover:bg-purple-500 
//                    disabled:bg-gray-600 
//                    transition duration-200 
//                    px-5 py-3 rounded-xl 
//                    font-semibold 
//                    text-white 
//                    shadow-md"
//       >
//         {loading ? "Running..." : "Run Quantum Model"}
//       </button>

//       {results && (
//         <div className="mt-6 space-y-3">
//           <div className="bg-black/40 p-4 rounded-xl border border-purple-500/20">
//             <p className="text-gray-300">
//               Encoding:
//               <span className="text-purple-400 font-bold ml-2">
//                 {results.encoding}
//               </span>
//             </p>
//           </div>

//           <div className="bg-black/40 p-4 rounded-xl border border-purple-500/20">
//             <p className="text-gray-300">
//               Total Samples:
//               <span className="text-green-400 font-bold ml-2">
//                 {results.scores.length}
//               </span>
//             </p>
//           </div>

//           <div className="bg-black/40 p-4 rounded-xl border border-purple-500/20">
//             <p className="text-gray-300">
//               Anomalies Detected:
//               <span className="text-red-500 font-bold ml-2 text-lg">
//                 {results.anomalies}
//               </span>
//             </p>
//           </div>
//         </div>
//       )}
//     </div>
//   );
// }
import { useState } from "react";
import api from "../../api/api";

export default function QuantumResults({ setData }) {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [encoding, setEncoding] = useState("ZZ");

  const runQuantum = async () => {
    try {
      setLoading(true);

      const res = await api.post("/quantum/run", {
        encoding: encoding,
      });

      setResults(res.data);
      setData(res.data);

    } catch (error) {
      console.error("Quantum error:", error);
      alert("Error running quantum model");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full flex flex-col space-y-4">
      
      <h2 className="text-2xl font-semibold text-purple-400">
        ⚛️ Quantum Model
      </h2>

      {/* Encoding Selector */}
      <select
        value={encoding}
        onChange={(e) => setEncoding(e.target.value)}
        className="w-full bg-slate-800 border border-purple-500/30 rounded-lg px-4 py-2 text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
      >
        <option value="ZZ">ZZ Feature Map</option>
        <option value="Z">Z Feature Map</option>
        <option value="PAULI">Pauli Feature Map</option>
      </select>

      {/* Run Button */}
      <button
        onClick={runQuantum}
        disabled={loading}
        className="w-full bg-purple-600 hover:bg-purple-700 transition-all duration-200 rounded-lg px-4 py-3 font-medium disabled:opacity-50"
      >
        {loading ? "Running Quantum..." : "Run Quantum Model"}
      </button>

      {/* Results */}
      {results && (
        <div className="mt-4 bg-slate-900/60 border border-purple-500/20 rounded-xl p-4 space-y-2">
          <p><strong>Encoding:</strong> {results.encoding}</p>
          <p><strong>Total Samples:</strong> {results.scores.length}</p>
          <p><strong>Anomalies Detected:</strong> {results.anomalies}</p>
        </div>
      )}
    </div>
  );
}
