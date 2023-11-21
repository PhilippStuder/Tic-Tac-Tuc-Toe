import React from 'react';
import Board from './Board';

class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      cells: Array(4)
        .fill()
        .map(() =>
          Array(4)
            .fill()
            .map(() => Array(4).fill(null))
        ),
      xIsNext: true,
      winner: null,
    };
  }
  handleRefreshClick = () => {
    this.setState({ cells: Array(4)
      .fill()
      .map(() =>
        Array(4)
          .fill()
          .map(() => Array(4).fill(null))
      ),
      xIsNext: true,
      winner: null,
     });
  };

  handleClick(rowIndex, cellIndex, layerIndex) {
    
    if (this.state.winner || this.state.cells[rowIndex][cellIndex][layerIndex]) {
      return;
    }
    const cells = [...this.state.cells];
    const row = [...cells[rowIndex]];
    const cell = [...row[cellIndex]];
    cell[layerIndex] = this.state.xIsNext ? 'X' : 'O';
    row[cellIndex] = cell;
    cells[rowIndex] = row;
    const winner = calculateWinner(cells);
    this.setState({
      cells,
      xIsNext: !this.state.xIsNext,
      winner,
    });
    
  }

  render() {
    const winnerMessage = this.state.winner
      ? `Winner: ${this.state.winner}`
      : `Next player: ${this.state.xIsNext ? 'X' : 'O'}`;

    return (
      <div className="game">
        <div className="game-info">{winnerMessage}</div>
        <div className="game-board">
          <Board
            cells={this.state.cells}
            onClick={(rowIndex, cellIndex,layerIndex) =>
              this.handleClick(rowIndex, cellIndex,layerIndex)
            }
          />
        </div>
        <div>
        <button className="refresh-button" onClick={this.handleRefreshClick}>Refresh</button>
        </div>
        
      </div>
    );
  }
}

function calculateWinner(cells) {
  let x=0;
  let y=0;
  let z=0;
  for (let x = 0; x < 4; x++) {
    for (let y = 0; y < 4; y++) {
      
        if (
          cells[x][y][z] &&
          cells[x][y][z] === cells[x][y][z + 1] &&
          cells[x][y][z] === cells[x][y][z + 2] &&
          cells[x][y][z] === cells[x][y][z + 3]
        ) {
          return cells[x][y][z];
        }
    }
  }

  for (let x = 0; x < 4; x++) {
      for (let z = 0; z < 4; z++) {
        if (
          cells[x][y][z] &&
          cells[x][y][z] === cells[x][y + 1][z] &&
          cells[x][y][z] === cells[x][y + 2][z] &&
          cells[x][y][z] === cells[x][y + 3][z]
        ) {
          return cells[x][y][z];
        }
      }
  }

    for (let y = 0; y < 4; y++) {
      for (let z = 0; z < 4; z++) {
        if (
          cells[x][y][z] &&
          cells[x][y][z] === cells[x + 1][y][z] &&
          cells[x][y][z] === cells[x + 2][y][z] &&
          cells[x][y][z] === cells[x + 3][y][z]
        ) {
          return cells[x][y][z];
        }
      }
    }
  
  for (let i=0; i<4 ; i++ ) {
    if (
      cells[i][0][0]&&
      cells[i][0][0]===cells[i][1][1]&&
      cells[i][0][0]===cells[i][2][2]&&
      cells[i][0][0]===cells[i][3][3]) {
        return cells[i][0][0];
      }
    if (
      cells[i][0][3]&&
      cells[i][0][3]===cells[i][1][2]&&
      cells[i][0][3]===cells[i][2][1]&&
      cells[i][0][3]===cells[i][3][0]) {
        return cells[i][0][3];
      }
    if (
      cells[0][i][0]&&
      cells[0][i][0]===cells[1][i][1]&&
      cells[0][i][0]===cells[2][i][2]&&
      cells[0][i][0]===cells[3][i][3]) {
        return cells[0][i][0];
      }
    if (
      cells[0][i][3]&&
      cells[0][i][3]===cells[1][i][2]&&
      cells[0][i][3]===cells[2][i][1]&&
      cells[0][i][3]===cells[3][i][0]) {
        return cells[0][i][3];
      }
    if (
      cells[0][0][i] &&
      cells[0][0][i] === cells[1][1][i] &&
      cells[0][0][i] === cells[2][2][i] &&
      cells[0][0][i] === cells[3][3][i]
    ) {
      return cells[0][0][i];
    }
    if (
      cells[0][3][i] &&
      cells[0][3][i] === cells[1][2][i] &&
      cells[0][3][i] === cells[2][1][i] &&
      cells[0][3][i] === cells[3][0][i]
    ) {
      return cells[0][3][i];
    }
  }
  if (
    cells[0][0][0] &&
    cells[0][0][0] === cells[1][1][1] &&
    cells[0][0][0] === cells[2][2][2] &&
    cells[0][0][0] === cells[3][3][3]
  ) {
    return cells[0][0][0];
  }
  if (
    cells[0][0][3] &&
    cells[0][0][3] === cells[1][1][2] &&
    cells[0][0][3] === cells[2][2][1] &&
    cells[0][0][3] === cells[3][3][0]
  ) {
    return cells[0][0][3];
  }
  if (
    cells[0][3][0] &&
    cells[0][3][0] === cells[1][2][1] &&
    cells[0][3][0] === cells[2][1][2] &&
    cells[0][3][0] === cells[3][0][3]
  ) {
    return cells[0][3][0];
  }
  if (
    cells[0][3][3] &&
    cells[0][3][3] === cells[1][2][2] &&
    cells[0][3][3] === cells[2][1][1] &&
    cells[0][3][3] === cells[3][0][0]
  ) {
    return cells[0][3][3];
  }
  
    // Check tie
    for (let x = 0; x < 4; x++) {
      for (let y = 0; y < 4; y++) {
        for (let z = 0; z < 4; z++) {
          if (!cells[x][y][z]) {
            return null;
          }
        }
      }
    }
    return 'tie';
  }
  
  export default Game;
  
