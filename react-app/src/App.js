import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import CreateTree from './CreateTree';
import ResultPage from './ResultPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<CreateTree />} />
        <Route path="/result" element={<ResultPage />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </Router>
  );
}

export default App;
