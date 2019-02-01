/*4. Write a function that retrieves the currency quote of the EURUSD and returns a
Promise containing result*/

//since Fetch is a native (ES6) function that returns a Promise,
// we can use that to get the EURUSD rate and output that to the console.log
// when the response has arrived

// On node Fetch api is not implemented, so this fetch is needed
const fetch = require("node-fetch");
const value = fetch(
  "https://free.currencyconverterapi.com/api/v6/convert?q=EUR_USD&compact=y"
)
  .then(response => {
    return response.json();
  })
  .then(json => {
    console.log(json.EUR_USD.val);
  });
