/*
Longest Palindrome

For this challenge, we will look not only at the entire string provided,
but also at the substrings within it. Return the longest palindromic
substring. Include spaces as well.

Second: Re-solve the problem but ignore spaces, tabs, returns, capitalization
and punctuation in the return string.
*/

//Helper function to check if string is palindrome
function palcheck(string) {
  for (var i = 0; i < string.length/2; i++) {
      if (string[i] != string[string.length-1-i]){
          return false;
      }
  }
  return true;
}

//Main function that gets longest palindrome
function longestpal(string) {
  //Check if the whole string is a palindrome
  if (palcheck(string)){
    return string;
  }
  //Create array of palindromes
  var pals = [];
  for (var idx = 0; idx < string.length-1; idx++){
    var pal = string[idx];
    var letter = string[idx];
    for (var i = idx+1; i < string.length; i++) {
      pal += string[i];
      if (string[i] == letter) {
        if (palcheck(pal)) {
          pals.push(pal);
        }
      }
    }
  }
  //Find longest palindrome in array
  if (pals.length < 1) {
    return string[0];
  } else {
    var longest = pals[0];
    for (var x = 0; x < pals.length; x++) {
      if (pals[x].length > longest.length) {
        longest = pals[x];
      }
    }
    return longest;
  }
}

var str1 = "what up, daddy-o?";
var str2 = "uh... not much";
var str3 = "Yikes! my favorite racecar erupted!"; 
console.log(longestpal(str1));
console.log(longestpal(str2));
console.log(longestpal(str3));
