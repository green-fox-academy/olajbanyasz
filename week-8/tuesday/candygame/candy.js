'use strict';

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
  candies++;
  displayStats();
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
  autoBuyer();
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
