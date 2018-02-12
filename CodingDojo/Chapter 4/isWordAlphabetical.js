/*
Is Word Alphabetical

Nikki, a queen of gentle sarcasm, loves the word 'facetiously'. Lance
helpfully points out that it is the only known English word that
contains all five vowels in alphabetical order, and it even
has a 'y' on the end! Nikki takes a break from debugging to turn and
give him an acid stare - indeed a look that was delivered 'arseniously'.

Given a string, return whether all contained letters are in alphabetical order.
*/

function isAlpha(str) {
  var V_MAP = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5,
    'y': 6
  };
  var s_arr = str.toLowerCase().split('');
  var pre_v = 0
  for (var i=0; i < s_arr.length; i++) {
    if (s_arr[i] in V_MAP) {
      if (V_MAP[s_arr[i]] < pre_v) {
        return false;
      }
      pre_v = V_MAP[s_arr[i]];
    }
  }
  return true;
}

console.log(isAlpha('facetiously'));
console.log(isAlpha('arseniously'));
console.log(isAlpha('oau'));
