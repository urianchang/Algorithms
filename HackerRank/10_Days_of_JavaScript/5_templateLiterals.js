//: https://www.hackerrank.com/challenges/js10-template-literals/problem
//: https://www.hackerrank.com/challenges/js10-template-literals/topics/javascript-template-literals

/*
 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 *
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
 */
function sides(literals, ...expressions) {
  const [A, P] = expressions;
  const root_val = Math.sqrt((P * P) - (16 * A));
  const s1 = (P + root_val) / 4;
  const s2 = (P - root_val) / 4;
  return [s1, s2].sort();
}

const [x, y] = sides`The area is: ${10 * 14}.\nThe perimeter is: ${2 * (10 + 14)}.`;
console.log(x, y);

// //: Example of tagged templates
// var a = 5;
// var b = 10;
//
// function foo(strings, ...values) {
//   const a = values[0];
//   const b = values[1];
//   console.log(strings, values);
//   return `Sum ${a + b}
// Product ${a * b}
// Division ${b / a}`;
// }
//
// console.log(foo`Num1 ${a + 10}
// Num2 ${b * 2}
// Num3 ${b / a}`);
