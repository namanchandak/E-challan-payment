function mysqlEjs(user, pass, stmt, db, ejsFilePath) {
    var mysql = require('mysql');
    var connection = mysql.createConnection({
        host: 'localhost',
        user: user,
        password: pass,
        database: db
    });

    connection.connect();
    const html = [];
    function mycb(error, results, fields) {
        // if (error) throw error;
        // ejs render code
        const ejs = require('ejs');
        const fs = require('fs');
        // Object of parameters that you want to render
        const param = { thead: fields, tbody: results };
        // String of .ejs file path as
        let ejsFile = ejsFilePath;
        // pharse file content to String
        const fileContents = fs.readFileSync(ejsFile, 'utf8');
        // console.log(results);
        html[0] = ejs.render(fileContents, param);
    }
    connection.query(stmt, mycb);
    connection.end();
    return html;
}

exports.mysqlEjs = mysqlEjs;