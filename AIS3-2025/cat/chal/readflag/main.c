#include <stdio.h>

int main() {
    FILE *fp = fopen("/f14g1337", "r");
    if (!fp) { perror("fopen"); return 1; }
    char buf[0x100] = {0};
    fgets(buf, sizeof buf, fp);
    puts(buf);
    fclose(fp);
    return 0;
}

