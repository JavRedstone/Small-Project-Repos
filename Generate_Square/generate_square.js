// list of colours printed
const char_list = ["⬜","🟨","🟧","🟥","🟪","🟦","🟩","🟫","⬛"];

// generate_square function
const generate_square = (n) => {
    var print_string = "";
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            print_string += char_list[Math.floor(Math.random()*char_list.length)];
        }
        print_string += "\n";
    }
    console.log(print_string);
}

// test case
generate_square(10);

// example output
/**
🟦🟧🟩🟪🟦🟧🟥🟪🟫🟧
🟫🟩🟪🟩🟩⬜🟫⬜🟩🟥
🟧🟧🟨⬜🟫🟪🟧🟦⬜🟧
🟦⬜🟦⬜🟦🟩⬛🟧🟩🟫
🟧🟨⬜🟫🟧⬛🟪🟫🟪🟥
🟨🟥🟧⬛🟪🟥🟩🟪⬜🟨
🟨🟫🟥🟪⬛🟥🟥⬛🟩⬛
🟧🟫🟩🟨⬛🟪🟥⬛🟦⬜
🟫🟫⬛🟨🟩🟩🟥🟦🟪🟦
⬜🟥🟧🟧🟧🟩🟨⬜🟫⬜
*/