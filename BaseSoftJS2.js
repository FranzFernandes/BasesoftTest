const findCombinationsRecursive = (remaining, text) => {
  //if theres only one character remaining, print the entire string
  if (remaining === 1) {
    console.log(text);
  } else {
    //for each possibility, execute the same function recursively. Afterwards, shuffle either the character at index or the first character
    // with the character character on the remaining -1 index. Afterwards execute again.
    for (let i = 0; i < remaining - 1; i++) {
      findCombinationsRecursive(remaining - 1, text);
      if (remaining % 2 === 0) {
        //execute swap
        [text[i], text[remaining - 1]] = [text[remaining - 1], text[i]];
      } else {
        [text[0], text[remaining - 1]] = [text[remaining - 1], text[0]];
      }
    }
    findCombinationsRecursive(remaining - 1, text);
  }
};

let text = "hallo";
findCombinationsRecursive(text.length, text.split(""));
