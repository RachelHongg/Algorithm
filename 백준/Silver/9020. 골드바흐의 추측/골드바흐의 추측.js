const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const T = input[0];

function is_prime(n) {
  if (n == 1) return false;
  for (let i = Math.floor(Math.sqrt(n)); i > 1; i--) {
    if (n % i == 0) return false;
  }
  return true;
}

for (let i = 0; i < T; i++) {
  let num = input[i + 1];
  let half = Math.floor(num / 2);
  for (let j = half; j > 1; j--) {
    if (is_prime(j) && is_prime(num - j)) {
      console.log(j, num - j);
      break;
    }
  }
}
