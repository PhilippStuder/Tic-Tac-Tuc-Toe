import React from 'react';

function Cell({ value, onClick, layerIndex }) {
  const color = value === 'X' ? '#fca311' : value === 'O' ? '#0c9271' : '#f2f2f2b6';

  return (
    <div className="cell" onClick={() => onClick(layerIndex)} style={{ backgroundColor: color }}>
      {value}
    </div>
  );
}


export default Cell;
