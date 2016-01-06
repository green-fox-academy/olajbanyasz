'use strict';

function triangle(number) {
  var output = '';
  for (var i = 1; i <= number; i++) {
    for (var j = 1; j < number*2; j++) {
      if (j <= number - i) {
        output += ' ';
      } else if (j >= number + i) {
        output += ' ';
      } else {
        output += '*';
      }
    }
    output += '\n';
  }
  return output;
};

console.log(triangle(4));
