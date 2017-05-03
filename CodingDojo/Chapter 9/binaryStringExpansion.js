/*
Binary String Expansion:

You are given a string containing chars '0',
'1', and '?'. For every '?', either '0' or '1'
can be substituted. Write a recursive function to
return array of all valid strings with '?' chars
expanded to '0' or '1'.
*/

function bse(string) {
  //: Split string by question mark.
  var strArr = string.split("?")
  //: If there are no question marks left, return the array of 1 string
  if (strArr.length == 1) {
    return strArr;
  }
  //: Else, split the string into separate characters.
  strArr = string.split("");
  //: Check every character
  for (var char = 0; char < strArr.length; char++) {
      //: If question mark is found...
      if (strArr[char] == "?") {
        //: Create a string with "?" replaced with "0"
        strArr[char] = 0;
        var string1 = strArr.join("");
        //: Create another string with "?" replaced with "1"
        strArr[char] = 1;
        var string2 = strArr.join("");
        //: Use recursive function and join/concatenate the string arrays
        return bse(string1).concat(bse(string2))
      }
  }
}

console.log(bse("0?1??"));
