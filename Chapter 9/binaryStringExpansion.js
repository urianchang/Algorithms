/*
Binary String Expansion:

You are given a string containing chars '0',
'1', and '?'. For every '?', either '0' or '1'
can be substituted. Write a recursive function to
return array of all valid strings with '?' chars
expanded to '0' or '1'.
*/

function bse(string) {
  var strArr = string.split("?", 2)
  if (strArr.length == 1) {
    return strArr;
  }
  strArr = string.split("");
  for (var char = 0; char < strArr.length; char++) {
      if (strArr[char] == "?") {
        strArr[char] = 0;
        var string1 = strArr.join("");
        strArr[char] = 1;
        var string2 = strArr.join("");
        return bse(string1).concat(bse(string2))
      }
  }
}

console.log(bse("0?1??"));
