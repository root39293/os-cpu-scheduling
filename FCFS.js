const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
console.log('hello world!');

rl.question('hello ! input data : ', (a) => {
  console.log(`hello ${a}`);
  process.exit();
});
