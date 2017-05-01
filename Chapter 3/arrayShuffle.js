/*
Array: Shuffle

In JavaScript, the Array object has numerous useful methods.
It does not, however, contain a method that will randomize
the order of an array's elements. Create shuffle(arr) to
efficiently shuffle an array's values. Work in-place.

*/

function shuffle(arr) {
    for (var i = 0; i < arr.length; i++) {
        var rand = Math.floor(Math.random()*arr.length);
        console.log(rand);
        var temp = arr[i];
        arr[i] = arr[rand];
        arr[rand] = temp;
    }
}

var arr1 = [1, 2, 3, 4, 5];
console.log(`Before shuffling: ${arr1}`);
shuffle(arr1);
console.log(`After shuffling: ${arr1}`);
