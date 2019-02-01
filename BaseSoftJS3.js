const findCombinations = text => {
  let length = text.length,
    result = [text.slice()],
    amountOfTries = new Array(length).fill(0),
    index = 1,
    parity;

  while (index < length) {
    // check if all the possibilites have been hit
    if (amountOfTries[index] < index) {
      //swap based on parity
      parity = index % 2 && amountOfTries[index];
      //ES6 destructuring swap
      [text[index], text[parity]] = [text[parity], text[index]];

      amountOfTries[index]++;
      index = 1;
      result.push(text.slice());
      // else go to the next one, by increasing the index and setting the amountoftries to 0 for this option
    } else {
      amountOfTries[index] = 0;
      index++;
    }
  }
  return result;
};

let text = "abc";
console.log(findCombinations(text.split("")));
