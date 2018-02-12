/*
Common Suffix

Lance is writing his opus: Epitome, an epic tome of beat poetry. Always
ready for a good rhyme, he constantly seeks words that end with the
same letters. Write a function that, when given a word array, returns
the largest suffix (word-end) common to all words in the array.
*/

function commonSuffix(array) {
  var suffix = [];

  //: Identify shortest word
  var shortest = array[0];
  for (word of array) {
    if (word.length < shortest.length) {
      shortest = word;
    }
  }

  var isValid = true;
  for (var i=1; i < shortest.length; i++) {
    var char = shortest[shortest.length - i].toLowerCase();
    for (word of array) {
      word = word.toLowerCase();
      if (char !== word[word.length - i]) {
        isValid = false;
        break;
      }
    }
    if (!isValid) {
      break;
    }
    suffix.push(char);
  }

  return suffix.reverse().join('');
}

var arrA = ['deforestation', 'citation', 'conviction', 'incarceration'];
var arrB = ['nice', 'ice', 'baby'];
console.log(commonSuffix(arrA));  //: "tion"
console.log(commonSuffix(arrB));  //: ""
