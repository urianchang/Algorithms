/*
String Anagrams:

Given a string, return array where each element is a string
representing a different anagram. For this challenge,
you can use built-in string functions such as split.
*/

function anagram(string, arr) {
  if (!arr) {arr = []};
  if arr.indexOf(string) != -1 {
    return arr;
  }
  var count = 0;
  while (count < string.length) {
    
  }
}

console.log(anagram("test"));
