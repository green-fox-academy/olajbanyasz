'use strict';

function Circle(radius) {
  this.radius = radius;

  this.getCircumference = function() {
    return this.radius*2*Math.PI;
  }

  this.getArea = function() {
    return this.radius*this.radius*Math.PI;
  }

  this.toString = function() {
    var output = '';
    output  += 'Radius: ' + this.radius + ', Circumference: ' + this.getCircumference() + ', Area: ' + this.getArea();
    return output;
  }
}

// Create a Circle constructor that creates a circle object:
// it should take the circle's radius as a parameter
// it should have a "getCircumference" method that returns it's circumference
// it should have a "getArea" method that returns it's area
// it should have a "toString" method that returns it's stats as a string like:
// 'Radius: 4, Circumference: 25.132741228718345, Area: 50.26548245743669'
var circle = new Circle(5);
console.log(circle.getCircumference());
console.log(circle.getArea());
console.log(circle.toString());
