const express = require('express');
const app = express();

app.get('/', (req, res) => {
    // Intentional vulnerability (Eval)
    eval(req.query.code);
    res.send('Hello World!');
});

app.listen(3000);
