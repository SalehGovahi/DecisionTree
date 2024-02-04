import axios from 'axios';
import React, { useState } from 'react';
import './CreateTree.css'; // Import your CSS file
import { useNavigate } from 'react-router-dom';

function CreateTree() {
  const navigate = useNavigate(); // Use navigate here

  // Replace your state declarations with useState hooks
  const [featureNames, setFeatureNames] = useState([
    'HighBP',
    'HighChol',
    'CholCheck',
    'Smoker',
    'Stroke',
    'HeartDiseaseorAttack',
    'PhysActivity',
    'Fruits',
    'Veggies',
    'HvyAlcoholConsump',
    'AnyHealthcare',
    'NoDocbcCost',
    'GenHlth',
    'DiffWalk',
    'Sex',
    'Education',
    'Income',
  ]);
  
  const [inputs, setInputs] = useState(Array(17).fill(''));
  const [showChart, setShowChart] = useState(false);
  const [backgroundColor, setBackgroundColor] = useState('rgba(255, 255, 255, 0.2)');
  const [animationActive, setAnimationActive] = useState(false);

  const handleInputChange = (index, event) => {
    const newInputs = [...inputs];
    newInputs[index] = event.target.value;
    setInputs(newInputs);
  };

  const handleInputClick = () => {
    const generateRandomColor = () => {
      const randomValue = () => Math.floor(Math.random() * 256);
      const color = `rgba(${randomValue()}, ${randomValue()}, ${randomValue()}, 0.2)`;

      const isTooCloseToGreen =
        Math.abs(color.charCodeAt(8) - '76') < 30 &&
        Math.abs(color.charCodeAt(11) - '175') < 30 &&
        Math.abs(color.charCodeAt(14) - '80') < 30;

      return isTooCloseToGreen ? generateRandomColor() : color;
    };

    setBackgroundColor(generateRandomColor());
    setAnimationActive(false);
  };
  

  const handleSave = () => {
    setBackgroundColor('rgba(0, 128, 0, 0.7)');
    setAnimationActive(true);

    setTimeout(() => {
      setBackgroundColor('rgba(255, 255, 255, 0.2)');
      setAnimationActive(false);
    }, 5000);

    let dataToSave = {};
    featureNames.forEach((feature, index) => {
      dataToSave[feature] = inputs[index];
    });

    axios.post('http://localhost:8080/process', dataToSave)
    .then(response => {
      console.log(response.data); // This should log the response to your console
      // after getting the response in CreateTree component
      localStorage.setItem('predictionResult', response.data.result);
      if (response.data.result) {
        navigate('/result');
      }
    })
    .catch(error => console.error('Error sending data to Flask API', error));
}


  return (
    <div
      className={`create-tree-container ${animationActive ? 'animate-background' : ''}`}
      style={{ backgroundColor }}
    >
      <div className="header">
        <h1>Input Page</h1>
      </div>
      <div className="input-fields">
        {featureNames.map((featureName, index) => (
          <div key={index} className="input-field">
            <label>{`${featureName}:`}</label>
            <input
              type="text"
              value={inputs[index]}
              onChange={(event) => handleInputChange(index, event)}
              onClick={handleInputClick}
            />
          </div>
        ))}
      </div>
      <button onClick={handleSave}>Save</button>
    </div>
  );
}

export default CreateTree;