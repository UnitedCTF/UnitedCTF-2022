<!DOCTYPE html>
<html lang="en">

<body>
    <form method="POST">
    <input name="str" placeholder="..." type="text" />
    <button>Submit</button>
    </form>
    <?php
        if (isset($_POST["str"])) {
            do_echo("<pre>".$_POST["str"]."</pre>");
        }
    ?>
</body>

</html>