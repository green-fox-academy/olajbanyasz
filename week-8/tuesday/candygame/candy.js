'use strict';
  var timerOn = false;
  var startTime = Date.now();
  var endTime = Date.now();
  var candies = 0;
  var lollypops = 0;
  var createCandyButton = document.querySelector('.create-candy');
  var buyLollypopButton = document.querySelector('.buy-lollypop');
  var autoBuy = document.querySelector('.auto-buy');
  var candiesText = document.querySelector('.candies');
  var lollypopsText = document.querySelector('.lollypops');
  createCandyButton.addEventListener('click', createCandy);
  buyLollypopButton.addEventListener('click', buyLollypop);
  autoCreateCandies();

function createCandy() {
  gameTimer();
  candies++;
  displayStats();
}

function gameTimer() {
  if ((!timerOn) && (candies === 0) && (lollypops === 0)) {
    startTime = Date.now();
    timerOn = true;
  }
}

function buyLollypop() {
  candies -= 10;
  lollypops++;
  displayStats();
}

function enableBuyLollypopButton() {
  if (candies > 9) {
  buyLollypopButton.removeAttribute('disabled');
  } else {
  buyLollypopButton.setAttribute('disabled', 'disabled');
  }
}

function displayStats() {
  gameEnd();
  autoBuyer();
  document.querySelector('h1').textContent = 'Candy Game: ' + (endTime-startTime)/1000 + ' sec';
  candiesText.textContent = 'Candies: ' + candies;
  lollypopsText.textContent = 'Lollypops: ' + lollypops;
  enableBuyLollypopButton();
}

function autoCreateCandies() {
  setInterval(candyFactory, 1000);
}

function candyFactory() {
  candies += Math.floor(lollypops/10);
  displayStats();
}

function newLollipops() {
  return Math.floor(candies/10);
}

function autoBuyer() {
  if (autoBuy.checked) {
    lollypops += newLollipops();
    candies -= newLollipops()*10;
  }
}

function gameEnd() {
  if ((candies >= 10000) && (timerOn)) {
    endTime = Date.now();
    timerOn = false;
  } else if ((candies < 10000) && (timerOn)) {
    endTime = Date.now();
  }
}
