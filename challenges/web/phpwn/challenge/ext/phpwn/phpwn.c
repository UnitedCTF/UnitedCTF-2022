#include <php.h>
#include "openssl/sha.h"

#define PHP_PHPWN_EXTNAME "phpwn"
#define PHP_PHPWN_VERSION "1.0.0"
#define SECRET_HASH "677c6686fbb8742a054f703c84d24f2ba0b875acf53c26552592006cfb6aa4ad"
#define SECRET_SALT "cr4ck1ng1sus3l3ss"
#define BUFF_LENGTH 256

char string[64];

PHP_FUNCTION(do_echo);
PHP_FUNCTION(print_date);
PHP_FUNCTION(check_creds);

ZEND_BEGIN_ARG_INFO(arginfo_do_echo, 0)
    ZEND_ARG_INFO(0, string)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_INFO(arginfo_print_date, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_INFO(arginfo_check_creds, 0)
    ZEND_ARG_INFO(0, id)
    ZEND_ARG_INFO(0, username)
    ZEND_ARG_INFO(0, password)
ZEND_END_ARG_INFO()

zend_function_entry phpwn_functions[] = {
    PHP_FE(do_echo, arginfo_do_echo)
    PHP_FE(print_date, arginfo_print_date)
    PHP_FE(check_creds, arginfo_check_creds)
    PHP_FE_END
};

zend_module_entry phpwn_module_entry = {
    STANDARD_MODULE_HEADER,
    PHP_PHPWN_EXTNAME,
    phpwn_functions,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    PHP_PHPWN_VERSION,
    STANDARD_MODULE_PROPERTIES
};

ZEND_GET_MODULE(phpwn)

void sha256(char *buff) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, buff, strlen(buff));
    SHA256_Final(hash, &sha256);
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        sprintf(buff + (i * 2), "%02x", hash[i]);
    }
    buff[SHA256_DIGEST_LENGTH*2] = 0;
}

void echo(char *s) {
    php_printf(s);
}

PHP_FUNCTION(do_echo) {
    char *s;
    size_t length;

    ZEND_PARSE_PARAMETERS_START(1, 1)
        Z_PARAM_STRING(s, length)
    ZEND_PARSE_PARAMETERS_END();

    strncpy(string, s, sizeof(string));
    echo(string);
}

PHP_FUNCTION(print_date) {
    ZEND_PARSE_PARAMETERS_NONE();
    system("date");
}

PHP_FUNCTION(check_creds) {
    unsigned char buff[BUFF_LENGTH];
    char *id;
    char *username;
    char *password;
    size_t id_length;
    size_t username_length;
    size_t password_length;

    ZEND_PARSE_PARAMETERS_START(3, 3)
            Z_PARAM_STRING(id, id_length)
            Z_PARAM_STRING(username, username_length)
            Z_PARAM_STRING(password, password_length)
    ZEND_PARSE_PARAMETERS_END();

    strncpy(buff, id, id_length);
    strncpy(buff + id_length, username, username_length);
    strncpy(buff + id_length + username_length, password, password_length);
    strncpy(buff + id_length + username_length + password_length, SECRET_SALT, strlen(SECRET_SALT));
    
    sha256(buff);

    if (!strncmp(buff, SECRET_HASH, SHA256_DIGEST_LENGTH*2)) {
        RETURN_TRUE;
    } else {
        RETURN_FALSE;
    }
}