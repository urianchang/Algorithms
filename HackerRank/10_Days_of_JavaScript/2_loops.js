//: https://www.hackerrank.com/challenges/js10-loops/problem
function vowelsAndConsonants(s) {
    const VOWELS = new Set(["a", "e", "i", "o", "u"]);
    for (let letter of s) {
      if (VOWELS.has(letter)) {
        console.log(letter);
      }
    }
    for (let letter of s) {
      if (!VOWELS.has(letter)) {
        console.log(letter);
      }
    }
}

vowelsAndConsonants("hello");
