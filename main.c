#include <stdio.h>

#include "networking.h"

int main() {
    int sockfd;

    sockfd = connect_socket("127.0.0.1", 1234);
    send_message(sockfd, "test", 4);

    return 0;
}
