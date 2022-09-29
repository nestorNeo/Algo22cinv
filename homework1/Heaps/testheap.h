#ifndef TESTHEAP_FILE
#define TESTHEAP_FILE

#include <stdio.h>
 
void max_heapify( int *arr, int i, int hs);

void min_heapify( int *arr, int i, int hs);

int _left_child(int i);

int _right_child(int i);

void build_max_heap(int *arr, int len);

void build_min_heap(int *arr, int len);

void help();

#endif
