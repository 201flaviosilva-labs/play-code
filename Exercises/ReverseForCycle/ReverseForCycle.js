const prompt = require("prompt-sync")(); // npm i prompt-sync

reverseForCycle();
function reverseForCycle() {
  console.log("-- Reverse Cycle --");

  const max = Number(prompt("Max: "));

  for (let i = max; i >= 0; i--) {
    console.log(i);
  }
}
