// list of colours printed
const char_list = ["โฌ","๐จ","๐ง","๐ฅ","๐ช","๐ฆ","๐ฉ","๐ซ","โฌ"];

// generate_square function
const generate_square = (n) => {
    var print_string = "";
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            print_string += char_list[Math.round(Math.random()*(char_list.length-1))];
        }
        print_string += "\n";
    }
    console.log(print_string);
}

// test case
generate_square(10);

// example output
/**
๐ฆ๐ง๐ฉ๐ช๐ฆ๐ง๐ฅ๐ช๐ซ๐ง
๐ซ๐ฉ๐ช๐ฉ๐ฉโฌ๐ซโฌ๐ฉ๐ฅ
๐ง๐ง๐จโฌ๐ซ๐ช๐ง๐ฆโฌ๐ง
๐ฆโฌ๐ฆโฌ๐ฆ๐ฉโฌ๐ง๐ฉ๐ซ
๐ง๐จโฌ๐ซ๐งโฌ๐ช๐ซ๐ช๐ฅ
๐จ๐ฅ๐งโฌ๐ช๐ฅ๐ฉ๐ชโฌ๐จ
๐จ๐ซ๐ฅ๐ชโฌ๐ฅ๐ฅโฌ๐ฉโฌ
๐ง๐ซ๐ฉ๐จโฌ๐ช๐ฅโฌ๐ฆโฌ
๐ซ๐ซโฌ๐จ๐ฉ๐ฉ๐ฅ๐ฆ๐ช๐ฆ
โฌ๐ฅ๐ง๐ง๐ง๐ฉ๐จโฌ๐ซโฌ
*/
