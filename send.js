var sid = "AC70ec0521a450f11d495d0a1e5a1375d5";
var auth_token = "ded5fe61053a647448b57f7aecfb6f4c";

var twilio = require("twilio")(sid, auth_token);

twilio.messages
  .create({
    from: "+18147040209",
    to: "+918959084494",
    body: "this is a testing message",
  })
  .then(function(res) {console.log("message has sent!")})
  .catch(function(err)  {
    console.log(err);
  });