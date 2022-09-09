#ifndef LISTX_H
#define LISTX_H
#include <stdio.h>


struct  Node  {
    struct Node* next;
    int value;
};
void show_list(struct Node* start);

#endif