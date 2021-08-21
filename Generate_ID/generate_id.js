// char_list array
const char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

// generate_id function
const generate_id = (l) => {
    var id = "";
    for (let i = 0; i < l; i++) id += char_list[Math.round(Math.random() * (char_list.length - 1))];
    return id;
}

// test case
console.log(generate_id(24));