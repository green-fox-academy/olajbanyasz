var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'test',
  password : 'test',
  database : 'todo'
});

connection.connect();

function addUser(attributes) {
  connection.query('INSERT INTO user SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}

function getUser(attributes) {
  connection.query('SELECT * FROM `user`', function(err, results) {
    if (err) throw err;
    console.log(results);
  });
}

module.exports = {
  add: addUser,
  get: getUser
};
