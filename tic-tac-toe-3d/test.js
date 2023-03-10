var cells= [
    [  // Row 1
      [null, 1, null, null], // Column 1 (Layer 1, 2, 3, 4)
      [null, 1, null, null], // Column 2 (Layer 1, 2, 3, 4)
      [null, 1, null, null], // Column 3 (Layer 1, 2, 3, 4)
      [null, 1, null, null], // Column 4 (Layer 1, 2, 3, 4)
    ],
    [  // Row 2
      [null, null, null, null], // Column 1 (Layer 1, 2, 3, 4)
      [null, null, null, null], // Column 2 (Layer 1, 2, 3, 4)
      [null, null, null, null], // Column 3 (Layer 1, 2, 3, 4)
      [null, null, null, null], // Column 4 (Layer 1, 2, 3, 4)
    ],
    [  // Row 3
      [null, null, null, null], // Column 1 (Layer 1, 2, 3, 4)
      [null, null, null, null], // Column 2 (Layer 1, 2, 3, 4)
      [null, null, null, null], // Column 3 (Layer 1, 2, 3, 4)
      [null, null, null, null], // Column 4 (Layer 1, 2, 3, 4)
    ],
    [  // Row 4
      [null, null, null, null], // Column 1 (Layer 1, 2, 3, 4)
      [null, null, null, null], // Column 2 (Layer 1, 2, 3, 4)
      [null, null, null, null], // Column 3 (Layer 1, 2, 3, 4)
      [null, null, null, null], // Column 4 (Layer 1, 2, 3, 4)
    ]
  ];
  
console.log(null===null);
console.log(cells);


function calculateWinner(cells) {
    let z=0;
    let y=0;
    let x=0;
    // Check horizontal
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
  
    // Check vertical
      for (let y = 0; y < 2; y++) {
        
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
  
    // Check diagonal
    for (let x = 0; x < 2; x++) {
      for (let y = 0; y < 2; y++) {
        for (let z = 0; z < 2; z++) {
          if (
            cells[x][y][z] &&
            cells[x][y][z] === cells[x + 1][y + 1][z + 1] &&
            cells[x][y][z] === cells[x + 2][y + 2][z + 2]
            ) {
              return cells[x][y][z];
            }
            if (
              cells[x][y + 3][z] &&
              cells[x][y + 3][z] === cells[x + 1][y + 2][z + 1] &&
              cells[x][y + 3][z] === cells[x + 2][y + 1][z + 2] &&
              cells[x][y + 3][z] === cells[x + 3][y][z + 3]
            ) {
              return cells[x][y + 3][z];
            }
            if (
              cells[x + 3][y][z] &&
              cells[x + 3][y][z] === cells[x + 2][y + 1][z + 1] &&
              cells[x + 3][y][z] === cells[x + 1][y + 2][z + 2] &&
              cells[x + 3][y][z] === cells[x][y + 3][z + 3]
            ) {
              return cells[x + 3][y][z];
            }
            if (
              cells[x][y + 3][z + 3] &&
              cells[x][y + 3][z + 3] === cells[x + 1][y + 2][z + 2] &&
              cells[x][y + 3][z + 3] === cells[x + 2][y + 1][z + 1] &&
              cells[x][y + 3][z + 3] === cells[x + 3][y][z]
            ) {
              return cells[x][y + 3][z + 3];
            }
            if (
              cells[x + 3][y][z + 3] &&
              cells[x + 3][y][z + 3] === cells[x + 2][y + 1][z + 2] &&
              cells[x + 3][y][z + 3] === cells[x + 1][y + 2][z + 1] &&
              cells[x + 3][y][z + 3] === cells[x][y + 3][z]
            ) {
              return cells[x + 3][y][z + 3];
            }
          }
        }
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
    calculateWinner(cells);