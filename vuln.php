<?php
// Intentional vulnerability (SQL Injection)
$db = new SQLite3('test.db');
$username = $_GET['username'];
$db->query("SELECT * FROM users WHERE username = '" . $username . "'");
?>
