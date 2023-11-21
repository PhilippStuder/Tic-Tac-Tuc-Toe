import React from 'react';
import Cell from './Cell';

function Board({ cells, onClick }) {
  return (
    <div>
      {[...Array(4)].map((_, z) => (
        <div key={z}>
          {[...Array(4)].map((_, y) => (
            <div className="row" key={y}>
              {[...Array(4)].map((_, x) => (
                <Cell
                  key={x}
                  value={cells[x][y][z]}
                  onClick={(layerIndex) => onClick(x, y, layerIndex)}
                  layerIndex={z}
                />
              ))}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}

export default Board;
