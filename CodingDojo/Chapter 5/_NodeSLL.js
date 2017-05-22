//: Node object for Singly Linked Lists

function Node(val) {
    this.val = val;
    this.next = null;
}

//: Return average
Node.prototype.average = function() {
    var sum = this.val;
    var count = 1;
    var N = this.next;
    while (N) {
      count++;
      sum += N.val;
      N = N.next;
    }
    return (sum/count);
}

//: Return maximum value
Node.prototype.max = function() {
    var max = this.val;
    var N = this.next;
    while (N) {
      if (N.val > max) {
        max = N.val;
      }
      N = N.next;
    }
    return max;
}

//: Return minimum value
Node.prototype.min = function() {
    var min = this.val;
    var N = this.next;
    while (N) {
      if (N.val < min) {
        min = N.val;
      }
      N = N.next;
    }
    return min;
}

module.exports = Node;
