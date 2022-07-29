var express = require("express");
const { exec } = require("child_process");


var app = express();
app.listen(3000, () => {
 console.log("Server running on port 3000");
});

app.get("/url", (req, res, next) => {
    res.json(["Tony","Lisa","Michael","Ginger","Food"]);
});

// console.log(fast)

exec("fast --json > file.json", (error, stdout, stderr) => {
    if (error) {
        console.log(`error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
});