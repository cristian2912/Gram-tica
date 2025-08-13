#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <regex.h>

bool check_regex(const char *pattern, const char *input) {
    regex_t regex;
    int ret = regcomp(&regex, pattern, REG_EXTENDED);
    if (ret) return false;
    ret = regexec(&regex, input, 0, NULL, 0);
    regfree(&regex);
    return ret == 0;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Uso: %s <G1|G2|G3|G4|G5>\n", argv[0]);
        return 1;
    }

    const char *patterns[] = {
        "^(0|1)((0|1)*\\1)?$",  // G1
        "^a*b+$",                // G2
        "^abb$",                 // G3
        "^(ab|abb)$",            // G4
        "^a(ab)*b$"              // G5
    };

    int index = argv[1][1] - '1';  // Convierte "G1" -> 0, "G2" -> 1, etc.
    if (index < 0 || index > 4) {
        printf("Gramática no válida.\n");
        return 1;
    }

    char input[100];
    while (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = '\0';  // Elimina el salto de línea
        printf("%s -> %s\n", input, check_regex(patterns[index], input) ? "acepta" : "NO acepta");
    }

    return 0;
}