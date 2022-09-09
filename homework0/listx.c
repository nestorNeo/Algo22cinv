#include "listx.h"

void show_list(struct Node* start){
    struct Node* i = start;
    while(i != 0){
        printf("%d - ", i->value);
        i = i->next;
    }
}