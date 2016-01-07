'use strict';

function triangle(number) {
  var output = '';
  for (var i = 1; i <= number; i++) {
    output += ' '.repeat(number-i);
    output += '*'.repeat((i-1)*2+1);
    output += ' '.repeat(number-i);
    output += '\n';
  }
  return output;
};

console.log(triangle(6));
