'use strict';

var todoContainer = document.querySelector('.todocontainer');
var url = 'http://localhost:3000/todos';
var listButton = document.querySelector('.list-todos');
var createButton = document.querySelector('.create-new-todo');
var inputText = document.querySelector('textarea');
listButton.addEventListener('click', callCreateRequest);
createButton.addEventListener('click', callCreateNewToDo);

function callCreateNewToDo() {
  if (inputText.value != '') {
    createNewTodo(inputText.value);
    setTimeout(callCreateRequest,800);
  }
  inputText.value = '';
}

function callCreateRequest() {
  createRequest(displayTodos);
}

function callDeleteTodo() {
  deleteTodo(event.target.parentNode.id);
  setTimeout(callCreateRequest,800);
}

function callCompleteTodo() {
  var text = event.target.parentNode.innerText.substring(0, ((event.target.parentNode.innerText).length)-2);
  completeTodo(event.target.parentNode.id, text);
  setTimeout(callCreateRequest,800);
}

function createRequest(callback) {
  var request = new XMLHttpRequest();
  request.open('GET', url);
  request.send();
  request.onreadystatechange = function() {
    if (request.readyState === 4) {
      displayTodos(request.response);
    }
  }
}

function clearTodosFromDisplay() {
  while (todoContainer.firstChild) {
    todoContainer.removeChild(todoContainer.firstChild);
  }
}

function displayTodos(response) {
  clearTodosFromDisplay();
  var todoArray = JSON.parse(response);
  todoArray.forEach(function(todoItem) {
    var newTodoItem = document.createElement('div');
    newTodoItem.setAttribute('id', todoItem.todo_id);
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
    newTodoItem.addEventListener('click', createDeleteAndCompleteButtons);
    newTodoItem.setAttribute('class', todoItem.completed)
  });
}

function createDeleteAndCompleteButtons() {
  deletePreviewsButtons();
  makeButton('\u2611', 'complete-button', callCompleteTodo);
  makeButton('\u2612', 'delete-button', callDeleteTodo);
}

function deletePreviewsButtons() {
  var deleteButton = document.querySelector('.delete-button');
  if (deleteButton) {
  document.querySelector('.delete-button').remove();
  document.querySelector('.complete-button').remove();
  }
}

function makeButton(buttonText, className, eventFunction) {
  var newButton = document.createElement('button');
  newButton.innerText = buttonText;
  newButton.setAttribute('class', className);
  event.target.appendChild(newButton);
  newButton.addEventListener('click', eventFunction);

}
function createNewTodo(todotext) {
  var request = new  XMLHttpRequest();
  request.open('POST', url);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send(JSON.stringify({text: todotext}));
}

function completeTodo(id, desc) {
  var request = new  XMLHttpRequest();
  request.open('PUT', url + '/' + id);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send(JSON.stringify({'text': desc, completed: 'true'}));
}

function deleteTodo(id) {
  var request = new  XMLHttpRequest();
  request.open('DELETE', url + '/' + id);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send();
}

createRequest(displayTodos);
