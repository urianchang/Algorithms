/***
Getting execution time and memory usage of some JavaScript code
  - Node's process.hrtime() method gives a higher resolution of real time
  - Node's process.memoryUsage() method returns:
    - rss: Total memory allocated for the process execution
    - heapTotal: Total size of the allocated heap
    - heapUsed: Actual memory used during execution of process
    - external: Memory used by "C++ objects bound to JavaScript objects managed by V8"
  - Use setTimeout in case the script takes way too long to execute

To run:
  1. Comment / Un-comment which function that you want to use
  2. In Terminal, run: `node perf.js`

References:
  - https://www.valentinog.com/blog/memory-usage-node-js/
  - https://blog.abelotech.com/posts/measure-execution-time-nodejs-javascript/
  - https://nodejs.org/api/process.html#
  - https://nodejs.org/api/process.html#process_process_memoryusage
***/

const TIMEOUT = 30;
const ALPHA = "abcdefghijklmnopqrstuvwxyz".repeat(100);


function use_array() {
  let arr = [];
  for (let i = 0; i < ALPHA.length; i++) {
      arr.push(ALPHA[i]);
  }
  return arr.join("");
}


function use_add() {
  let msg_str = "";
  for (let i = 0; i < ALPHA.length; i++) {
      msg_str += ALPHA[i];
  }
  return msg_str;
}


/* Example of printing out all the values from process.memoryUsage():

```
  const used = process.memoryUsage();
  for (let key in used) {
    console.log(`${key} ${Math.round(used[key] / 1024 / 1024 * 100) / 100} MB`);
  }
```

NOTE: We're primarily concerned with `heapUsed`.
*/


// setTimeout(() => {
//   const hrstart = process.hrtime();
//   const message = use_array();
//   const hrend = process.hrtime(hrstart);
//   const used = process.memoryUsage();
//   console.log(`heapUsed: ${Math.round(used['heapUsed'] / 1024 / 1024 * 100) / 100} MB`);
//   console.log("Execution time with array: %ds %dms", hrend[0], hrend[1]/1000000);
// }, TIMEOUT);


setTimeout(() => {
  const hrstart = process.hrtime();
  const message = use_add();
  const hrend = process.hrtime(hrstart);
  const used = process.memoryUsage();
  console.log(`heapUsed: ${Math.round(used['heapUsed'] / 1024 / 1024 * 100) / 100} MB`);
  console.log("Execution time with string addition: %ds %dms", hrend[0], hrend[1]/1000000);
}, TIMEOUT);

