#define ANSI_RED     "\x1b[31m"
#define ANSI_GREEN   "\x1b[32m"
#define ANSI_YELLOW  "\x1b[33m"
#define ANSI_RESET   "\x1b[0m"

#define ON ANSI_GREEN "ON" ANSI_RESET "     "
#define OFF ANSI_RED "OFF" ANSI_RESET "    "
#define PARTIAL ANSI_YELLOW "Partial" ANSI_RESET
#define FULL ANSI_GREEN "Full" ANSI_RESET "   "

#ifdef NOASLR
# define ASLR_STATE OFF
#else
# define ASLR_STATE ON
#endif

#ifdef SSP
# define SSP_STATE ON
#else
# define SSP_STATE OFF
#endif

#ifdef NODEP
# define DEP_STATE OFF
#else
# define DEP_STATE ON
#endif

#ifdef NOPIE
# define PIE_STATE OFF
#else
# define PIE_STATE ON
#endif

#ifdef FORTIFY
# define FORTIFY_STATE ON
#else
# define FORTIFY_STATE OFF
#endif

#ifdef RELRO
# define RELRO_STATE FULL
#else
# define RELRO_STATE PARTIAL
#endif

#define PROTECTIONS ".--------------- [ Protections ] ---------------.\n" \
                    "| ASLR                                  " ASLR_STATE      " |\n" \
                    "| SSP/Canary                            " SSP_STATE       " |\n" \
                    "| DEP/NX                                " DEP_STATE       " |\n" \
                    "| PIE                                   " PIE_STATE       " |\n" \
                    "| Fortify                               " FORTIFY_STATE   " |\n" \
                    "| RelRO                                 " RELRO_STATE     " |\n" \
                    "`-----------------------------------------------'\n"

#define FLAG_SIZE 54

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    puts(PROTECTIONS);
}