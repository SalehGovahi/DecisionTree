import React, { useEffect, useState } from 'react';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import './chart.css'; // Import the CSS file with styles

function Chart() {
  const [isVisible, setIsVisible] = useState(false);
  const percentage = 75
  ;

  useEffect(() => {
    // Set a timeout to delay the appearance of the chart for a smoother animation
    const timeout = setTimeout(() => {
      setIsVisible(true);
    }, 500);

    // Clear the timeout on component unmount
    return () => clearTimeout(timeout);
  }, []);

  let pathColor = null;
  if(percentage>=0 && percentage<=45){
    pathColor = 'red';
  }
  else if(percentage>45 && percentage<75){
    pathColor = 'yellow';
  }
  else{pathColor = 'green'}
   

  return (
    <div className={`chart-container ${isVisible ? 'show-chart' : ''}`}>
      <h1 style={{ textAlign: 'center', color: '#333', fontFamily: 'Arial, sans-serif' }}>The accuracy of the tree</h1>
      <div style={{ position: '', width: '75%', height: '10%' }}>
        <CircularProgressbar
          value={isVisible ? percentage : 0} // Animate from 0 to the specified percentage
          text={`${isVisible ? percentage : 0}%`}
          styles={buildStyles({
            pathTransitionDuration: 1.5,
            textSize: '24px',
            pathColor: pathColor,
            textColor: '#4d4d4d',
            trailColor: '#eee',
            backgroundColor: '#fff',
          })}
        />
      </div>
      <p style={{ textAlign: 'center', fontSize: '14px', color: '#666' }}>The accuracy of the tree</p>
    </div>
  );
}

export default Chart;
