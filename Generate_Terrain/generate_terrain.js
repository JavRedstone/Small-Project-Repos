// generate_terrain function
const generate_terrain = (n, a) => {
    const terrain_values = [];
    for (let i = 0; i < n; i++) {
        terrain_values.push([]);
        for (let j = 0; j < n; j++) {
            terrain_values[i].push(Math.random());
            if (j > 0) {
                if (terrain_values[i][j-1] < terrain_values[i][j]){
                    terrain_values[i][j-1] += terrain_values[i][j] / a;
                    terrain_values[i][j] -= terrain_values[i][j] / a;
                }
                else {
                    terrain_values[i][j-1] -= terrain_values[i][j] / a;
                    terrain_values[i][j] += terrain_values[i][j] / a;
                }
            }
            if (i > 0) {
                if (terrain_values[i-1][j] < terrain_values[i][j]){
                    terrain_values[i-1][j] += terrain_values[i][j] / a;
                    terrain_values[i][j] -= terrain_values[i][j] / a;
                }
                else {
                    terrain_values[i-1][j] -= terrain_values[i][j] / a;
                    terrain_values[i][j] += terrain_values[i][j] / a;
                }
            }
        }
    }

    // visualization
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const terrain = document.createElement("terrain");
            const wrapper = document.getElementById("wrapper");
            wrapper.append(terrain);
            terrain.style.position = "absolute";
            terrain.style.left = i * 500/n + "px";
            terrain.style.top = j * 500/n + "px";
            terrain.style.width = 500/n + "px";
            terrain.style.height = 500/n + "px";
            terrain.style.backgroundColor = "black";
            terrain.style.opacity = terrain_values[i][j];
        }
    }
}

// test case
generate_terrain(50, 5);
