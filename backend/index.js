const express = require("express");
const connection = require("./connection");
const app = express();
const port = 3000;
const path = require("path");
const queryFunc = require("./mysqlEjs_func.js");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

let user = "root"; // username
let pass = "root"; // password
let con = connection.con(user, pass, "traffic");
con.connect();
//     ShoW table     
app.get("/", (req, res) => {
  let stmt = "SELECT * FROM challanlist LIMIT 0,500";
  let filePath = path.join(__dirname, "/search_ajax.ejs");
  const html = queryFunc.mysqlEjs(user, pass, stmt, "traffic", filePath);
  // console.log("challanlist list");
  setTimeout(() => {
    res.send(html[0]);
  }, 100);
});
//  Searching  
app.post("/searching", (req, res) => {
  var values = req.body;
  console.log(values.stmt);
  let filePath = path.join(__dirname, "/table.ejs");
  const html = queryFunc.mysqlEjs(user, pass, values.stmt, "traffic", filePath);
  console.log(html);
  setTimeout(() => {
    console.log(html);
    res.send(html[0]);
  }, 100);
});
// 8888888888888888888888888888888888888888  Add new  888888888888888888888888888888888888888888888888
app.post("/addNew", function (req, res) {
  let values = req.body;
  let id = req.body.id;
  console.log(values.stmt, id);
  let filePath = path.join(__dirname, "/table.ejs");
  queryFunc.mysqlEjs(user, pass, values.stmt, "traffic", filePath);
  console.log(id);
  res.send("challanlist id " + id + " is successfully added to database");
});
// 8888888888888888888888888888888888888888  Delete   8888888888888888888888888888888888888888888888
app.post("/deleting", (req, res) => {
  let values = req.body;
  let id = req.body.id;
  let filePath = path.join(__dirname, "/table.ejs");
  queryFunc.mysqlEjs(user, pass, values.stmt, "traffic", filePath);
  res.send("challanlist id " + id + " is deleted from database");
});
// 888888888888888888888888888888888888888888  update  88888888888888888888888888888888888888888888888
  function showTable(res){
    console.log("function entered");
    let stmt2 = "SELECT * FROM challanlist LIMIT 0,500";       //this query is not working
    let filePath2 = path.join(__dirname, "/search_ajax.ejs");
    const html = queryFunc.mysqlEjs(user, pass, stmt2, "traffic", filePath2);
    console.log("challanlist list",html[0]);     //html[0] is undefined
    setTimeout(() => {
      res.send(html[0]);
    }, 5000);
  }

app.get("/Edit", (req, res) => {
  var id = req.query.id;
  console.log(id);
  let stmt = "SELECT * FROM challanlist where id="+id+";";
  let filePath = path.join(__dirname, "Edit.ejs");
  const html = queryFunc.mysqlEjs(user, pass, stmt, "traffic", filePath);
  console.log("challanlist list update");
  setTimeout(() => {
    console.log("challanlist list update",html[0]);
    res.send(html[0]);
  }, 100);
});
app.post("/Edit", (req, res) => {
  let values = req.body;
  console.log("update file", values.stmt);
  let filePath = path.join(__dirname, "/table.ejs");
  queryFunc.mysqlEjs(user, pass, values.stmt, "traffic", filePath);     //update query is running

  // showTable(res);       
  res.send("Student Record Updated Please refresh the page to view changes");
});
// 8888888888888888888888888888888888888888  listen(3000)   888888888888888888888888888888888888888888
app.listen(port, () => {
  console.log(`server is on localhost:${port}`);
});
