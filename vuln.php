<?php
$file = $_GET['page'];
// Trigger: Including a file path directly from a URL parameter
include($file . ".php");
?>
