//: Iteration protocols: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols

function* numbers() {
    yield 1;
    yield 2;
}

let gen = numbers();
for (let num of gen) {
    break;
}

/*
`next()` method of an iterator returns an object with two properties:
  - done (boolean): true if iterator is past the end of the sequence
  - value (any JS value)

In for...of loops, abrupt iteration termination can be caused by break,
continue, throw or return. In these cases, the iterator is closed.
*/
console.log(gen.next());  // { value: undefined, done: true }
