function largest(arr, n){
    max = arr[0];
    min = arr[0];
    count = 1;
    while (count <= n) {
        var min2 = min;
        for (var x = 0; x < arr.length; x++) {
            if (count == 1) {
                if (arr[x] > max){
                    max = arr[x];
                    min2 = max;
                }
                if (arr[x] < min) {
                    min = arr[x];
                }
            } else {
                if (arr[x] < max && arr[x] > min2) {
                    min2 = arr[x];
                }
            }
        }
        max = min2;
        count++;
    }
    return max;
}

var a = [200, 6, 8, 10, 12, 1, 20];
console.log(largest(a, 1));
