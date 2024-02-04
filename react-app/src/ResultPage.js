import React, { useState, useEffect } from 'react';
import './ResultPage.css';
import axios from 'axios';

function ResultPage() {
  const [result, setResult] = useState("");


  useEffect(() => {
    setResult(localStorage.getItem('predictionResult'))
  }, []);

  return (
    <div>
      <header className="App-header">
        <div>
          <h1>DOCTOR REPORT</h1>
          <div className="patient-info">
             <p>{result}</p>
          </div>
        </div>
      </header>
    </div>
  );
}

export default ResultPage;
