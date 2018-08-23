let str = "";
let str1 = " ";
let str2 = "  ";
let str3 = "hello";
let str4 = " hello";
let str5 = "hello ";

//: Match if string is only spaces
const re = /^\s+$/;

console.log(re.test(str));
