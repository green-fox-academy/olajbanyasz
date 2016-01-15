'use strict';

var todoContainer = document.querySelector('.todocontainer');
var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var listButton = document.querySelector('.list-todos');
var createButton = document.querySelector('.create-new-todo');
var inputText = document.querySelector('textarea');
listButton.addEventListener('click', callCreateRequest);
createButton.addEventListener('click', callCreateNewToDo);

function callCreateNewToDo() {
  if (inputText.value != '') {
    createNewTodo(inputText.value);
    setTimeout(callCreateRequest,600);
  }
  inputText.value = '';
}

function callCreateRequest() {
  createRequest(displayTodos);
}

function callDeleteTodo() {
  deleteTodo(event.target.parentNode.id);
  setTimeout(callCreateRequest,600);
}

function callCompleteTodo() {
  var text = event.target.parentNode.innerText.substring(0, ((event.target.parentNode.innerText).length)-2);
  completeTodo(event.target.parentNode.id, text);
  setTimeout(callCreateRequest,600);
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
    newTodoItem.setAttribute('id', todoItem.id);
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
    newTodoItem.addEventListener('click', createDeleteAndCompleteButtons);
    newTodoItem.setAttribute('class', todoItem.completed)
  });
}

function createDeleteAndCompleteButtons() {
  deletePreviewsButtons();
  makeCompleteButton();
  makeDeleteButton();
}

function deletePreviewsButtons() {
  var deleteButton = document.querySelector('.delete-button');
  if (deleteButton) {
  document.querySelector('.delete-button').remove();
  document.querySelector('.complete-button').remove();
  }
}

function makeCompleteButton() {
  var newCompleteButton = document.createElement('button');
  newCompleteButton.setAttribute('class', 'complete-button');
  newCompleteButton.innerText = '\u2611';
  event.target.appendChild(newCompleteButton);
  newCompleteButton.addEventListener('click', callCompleteTodo);
}

function makeDeleteButton() {
  var newDeleteButton = document.createElement('button');
  newDeleteButton.innerText = '\u2612';
  newDeleteButton.setAttribute('class', 'delete-button');
  event.target.appendChild(newDeleteButton);
  newDeleteButton.addEventListener('click', callDeleteTodo);
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
