//: https://www.w3schools.com/js/js_function_closures.asp

/*
Method 1 - Using a global variable
// Initiate counter
var counter = 0;

// Function to increment counter
function add() {
    counter += 1;
    return counter;
}

Issue with this method is that any other function can change
the counter variable, not just `add()`
*/

/*
Method 2 - Use global and local variable
// Initiate counter
var counter = 0;

// Function to increment counter
function add() {
    var counter;
    counter += 1;
}

Issue with this method is that global and local variables are mixed up.
*/

/*
Method 3 - Use a closure

The variable add is assigned the return value of a self-invoking function, which
only runs once: sets counter to 0 and returns a function. Add can access the counter
in the parent scope (even after the parent function has closed). This makes it possible
for a function to have "private" variables: `counter` is protected by the scope of the
anonymous function, and can only be changed using the add function.
*/
var add = (function () {
    var counter = 0;
    return function () {counter += 1; return counter}
})();

console.log(add());
console.log(add());
console.log(add());
