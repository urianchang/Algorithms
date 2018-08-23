/*
     * Return the number of times that the string "code" appears anywhere in the given string,
     * except we'll accept any letter for the 'd', so "cope" and "cooe" count.
     * countCode("aaacodebbb") - 1
     * countCode("codexxcode") - 2
     * countCode("cozexxcope") - 2
*/

function codeCounter(string) {
    var stringArr = string.split('');   //: Split string into array
    var count = 0   //: Create count variable
    for (var i = 0; i < stringArr.length; i++) {
        if (stringArr[i] === "c") {     //: Look for "c" character
            var temp = stringArr.slice(i, i+4); //: Take out the 4-letter word
            if (temp[1] == "o" && temp[3] == "e") { //: Check for "o" and "e" at respective locations
                count++;    //: Increase count if true
            }
        }
    }
    return count;
}

var string = "coexxcode";
console.log(codeCounter(string));
