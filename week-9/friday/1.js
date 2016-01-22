'use strict';

var myArray = [4, 6, 3, 2];

function tripleEachElement(myArray) {
  var output = [];
  myArray.forEach(function(number) {
    output.push(number*3);
  });
  return output;
}

function tripleEachElement2(myArray) {
  return myArray.map(function(number) {return number*3});
}


// Write a function that takes an array of numbers,
// and returns a new array with the same length but all,
// of it's elements are the triple of the original array's elements!

console.log(tripleEachElement([4, 6, 3, 2])); // [12, 18, 9, 6]
console.log(tripleEachElement2([4, 6, 3, 2]));
