const express = require("express")
const { exec } = require("child_process")

const app = express()

// Hardcoded secret
const API_KEY = "super-secret-api-key"

app.get("/run", (req, res) => {
    const cmd = req.query.cmd

    // Command injection
    exec(cmd, (err, stdout) => {
        res.send(stdout)
    })
})

app.get("/eval", (req, res) => {
    const input = req.query.code

    // Eval injection
    eval(input)

    res.send("executed")
})

app.listen(3000)