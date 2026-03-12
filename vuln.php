<?php

// SQL Injection
$conn = mysqli_connect("localhost", "root", "password", "test");

$user = $_GET['user'];
$query = "SELECT * FROM users WHERE username = '$user'";
$result = mysqli_query($conn, $query);

// Command Injection
if(isset($_GET['cmd'])){
    $cmd = $_GET['cmd'];
    system($cmd);
}

// File Inclusion
$page = $_GET['page'];
include($page);

// Hardcoded secret
$api_key = "sk_live_123456789";

echo "Done";
?>