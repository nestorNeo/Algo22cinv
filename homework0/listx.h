#ifndef LISTX_H
#define LISTX_H
#include <stdio.h>


struct  Node  {
    struct Node* next;
    int value;
};
// ugly as hell
void show_list(void* start);

#endif