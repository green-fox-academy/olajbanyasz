'use strict';

var probaRequest = new XMLHttpRequest();
console.log('probaRequest: ', probaRequest);

var ACCESS_TOKEN = 'JNDzfN0Pz8mshV6DHISeFTRHJy00p1LvLoKjsnSUpz0krIeYGX';
var url = 'https://yoda.p.mashape.com/yoda';

probaRequest.open('GET', url);
probaRequest.setRequestHeader('X-Mashape-Key', ACCESS_TOKEN);
probaRequest.send();
