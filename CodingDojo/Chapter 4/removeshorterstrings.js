/*
Remove Shorter Strings

Given a string array and value (length), remove any strings
shorter than length from the array.
*/

function removeShort(strArr, val) {
    for (var ind = strArr.length-1; ind >= 0; ind--) {
        if (strArr[ind].length < val) {
            for (var i = ind; i < strArr.length-1; i++){
                var temp = strArr[i];
                strArr[i] = strArr[i+1];
                strArr[i+1] = temp;
            }
            strArr.pop();
        }
    }
    return strArr;
}

var str1 = ["Hello", "World", "I", "am", "Here"];
console.log(removeShort(str1, 4));
