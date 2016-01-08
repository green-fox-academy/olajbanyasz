'use strict';

var pictures = [
  './img/2011-06-25 11.22.07.jpg',
  './img/AndréRené_IIRákocziÁltIsk_Kontraszt.jpg',
  './img/AndréRené_IIRákocziÁltIsk_Labirintus.jpg',
  './img/AndréRené_IIRákocziÁltIsk_Mátrix.jpg',
  './img/20140703_130225.jpg',
  './img/SAM_0786.jpg',
  './img/SAM_0816.jpg',
  './img/SAM_0906.jpg',
  './img/functions.jpg'
]

var rightButton = document.querySelector('.right');
var leftButton = document.querySelector('.left');
var pictureIndex = 4;
var mainPicture = document.getElementById('mainPicture');
var thumbnailRow = document.querySelector('.thumbnail');
mainPicture.setAttribute('src', pictures[pictureIndex]);

function indexChecking() {
  if (pictureIndex > pictures.length - 1) {
    pictureIndex = 0;
  } else if (pictureIndex < 0) {
    pictureIndex = pictures.length - 1;
  }
}

function smallPictureClick(event) {
  removeSeenowClass();
  pictureIndex = event.target.id;
  mainPicture.setAttribute('src', pictures[pictureIndex]);
  document.getElementById(event.target.id).classList.add('haveseen', 'seenow');
}

function makeThumbnail() {
  for (var i = 0; i < pictures.length; i++) {
    var smallPicture = document.createElement('img');
    smallPicture.classList.add('thumbnailimages');
    smallPicture.addEventListener('click', smallPictureClick);
    smallPicture.setAttribute('id' , i);
    smallPicture.setAttribute('src', pictures[i]);
    thumbnailRow.appendChild(smallPicture);
  }
}

function removeSeenowClass(argument) {
  document.querySelector('.seenow').classList.remove('seenow');
}

function addClassToElement(pictureIndex) {
  document.getElementById(pictureIndex).classList.add('haveseen' , 'seenow');
}

function rightClick() {
  removeSeenowClass();
  pictureIndex++;
  indexChecking();
  mainPicture.setAttribute('src', pictures[pictureIndex]);
  addClassToElement(pictureIndex);
}

function leftClick() {
  removeSeenowClass();
  pictureIndex--;
  indexChecking();
  mainPicture.setAttribute('src', pictures[pictureIndex]);
  addClassToElement(pictureIndex);
}

rightButton.addEventListener('click', rightClick);
leftButton.addEventListener('click', leftClick);
makeThumbnail();
addClassToElement(pictureIndex);
