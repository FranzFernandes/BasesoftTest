var nodes = document.getElementsByTagName("a");
var names = ["henk", "joop", "piet"];

/*
Instead of the value of i, the reference of i is being used. After the for loop the value of i becomes 3.
Meaning that instead of i.e. names[1] being called, names[3] is being called, which results into undefined.
*/
for (let i = 0; i < names.length; i++) {
  nodes[i].addEventListener("click", function() {
    console.log("You clicked name " + names[i]);
  });
}
