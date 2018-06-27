//: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance

function Human(first, last, age, gender) {
  this.name = {
    first,
    last
  };
  this.age = age;
  this.gender = gender;
};

Human.prototype.greeting = function() {
  console.log("My name is", this.name.first);
};

function SuperHuman(first, last, age, gender, powers) {
  Human.call(this, first, last, age, gender);
  this.powers = powers;
};

//: Inherit all methods available on Human.prototype
SuperHuman.prototype = Object.create(Human.prototype);
//: SuperHuman.prototype constructor should be set to SuperHuman
SuperHuman.prototype.constructor = SuperHuman;

SuperHuman.prototype.greeting = function() {
  console.log("Never fear for I am here!");
};

let h1 = new Human('Bruce', 'Wayne', 18, 'Male');
let s1 = new SuperHuman('Clark', 'Kent', 18, 'Male');

h1.greeting();
s1.greeting();
