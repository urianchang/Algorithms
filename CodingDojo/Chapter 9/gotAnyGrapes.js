/*
Got Any Grapes?!?
Martin loves grapes. He sees a number of baggies containing grapes,
all in a row. Stephen tells him that he can take as many of the baggies
as he wants, as long as he doesn't take two that are next to each other.
Martin wants to maximize his number of grapes. Grapes are pretty healthy,
so let's help him out.

Create a function to accept an array of non-negative integers
representing number of grapes in each adjacent baggy. Your
function should return the maximum amount of grapes he can obtain.
*/

function grapes(arr) {
    return findMax(arr, arr.length - 1);
}

function findMax(arr, i) {
    if (i === 0) {
        return arr[0];
    }
    if (i === 1) {
        if (arr[1] > arr[0]) {
            return arr[1];
        }
        return arr[0]
    }
    if (arr[i] + findMax(arr, i-2) > findMax(arr, i-1)) {
        return arr[i] + findMax(arr, i-2);
    }
    return findMax(arr, i-1);
}

//: Arnold's solution
function gotAnyGrapes2(arr,i){
    if(i === 0){
        return arr[i];
    }
    if(i === 1){
        return arr[1] > arr[0] ? arr[1] : arr[0];
    }

    if(i === undefined){
        return gotAnyGrapes2(arr,arr.length-1);
    }
    return (arr[i] + gotAnyGrapes2(arr,i-2)) > gotAnyGrapes2(arr,i-1) ? arr[i] + gotAnyGrapes2(arr,i-2) : gotAnyGrapes2(arr,i-1);
}

var arr1 = [2,2,999,2,999,2,2];
console.log(grapes(arr1));
console.log(gotAnyGrapes2(arr1));
