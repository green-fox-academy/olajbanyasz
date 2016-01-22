'use strict';

// Write a function that checks, if an array contains a number
// that has 5 as divisor. If it has it should return true otherwise false.
var myArray = [4, 6, 3, 2];

function hasDivisableBy5(myArray) {
  var output = false;
  myArray.forEach(function(number) {
    if (number % 5 === 0) {
      output = true;
    }
  });
  return output;
}

function hasDivisableBy5two(myArray) {
  return !!(myArray.reduce((acc, number) => number%5===0 ? acc+1 : acc+0, 0));
}

console.log(hasDivisableBy5([1, 8, 3, 6, 2])); // false
console.log(hasDivisableBy5([11, 7, 15, 9])); // true
console.log(hasDivisableBy5two([1, 8, 3, 6, 2])); // false
console.log(hasDivisableBy5two([11, 7, 15, 9])); // true
