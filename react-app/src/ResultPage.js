import React, { useState, useEffect } from 'react';
import './ResultPage.css';
import axios from 'axios';

function ResultPage() {
  const [loading, setLoading] = useState(true);
  const [result, setResult] = useState("");
  const [showBoard, setShowBoard] = useState(false);

  useEffect(() => {
    axios.get('http://localhost:8080/getresult')
      .then(response => {
        setResult(response.data.result["result"]);
        console.log(response.data.result);
        setShowBoard(true);
        setLoading(false);
      })
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div className={`App ${showBoard ? 'show' : ''}`}>
      <header className="App-header">
        <div className={`doctor-board ${showBoard ? 'rotate' : ''}`}>
          <h1>DOCTOR REPORT</h1>
          <div className="patient-info">
            {loading ? <p>Loading...</p> : <p>{result}</p>}
          </div>
        </div>
      </header>
    </div>
  );
}

export default ResultPage;
