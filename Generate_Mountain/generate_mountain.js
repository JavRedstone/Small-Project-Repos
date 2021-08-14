// generate road function
const generate_road = (n, a, b) => {
    const mountain_values = [];
    for (let i = 0; i < n; i++) {
        const prev_value = i > 0 ? mountain_values[i - 1 + a * i] : 0;
        const next_value = Math.random()/6 * (i % b == 0 ? -1 : 1) + prev_value;
        const difference = next_value - prev_value;
        for (let j = 0; j < a; j++) {
            mountain_values.push(difference/a * j + prev_value);
        }
        mountain_values.push(next_value);
    }

    // visualization
    for (let i = 0; i < mountain_values.length; i++) {
        const terrain = document.createElement("terrain");
        const wrapper = document.getElementById("wrapper");
        wrapper.append(terrain);
        terrain.style.position = "absolute";
        terrain.style.left = i * window.screen.width/(mountain_values.length) + "px";
        terrain.style.bottom = "0%";
        terrain.style.width = window.screen.width/(mountain_values.length) + "px";
        terrain.style.height = mountain_values[i] * 200  + "px";
        terrain.style.backgroundColor = "black";
    }
}

// test case
generate_road(100, 100, 3)