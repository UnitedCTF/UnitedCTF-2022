<h1>Welcome to my CSSless blog!</h1>

<form method="GET">
  <select name="page">
    <option value="./inc/echoaas.php">Echo as a Service</option>
    <option value="./inc/quotes.php">Random quotes</option>
    <!-- <option value="./inc/admin.php">Admin panel</option> -->
    <!-- <option value="./inc/info.php">Debug</option> -->
  </select>
  <button>Go</button>
</form>

<?php
    if (isset($_GET["page"])) require_once($_GET["page"]);
?>
