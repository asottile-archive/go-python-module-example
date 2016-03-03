#include <stdio.h>
#include <stdlib.h>

#include "hello.h"

int main(int argc, char* argv[]) {
    // asottile: added some commandline for fun
    if (argc != 2) {
        printf("Usage: %s: STRING\n", argv[0]);
        return 1;
    }

    GoString ret = AddsHello(argv[1]);
    printf("%s\n", ret.p);
    return 0;
}
