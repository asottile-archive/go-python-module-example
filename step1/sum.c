#include <stdio.h>
#include <stdlib.h>

#include "sum.h"

int main(int argc, char* argv[]) {
    // asottile: added some commandline for fun
    if (argc != 3) {
        printf("Usage: %s: INT1 INT2\n", argv[0]);
        return 1;
    }
    // asottile: originally %d -- however GoInt is a long long
    // warning: format ‘%d’ expects argument of type ‘int’, but argument 2 has
    // type ‘GoInt’ [-Wformat=]
    printf("%lld\n", Sum(atoi(argv[1]), atoi(argv[2])));
    return 0;
}
