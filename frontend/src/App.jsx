import { useState } from "react";
import axios from "axios";

function App() {
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [ip, setIp] = useState("");
  const [intel, setIntel] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const testPrediction = async () => {
    try {
      const payload = {
        features: Array(78).fill(0),
      };

      const response = await axios.post(
        "http://127.0.0.1:8000/predict",
        payload
      );

      setResult(response.data);

      setHistory((prev) => [
        response.data,
        ...prev.slice(0, 9),
      ]);
    } catch (error) {
      console.error(error);
    }
  };

  const lookupThreatIntel = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/threat-intel/${ip}`
      );

      setIntel(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const askCopilot = async () => {
    try {
      setLoading(true);
      const response = await axios.post(
        "http://127.0.0.1:8000/copilot",
        {
          question: question,
        }
      );

      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
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
    <div className="min-h-screen bg-black text-white p-10 max-w-7xl mx-auto">
      <h1 className="text-5xl font-bold mb-2">
        CyberSentinel-AI
      </h1>

      <p className="text-green-400 mb-4">
        Security Operations Dashboard
      </p>

      <p className="text-gray-400 mb-8">
        AI-Powered Cyber Threat Intelligence Platform
      </p>

      {/* System Status */}
      <div className="bg-gray-900 p-6 rounded-xl mb-8 w-full max-w-md">
        <h2 className="text-xl font-bold mb-4">
          System Status
        </h2>

        <p className="text-green-400">
          ● Backend Online
        </p>

        <p className="text-green-400">
          ● XGBoost Loaded
        </p>

        <p className="text-green-400">
          ● Isolation Forest Loaded
        </p>
      </div>

      {/* Threat Analysis Button */}
      <button
        onClick={testPrediction}
        className="bg-blue-600 px-6 py-3 rounded-lg hover:bg-blue-700"
      >
        Run Threat Analysis
      </button>

      {/* Prediction Results */}
      {result && (
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mt-10">
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

      {/* Threat History */}
      {history.length > 0 && (
        <div className="mt-10">
          <h2 className="text-2xl font-bold mb-4">
            Recent Threat Activity
          </h2>

          <div className="space-y-3">
            {history.map((item, index) => (
              <div
                key={index}
                className="bg-gray-900 p-4 rounded-lg flex justify-between"
              >
                <span>{item.attack_type}</span>

                <span className={getRiskColor(item.risk_level)}>
                  {item.risk_level}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Threat Intel Lookup */}
      <div className="mt-10">
        <h2 className="text-2xl font-bold mb-4">
          Threat Intelligence Lookup
        </h2>

        <div className="flex gap-3 flex-wrap">
          <input
            type="text"
            value={ip}
            onChange={(e) => setIp(e.target.value)}
            placeholder="Enter IP Address"
            className="bg-gray-900 p-3 rounded-lg text-white w-80"
          />

          <button
            onClick={lookupThreatIntel}
            className="bg-purple-600 px-5 py-3 rounded-lg hover:bg-purple-700"
          >
            Lookup
          </button>
        </div>
      </div>

      {/* Threat Intel Result */}
      {intel && (
        <div className="bg-gray-900 p-6 rounded-xl mt-6 w-full max-w-3xl">
          <h3 className="text-xl font-bold mb-4">
            Threat Intelligence Result
          </h3>

          <div className="space-y-2">
            <p>🌐 IP Address: {intel.ip}</p>

            <p>🌍 Country: {intel.country}</p>

            <p>📋 Reports: {intel.reports}</p>

            <p>🚨 Risk Score: {intel.risk_score}</p>

            <p
              className={`font-bold ${intel.threat_level === "HIGH"
                  ? "text-red-500"
                  : intel.threat_level === "MEDIUM"
                    ? "text-orange-500"
                    : "text-green-500"
                }`}
            >
              🚨 Threat Level: {intel.threat_level}
            </p>
          </div>
        </div>
      )}

      {/* AI Security Copilot */}
      <div className="mt-10">
        <h2 className="text-2xl font-bold mb-4">
          AI Security Copilot
        </h2>

        <div className="flex gap-3 flex-wrap">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask a security question..."
            className="bg-gray-900 p-3 rounded-lg text-white w-96"
          />

          <button
            onClick={askCopilot}
            className="bg-green-600 px-5 py-3 rounded-lg hover:bg-green-700"
          >
            {loading ? "Thinking..." : "Ask"}
          </button>
        </div>
      </div>

      {/* Copilot Response */}
      {answer && (
        <div className="bg-gray-900 p-6 rounded-xl mt-6 w-full max-w-3xl">
          <h3 className="text-xl font-bold mb-3">
            Copilot Response
          </h3>

          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;