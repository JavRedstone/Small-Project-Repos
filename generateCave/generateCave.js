// Document Elements
const wrapper = document.getElementById("wrapper");

// Settings
const size = 50;
const blockSize = 10;
const numCaves = 15;
const depthCaves = 20;
const directions = [0, 1, 2, 3];

const FILLBLOCK = {
    filled: true,
    type: 0
};
const SEEDBLOCK = {
    filled: false,
    type: 1
};
const CAVEBLOCK = {
    filled: false,
    type: 2
};

// Variables
const grid = [];

// Helper Functions
const rand = function (n) {
    return ~~(Math.random() * n);
}

// Main Functions
const genGrid = function () {
    for (let i = 0; i < size; i++) {
        let row = [];
        for (let j = 0; j < size; j++) {
            row.push(FILLBLOCK);
        }
        grid.push(row);
    }
}
const randPoints = function () {
    for (let i = 0; i < numCaves; i++) {
        grid[rand(size)][rand(size)] = SEEDBLOCK;
    }
}
const pathCaves = function () {
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            if (grid[i][j].type == 1) {
                let pointer = {
                    i: i,
                    j: j
                };
                for (let k = 0; k < depthCaves; k++) {
                    switch (directions[rand(directions.length)]) {
                        case 1:
                            if (pointer.i + 1 < size) {
                                grid[pointer.i + 1][pointer.j] = CAVEBLOCK;
                                pointer.i++;
                            }
                            break;
                        case 2:
                            if (pointer.i - 1 > 0) {
                                grid[pointer.i - 1][pointer.j] = CAVEBLOCK;
                                pointer.i--;
                            }
                            break;
                        case 3:
                            if (pointer.j + 1 < size) {
                                grid[pointer.i][pointer.j + 1] = CAVEBLOCK;
                                pointer.j++;
                            }
                            break;
                        case 4:
                            if (pointer.j - 1 > 0) {
                                grid[pointer.i][pointer.j - 1] = CAVEBLOCK;
                                pointer.j--;
                            }
                            break;
                    }
                }
            }
        }
    }
}

const visGrid = function () {
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            let block = document.createElement("block");
            wrapper.append(block);
            block.style.position = "absolute";
            block.style.width = `${blockSize}px`;
            block.style.height = `${blockSize}px`;
            block.style.left = `${j * blockSize}px`;
            block.style.top = `${i * blockSize}px`;
            block.style.border = "1px solid black"
            block.style.background = grid[i][j].filled ? "radial-gradient(black, grey)" : "radial-gradient(orange, yellow)";
        }
    }
}

// Main
genGrid();
randPoints();
pathCaves();
visGrid();
