import axios from "axios";
import samples from "./samples.json";
import { useState, useEffect } from "react";

function App() {
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [ip, setIp] = useState("");
  const [intel, setIntel] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState("");
  const [generating, setGenerating] = useState(false);
  const [investigation, setInvestigation] = useState("");
  const [investigating, setInvestigating] = useState(false);
  const [mitreTactic, setMitreTactic] = useState("");
  const [mitreTechnique, setMitreTechnique] = useState("");
  const [analysis, setAnalysis] = useState("");
  const [analyzing, setAnalyzing] = useState(false);
  const [analysisData, setAnalysisData] = useState(null);
  const [explanation, setExplanation] = useState([]);
  const [explaining, setExplaining] = useState(false);
  const [alerts, setAlerts] = useState([]);

  const [selectedAttack, setSelectedAttack] = useState("BENIGN");

  useEffect(() => {
  const fetchAlerts = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/alerts"
      );

      setAlerts(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  fetchAlerts();
}, []);

  const loadAlerts = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/alerts"
      );

      setAlerts(response.data);

    } catch (error) {
      console.error(error);
    }
  };




  const explainPrediction = async () => {
    try {
      setExplaining(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/explain",
        {
          features: samples[selectedAttack]
        }
      );

      setExplanation(
        response.data.top_features
      );

    } catch (error) {
      console.error(error);
    } finally {
      setExplaining(false);
    }
  };

