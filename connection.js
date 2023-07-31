const mysql = require("mysql");

function getConnection(user,pass,db){
    return mysql.createConnection({
        host : 'localhost',
        user : user,
        password : pass,
        database : db,
    })
}

exports.con = getConnection;