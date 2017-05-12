//: Singly Linked List Queue

function SLQueue() {
    var head = null;
    var tail = null;
}

//: Enqueue / Add a value to the queue
SLQueue.prototype.enqueue = function(val) {
    var newNode = new Node(val);
    if (!this.head) {
        this.head = newNode;
    } else {
        var runner = this.head;
        while (runner.next) {
            runner = runner.next;
        }
        runner.next = newNode;
    }
}

//: Dequeue / Remove and return the value at the front of the queue
SLQueue.prototype.dequeue = function() {
    if (!this.head) {
        return "Queue is empty";
    }
    var removedNode = this.head;
    this.head = this.head.next;
    return `Dequeued value: ${removedNode.val}`;
}

//: Return the value at the front of the queue
SLQueue.prototype.front = function() {
    if (!this.head) {
        return "Queue is empty";
    }
    return `Value at front of queue: ${this.head.val}`;
}

//: Check if queue is empty
SLQueue.prototype.isEmpty = function() {
    if (!this.head) {
        return "Queue is empty";
    }
    return "Queue is NOT empty";
}

//: Return the size of the queue
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

//: Check if queue contains a given value
SLQueue.prototype.contains = function(val) {
    if (!this.head) {
        return "Queue is empty";
    }
    var runner = this.head;
    while (runner) {
        if (runner.val === val) {
            return `${val} is in the queue`;
        }
        runner = runner.next;
    }
    return `${val} is NOT in the queue`;
}

module.exports = SLQueue;
