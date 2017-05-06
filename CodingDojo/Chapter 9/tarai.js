/*
Tarai:

The tarai (Japanese: "to pass around") function was created
to profile recursive performance in various systems and
languages. Unlike other functions, numbers don't get particularly
large, but the amount of recursion is significant. The tarai function
accepts three parameters, and is defined as:
    1) tarai(x, y, z) == y, if x <= y
    2) tarai(x, y, z) == tarai(tarai(x-1, y, z), tarai(y-1, z, x), tarai(z-1, x, y))
*/

function tarai(x, y, z) {
    if (x <= y) {
        return y;
    }
    return tarai(tarai(x-1, y, z), tarai(y-1, z, x), tarai(z-1, x, y));
}

console.log(tarai(10, 2, 9));   // 9
