var mysql = require("mysql");

var connection = mysql.createConnection({
  host : 'localhost',
  user : 'root',
  password : '',
  database : 'todo'
});

connection.connect();

function startingDatasLoad() {
  addTodo({text: 'Buy milk'});
  addTodo({text: 'Make dinner'});
  addTodo({text: 'Save the world'});
}

function addTodo(attributes) {
  connection.query('INSERT INTO todo SET ?', attributes, function(err, result) {
    if (err) throw err;
  });
}

function getTodo(attributes) {
  connection.query('SELECT * FROM todo WHERE todo_id= ?', attributes, function(err, result) {
    if (err) throw err;
  });
}

function getAllTodo(cb) {
  connection.query('SELECT * FROM todo', function(err, result) {
    if (err) throw err;
    cb(result);
  });
}

function deleteTodo(attributes) {
  connection.query('DELETE FROM todo WHERE todo_id= ?', attributes, function(err, result) {
    if (err) throw err;
  });
}

function completeTodo(attributes) {
  connection.query('UPDATE todo SET completed=true WHERE todo_id= ?', attributes, function(err, result) {
    if (err) throw err;
  });
}

startingDatasLoad();

module.exports = {
  addItem : addTodo,
  getItem : getTodo,
  getAllItem : getAllTodo,
  deleteItem : deleteTodo,
  completeItem : completeTodo
};
