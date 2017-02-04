// Only Keep Last Few
// Stan learned something today: that reducing
// an array's .length immediately shortens it
// by that amount. Given array arr and number x
// remove all except the last x elements, and return
// arr (changed and shorter).

function keep(arr, num) {
  if (arr.length > num) {
    for (var i = 0; i < num; i++) {
      arr[i] = arr[arr.length-num+i];
    }
    arr.length = num;
    return arr;
  } else {
    return 0;
  }
}

var a = [2, 4, 6, 8, 10];
var n = 3;
console.log(keep(a, n));
