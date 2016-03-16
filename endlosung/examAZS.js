'use strict';

var fs = require('fs');

function writeObjectToFileAsJson(fileName, object, cb) {
  setTimeout(function() {
    cb(fileName, object);
  }, 2000);
}

function cb(fileName, object) {
  var exam = JSON.stringify(object);
  fs.writeFile(fileName, exam, function(err) {
  if (err) {
    console.log(err);
  } else {
  console.log('Object saved to file!')
  }
  });
}
  
writeObjectToFileAsJson('exam.json', {'exam': false}, cb);