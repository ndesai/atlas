// #include <iostream>

// int main(int argc, const char * argv[]) {
//     std::cout << "Hello, World!\n";
//     return 0;
// }

#include <grpc/grpc.h>

int main() {
    grpc_init();
    grpc_shutdown();
    return GRPC_STATUS_OK;
}