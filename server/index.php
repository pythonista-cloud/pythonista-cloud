<?php

if ($_SERVER["REQUEST_METHOD"] === "GET") {
  // A GET request was made; this is either someone accessing the homepage or
  // someone trying to download a module. We decide which it is by checking
  // whether the user passed "module" as a query parameter
  if (array_key_exists("module", $_GET)) {
    // Someone wants to download a module
    header("Content-Type: application/json; charset=utf-8");
    echo "You requested the module '".$_GET["module"]."'";
  } else {
    // Someone is visiting the homepage normally
    header("Content-Type: text/html; charset=utf-8");
    echo file_get_contents("main.html");
  }
} elseif ($_SERVER["REQUEST_METHOD"] === "POST") {
  // A POST request was made; someone is trying to upload a module
}


?>
