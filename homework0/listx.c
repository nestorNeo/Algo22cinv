#include "listx.h"

void show_list(void* start){
    if (start == 0){
        printf("a invalid pointer");
        return;
    }
    struct Node* i = (struct Node*)start;
    while(i != 0){
        printf("%d - ", i->value);
        i = (struct Node*)(i->next);
    }
}