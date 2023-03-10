import React from 'react';

// function Cell({ value, onClick }) {
//   const color = value === 'X' ? '#fca311' : value === 'O' ? '#0c4271' : '#edf2f4';

//   return (
//     <div className="cell" onClick={onClick} style={{ backgroundColor: color }}>
//       {value}
//     </div>
//   );
// }

function Cell({ value, onClick, layerIndex }) {
  const color = value === 'X' ? '#fca311' : value === 'O' ? '#0c4271' : '#edf2f4';

  return (
    <div className="cell" onClick={() => onClick(layerIndex)} style={{ backgroundColor: color }}>
      {value}
    </div>
  );
}


export default Cell;
