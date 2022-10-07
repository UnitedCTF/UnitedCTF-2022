<!DOCTYPE html>
<html lang="en">

<head>
  <link rel="stylesheet" href="../css/style.css">
  <title>Admin panel</title>
</head>

<body>
  <div class="container">
    <div class="container-info">
      <div class="info-item">
        <div class="table">
          <div class="table-cell">
            <p>
            <?php
                if (isset($_POST["id"]) && isset($_POST["username"]) && isset($_POST["password"])) {
                    if (check_creds($_POST["id"], $_POST["username"], $_POST["password"])) {
                        do_echo("Access granted!");
                    } else {
                        do_echo("Wrong combination.");
                    }
                } else {
                    do_echo("Enter your credentials");
                }
            ?>
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="container-forms">
      <div class="container-form">
        <div class="form-item log-in">
          <div class="table">
            <div class="table-cell">
              <form method="POST">
                <input name="id" placeholder="Identifier" type="text" />
                <input name="username" placeholder="username" type="text" />
                <input name="password" placeholder="password" type="password" />
                <button class="btn">Log in</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="../js/form.js"></script>
</body>

</html>