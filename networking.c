//
// Created by shahar on 27/09/2020.
//

#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "networking.h"


int connect_socket(char* address, int port) {
    int sockfd;
    struct sockaddr_in serveraddr;

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("Socket creation failed\n");
        exit(1);
    }
    bzero(&serveraddr, sizeof(serveraddr));

    serveraddr.sin_family = AF_INET;
    serveraddr.sin_port = htons(port);
    if(inet_pton(AF_INET, address, &serveraddr.sin_addr)<=0)
    {
        printf("Invalid address/ Address not supported \n");
        exit(1);
    }


    if(connect(sockfd, (struct sockaddr *)&serveraddr, sizeof(serveraddr)) < 0) {
        printf("Connection failed\n");
        exit(1);
    }
    return sockfd;
}

void send_buffer_or_crash(int sockfd, void* message, unsigned int length) {
    if(send(sockfd, message, length, 0) < 0) {
        printf("Send failed\n");
        exit(1);
    }
}

void send_message(int sockfd, void* message, unsigned int length) {
    send_buffer_or_crash(sockfd, &length, sizeof(unsigned int));
    send_buffer_or_crash(sockfd, message, length);
}