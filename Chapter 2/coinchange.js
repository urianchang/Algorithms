// Generate Coin change
// Make generateCoinChange(cents). Accept a number
// of American cents, compute and print how to represent
// that amount with smallest number of coins.
// Common American coins: pennies (1 cent), nickels (5 cents),
// dimes (10 cents), and quarters (25 cents)

//Initial function
function generateCoinChange(cents) {
    console.log("Quarters: " + Math.trunc(cents/25));
    cents = cents%25;
    console.log("Dimes: " + Math.trunc(cents/10));
    cents = cents%10;
    console.log("Nickels: " + Math.trunc(cents/5));
    console.log("Pennies: " + (cents%5));
}

//Optimized function: implemented 2 arrays to coordinate coin and value for order
function coin_op(cents) {
    var denom = [100, 50, 25, 10, 5, 1];
    var coins = ["dollars", "half-dollars", "quarters", "dimes", "nickels", "pennies"];
    for (var x = 0; x < coins.length; x++) {
        console.log(coins[x] + ": " + Math.trunc(cents/denom[x]));
        cents = cents%denom[x];
    }
}

coin_op(94);
console.log();
coin_op(134);
