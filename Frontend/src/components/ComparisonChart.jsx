import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

export default function ComparisonChart({ classical, quantum }) {
  if (!classical || !quantum) return null;

  const data = [
    {
      name: "Isolation Forest",
      anomalies: classical["Isolation Forest"],
    },
    {
      name: "LOF",
      anomalies: classical["LOF"],
    },
    {
      name: "Quantum",
      anomalies: quantum.anomalies,
    },
  ];

  return (
    <div className="mt-10 bg-white/5 p-6 rounded-2xl border border-white/10">
      <h2 className="text-xl font-semibold mb-4 text-cyan-400">
        📊 Anomaly Comparison
      </h2>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#444" />
          <XAxis dataKey="name" stroke="#aaa" />
          <YAxis stroke="#aaa" />
          <Tooltip />
          <Bar dataKey="anomalies" fill="#8b5cf6" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
