import { useState } from "react";
import axios from "axios";

function App() {

  const [result, setResult] = useState(null);

  const testPrediction = async () => {

    const payload = {
      features: Array(78).fill(0)
    };

    const response = await axios.post(
      "http://127.0.0.1:8000/predict",
      payload
    );

    setResult(response.data);
  };

  const getRiskColor = (risk) => {

    switch (risk) {
      case "LOW":
        return "text-green-500";

      case "MEDIUM":
        return "text-yellow-500";

      case "HIGH":
        return "text-orange-500";

      case "CRITICAL":
        return "text-red-500";

      default:
        return "text-white";
    }
  };

  return (
    <div className="min-h-screen bg-black text-white p-10">

      <h1 className="text-4xl font-bold mb-2">
        CyberSentinel-AI
      </h1>

      <p className="text-gray-400 mb-8">
        AI-Powered Cyber Threat Intelligence Platform
      </p>

      <button
        onClick={testPrediction}
        className="bg-blue-600 px-6 py-3 rounded-lg hover:bg-blue-700"
      >
        Run Threat Analysis
      </button>

      {result && (

        <div className="grid grid-cols-2 gap-6 mt-10">

          <div className="bg-gray-900 p-6 rounded-xl">
            <h3 className="text-gray-400">
              Attack Type
            </h3>

            <p className="text-2xl font-bold">
              {result.attack_type}
            </p>
          </div>

          <div className="bg-gray-900 p-6 rounded-xl">
            <h3 className="text-gray-400">
              Confidence
            </h3>

            <p className="text-2xl font-bold">
              {(result.confidence * 100).toFixed(2)}%
            </p>
          </div>

          <div className="bg-gray-900 p-6 rounded-xl">
            <h3 className="text-gray-400">
              Anomaly
            </h3>

            <p className="text-2xl font-bold">
              {String(result.anomaly)}
            </p>
          </div>

          <div className="bg-gray-900 p-6 rounded-xl">
            <h3 className="text-gray-400">
              Risk Level
            </h3>

            <p
              className={`text-2xl font-bold ${getRiskColor(
                result.risk_level
              )}`}
            >
              {result.risk_level}
            </p>
          </div>

        </div>

      )}

    </div>
  );
}

export default App;