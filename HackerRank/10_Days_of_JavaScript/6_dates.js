//: https://www.hackerrank.com/challenges/js10-date/problem
// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
function getDayName(dateString) {
    let dayName;
    // Write your code here
    const weekDay = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    dayName = weekDay[new Date(dateString).getDay()]
    return dayName;
}

console.log(getDayName('06/22/2018'));
