// Rockin' the Dojo Sweatshirt
// Let's say a Dojo sweatshirt costs $20 (including tax), but
// discount of 9% if you buy two, a nice 19% discount for three,
// and 35% discount for 4+. Build function sweatshirtPricing(num) that,
// given a number of sweatshirts, returns the cost. Round up to nearest dollar.

function sweatshirtPricing(num) {
    var total = num * 20;
    if (num == 2) {
        total *= 0.91;
    }
    if (num == 3) {
        total *= 0.81;
    }
    if (num >= 4) {
        total *= 0.65;
    }
    return Math.ceil(total);
}

console.log(sweatshirtPricing(1));
console.log(sweatshirtPricing(2));
console.log(sweatshirtPricing(3));
console.log(sweatshirtPricing(4));
console.log(sweatshirtPricing(5));
