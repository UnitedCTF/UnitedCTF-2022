PHP_ARG_ENABLE(phpwn, Whether to enable the PHPwn extension, [ --enable-phpwn Enable PHPwn])

if test "$PHP_PHPWN" != "no"; then
    PHP_NEW_EXTENSION(phpwn, phpwn.c, $ext_shared)
fi