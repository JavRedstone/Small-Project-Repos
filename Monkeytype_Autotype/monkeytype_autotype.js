var list = "";
var words = document.getElementById("words");
for (let i = 0; i < words.children.length; i++) {    
    var word = document.getElementsByClassName("word")[i].innerHTML;
    var cleaned_word = word.replace(/<letter>/g, "").replace(/<\/letter>/g, "");
    list += cleaned_word + " ";
}
console.log(list);