const clearOutputs = () => {
  setResult(null);
  setReport("");
  setInvestigation("");
  setMitreTactic("");
  setMitreTechnique("");
  setAnalysis("");
  setAnalysisData(null);
  setAnswer("");
  setQuestion("");
  setIp("");
  setExplanation([]);
};
  const runSample = async (attack) => {
    try {
      clearOutputs();
      setIntel(null);
      const response = await axios.post("http://127.0.0.1:8000/predict", {
        features: samples[attack],
      });
      setResult(response.data);
      await loadAlerts();
      setHistory((prev) => [response.data, ...prev.slice(0, 9)]);
    } catch (error) {
      console.error(error);
    }
  };

  const analyzeThreat = async () => {
    try {
      setAnalyzing(true);
      setAnalysis("");
      setAnalysisData(null);
      setInvestigation("");
      setReport("");

      const response = await axios.post("http://127.0.0.1:8000/analyze-threat", {
        attack_type: result?.attack_type || "BENIGN",
        risk_level: result?.risk_level || "LOW",
        ip: intel?.ip || "N/A",
      });

      setAnalysis(response.data.analysis);
      setAnalysisData(response.data);
    } catch (error) {
      console.error(error);
    } finally {
      setAnalyzing(false);
    }
  };

  const investigateThreat = async () => {
    try {
      setInvestigating(true);
      setInvestigation("");
      setMitreTactic("");
      setMitreTechnique("");

      const response = await axios.post("http://127.0.0.1:8000/investigate", {
        attack_type: result?.attack_type || "BENIGN",
        risk_level: result?.risk_level || "LOW",
        ip: intel?.ip || "N/A",
      });

      setMitreTactic(response.data.mitre_tactic);
      setMitreTechnique(response.data.mitre_technique);
      setInvestigation(response.data.investigation);
    } catch (error) {
      console.error(error);
    } finally {
      setInvestigating(false);
    }
  };

  const generateReport = async () => {
    try {
      setGenerating(true);
      const response = await axios.post("http://127.0.0.1:8000/generate-report", {
        attack_type: result?.attack_type || "Unknown",
        risk_level: result?.risk_level || "LOW",
        threat_score: intel?.risk_score || 0,
        ip: intel?.ip || "N/A",
      });
      setReport(response.data.report);
    } catch (error) {
      console.error(error);
    } finally {
      setGenerating(false);
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
      const response = await axios.post("http://127.0.0.1:8000/copilot", {
        question: question,
      });
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
      <h1 className="text-5xl font-bold mb-2">CyberSentinel-AI</h1>
      <p className="text-green-400 mb-4">Security Operations Dashboard</p>
      <p className="text-gray-400 mb-8">
        AI-Powered Cyber Threat Intelligence Platform
      </p>

      {/* System Status */}
      <div className="bg-gray-900 p-6 rounded-xl mb-8 w-full max-w-md">
        <h2 className="text-xl font-bold mb-4">System Status</h2>
        <p className="text-green-400">● Backend Online</p>
        <p className="text-green-400">● XGBoost Loaded</p>
        <p className="text-green-400">● Isolation Forest Loaded</p>
      </div>

      {/* ✅ Threat Simulation – Dropdown + Button */}
      <div className="bg-gray-900 p-6 rounded-xl mt-8">
        <h2 className="text-2xl font-bold mb-4">
          Attack Simulation Lab
        </h2>
        <p className="text-gray-400 mb-4">
          Simulate real CICIDS2017 attack samples
        </p>
        <div className="flex gap-3 flex-wrap">
          <select
            value={selectedAttack}
            onChange={(e) => setSelectedAttack(e.target.value)}
            className="bg-black border border-gray-700 p-3 rounded-lg text-white"
          >
            <option value="BENIGN">BENIGN</option>
            <option value="PortScan">PortScan</option>
            <option value="DDoS">DDoS</option>
            <option value="DoS">DoS</option>
            <option value="BruteForce">BruteForce</option>
            <option value="Bot">Bot</option>
            <option value="WebAttack">WebAttack</option>
          </select>
          <button
            onClick={() => runSample(selectedAttack)}
            className={`px-6 py-3 rounded-lg ${selectedAttack === "BENIGN"
              ? "bg-green-600 hover:bg-green-700"
              : "bg-red-600 hover:bg-red-700"
              }`}
          >
            Simulate Attack
          </button>
        </div>
        <p className="text-gray-400 mt-3">
          Selected Sample:
          <span className="text-white font-semibold ml-2">
            {selectedAttack}
          </span>
        </p>
      </div>

      {/* Threat Analysis Controls */}
      <div className="flex items-center flex-wrap gap-2 mt-8">

        <button
          onClick={generateReport}
          disabled={!result || !intel || generating}
          className="bg-red-600 px-6 py-3 rounded-lg hover:bg-red-700 disabled:opacity-50"
        >
          {generating ? "Generating..." : "Generate Incident Report"}
        </button>

        <button
          onClick={investigateThreat}
          disabled={!result || !intel || investigating}
          className="bg-orange-600 px-6 py-3 rounded-lg hover:bg-orange-700 disabled:opacity-50"
        >
          {investigating ? "Investigating..." : "Investigate Threat"}
        </button>

        <button
          onClick={analyzeThreat}
          disabled={!result || !intel || analyzing}
          className="bg-cyan-600 px-6 py-3 rounded-lg hover:bg-cyan-700 disabled:opacity-50"
        >
          {analyzing ? "Analyzing..." : "Analyze Threat"}
        </button>

        <button
          onClick={explainPrediction}
          disabled={!result || explaining}
          className="bg-purple-600 px-6 py-3 rounded-lg hover:bg-purple-700 disabled:opacity-50"
        >
          {explaining ? "Explaining..." : "Explain Prediction"}
        </button>

      </div>

      {/* Loading indicator for SOC Analysis */}
      {analyzing && (
        <div className="mt-8 text-cyan-400 animate-pulse">
          🔍 Generating SOC Analysis... Please wait.
        </div>
      )}

      {/* Prediction Results */}
      {result && (
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mt-10">
          <div className="bg-gray-900 p-6 rounded-xl">
            <h3 className="text-gray-400">Attack Type</h3>
            <p className="text-2xl font-bold">{result.attack_type}</p>
          </div>
          <div className="bg-gray-900 p-6 rounded-xl">
            <h3 className="text-gray-400">Confidence</h3>
            <p className="text-2xl font-bold">
              {(result.confidence * 100).toFixed(2)}%
            </p>
          </div>
          <div className="bg-gray-900 p-6 rounded-xl">
            <h3 className="text-gray-400">Anomaly</h3>
            <p className="text-2xl font-bold">{String(result.anomaly)}</p>
          </div>
          <div className="bg-gray-900 p-6 rounded-xl">
            <h3 className="text-gray-400">Risk Level</h3>
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

      {/* Incident Report Output */}
      {report && (
        <div className="bg-gray-900 p-6 rounded-xl mt-8">
          <h2 className="text-2xl font-bold mb-4 text-red-400">
            AI Generated Incident Report
          </h2>
          <pre className="whitespace-pre-wrap text-gray-300">{report}</pre>
        </div>
      )}

      {/* Investigation Output */}
      {investigation && (
        <div className="bg-gray-900 p-6 rounded-xl mt-8">
          <h2 className="text-2xl font-bold mb-4 text-orange-400">
            AI Threat Investigation
          </h2>
          <div className="mb-4">
            <p>
              <strong>MITRE Tactic:</strong> {mitreTactic}
            </p>
            <p>
              <strong>MITRE Technique:</strong> {mitreTechnique}
            </p>
          </div>
          <pre className="whitespace-pre-wrap text-gray-300">
            {investigation}
          </pre>
        </div>
      )}

      {/* SOC Analyst Report Output */}
      {analysis && (
        <div className="bg-gray-900 p-6 rounded-xl mt-8">
          <h2 className="text-2xl font-bold mb-4 text-cyan-400">
            SOC Analyst Report
          </h2>
          {analysisData && (
            <div className="mb-4">
              <p>
                <strong>MITRE Tactic:</strong> {analysisData.mitre_tactic}
              </p>
              <p>
                <strong>MITRE Technique:</strong>{" "}
                {analysisData.mitre_technique}
              </p>
            </div>
          )}
          <pre className="whitespace-pre-wrap text-gray-300">{analysis}</pre>
        </div>
      )}

      {/* SHAP / Explainable AI Panel */}
      {explanation.length > 0 && (
        <div className="bg-gray-900 p-6 rounded-xl mt-8">
          <h2 className="text-2xl font-bold mb-4 text-purple-400">
            Explainable AI Analysis
          </h2>

          <p className="text-gray-400 mb-4">
            Top features influencing the prediction
          </p>

          <div className="space-y-3">
            {explanation.map((item, index) => (
              <div
                key={index}
                className="flex justify-between bg-black p-3 rounded-lg"
              >
                <span>{index + 1}. {item.feature}</span>

                <span className="text-purple-400 font-bold">
                  {item.importance}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}

      {alerts.length > 0 && (
        <div className="bg-gray-900 p-6 rounded-xl mt-8">
          <h2 className="text-2xl font-bold mb-4 text-red-400">
            Live SOC Alert Feed
          </h2>

          <div className="space-y-3">
            {alerts.map((alert, index) => (
              <div
                key={index}
                className="bg-black p-3 rounded-lg flex justify-between"
              >
                <span>
                  {alert.attack_type}
                </span>

                <span
                  className={
                    alert.risk_level === "CRITICAL"
                      ? "text-red-500"
                      : alert.risk_level === "HIGH"
                        ? "text-orange-500"
                        : alert.risk_level === "MEDIUM"
                          ? "text-yellow-500"
                          : "text-green-500"
                  }
                >
                  {alert.risk_level}
                </span>

                <span className="text-gray-400">
                  {alert.timestamp}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
      {/* Threat History */}
      {history.length > 0 && (
        <div className="mt-10">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-2xl font-bold">
              Recent Threat Activity
            </h2>

            <button
              onClick={() => setHistory([])}
              className="bg-gray-700 px-3 py-2 rounded-lg hover:bg-gray-600"
            >
              Clear
            </button>
          </div>
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
        <h2 className="text-2xl font-bold mb-4">Threat Intelligence Lookup</h2>
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
          <h3 className="text-xl font-bold mb-4">Threat Intelligence Result</h3>
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
      <div className="mt-10 mb-20">
        <h2 className="text-2xl font-bold mb-4">AI Security Copilot</h2>
        <div className="flex gap-3 flex-wrap">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask the copilot about this threat..."
            className="bg-gray-900 p-3 rounded-lg text-white w-full max-w-xl"
          />
          <button
            onClick={askCopilot}
            disabled={loading}
            className="bg-green-600 px-5 py-3 rounded-lg hover:bg-green-700 disabled:opacity-50"
          >
            {loading ? "Thinking..." : "Ask"}
          </button>
        </div>
        {answer && (
          <div className="bg-gray-900 p-6 rounded-xl mt-6 w-full max-w-3xl">
            <p className="text-gray-300 whitespace-pre-wrap">{answer}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;