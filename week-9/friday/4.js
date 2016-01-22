'use strict';

// Create a function that counts all the letters in a string,
// and returns an object that has the letters as keys and the counts as values.
function countLetters(text) {
  var output = {};
  for (var i = 0; i < text.length; i++) {
    if (!(text[i] in output)) {
      output[text[i]] = 0;
    }
    output[text[i]]++;
  }
  return output;
}


console.log(countLetters('appletree')); // {a: 1, p: 2, l: 1, e: 3, t: 1, r: 1}
