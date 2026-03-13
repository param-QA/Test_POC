import express from "express"
import { exec } from "child_process"

const app = express()

// Hardcoded token
const TOKEN: string = "ghp_123456789"

app.get("/exec", (req, res) => {
    const userCmd = req.query.cmd as string

    // Command injection
    exec(userCmd, (err, stdout) => {
        res.send(stdout)
    })
})

app.get("/danger", (req, res) => {
    const userInput = req.query.input as string

    // Eval injection
    eval(userInput)

    res.send("done")
})

app.listen(4000)