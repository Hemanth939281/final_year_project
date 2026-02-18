import Upload from "./components/Upload";
import ClassicalResults from "./components/ClassicalResults";
import QuantumResults from "./components/QuantumResults";
import { useState } from "react";
import ComparisonChart from "./components/ComparisonChart";

function App() {
  const [classicalData, setClassicalData] = useState(null);
  const [quantumData, setQuantumData] = useState(null);
  console.log("Classical:", classicalData);
  console.log("Quantum:", quantumData);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-black text-white">
      <div className="max-w-6xl mx-auto px-6 py-10">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold tracking-wide">
            ⚛️ Hybrid Quantum–Classical Dashboard
          </h1>
          <p className="text-gray-400 mt-3">
            Environmental Anomaly Detection using Classical ML and Quantum
            Feature Encoding
          </p>
        </div>

        {(classicalData || quantumData) && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
            <div
              className="bg-gradient-to-br from-indigo-600/20 to-indigo-800/20 
                    border border-indigo-500/30 rounded-2xl p-6 text-center shadow-xl"
            >
              <p className="text-gray-400 text-sm">Total Samples</p>
              <h2 className="text-3xl font-bold mt-2">
                {quantumData?.scores?.length || "-"}
              </h2>
            </div>

            <div
              className="bg-gradient-to-br from-blue-600/20 to-blue-800/20 
                    border border-blue-500/30 rounded-2xl p-6 text-center shadow-xl"
            >
              <p className="text-gray-400 text-sm">Classical Anomalies</p>
              <h2 className="text-3xl font-bold mt-2">
                {classicalData?.["Isolation Forest"] || "-"}
              </h2>
            </div>

            <div
              className="bg-gradient-to-br from-purple-600/20 to-purple-800/20 
                    border border-purple-500/30 rounded-2xl p-6 text-center shadow-xl"
            >
              <p className="text-gray-400 text-sm">Quantum Anomalies</p>
              <h2 className="text-3xl font-bold mt-2">
                {quantumData?.anomalies || "-"}
              </h2>
            </div>
          </div>
        )}

        {/* Upload Section */}
        <div className="w-full bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-6 shadow-xl mb-8 flex flex-col">
          <div className="w-full">
            <Upload />
          </div>
        </div>

        {/* Models Section */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="w-full bg-white/5 backdrop-blur-md border border-indigo-500/20 rounded-2xl p-6 shadow-xl flex flex-col">
            <div className="w-full">
              <ClassicalResults setData={setClassicalData} />
            </div>
          </div>

          <div className="w-full bg-white/5 backdrop-blur-md border border-purple-500/20 rounded-2xl p-6 shadow-xl flex flex-col">
            <div className="w-full">
              <QuantumResults setData={setQuantumData} />
            </div>
          </div>
        </div>
        {/* Charts Section */}
        <ComparisonChart classical={classicalData} quantum={quantumData} />
      </div>
    </div>
  );
}

export default App;
