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

  return (
    <div style={{ padding: "2rem" }}>
      <h1>CyberSentinel-AI</h1>

      <button onClick={testPrediction}>
        Run Prediction
      </button>

      {result && (
        <div>
          <h3>Result</h3>

          <p>
            Attack Type:
            {result.attack_type}
          </p>

          <p>
            Confidence:
            {result.confidence}
          </p>

          <p>
            Anomaly:
            {String(result.anomaly)}
          </p>

          <p>
            Risk Level:
            {result.risk_level}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;