const express = require("express");
const connection = require("./connection");
const app = express();
const port = 3000;
const path = require("path");
const queryFunc = require("./mysqlEjs_func.js");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

let user = "beta"; // username
let pass = "beta"; // password
let con = connection.con(user, pass, "sakila");
con.connect();
// 88888888888888888888888888888888     ShoW table     88888888888888888888888888888888888888888
app.get("/", (req, res) => {
  let stmt = "SELECT * FROM actor LIMIT 0,500";
  let filePath = path.join(__dirname, "/search_ajax.ejs");
  const html = queryFunc.mysqlEjs(user, pass, stmt, "sakila", filePath);
  console.log("actor list");
  setTimeout(() => {
    res.send(html[0]);
  }, 100);
});
// 888888888888888888888888888888888888  Searching  88888888888888888888888888888888888888888888
app.post("/searching", (req, res) => {
  var values = req.body;
  console.log(values.stmt);
  let filePath = path.join(__dirname, "/table.ejs");
  const html = queryFunc.mysqlEjs(user, pass, values.stmt, "sakila", filePath);
  console.log(html);
  setTimeout(() => {
    console.log(html);
    res.send(html[0]);
  }, 100);
});
// 8888888888888888888888888888888888888888  Add new  888888888888888888888888888888888888888888888888
app.post("/addNew", function (req, res) {
  let values = req.body;
  let actor_id = req.body.actor_id;
  console.log(values.stmt, actor_id);
  let filePath = path.join(__dirname, "/table.ejs");
  queryFunc.mysqlEjs(user, pass, values.stmt, "sakila", filePath);
  console.log(actor_id);
  res.send("Actor id " + actor_id + " is successfully added to database");
});
// 8888888888888888888888888888888888888888  Delete   8888888888888888888888888888888888888888888888
app.post("/deleting", (req, res) => {
  let values = req.body;
  let actor_id = req.body.actor_id;
  let filePath = path.join(__dirname, "/table.ejs");
  queryFunc.mysqlEjs(user, pass, values.stmt, "sakila", filePath);
  res.send("Actor id " + actor_id + " is deleted from database");
});
// 888888888888888888888888888888888888888888  update  88888888888888888888888888888888888888888888888
  function showTable(res){
    console.log("function entered");
    let stmt2 = "SELECT * FROM actor LIMIT 0,500";       //this query is not working
    let filePath2 = path.join(__dirname, "/search_ajax.ejs");
    const html = queryFunc.mysqlEjs(user, pass, stmt2, "sakila", filePath2);
    console.log("actor list",html[0]);     //html[0] is undefined
    setTimeout(() => {
      res.send(html[0]);
    }, 5000);
  }

app.get("/Edit", (req, res) => {
  var actor_id = req.query.actor_id;
  console.log(actor_id);
  let stmt = "SELECT * FROM actor where actor_id="+actor_id+";";
  let filePath = path.join(__dirname, "Edit.ejs");
  const html = queryFunc.mysqlEjs(user, pass, stmt, "sakila", filePath);
  console.log("actor list update");
  setTimeout(() => {
    console.log("actor list update",html[0]);
    res.send(html[0]);
  }, 100);
});
app.post("/Edit", (req, res) => {
  let values = req.body;
  console.log("update file", values.stmt);
  let filePath = path.join(__dirname, "/table.ejs");
  queryFunc.mysqlEjs(user, pass, values.stmt, "sakila", filePath);     //update query is running

  // showTable(res);       
  res.send("Student Record Updated Please refresh the page to view changes");
});
// 8888888888888888888888888888888888888888  listen(3000)   888888888888888888888888888888888888888888
app.listen(port, () => {
  console.log(`server is on localhost:${port}`);
});
