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
