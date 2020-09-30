cmake_minimum_required(VERSION 3.17)
project(mem_editor C)

set(CMAKE_C_STANDARD 99)

add_executable(mem_editor main.c networking.c networking.h commander.c commander.h)