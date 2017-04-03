/*
Balance Index:

Here, a balance point is on an index, not between indices.
Return the balance index, where sums are equal on either side.
Return -1 if none exist.
*/

function balIndex (arr) {
    if (arr.length <= 2) {
        return -1;
    }
    var sumLeft = arr[0];
    var trackerLeft = 0;
    var sumRight = arr[arr.length-1];
    var trackerRight = arr.length - 1;
    var count = 2;
    while (count < arr.length) {
        if (sumRight > sumLeft) {
            trackerLeft++;
            sumLeft += arr[trackerLeft];
        } else if (sumLeft > sumRight) {
            trackerRight--;
            sumRight += arr[trackerRight];
        } else if (sumLeft == sumRight) {
            trackerLeft++;
            return trackerLeft;
        }
        count++;
    }
    return -1;
}


var arr1 = [-2, 5, 7, 0, 3];    //: 2
var arr2 = [9, 9];      //: -1
console.log(balIndex(arr1));
console.log(balIndex(arr2));
