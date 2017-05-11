//: Singly Linked List Queue

function SLQueue() {
    var head = null;
    var tail = null;
}

SLQueue.prototype.size = function() {
    if (!this.head) {
        return 0;
    }
    var count = 0;
    var runner = this.head;
    while (runner) {
        count++;
        runner = runner.next;
    }
    return count;
}

module.exports = SLQueue;
