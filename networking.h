//
// Created by shahar on 27/09/2020.
//

#ifndef MEM_EDITOR_NETWORKING_H
#define MEM_EDITOR_NETWORKING_H

/**
 * Creates a socket and connects to the target address
 * @param address Address to connect to
 * @param port Port to connect to
 * @return File descriptor of the socket
 */
int connect_socket(char* address, int port);

/**
 * Sends the length of the message and then the message
 * @param sockfd File descriptor of the socket
 * @param message Message to send
 * @param length Length of the message
 */
void send_message(int sockfd, void* message, unsigned int length);

#endif //MEM_EDITOR_NETWORKING_H
